# FXMacroData for CAMEL

Build CAMEL research agents that work with official macroeconomic observations, release calendars and sourced market context.

[Subscribe to FXMacroData](https://fxmacrodata.com/subscribe?utm_source=github&utm_medium=referral&utm_campaign=open_source_integrations&utm_content=camel_subscribe) for non-USD data, full available history, FX, commodities and positioning. Use the public USD workflow to evaluate the integration before connecting your subscription.

[Explore FXMacroData](https://fxmacrodata.com/?utm_source=github&utm_medium=referral&utm_campaign=open_source_integrations&utm_content=camel_readme) · [API documentation](https://fxmacrodata.com/documentation/reference?utm_source=github&utm_medium=referral&utm_campaign=open_source_integrations&utm_content=camel_docs)

The public USD catalogue, recent macro history and release calendar support evaluation without an API key. The history example requests the most recent 90 days. Data availability varies by series; your subscription and its terms govern protected access.

## Install from source

With both source projects in sibling directories:

```bash
python -m pip install ./fxmacrodata-public-client ./camel-fxmacrodata
```

This installation uses local source packages and assumes no package-registry publication. The package is validated with CAMEL 0.2.90 and Python 3.12; Python 3.10+ is required.

## Research workflow

```python
from camel.agents import ChatAgent
from camel_fxmacrodata import FXMacroDataToolkit

toolkit = FXMacroDataToolkit()
agent = ChatAgent(
    system_message="Research macroeconomic conditions. Preserve source links, units and release timestamps.",
    tools=toolkit.get_tools(),
)
# Configure your preferred CAMEL model before asking the agent to run.
```

`python examples/usd_macro_brief.py` runs actual registered FunctionTools without a language model. It reads the USD catalogue, recent inflation observations and upcoming releases.

All 72 REST/MCP operations are separately registered with complete input schemas and a `fxmd_` prefix. `operations=["data_catalogue", "indicator_history", "release_calendar"]` limits an individual toolkit to the public USD workflow. See [CAPABILITIES.md](CAPABILITIES.md) for the complete inventory.

Each result preserves the original payload as `data`, exposes `records` for analysis and includes public source/provider links. Keep FXMacroData-generated forecasts separate from market consensus. Do not infer missing values or future release times. MCP visual artifacts are preserved but not rendered as MCP Apps.

## Connect your FXMacroData subscription

Supply your own `FXMACRODATA_API_KEY` environment variable or pass a key from your application's secret manager. No key is required for the USD example; `api_key=""` explicitly disables environment credentials. Access to other datasets follows your FXMacroData entitlement.

The links contain static referral parameters. The toolkit does not emit tracking events or send user identifiers for attribution.

## Test

```bash
python -m pytest tests -n 8 --dist load
```

This integration's code is Apache-2.0 licensed. Data access and brand usage are governed separately by the applicable FXMacroData terms.
