# Supported operations

Every operation is registered as `fxmd_<operation>` in the native tool surface. The original response is preserved alongside its record view.

| Operation | Contract | Native surface |
| --- | --- | --- |
| `health` | `GET /v1/health` | CAMEL FunctionTool |
| `ping` | `GET /v1/ping` | CAMEL FunctionTool |
| `forex` | `GET /v1/forex/{base}/{quote}` | CAMEL FunctionTool |
| `intraday_reference_rates` | `GET /v1/fx/intraday-reference-rates/{base}/{quote}` | CAMEL FunctionTool |
| `fx_sources` | `GET /v1/fx/sources` | CAMEL FunctionTool |
| `fx_source_universe` | `GET /v1/fx/source-universe` | CAMEL FunctionTool |
| `data_catalogue` | `GET /v1/data_catalogue/{currency}` | CAMEL FunctionTool |
| `release_calendar` | `GET /v1/calendar/{currency}` | CAMEL FunctionTool |
| `market_sessions` | `GET /v1/market_sessions` | CAMEL FunctionTool |
| `rate_differentials` | `GET /v1/rate_differentials/{base}/{quote}` | CAMEL FunctionTool |
| `curves` | `GET /v1/curves/{currency}` | CAMEL FunctionTool |
| `financial_prices` | `GET /v1/financial_prices/{currency}` | CAMEL FunctionTool |
| `press_releases` | `GET /v1/press-releases/{currency}` | CAMEL FunctionTool |
| `risk_sentiment` | `GET /v1/risk_sentiment` | CAMEL FunctionTool |
| `factors` | `GET /v1/factors/{currency}/{factor}` | CAMEL FunctionTool |
| `event_predictions` | `GET /v1/predictions/{currency}/{indicator}` | CAMEL FunctionTool |
| `latest_announcements` | `GET /v1/announcements/{currency}/latest` | CAMEL FunctionTool |
| `indicator_history` | `GET /v1/announcements/{currency}/{indicator}` | CAMEL FunctionTool |
| `cot` | `GET /v1/cot/{currency}` | CAMEL FunctionTool |
| `latest_commodities` | `GET /v1/commodities/latest` | CAMEL FunctionTool |
| `commodities` | `GET /v1/commodities/{indicator}` | CAMEL FunctionTool |
| `announcement_changes` | `GET /v1/announcements/changes` | CAMEL FunctionTool |
| `stream_events` | `GET /v1/stream/events` | CAMEL FunctionTool |
| `mcp_ping` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_mcp_capabilities` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_mcp_auth_guide` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_subscribe_for_mcp_access` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_data_catalogue` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_risk_sentiment` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_macro_news` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_release_calendar` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_release_calendar_visual_artifact` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_event_predictions` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_latest_announcements` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_announcement_changes` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_press_releases` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_macro_factor` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_fx_reference_sources` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_fx_reference_universe` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_fx_intraday_reference_rates` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_rate_curve` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_rate_differentials` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_latest_commodities` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_forex` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_seasonality` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_indicator_query` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_plot_visual_artifact` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_indicator_visual_artifact` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_forex_visual_artifact` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_commodities_visual_artifact` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_cot_visual_artifact` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_policy_rate_differential_visual_artifact` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_macro_briefing_task` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_indicator_intel_task` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_pair_intel_task` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_macro_heatmap_task` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_policy_scenario_modeler_task` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_macro_war_room_task` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_event_impact_replay_task` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_quant_scenario_lab_task` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_known_at_time_task` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_macro_regime_classifier_task` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_release_risk_score_task` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_portfolio_risk_engine_task` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_fx_trade_setup_task` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_fx_backtest_task` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_macro_research_pack_task` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_market_sessions` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_cot_data` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_commodities` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_financial_prices` | `MCP /mcp` | CAMEL FunctionTool |
| `mcp_official_dataset_family` | `MCP /mcp` | CAMEL FunctionTool |

REST supplies 23 operations and hosted MCP supplies 49 tools. The `mcp_` prefix distinguishes MCP capabilities from REST operations. Parameters retain their complete documented JSON schemas, including required fields, arrays, nested objects and enums.

USD catalogue, macro history and release-calendar examples are no-key. Access to other datasets follows the service's published access rules; a tool being discoverable is not a guarantee of account entitlement.

SSE event collection is finite: `max_events` and `max_seconds` bound the stream. MCP analytical operations retain their hosted semantics. MCP Apps resources and visual artifacts remain in the original response; these integrations expose data, documents and tools but do not embed an MCP Apps iframe renderer.

Forecasts retain their product labels. FXMacroData-generated predictions must not be relabelled as market consensus. No timestamps, missing observations or future release dates are inferred.
