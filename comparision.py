import nvidia_2025


from prettytable import PrettyTable 

# specify the Column Names while initializing the Table 
table = PrettyTable(["Company Name", "Year", "ROE", "Net Profit Margin",
                     "P/E", "P/B", "Current Ratio", "Quick Ratio",
                    "Debt-to-Equit", "Interest Coverage", "Asset Turnover",
                    "Inventory Turnover"]) 

# add rows 
table.add_row(["NVDIA", "2025", nvidia_2025.nvda_ROE_2025, nvidia_2025.nvda_net_profit_margin_2025, nvidia_2025.nvda_PE_ratio_2025,
               nvidia_2025.nvda_PB_ratio_2025, nvidia_2025.nvda_current_ratio_2025, nvidia_2025.nvda_quick_assets_2025,
               nvidia_2025.nvda_interest_coverage_2025, nvidia_2025.nvda_debt_to_equity_2025, nvidia_2025.nvda_asset_turnover_2025,
               nvidia_2025.nvda_inventory_turnover_2025]) 

print(table)

