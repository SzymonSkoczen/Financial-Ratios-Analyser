import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

nvda = yf.Ticker("NVDA")
info = nvda.get_info()

#print("Available rows:", nvda.balance_sheet.index.tolist())
#print("Available columns:",nvda.balance_sheet.columns.tolist())
#print(nvda.financials)
#print(nvda.balancesheet)

print("NVIDIA 2025")

print("Profitability")
nvda_ROE_2025 = round(info.get("returnOnEquity"),2)
print(f"Return on Equity (2025): {nvda_ROE_2025}")

nvda_net_profit_2025 = nvda.financials.loc["Net Income"].iloc[0]
nvda_revenue_2025 = nvda.financials.loc["Total Revenue"].iloc[0]
nvda_net_profit_margin_2025 = round((nvda_net_profit_2025/nvda_revenue_2025)*100, 2)
print(f"Net Profit Margin (2025): {nvda_net_profit_margin_2025}%")
print('')

print("Valuation")
nvda_PE_ratio_2025 = round(info.get("trailingPE"),2)
print(f"PE Ratio (2025): {nvda_PE_ratio_2025}")

nvda_PB_ratio_2025 = round(info.get("priceToBook"),2)
print(f"PB Ratio (2025): {nvda_PB_ratio_2025}")
print('')

print("Liquidity")
nvda_current_assets_2025 = nvda.balance_sheet.loc["Current Assets"].iloc[0]
nvda_current_liabilities_2025 = nvda.balance_sheet.loc["Current Liabilities"].iloc[0]
nvda_current_ratio_2025 = round(nvda_current_assets_2025/nvda_current_liabilities_2025,2)
print(f"Current Ratio (2025): {nvda_current_ratio_2025}")

nvda_cash_2025 = nvda.balance_sheet.loc["Cash And Cash Equivalents"].iloc[0]
nvda_short_term_investments_2025 = nvda.balance_sheet.loc["Other Short Term Investments"].iloc[0]
nvda_recieveables_2025 = nvda.balance_sheet.loc["Accounts Receivable"].iloc[0]
nvda_quick_assets_2025 = round((nvda_cash_2025+nvda_short_term_investments_2025+nvda_recieveables_2025)/nvda_current_liabilities_2025,2)
print(f"Quick Ratio (2025): {nvda_quick_assets_2025}")
print('')

print("Leverage")
nvda_ebit_2025 = nvda.financials.loc["EBIT"].iloc[0]
nvda_interest_expense_2025 = nvda.financials.loc["Interest Expense"].iloc[0]
nvda_interest_coverage_2025 = round(nvda_ebit_2025/nvda_interest_expense_2025,2)
print(f"Interest Coverage Ratio (2025): {nvda_interest_coverage_2025}")

nvda_total_liabilities_2025 = nvda.balance_sheet.loc["Total Liabilities Net Minority Interest"].iloc[0]
nvda_shareholder_equity_2025 = nvda.balance_sheet.loc["Stockholders Equity"].iloc[0]
nvda_debt_to_equity_2025 = round(nvda_total_liabilities_2025/nvda_shareholder_equity_2025,2)
print(f"Debt-To-Equity (2025): {nvda_debt_to_equity_2025}")
print('')

print("Efficiency")
nvda_net_sales_2025 = nvda.financials.loc["Total Revenue"].iloc[0]
nvda_previous_assets_2025 = nvda.balance_sheet.loc["Current Assets"].iloc[1]
nvda_average_total_assets_2025 = (nvda_current_assets_2025+nvda_previous_assets_2025)/2
nvda_asset_turnover_2025 = round(nvda_net_sales_2025/nvda_average_total_assets_2025,2)
print(f"Asset Turnover (2025): {nvda_asset_turnover_2025}")

nvda_cost_of_goods_sold_2025 = nvda.financials.loc["Cost Of Revenue"].iloc[0]
nvda_current_inventory_2025 = nvda.balance_sheet.loc["Inventory"].iloc[0]
nvda_previous_inventory_2025 = nvda.balance_sheet.loc["Inventory"].iloc[1]
nvda_average_inventory_2025 = (nvda_current_inventory_2025+nvda_previous_inventory_2025)/2
nvda_inventory_turnover_2025 = round((nvda_cost_of_goods_sold_2025/nvda_average_inventory_2025),2)
print(f"Inventory Turnover (2025): {nvda_inventory_turnover_2025}")
print('')


 
