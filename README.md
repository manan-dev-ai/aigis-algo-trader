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
