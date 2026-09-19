# Market Signal Reviewer: Explainability

## Decision and reasoning

The strategy decision is whether its documented RSI and moving-average conditions produce a buy, sell, or neutral signal. The reasoning should show the relevant RSI value, oversold or overbought threshold, moving-average direction or crossover, and whether the indicators confirm one another. The assistant explains the existing rule output and its evidence; it does not convert the output into a promise, probability of profit, or instruction to trade.

## Inputs and data sources

Inputs may include the selected market symbol, historical or current price series, calculated RSI values, moving-average values, configured thresholds, generated signal records, and historical backtest results. The repository describes Python analysis using Pandas, NumPy, Matplotlib, and optional Telegram Bot API alerts. The precise market-data provider, time interval, backtest period, transaction assumptions, and live-data freshness should be documented for each run before its results are relied upon.

## Limits and known constraints

The main limitation is that RSI and moving-average rules can generate false or delayed signals, particularly in volatile or sideways markets, and their apparent performance is sensitive to parameter choices. Historical backtesting does not guarantee future results and can be distorted by data leakage, overfitting, survivorship bias, ignored transaction costs, slippage, taxes, or incomplete data. The performance figures stated in project documentation require reproducible evidence before being treated as verified. The system does not incorporate all news, macroeconomic, liquidity, or company-specific risks and must not autonomously execute financial transactions.
