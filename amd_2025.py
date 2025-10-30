import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

amd = yf.Ticker("AMD")
info = amd.get_info()
financials_amd = amd.financials.loc
balance_sheet_amd = amd.balance_sheet.loc

#print("Available rows:", amd.balance_sheet.index.tolist())
#print("Available columns:",amd.balance_sheet.columns.tolist())
#print(amd.financials)
#print(amd.balancesheet)

print("AMD 2025")
print('')

print("Profitability")
amd_ROE_2025 = round(info.get("returnOnEquity"),2)
print(f"Return on Equity (2025): {amd_ROE_2025}")

amd_net_profit_2025 = financials_amd["Net Income"].iloc[0]
amd_revenue_2025 = financials_amd["Total Revenue"].iloc[0]
amd_net_profit_margin_2025 = round((amd_net_profit_2025/amd_revenue_2025)*100, 2)
print(f"Net Profit Margin (2025): {amd_net_profit_margin_2025}%")
print('')

print("Valuation")
amd_PE_ratio_2025 = round(info.get("trailingPE"),2)
print(f"PE Ratio (2025): {amd_PE_ratio_2025}")

amd_PB_ratio_2025 = round(info.get("priceToBook"),2)
print(f"PB Ratio (2025): {amd_PB_ratio_2025}")
print('')

print("Liquidity")
amd_current_assets_2025 = balance_sheet_amd["Current Assets"].iloc[0]
amd_current_liabilities_2025 = balance_sheet_amd["Current Liabilities"].iloc[0]
amd_current_ratio_2025 = round(amd_current_assets_2025/amd_current_liabilities_2025,2)
print(f"Current Ratio (2025): {amd_current_ratio_2025}")

amd_cash_2025 = balance_sheet_amd["Cash And Cash Equivalents"].iloc[0]
amd_short_term_investments_2025 = balance_sheet_amd["Other Short Term Investments"].iloc[0]
amd_recieveables_2025 = balance_sheet_amd["Accounts Receivable"].iloc[0]
amd_quick_assets_2025 = round((amd_cash_2025+amd_short_term_investments_2025+amd_recieveables_2025)/amd_current_liabilities_2025,2)
print(f"Quick Ratio (2025): {amd_quick_assets_2025}")
print('')

print("Leverage")
amd_ebit_2025 = financials_amd["EBIT"].iloc[0]
amd_interest_expense_2025 = financials_amd["Interest Expense"].iloc[0]
amd_interest_coverage_2025 = round(amd_ebit_2025/amd_interest_expense_2025,2)
print(f"Interest Coverage Ratio (2025): {amd_interest_coverage_2025}")

amd_total_liabilities_2025 = balance_sheet_amd["Total Liabilities Net Minority Interest"].iloc[0]
amd_shareholder_equity_2025 = balance_sheet_amd["Stockholders Equity"].iloc[0]
amd_debt_to_equity_2025 = round(amd_total_liabilities_2025/amd_shareholder_equity_2025,2)
print(f"Debt-To-Equity (2025): {amd_debt_to_equity_2025}")
print('')

print("Efficiency")
amd_net_sales_2025 = financials_amd["Total Revenue"].iloc[0]
amd_previous_assets_2025 = balance_sheet_amd["Current Assets"].iloc[1]
amd_average_total_assets_2025 = (amd_current_assets_2025+amd_previous_assets_2025)/2
amd_asset_turnover_2025 = round(amd_net_sales_2025/amd_average_total_assets_2025,2)
print(f"Asset Turnover (2025): {amd_asset_turnover_2025}")

amd_cost_of_goods_sold_2025 = financials_amd["Cost Of Revenue"].iloc[0]
amd_current_inventory_2025 = balance_sheet_amd["Inventory"].iloc[0]
amd_previous_inventory_2025 = balance_sheet_amd["Inventory"].iloc[1]
amd_average_inventory_2025 = (amd_current_inventory_2025+amd_previous_inventory_2025)/2
amd_inventory_turnover_2025 = round((amd_cost_of_goods_sold_2025/amd_average_inventory_2025),2)
print(f"Inventory Turnover (2025): {amd_inventory_turnover_2025}")
print('')


 
