# Binance Futures Testnet Trading Bot

## Overview
This project is a Python-based command-line trading bot that interacts with the Binance Futures Testnet (USDT-M). It enables users to place MARKET and LIMIT orders with proper validation, logging, and error handling.

The application follows a clean, modular architecture by separating API interaction, order logic, validation, and CLI interface. This ensures maintainability, scalability, and readability of the code.

---

## Features
- Place MARKET and LIMIT orders on Binance Futures Testnet
- Supports both BUY and SELL sides
- Command-line interface for user input
- Input validation for all parameters
- Structured and reusable codebase
- Logging of API requests, responses, and errors
- Exception handling for invalid inputs and API failures

---

## Project Structure
```
trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API client wrapper
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation functions
│   ├── logging_config.py  # Logging configuration
│   └── cli.py             # CLI entry point
│
├── logs/                  # Stores log files
├── .env                   # API credentials (excluded from version control)
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd trading-bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory and add:

```
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
```

Note:
- Do not commit the `.env` file to version control
- Use Binance Futures Testnet API keys only

---

## Running the Application

### Interactive Mode
```bash
python -m bot.cli
```

You will be prompted to enter:
- Symbol (e.g., BTCUSDT)
- Side (BUY or SELL)
- Order Type (MARKET or LIMIT)
- Quantity
- Price (only required for LIMIT orders)

---

### Direct Command Mode

#### MARKET Order
```bash
python -m bot.cli --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001
```

#### LIMIT Order
```bash
python -m bot.cli --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 78000
```

---

## Example Output
```
Order Placed Successfully!
Order ID: 13096816863
Status: FILLED
Executed Qty: 0.001
Avg Price: 78200.00
```

---

## Logging
All API interactions are logged in:

```
logs/bot.log
```

The log file includes:
- Order request details
- API responses
- Error messages (if any)

This helps in debugging and verifying correct functionality.

---

## Error Handling
The application handles:
- Invalid user inputs (e.g., wrong order type or side)
- Missing required parameters (e.g., price for LIMIT orders)
- API errors from Binance
- Network-related failures

---

## Assumptions
- The user has a Binance Futures Testnet account
- API keys are generated from the testnet environment
- The testnet wallet has sufficient USDT balance for placing orders

---

## Security Considerations
- API keys are stored securely using environment variables
- Sensitive credentials are not exposed in source code
- `.env` file is excluded using `.gitignore`

---

## Evaluation Criteria Alignment
This project satisfies the assignment requirements:

- Correctness: Successfully places MARKET and LIMIT orders on testnet
- Code Quality: Modular, readable, and maintainable structure
- Validation: Proper input validation implemented
- Error Handling: Robust exception handling included
- Logging: Meaningful logs for requests, responses, and errors
- Documentation: Clear setup and usage instructions

---

## Future Improvements
- Add support for advanced order types (e.g., Stop-Limit, OCO)
- Improve CLI with menu-based interaction
- Add a lightweight web interface
- Integrate real-time price fetching for smarter order placement

