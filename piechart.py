import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('wine.data')
country_data=df["country"]
medal_data=df["gold_medal"]
plt.pie(medal_data,labels=country_data)
plt.title("Gold medal achivement of five most successful\n"+"countries in 2016 summer olympics")
plt.show()
