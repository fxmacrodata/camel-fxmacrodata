"""Read public USD data through CAMEL FunctionTools without an LLM."""

from datetime import date, timedelta

from camel_fxmacrodata import FXMacroDataToolkit


def main() -> None:
    toolkit = FXMacroDataToolkit(api_key="")
    tools = {tool.get_function_name(): tool for tool in toolkit.get_tools()}
    today = date.today()
    calls = [
        ("data_catalogue", {"currency": "USD"}),
        (
            "indicator_history",
            {
                "currency": "USD",
                "indicator": "inflation",
                "start_date": (today - timedelta(days=90)).isoformat(),
                "end_date": today.isoformat(),
            },
        ),
        (
            "release_calendar",
            {
                "currency": "USD",
                "start_date": today.isoformat(),
                "end_date": (today + timedelta(days=30)).isoformat(),
            },
        ),
    ]
    for operation, arguments in calls:
        result = tools["fxmd_" + operation](**arguments)
        if result.get("error"):
            raise RuntimeError(result["error"])
        print(f"{operation}: {len(result['records'])} records")
        print(result["source_url"])
        print(result["provider_url"])
        if not result["records"]:
            print("No records available in this window.")


if __name__ == "__main__":
    main()
