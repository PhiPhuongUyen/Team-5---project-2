import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
from pandasql import sqldf
import numpy as np

url = "https://raw.githubusercontent.com/PhiPhuongUyen/Team-5/main/marketing_campaign.csv"
df= pd.read_csv(url, sep="\t")
pysqldf = lambda q: sqldf(q, globals())
print(df)


df1=pysqldf("SELECT ID, Year_Birth, Income, Dt_Customer, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth\
             FROM df")

print(df1)


df1["Spent"] = df1["MntWines"]+ df1["MntFruits"]+ df1["MntMeatProducts"]+ df1["MntFishProducts"]+ df1["MntSweetProducts"]+ df1["MntGoldProds"]
df1=df1.rename(columns={"MntWines": "Wines","MntFruits":"Fruits","MntMeatProducts":"Meat","MntFishProducts":"Fish","MntSweetProducts":"Sweets","MntGoldProds":"Gold"})
to_drop = ["ID"]
df1 = df1.drop(to_drop, axis=1)

dfscatters=df1[['Income','Spent']]
plt.scatter(dfscatters['Income'], dfscatters['Spent'], color='orange', s=30, marker='*')

plt.ylabel("Spent")
plt.xlabel("Income")
plt.title("RELATIONSHIP BETWEEN REVENUES AND EXPENDITURES")
plt.show()




