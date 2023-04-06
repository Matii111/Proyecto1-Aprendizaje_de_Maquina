import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro

def iqr_function(df,replacement_value):
    for column in df.columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[column][(df[column] < lower_bound) | (df[column] > upper_bound)] = replacement_value
    return df

data = pd.read_excel('p2_serie_de_tiempo.xlsx', engine='openpyxl')

data = data.apply(pd.to_numeric, errors='coerce')

data = data.rename(columns = {'Fecha':'date', 'Horas':'hours','fest':'holiday','Agno':'year',\
                              'Dia_mes':'day_month','Dia_sem':'day_week','Mes':'month'})


table1 = data.iloc[:, 1:3]

table2 = data.iloc[:, 3:8]

table3 = data.iloc[1:, 8:]

# raw data table
table_raw = table3.stack()

# get median value
mediana = table_raw.median()

# IQR TO REPLACE OUTLIERS WITH MEDIAN
table_med = iqr_function(table3, mediana)
table_med = table_med.stack()


# IQR TO REMOVE OUTLIERS
table_outliers = iqr_function(table3, float('nan'))
table_outliers = table_outliers.dropna()
table_outliers = table_outliers.stack()


plt.hist(table_raw,alpha=0.8,edgecolor='black', color='navy',label='Raw Data')
plt.hist(table_med,alpha=0.8,edgecolor='black', color='saddlebrown',label='IQR Data replace by median')
plt.hist(table_outliers,alpha=0.8,edgecolor='black', color='darkgreen',label='IQR Data removed')
plt.legend()
plt.show()


