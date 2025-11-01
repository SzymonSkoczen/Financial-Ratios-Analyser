import nvidia_2025
#import nvidia_2022
#import intc_2025



def higher_lower(a, b, a_name, b_name):
    if a > b:
        print(f"The {a_name} ratio of {a} was greater than the {b_name} ratio of {b}")
    else:
        print(f"The {b_name} ratio of {b} was greater than the {a_name} ratio of {a}")

#def compare_ratios(file_name_a, file_name_b, ticker_a, ticker_b, company_name_a, company_name_b, year_a, year_b):

    #def create_names(file_name_a, file_name_b, ticker_a, ticker_b,  year_a, year_b)
        #a = (str(file_name_a)+"."+str(ticker_a)+"_"+c+"_year_a")
    #print("Profitability")
    #higher_lower(file_name_and_ratio_a, file_name_and_ratio_b, company_name_a, company_name_b)          





#compare_ratios(nvidia_2025.nvda_PE_ratio_2025, intc_2025.intc_PE_ratio_2025, "NVIDIA PE Ratio 2025", "INTEL PE Ratio 2025")

#nvidia_2025.nvda_asset_turnover_2025
#"NVIDIA Asset Turnover 2022"

#higher_lower(nvidia_2025.nvda_PE_ratio_2025,nvidia_2022.nvda_PE_ratio_2022, "NVIDIA PE Ratio " \
#" 2025", "NVIDIA PE Ratio 2022")

def create_names(file_name_a, ticker_a, year_a,):
        c = "PE_Ratio"
        a = (str(file_name_a)+"."+str(ticker_a)+"_"+c+year_a)
        print(a)

create_names(nvidia_2025, "nvda", "2025")