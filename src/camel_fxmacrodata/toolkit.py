"""Native CAMEL FunctionTools for FXMacroData research."""

from collections.abc import Callable
from copy import deepcopy
from typing import Any

from camel.toolkits import BaseToolkit, FunctionTool
from camel.toolkits.base import manual_timeout
from fxmacrodata_public import (
    FXMacroDataClient,
    FXMacroDataError,
    Operation,
    list_operations,
)

SITE_URL = (
    "https://fxmacrodata.com/?utm_source=camel&utm_medium=integration"
    "&utm_campaign=open_source_integrations&utm_content=app"
)


def _entrypoint(
    client: FXMacroDataClient, operation: Operation
) -> Callable[..., dict[str, Any]]:
    def invoke(**arguments: Any) -> dict[str, Any]:
        try:
            output = client.execute(operation.name, arguments).as_dict()
            output["provider_url"] = SITE_URL
            return output
        except Exception as error:  # noqa: BLE001 - sanitize the external SDK boundary
            return {
                "error": (
                    str(error)
                    if isinstance(error, FXMacroDataError)
                    else "FXMacroData request failed. Check parameters and access."
                ),
                "operation": operation.name,
            }

    invoke.__name__ = "fxmd_" + operation.name
    invoke.__doc__ = operation.description
    return invoke


class FXMacroDataToolkit(BaseToolkit):
    r"""Discover and query FXMacroData using CAMEL's normal tool interface.

    Args:
        api_key: User key, or None to read FXMACRODATA_API_KEY. An empty
            string selects no-key public access.
        timeout: Maximum request duration in seconds.
        operations: Optional operation-name allowlist; all are exposed
            when omitted.
    """

    def __init__(
        self,
        api_key: str | None = None,
        timeout: float = 30,
        operations: list[str] | None = None,
    ) -> None:
        super().__init__(timeout=timeout)
        available = {
            operation.name: operation for operation in list_operations()
        }
        if operations is not None and set(operations) - available.keys():
            raise ValueError("Unknown FXMacroData operation.")
        selected = list(available) if operations is None else operations
        self._client = FXMacroDataClient(api_key=api_key, timeout=timeout)
        self._tools = [
            FunctionTool(
                _entrypoint(self._client, available[name]),
                openai_tool_schema={
                    "type": "function",
                    "function": {
                        "name": "fxmd_" + name,
                        "description": available[name].description,
                        "parameters": deepcopy(available[name].input_schema),
                    },
                },
            )
            for name in selected
        ]

    @manual_timeout
    def get_tools(self) -> list[FunctionTool]:
        r"""Return native callable tools with their complete input schemas."""
        return list(self._tools)

    @manual_timeout
    def close(self) -> None:
        r"""Release the toolkit's HTTP session after use."""
        self._client.close()
