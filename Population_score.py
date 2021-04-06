import pandas as pd

# importing data
data_1 = 'parliamentary-constituency-profiles-data.csv'
data_2 = 'Ranking_Scores.csv'
df_population = pd.read_csv(data_1, usecols=["Parliamentary Constituency", 'Persons-2008'])
df_ranking = pd.read_csv(data_2)
# cleaning data
df_population = df_population.dropna()
df_population = df_population.reset_index(drop=True)


# Removing the total
df_population = df_population[:-2]
sorted_df_population = df_population.sort_values(by='Persons-2008', ascending=False)

length = len(sorted_df_population)

# reset index
sorted_df_population.reset_index(drop=True, inplace=True)


# add new column
scores = df_ranking.Scores.to_list()
sorted_df_population["population_score"] = scores
print(sorted_df_population)
