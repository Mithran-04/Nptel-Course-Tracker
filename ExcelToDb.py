import sqlite3
import pandas as pd
cnn=None
filename="Exdataa.db"
try:
    df=pd.read_excel(r"C:\Users\mithr\Downloads\4_Odd 2022-23_IT_NPTEL.xlsx",header=0,engine='openpyxl')
    cnn=sqlite3.connect(filename)
    df.to_sql('Ex_Data',cnn,if_exists='replace')
except Exception as e:
    print(e)
finally:
    if cnn:
        cnn.close()



