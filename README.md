# daily_update

The purpose to this code is to update daily stock data to the previously stored csv files. In this code, we will retrieve the index data from Tushare for analyzing. Tushare is a free and open financial big data platform of all data categories. You can easily retrieve the data you want by simply a few lines of code, and do not need to worry about the integrality and the accuracy of the data, which will greatly improve the productivity and eliminate the need for data preprocessing.

If you would like to have a try, please register through the following link: https://tushare.pro/register?reg=456046.

Codes:

First, we need to import tushare and pandas (You can get your token from Profile-TOKEN and the index code from Data Api), and set the dictory path.

    import tushare as ts
    import pandas as pd
    import os
    from datetime import date, datetime

    # Please enter your token (minimum 120 credits required for this code)
    pro = ts.pro_api("Please enter your token hear!")

    file_path = r"..\Stock History\history"
 
 Second, retrieve all the listed stocks's ts_code, which will be used to retrieve daily history of each stock later.
 
    # all the listed stocks' codes and list dates
    listed_stocks = list(
        pro.stock_basic(exchange='', list_status='L',
                        fields='ts_code, list_date')['ts_code'])
 
Finally, retrieve each stocks' today's data and append them in each csv file.

    # get daily data for each stock
    for each_stock in listed_stocks:
        df_each = pro.daily(ts_code=each_stock,
                            trade_date=datetime.strftime(date.today(), "%Y%m%d"))
        df_each["trade_date"] = pd.to_datetime(df_each["trade_date"])
        df_each.to_csv(os.path.join(file_path, each_stock + ".csv"),
                       index=False,
                       mode='a')

    print("Finish Update!")

P.S.
Next code will be the encapsulation of the previous code.
