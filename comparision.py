import nvidia_2025
import nvidia_2022
from prettytable import PrettyTable 


nvda_table_2025 = PrettyTable(["Company Name", "Year", "ROE", "Net Profit Margin",
                     "P/E", "P/B", "Current Ratio", "Quick Ratio",
                    "Debt-to-Equit", "Interest Coverage", "Asset Turnover",
                    "Inventory Turnover"]) 

 
nvda_table_2025.add_row(["NVDIA", "2025", nvidia_2025.nvda_ROE_2025, nvidia_2025.nvda_net_profit_margin_2025, nvidia_2025.nvda_PE_ratio_2025,
               nvidia_2025.nvda_PB_ratio_2025, nvidia_2025.nvda_current_ratio_2025, nvidia_2025.nvda_quick_assets_2025,
               nvidia_2025.nvda_interest_coverage_2025, nvidia_2025.nvda_debt_to_equity_2025, nvidia_2025.nvda_asset_turnover_2025,
               nvidia_2025.nvda_inventory_turnover_2025]) 

#print(nvda_table_2025)

nvda_table_2022 = PrettyTable(["Company Name", "Year", "ROE", "Net Profit Margin",
                     "P/E", "P/B", "Current Ratio", "Quick Ratio",
                    "Debt-to-Equit", "Interest Coverage", "Asset Turnover",
                    "Inventory Turnover"])

nvda_table_2022.add_row(["NVDIA", "2022", nvidia_2022.nvda_ROE_2022, nvidia_2022.nvda_net_profit_margin_2022, nvidia_2022.nvda_PE_ratio_2022,
               nvidia_2022.nvda_PB_ratio_2022, nvidia_2022.nvda_current_ratio_2022, nvidia_2022.nvda_quick_assets_2022,
               nvidia_2022.nvda_interest_coverage_2022, nvidia_2022.nvda_debt_to_equity_2022, nvidia_2022.nvda_asset_turnover_2022,
               nvidia_2022.nvda_inventory_turnover_2022])

#print(nvda_table_2022)

def higher_lower(a, b, a_name, b_name):
    if a > b:
        print(f"The {a_name} ratio of {a} was greater than the {b_name} ratio of {b}")
    else:
        print(f"The {b_name} ratio of {b} was greater than the {a_name} ratio of {a}")

print("Profitability")
higher_lower(nvidia_2025.nvda_ROE_2025,nvidia_2022.nvda_ROE_2022, "NVIDIA ROE 2025", "NVIDIA ROE 2022")
higher_lower(nvidia_2025.nvda_net_profit_margin_2025,nvidia_2022.nvda_net_profit_margin_2022, "NVIDIA Net Profit " \
"Margin 2025", "NVIDIA Net Profit Margin 2022")
print("")

print("Valuation")
higher_lower(nvidia_2025.nvda_PE_ratio_2025,nvidia_2022.nvda_PE_ratio_2022, "NVIDIA PE Ratio " \
" 2025", "NVIDIA PE Ratio 2022")
higher_lower(nvidia_2025.nvda_PB_ratio_2025,nvidia_2022.nvda_PB_ratio_2022, "NVIDIA PB Ratio " \
" 2025", "NVIDIA PB Ratio 2022")
print("")

print("Liquidity")
higher_lower(nvidia_2025.nvda_current_ratio_2025,nvidia_2022.nvda_current_ratio_2022, "NVIDIA Current Ratio " \
" 2025", "NVIDIA Current Ratio 2022")
higher_lower(nvidia_2025.nvda_quick_assets_2025,nvidia_2022.nvda_quick_assets_2022, "NVIDIA Quick Assets Ratio " \
" 2025", "NVIDIA Quick Assets Ratio 2022")
print("")

print("Leverage")
higher_lower(nvidia_2025.nvda_interest_coverage_2025,nvidia_2022.nvda_interest_coverage_2022, "NVIDIA Interest Coverage " \
" 2025", "NVIDIA Interest Coverage 2022")
higher_lower(nvidia_2025.nvda_debt_to_equity_2025,nvidia_2022.nvda_debt_to_equity_2022, "NVIDIA Debt-to-Equity Ratio " \
" 2025", "NVIDIA Debt-to-Equity Ratio 2022")
print("")

print("Efficiency")
higher_lower(nvidia_2025.nvda_asset_turnover_2025,nvidia_2022.nvda_asset_turnover_2022, "NVIDIA Asset Turnover Ratio " \
" 2025", "NVIDIA Asset Turnover 2022")
higher_lower(nvidia_2025.nvda_inventory_turnover_2025,nvidia_2022.nvda_inventory_turnover_2022, "NVIDIA Inventory Turnover Ratio " \
" 2025", "NVIDIA Inventory Turnover 2022")
print("")