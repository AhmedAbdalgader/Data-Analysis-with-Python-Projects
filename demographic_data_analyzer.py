import pandas as pd


def calculate_demographic_data(print_data=True):
# Read data from file
    df = pd.read_csv('adult.data.csv')
    # print(df.head())
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    df1 = pd.read_csv('adult.data.csv')
    race_count = df1.groupby('race')['race'].count().sort_values(ascending=False)
    # race_count_values = df['race'].value_counts()
    # print(race_count_values.head())
    # print(type(race_count_values))
    # print(race_count.head())
    # print(type(race_count))
    # print(race_count.info())
    # print(race_count.describe())
    # print(race_count)
    # What is the average age of men?
    df2 = df1.loc[:, ['age','sex']]
    # print(df2.head())
    df2 = df2[df2['sex']== 'Male']
    # print(df2['age'].mean())
    average_age_men = round(df2['age'].mean(), 1) # !=39.4
    # print('average_age_men: ', average_age_men)
    # What is the percentage of people who have a Bachelor's degree?
    # df3 = df1.loc[:, ['education']]
    # print(df3.head())
    # df31 = df1['education'].value_counts()['Bachelors'] # 5355
    df31 = df1['education'].value_counts().sum() # 32561
    # print(df31)
    # Bachelors = 5355
    # All = 32561
    df3 = df[df['education'] == 'Bachelors']['education']
    # print(df3.count())
    percentage_bachelors = round(df3.count()/df31*100, 1) # 16.44605509658794 !=16.4
    # print(df3.groupby('education').count()/df.count()*100)
    # print(percentage_bachelors)


    # # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    df4 = df1.loc[:, ['education', 'salary']]
    # print(df4.head())
    df41 = df4[(df4['education'] == 'Bachelors') | (df4['education'] == 'Masters') | (df4['education'] == 'Doctorate')  ]
    # print(df41.head())
    df42 = df41[ df41['salary'] == '>50K']
    # print(df42.shape)
    percent =  df42.count()/df41.count()*100
    higher_education_rich = round(percent.iloc[0], 1) # 10.706059396210192 !=46.5
    # print(higher_education_rich)

    # # What percentage of people without advanced education make more than 50K?

    # # with and without `Bachelors`, `Masters`, or `Doctorate`
    # higher_education = df4[(df4['education'] == 'Bachelors') | (df4['education'] == 'Masters') | (df4['education'] == 'Doctorate')  ]
    df51 =  df4[~((df4['education'] == 'Bachelors') | (df4['education'] == 'Masters') | (df4['education'] == 'Doctorate'))]
    # print(df51.head())
    # print(df51.shape)
    df52 = df51[ df51['salary'] == '>50K']
    # print(df52.shape)
    percent2 =  df52.count()/df51.count()*100
    lower_education_rich = round(percent2.iloc[0], 1) # 13.374896348392248 !=17.4
    # print(lower_education_rich)
    # # percentage with salary >50K
    # # df6 = 
    # # print(df6)
    # higher_education_rich = higher_education[higher_education == '>50K'].count()/df4.count()*100
    # lower_education_rich =  lower_education[lower_education == '>50K'].count()/df4.count()*100
    # print(higher_education_rich)

    # # What is the minimum number of hours a person works per week (hours-per-week feature)?
    df6 = df.loc[:, ['hours-per-week']]
    # print(df6.value_counts())
    # print(type(df6))
    # print(df6.min())
    min_work_hours = df6['hours-per-week'].min()
    # print(min_work_hours)

    # # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df7 = df.loc[:, ['hours-per-week', 'salary']]
    # print(df7.head())
    df71 = df7[df7['hours-per-week'] == min_work_hours]
    # print(df71.head())
    # print(df71.shape)
    # df72 = df7[(df7['hours-per-week'] == min_work_hours) & (df7['salary'] == '>50K')] # two filters at once.
    df72 = df71[df71['salary'] == '>50K']
    # print(df72.head())
    # print(df72.shape)
    percent3 = df72.count()/df71.count()*100
    rich_percentage = percent3.iloc[0] # 0.006142317496391388 !=10
    # print(percent3)
    # num_min_workers = df[((df['hours-per-week'] == min_work_hours)) & (df['salary'] == '>50K')]
    # print(num_min_workers)
    # rich_percentage = num_min_workers.count()/df.count()*100
    # print(rich_percentage)

    # # What country has the highest percentage of people that earn >50K?
    df8 = df.loc[:, ['native-country', 'salary']]

# Calculate percentage for each country
    country_stats = df8.groupby('native-country')['salary'].apply(
        lambda x: (x == '>50K').sum() / len(x) * 100
    )

    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(), 1)
    # print(highest_earning_country)
    # percent4 = df82.max()/df81['native-country'].value_counts().sum()*100
    # highest_earning_country_percentage = percent4 # 91.45517153424308 !=41.9
    # print(percent4)
    # df9 = df[df['salary'] == '>50K'].groupby('native-country').count().sort_values(by='age', ascending=0).head(1)
    # highest_earning_country = df9
    # # df9 = df[df['salary'] == '>50K'].groupby('native-country').count().max()

    # print(df.count())
    # # highest_earning_country_percentage = None
    # highest_earning_country_percentage =  df9/df.count()*100
    # print(highest_earning_country_percentage)

    # # Identify the most popular occupation for those who earn >50K in India.
    df9 = df.loc[:, ['native-country', 'occupation', 'salary']]
    # print(df9.head())
    # print(df9.shape)
    df91 = df9[(df9['native-country'] == 'India') & (df9['salary'] == '>50K')]
    # print(df91.head())
    # print(df91.shape)
    df92 = df91['occupation'].value_counts().head(1)
    # print(df92)
    top_IN_occupation = df92.idxmax()
    # top_IN_occupation = df[(df['salary'] == '>50K') & (df['native-country'] == 'India') ].groupby('occupation').count().sort_values(by='age', ascending=0).head(1)

    # print(top_IN_occupation)

# DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
