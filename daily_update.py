import tushare as ts
import pandas as pd
import os
from datetime import date, datetime

# Please enter your token (minimum 120 credits required for this code)
pro = ts.pro_api("14beec506af6057d5a5795e6ea344b974783b2e0bd4b7679bffcc843")
# ("Please enter your token hear!")

file_path = r"..\Stock History\history"

# all the listed stocks' codes and list dates
listed_stocks = list(
    pro.stock_basic(exchange='', list_status='L',
                    fields='ts_code, list_date')['ts_code'])

# get daily data for each stock
for each_stock in listed_stocks:
    df_each = pro.daily(ts_code=each_stock,
                        trade_date=datetime.strftime(date.today(), "%Y%m%d"))
    df_each["trade_date"] = pd.to_datetime(df_each["trade_date"])
    df_each.to_csv(os.path.join(file_path, each_stock + ".csv"),
                   index=False,
                   mode='a')

print("Finish Update!")
