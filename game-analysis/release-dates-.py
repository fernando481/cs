import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("game-rating-by-release-dates.cvs")

#clean up data,
df["first_release_date"] = pd.to_datetime(df["first_release_date"])

# Analyze data though visualization.
plt.scatter(df["first_release_date"],df["critic_rating_value"],color = "blue",label = "critic ratings")
plt.scatter (df["first_relase_data"], df["user_rating_value"],color = "red" ,label = "user rating" )

plt.legend(loc = "upper left ")

plt.show()