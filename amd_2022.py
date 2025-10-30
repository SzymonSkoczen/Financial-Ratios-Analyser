import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

amd = yf.Ticker("AMD")
info = amd.get_info()
financials_amd = amd.financials.loc
balance_sheet_amd = amd.balance_sheet.loc

#print("Available rows:", amd.financials.index.tolist())
#print("Available columns:",amd.balance_sheet.columns.tolist())
#print(amd.financials)
#print(amd.balancesheet)

print("NVIDIA 2022")
print('')

print("Profitability")
amd_net_income_2022 = financials_amd["Net Income"].iloc[3]
amd_shareholder_equity_2022 = balance_sheet_amd["Stockholders Equity"].iloc[3]
amd_ROE_2022 = round(amd_net_income_2022/amd_shareholder_equity_2022,2)
print(f"Return on Equity (2022): {amd_ROE_2022}")

amd_net_profit_2022 = financials_amd["Net Income"].iloc[3]
amd_revenue_2022 = financials_amd["Total Revenue"].iloc[3]
amd_net_profit_margin_2022 = round((amd_net_profit_2022/amd_revenue_2022)*100, 2)
print(f"Net Profit Margin (2022): {amd_net_profit_margin_2022}%")
print('')

print("Valuation")
amd_eps_2022 = financials_amd["Basic EPS"].iloc[3]
amd_share_price_2022 = amd.history(start="2022-01-31", end="2023-01-31")["Close"].iloc[0]
amd_PE_ratio_2022 = round(amd_share_price_2022/amd_eps_2022,2)
print(f"PE Ratio (2022): {amd_PE_ratio_2022}")

amd_market_price_2022 = amd.history(start="2022-12-31", end="2023-01-31")["Close"].iloc[0]
amd_shares_outstanding_2022 = amd.get_info().get("sharesOutstanding")
amd_book_price_per_share_2022 = amd_shareholder_equity_2022/amd_shares_outstanding_2022
amd_PB_ratio_2022 = round(amd_market_price_2022/amd_book_price_per_share_2022,2)
print(f"PB Ratio (2022): {amd_PB_ratio_2022}")
print('')

print("Liquidity")
amd_current_assets_2022 = balance_sheet_amd["Current Assets"].iloc[3]
amd_current_liabilities_2022 = balance_sheet_amd["Current Liabilities"].iloc[3]
amd_current_ratio_2022 = round(amd_current_assets_2022/amd_current_liabilities_2022,2)
print(f"Current Ratio (2022): {amd_current_ratio_2022}")

amd_cash_2022 = balance_sheet_amd["Cash And Cash Equivalents"].iloc[3]
amd_short_term_investments_2022 = balance_sheet_amd["Other Short Term Investments"].iloc[3]
amd_recieveables_2022 = balance_sheet_amd["Accounts Receivable"].iloc[3]
amd_quick_assets_2022 = round((amd_cash_2022+amd_short_term_investments_2022+amd_recieveables_2022)/amd_current_liabilities_2022,2)
print(f"Quick Ratio (2022): {amd_quick_assets_2022}")
print('')

print("Leverage")
amd_ebit_2022 = financials_amd["EBIT"].iloc[3]
amd_interest_expense_2022 = financials_amd["Interest Expense"].iloc[3]
amd_interest_coverage_2022 = round(amd_ebit_2022/amd_interest_expense_2022,2)
print(f"Interest Coverage Ratio (2022): {amd_interest_coverage_2022}")

amd_total_liabilities_2022 = balance_sheet_amd["Total Liabilities Net Minority Interest"].iloc[3]
amd_debt_to_equity_2022 = round(amd_total_liabilities_2022/amd_shareholder_equity_2022,2)
print(f"Debt-To-Equity (2022): {amd_debt_to_equity_2022}")
print('')

print("Efficiency")
amd_net_sales_2022 = financials_amd["Total Revenue"].iloc[3]
amd_average_total_assets_2022 = (amd_current_assets_2022)/2
amd_asset_turnover_2022 = round(amd_net_sales_2022/amd_average_total_assets_2022,2)
print(f"Asset Turnover (2022): {amd_asset_turnover_2022}")

amd_cost_of_goods_sold_2022 = financials_amd["Cost Of Revenue"].iloc[0]
amd_current_inventory_2022 = balance_sheet_amd["Inventory"].iloc[0]
amd_previous_inventory_2022 = balance_sheet_amd["Inventory"].iloc[1]
amd_average_inventory_2022 = (amd_current_inventory_2022+amd_previous_inventory_2022)/2
amd_inventory_turnover_2022 = round((amd_cost_of_goods_sold_2022/amd_average_inventory_2022),2)
print(f"Inventory Turnover (2022): {amd_inventory_turnover_2022}")
print('')


 
