import pandas as pd

# importing data
data_1 = 'parliamentary-constituency-profiles-data.csv'
data_2 = 'Ranking_Scores.csv'
df_population = pd.read_csv(data_1, usecols=["Parliamentary Constituency", 'Persons-2008'])
df_crime = pd.read_csv(data_1, usecols=["Parliamentary Constituency", 'Total Notifiable Offences-2009'])
df_ranking = pd.read_csv(data_2)

# cleaning data
df_population = df_population.dropna()
df_population = df_population.reset_index(drop=True)

df_crime = df_crime.dropna()
df_crime = df_crime.reset_index(drop=True)

# Removing the total
df_population = df_population[:-2]
sorted_df_population = df_population.sort_values(by='Persons-2008', ascending=False)

df_crime = df_crime[:-1]
sorted_df_crime = df_crime.sort_values(by='Total Notifiable Offences-2009', ascending=True)

# reset index
sorted_df_crime .reset_index(drop=True, inplace=True)
sorted_df_population.reset_index(drop=True, inplace=True)

# add new column
scores = df_ranking.Scores.to_list()
sorted_df_crime["crime_score"] = scores
sorted_df_population["population_score"] = scores

# weightage
A = 5
B = 4
total = A + B

# adding weighted score
sorted_df_crime['weighted_crime_score'] = (sorted_df_crime["crime_score"]*A)/total
sorted_df_population["weighted_population_score"] = (sorted_df_population["population_score"]*B)/total

# using merge function by setting how='inner'
output = pd.merge(sorted_df_population, sorted_df_crime,
                   on='Parliamentary Constituency',
                   how='inner')

# displaying result
output['actual_score'] = output['weighted_population_score'] + output['weighted_crime_score']
sorted_output= output.sort_values(by='actual_score', ascending=False)

print(sorted_output)
