
def ranking_number():
    ranking = 0
    if number == 1:
        ranking = 1
        return ranking
    if number == 2:
        ranking = 2
        return ranking
    if number == 3:
        ranking = 3
        return ranking
    if number == 4:
        ranking = 4
        return ranking
    if number == 5:
        ranking = 5
        return ranking
    if number == 0 :
        ranking = 0
        return ranking

def final_weightage():
# using merge function by setting how='inner'
    output = pd.merge(sorted_df_population, sorted_df_crime, sorted_df_education,sorted_df_business,sorted_df_salary
                   on='Parliamentary Constituency',
                   how='inner')
#adding new column for total scores
    output['actual_score'] = output['weighted_population_score'] + output['weighted_crime_score']+output['weighted_business_score'] + output['weighted_salary_score']+ output['weighted_education_score']
    sorted_output= output.sort_values(by='actual_score', ascending=False)


    return sorted_output

