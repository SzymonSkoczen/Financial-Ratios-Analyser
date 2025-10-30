import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

intc = yf.Ticker("INTC")
info = intc.get_info()
financials_intc = intc.financials.loc
balance_sheet_intc = intc.balance_sheet.loc

#print("Available rows:", intc.financials.index.tolist())
#print("Available columns:",intc.balance_sheet.columns.tolist())
#print(intc.financials)
#print(intc.balancesheet)

print("INTEL 2022")
print('')

print("Profitability")
intc_net_income_2022 = financials_intc["Net Income"].iloc[3]
intc_shareholder_equity_2022 = balance_sheet_intc["Stockholders Equity"].iloc[3]
intc_ROE_2022 = round(intc_net_income_2022/intc_shareholder_equity_2022,2)
print(f"Return on Equity (2022): {intc_ROE_2022}")

intc_net_profit_2022 = financials_intc["Net Income"].iloc[3]
intc_revenue_2022 = financials_intc["Total Revenue"].iloc[3]
intc_net_profit_margin_2022 = round((intc_net_profit_2022/intc_revenue_2022)*100, 2)
print(f"Net Profit Margin (2022): {intc_net_profit_margin_2022}%")
print('')

print("Valuation")
intc_eps_2022 = financials_intc["Basic EPS"].iloc[3]
intc_share_price_2022 = intc.history(start="2022-01-31", end="2023-01-31")["Close"].iloc[0]
intc_PE_ratio_2022 = round(intc_share_price_2022/intc_eps_2022,2)
print(f"PE Ratio (2022): {intc_PE_ratio_2022}")

intc_market_price_2022 = intc.history(start="2022-12-31", end="2023-01-31")["Close"].iloc[0]
intc_shares_outstanding_2022 = intc.get_info().get("sharesOutstanding")
intc_book_price_per_share_2022 = intc_shareholder_equity_2022/intc_shares_outstanding_2022
intc_PB_ratio_2022 = round(intc_market_price_2022/intc_book_price_per_share_2022,2)
print(f"PB Ratio (2022): {intc_PB_ratio_2022}")
print('')

print("Liquidity")
intc_current_assets_2022 = balance_sheet_intc["Current Assets"].iloc[3]
intc_current_liabilities_2022 = balance_sheet_intc["Current Liabilities"].iloc[3]
intc_current_ratio_2022 = round(intc_current_assets_2022/intc_current_liabilities_2022,2)
print(f"Current Ratio (2022): {intc_current_ratio_2022}")

intc_cash_2022 = balance_sheet_intc["Cash And Cash Equivalents"].iloc[3]
intc_short_term_investments_2022 = balance_sheet_intc["Other Short Term Investments"].iloc[3]
intc_recieveables_2022 = balance_sheet_intc["Accounts Receivable"].iloc[3]
intc_quick_assets_2022 = round((intc_cash_2022+intc_short_term_investments_2022+intc_recieveables_2022)/intc_current_liabilities_2022,2)
print(f"Quick Ratio (2022): {intc_quick_assets_2022}")
print('')

print("Leverage")
intc_ebit_2022 = financials_intc["EBIT"].iloc[3]
intc_interest_expense_2022 = financials_intc["Interest Expense"].iloc[3]
intc_interest_coverage_2022 = round(intc_ebit_2022/intc_interest_expense_2022,2)
print(f"Interest Coverage Ratio (2022): {intc_interest_coverage_2022}")

intc_total_liabilities_2022 = balance_sheet_intc["Total Liabilities Net Minority Interest"].iloc[3]
intc_debt_to_equity_2022 = round(intc_total_liabilities_2022/intc_shareholder_equity_2022,2)
print(f"Debt-To-Equity (2022): {intc_debt_to_equity_2022}")
print('')

print("Efficiency")
intc_net_sales_2022 = financials_intc["Total Revenue"].iloc[3]
intc_average_total_assets_2022 = (intc_current_assets_2022)/2
intc_asset_turnover_2022 = round(intc_net_sales_2022/intc_average_total_assets_2022,2)
print(f"Asset Turnover (2022): {intc_asset_turnover_2022}")

intc_cost_of_goods_sold_2022 = financials_intc["Cost Of Revenue"].iloc[0]
intc_current_inventory_2022 = balance_sheet_intc["Inventory"].iloc[0]
intc_previous_inventory_2022 = balance_sheet_intc["Inventory"].iloc[1]
intc_average_inventory_2022 = (intc_current_inventory_2022+intc_previous_inventory_2022)/2
intc_inventory_turnover_2022 = round((intc_cost_of_goods_sold_2022/intc_average_inventory_2022),2)
print(f"Inventory Turnover (2022): {intc_inventory_turnover_2022}")
print('')


 
