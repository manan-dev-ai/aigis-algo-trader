# 📈 AIGIS Algo Trader

A high-performance algorithmic trading engine built with a fully asynchronous Python architecture. AIGIS is designed for rapid trade execution, real-time market data processing, and highly extensible trading strategy implementations.

## 🚀 Overview
**AIGIS** (Algorithmic Intelligent Growth & Investment System) provides a robust infrastructure for quantitative trading. Leveraging Python's `asyncio` capabilities, the system handles concurrent market data streams, order routing, and execution without blocking, ensuring millisecond-level responsiveness in volatile markets.

## ✨ Features
* **Asynchronous Engine:** Fully non-blocking architecture designed for high-frequency data ingestion and order execution.
* **Modular Strategy Framework (`strategies/`):** Plug-and-play directory to easily write, backtest, and deploy custom trading algorithms.
* **Core Execution Logic (`core/`):** Secure and reliable order management, risk control, and API gateway handling.
* **Centralized Configuration (`config.yaml`):** Easily manage trading parameters, risk limits, and API endpoints without modifying code.
* **Lightning-Fast Dependency Management:** Powered by `uv` for strict, deterministic, and rapid environment setups.

## 🛠️ Tech Stack
* **Language:** Python 3 (100% Async)
* **Architecture:** Asynchronous Event-Driven Loop
* **Configuration:** YAML
* **Package Management:** `uv` (`pyproject.toml`, `uv.lock`)

## 📁 Project Structure
```text
aigis-algo-trader/
├── core/               # Core engine, order management, and API connections
├── strategies/         # Custom trading algorithms and logic
├── utils/              # Helper functions, logging, and data formatters
├── main.py             # Entry point for the trading loop
├── config.yaml         # System and strategy parameters
├── .env                # Private API keys and secrets (Do not commit)
├── pyproject.toml      # Project metadata and dependencies
└── uv.lock             # Locked dependencies for deterministic builds

```
💻 Local Setup Instructions
1. Clone the repository:


git clone [https://github.com/manan-dev-ai/aigis-algo-trader.git](https://github.com/manan-dev-ai/aigis-algo-trader.git)
cd aigis-algo-trader
2. Install dependencies:
This project uses uv for extremely fast dependency management. If you don't have it installed, run pip install uv first.


uv sync
3. Set up Environment Variables & Configuration:

Create a .env file in the root directory and add your broker API keys and secrets.

Review and update config.yaml to set your risk parameters, active strategies, and trading pairs.

4. Run the Trading Engine:


uv run main.py
⚠️ Disclaimer & Security
Algorithmic trading carries significant financial risk. This software is provided for educational and research purposes. Never deploy capital you cannot afford to lose.
Ensure that your .env file containing live API keys is added to your .gitignore and never committed to a public repository.

🤝 Contributing
Contributions, issue reports, and pull requests to optimize execution speed or add new strategy templates are welcome!

