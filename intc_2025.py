import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

intc = yf.Ticker("INTC")
info = intc.get_info()
financials_intc = intc.financials.loc
balance_sheet_intc = intc.balance_sheet.loc

#print("Available rows:", intc.balance_sheet.index.tolist())
#print("Available columns:", intc.balance_sheet.columns.tolist())
#print(intc.financials)
#print(intc.balancesheet)

print("INTEL 2025")
print('')

print("Profitability")
intc_ROE_2025 = round(info.get("returnOnEquity"),2)
print(f"Return on Equity (2025): {intc_ROE_2025}")

intc_net_profit_2025 = financials_intc["Net Income"].iloc[0]
intc_revenue_2025 = financials_intc["Total Revenue"].iloc[0]
intc_net_profit_margin_2025 = round((intc_net_profit_2025/intc_revenue_2025)*100, 2)
print(f"Net Profit Margin (2025): {intc_net_profit_margin_2025}%")
print('')

print("Valuation")
intc_PE_ratio_2025 = round(info.get("trailingPE"),2)
print(f"PE Ratio (2025): {intc_PE_ratio_2025}")

intc_PB_ratio_2025 = round(info.get("priceToBook"),2)
print(f"PB Ratio (2025): {intc_PB_ratio_2025}")
print('')

print("Liquidity")
intc_current_assets_2025 = balance_sheet_intc["Current Assets"].iloc[0]
intc_current_liabilities_2025 = balance_sheet_intc["Current Liabilities"].iloc[0]
intc_current_ratio_2025 = round(intc_current_assets_2025/intc_current_liabilities_2025,2)
print(f"Current Ratio (2025): {intc_current_ratio_2025}")

intc_cash_2025 = balance_sheet_intc["Cash And Cash Equivalents"].iloc[0]
intc_short_term_investments_2025 = balance_sheet_intc["Other Short Term Investments"].iloc[0]
intc_recieveables_2025 = balance_sheet_intc["Accounts Receivable"].iloc[0]
intc_quick_assets_2025 = round((intc_cash_2025+intc_short_term_investments_2025+intc_recieveables_2025)/intc_current_liabilities_2025,2)
print(f"Quick Ratio (2025): {intc_quick_assets_2025}")
print('')

print("Leverage")
intc_ebit_2025 = financials_intc["EBIT"].iloc[0]
intc_interest_expense_2025 = financials_intc["Interest Expense"].iloc[0]
intc_interest_coverage_2025 = round(intc_ebit_2025/intc_interest_expense_2025,2)
print(f"Interest Coverage Ratio (2025): {intc_interest_coverage_2025}")

intc_total_liabilities_2025 = balance_sheet_intc["Total Liabilities Net Minority Interest"].iloc[0]
intc_shareholder_equity_2025 = balance_sheet_intc["Stockholders Equity"].iloc[0]
intc_debt_to_equity_2025 = round(intc_total_liabilities_2025/intc_shareholder_equity_2025,2)
print(f"Debt-To-Equity (2025): {intc_debt_to_equity_2025}")
print('')

print("Efficiency")
intc_net_sales_2025 = financials_intc["Total Revenue"].iloc[0]
intc_previous_assets_2025 = balance_sheet_intc["Current Assets"].iloc[1]
intc_average_total_assets_2025 = (intc_current_assets_2025+intc_previous_assets_2025)/2
intc_asset_turnover_2025 = round(intc_net_sales_2025/intc_average_total_assets_2025,2)
print(f"Asset Turnover (2025): {intc_asset_turnover_2025}")

intc_cost_of_goods_sold_2025 = financials_intc["Cost Of Revenue"].iloc[0]
intc_current_inventory_2025 = balance_sheet_intc["Inventory"].iloc[0]
intc_previous_inventory_2025 = balance_sheet_intc["Inventory"].iloc[1]
intc_average_inventory_2025 = (intc_current_inventory_2025+intc_previous_inventory_2025)/2
intc_inventory_turnover_2025 = round((intc_cost_of_goods_sold_2025/intc_average_inventory_2025),2)
print(f"Inventory Turnover (2025): {intc_inventory_turnover_2025}")
print('')


 
