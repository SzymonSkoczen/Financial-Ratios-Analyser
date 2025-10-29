import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

nvda = yf.Ticker("NVDA")
info = nvda.get_info()

#print("P/E Ratio:", info.get("trailingPE"))
#print("Price-to-Book:", info.get("priceToBook"))
#print("Return on Equity:", info.get("returnOnEquity"))
#print("Net Profit:", info.get("netProfit"))
#print(nvda.financials)
ebit_2025 = nvda.financials.loc["EBIT", "2025-01-31"]
interest_expense_2025 = nvda.financials.loc["Interest Expense", "2025-01-31"]
interest_coverage = ebit_2025/interest_expense_2025
#print(f"Interest Coverage Ratio (2025): {interest_coverage}")
total_liabilities_2025 = nvda.balance_sheet.loc["Total Liabilities Net Minority Interest"].iloc[0]
shareholder_equity_2025 = nvda.balance_sheet.loc["Stockholders Equity"].iloc[0]
debt_to_equity = total_liabilities_2025/shareholder_equity_2025
print(f"Debt-To-Equity (2025): {debt_to_equity}")
 
