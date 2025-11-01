import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

nvda = yf.Ticker("NVDA")
info = nvda.get_info()
financials_nvda = nvda.financials.loc
balance_sheet_nvda = nvda.balance_sheet.loc

#print("Available rows:", nvda.financials.index.tolist())
#print("Available columns:",nvda.balance_sheet.columns.tolist())
#print(nvda.financials)
#print(nvda.balancesheet)

#print("NVIDIA 2022")
#print('')

#print("Profitability")
nvda_net_income_2022 = financials_nvda["Net Income"].iloc[3]
nvda_shareholder_equity_2022 = balance_sheet_nvda["Stockholders Equity"].iloc[3]
nvda_ROE_2022 = round(nvda_net_income_2022/nvda_shareholder_equity_2022,2)
#print(f"Return on Equity (2022): {nvda_ROE_2022}")

nvda_net_profit_2022 = financials_nvda["Net Income"].iloc[3]
nvda_revenue_2022 = financials_nvda["Total Revenue"].iloc[3]
nvda_net_profit_margin_2022 = round((nvda_net_profit_2022/nvda_revenue_2022)*100, 2)
#print(f"Net Profit Margin (2022): {nvda_net_profit_margin_2022}%")
#print('')

#print("Valuation")
nvda_eps_2022 = financials_nvda["Basic EPS"].iloc[3]
nvda_share_price_2022 = nvda.history(start="2022-01-31", end="2023-01-31")["Close"].iloc[0]
nvda_PE_ratio_2022 = round(nvda_share_price_2022/nvda_eps_2022,2)
#print(f"PE Ratio (2022): {nvda_PE_ratio_2022}")

nvda_market_price_2022 = nvda.history(start="2022-12-31", end="2023-01-31")["Close"].iloc[0]
nvda_shares_outstanding_2022 = nvda.get_info().get("sharesOutstanding")
nvda_book_price_per_share_2022 = nvda_shareholder_equity_2022/nvda_shares_outstanding_2022
nvda_PB_ratio_2022 = round(nvda_market_price_2022/nvda_book_price_per_share_2022,2)
#print(f"PB Ratio (2022): {nvda_PB_ratio_2022}")
#print('')

#print("Liquidity")
nvda_current_assets_2022 = balance_sheet_nvda["Current Assets"].iloc[3]
nvda_current_liabilities_2022 = balance_sheet_nvda["Current Liabilities"].iloc[3]
nvda_current_ratio_2022 = round(nvda_current_assets_2022/nvda_current_liabilities_2022,2)
#print(f"Current Ratio (2022): {nvda_current_ratio_2022}")

nvda_cash_2022 = balance_sheet_nvda["Cash And Cash Equivalents"].iloc[3]
nvda_short_term_investments_2022 = balance_sheet_nvda["Other Short Term Investments"].iloc[3]
nvda_recieveables_2022 = balance_sheet_nvda["Accounts Receivable"].iloc[3]
nvda_quick_assets_2022 = round((nvda_cash_2022+nvda_short_term_investments_2022+nvda_recieveables_2022)/nvda_current_liabilities_2022,2)
#print(f"Quick Ratio (2022): {nvda_quick_assets_2022}")
#print('')

#print("Leverage")
nvda_ebit_2022 = financials_nvda["EBIT"].iloc[3]
nvda_interest_expense_2022 = financials_nvda["Interest Expense"].iloc[3]
nvda_interest_coverage_2022 = round(nvda_ebit_2022/nvda_interest_expense_2022,2)
#print(f"Interest Coverage Ratio (2022): {nvda_interest_coverage_2022}")

nvda_total_liabilities_2022 = balance_sheet_nvda["Total Liabilities Net Minority Interest"].iloc[3]
nvda_debt_to_equity_2022 = round(nvda_total_liabilities_2022/nvda_shareholder_equity_2022,2)
#print(f"Debt-To-Equity (2022): {nvda_debt_to_equity_2022}")
#print('')

#print("Efficiency")
nvda_net_sales_2022 = financials_nvda["Total Revenue"].iloc[3]
nvda_average_total_assets_2022 = (nvda_current_assets_2022)/2
nvda_asset_turnover_2022 = round(nvda_net_sales_2022/nvda_average_total_assets_2022,2)
#print(f"Asset Turnover (2022): {nvda_asset_turnover_2022}")

nvda_cost_of_goods_sold_2022 = financials_nvda["Cost Of Revenue"].iloc[0]
nvda_current_inventory_2022 = balance_sheet_nvda["Inventory"].iloc[0]
nvda_previous_inventory_2022 = balance_sheet_nvda["Inventory"].iloc[1]
nvda_average_inventory_2022 = (nvda_current_inventory_2022+nvda_previous_inventory_2022)/2
nvda_inventory_turnover_2022 = round((nvda_cost_of_goods_sold_2022/nvda_average_inventory_2022),2)
#print(f"Inventory Turnover (2022): {nvda_inventory_turnover_2022}")
#print('')


 
