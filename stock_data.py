import json
import pandas as pd
import pandas_datareader.data as pdr

data_path = "data/"
stock_ext = ".csv"


class StockData:
    def __init__(self, infopath=".certification.json"):
        f = open(infopath, 'r')
        json_dict = json.loads(f.read())
        self.pandas_key = json_dict["pandas_key"]

    def update_stock_data(self, company_code):
        df = pdr.get_data_tiingo(company_code, api_key=self.pandas_key)
        df.to_csv(data_path + company_code + stock_ext)

    def get_stock_data(self, company_code):
        return pd.read_csv(data_path + company_code + stock_ext)


