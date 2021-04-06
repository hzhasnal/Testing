import pandas as pd

# importing data
data_1 = 'parliamentary-constituency-profiles-data.csv'
data_2 = 'Ranking_Scores.csv'
df_crime = pd.read_csv(data_1, usecols=["Parliamentary Constituency", 'Total Notifiable Offences-2009'])
df_ranking = pd.read_csv(data_2)
# cleaning data
df_crime = df_crime.dropna()
df_crime = df_crime.reset_index(drop=True)


# Removing the total
df_crime = df_crime[:-1]
sorted_df_crime = df_crime.sort_values(by='Total Notifiable Offences-2009', ascending=True)

length = len(sorted_df_crime)

# reset index
sorted_df_crime .reset_index(drop=True, inplace=True)


# add new column
scores = df_ranking.Scores.to_list()
sorted_df_crime["crime_score"] = scores
print(sorted_df_crime)
