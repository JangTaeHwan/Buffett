import sys

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

from stock_data import *


if __name__ == "__main__":
    print(sys.version_info)

    st = StockData()

#    st.update_stock_data("AAPL")
    df = st.get_stock_data("AAPL")

    print(df.tail())

    df1 = df.reset_index()['close']

    print(df1.shape)

