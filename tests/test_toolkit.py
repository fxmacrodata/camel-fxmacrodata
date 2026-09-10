"""Run actual CAMEL FunctionTools against a mocked transport boundary."""

from unittest.mock import patch

import pytest
from camel.toolkits import FunctionTool
from fxmacrodata_public import Result, list_operations

from camel_fxmacrodata import FXMacroDataToolkit

PAYLOAD = {
    "data": [
        {
            "fixture": "synthetic",
            "announcement_datetime": "2026-01-01T12:00:00Z",
            "value": None,
        }
    ]
}


@pytest.mark.parametrize(
    "operation", list_operations(), ids=lambda item: item.name
)
def test_functiontool_schema_and_execution(operation):
    tool = FXMacroDataToolkit(
        api_key="", operations=[operation.name]
    ).get_tools()[0]
    assert isinstance(tool, FunctionTool)
    assert tool.get_function_name() == "fxmd_" + operation.name
    assert (
        tool.get_openai_function_schema()["parameters"]
        == operation.input_schema
    )
    arguments = {"fixture_argument": {"nested": [1, None]}}
    with patch(
        "camel_fxmacrodata.toolkit.FXMacroDataClient.execute",
        return_value=Result(operation.name, PAYLOAD),
    ) as execute:
        result = tool(**arguments)
    execute.assert_called_once_with(operation.name, arguments)
    assert result["data"] == PAYLOAD
    assert result["records"][0]["value"] is None
    assert "utm_source=camel" in result["provider_url"]


def test_inventory_and_caller_list_are_independent():
    toolkit = FXMacroDataToolkit(api_key="")
    first = toolkit.get_tools()
    assert {tool.get_function_name() for tool in first} == {
        "fxmd_" + op.name for op in list_operations()
    }
    first.clear()
    assert len(toolkit.get_tools()) == len(list_operations())


def test_error_sanitization_and_empty_result():
    tool = FXMacroDataToolkit(
        api_key="", operations=["release_calendar"]
    ).get_tools()[0]
    with patch(
        "camel_fxmacrodata.toolkit.FXMacroDataClient.execute",
        side_effect=RuntimeError(
            "https://example.org/?api_key=DO_NOT_DISCLOSE_SENTINEL"
        ),
    ):
        result = tool(currency="USD")
    assert "error" in result
    assert "SENTINEL" not in str(result)
    with patch(
        "camel_fxmacrodata.toolkit.FXMacroDataClient.execute",
        return_value=Result("release_calendar", []),
    ):
        assert tool(currency="USD")["records"] == []


def test_rejects_unknown_operations():
    with pytest.raises(ValueError, match="Unknown FXMacroData operation"):
        FXMacroDataToolkit(operations=["unknown"])
