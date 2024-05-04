import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    
    races_series = list(df['race'])
    races_dict = {}
    for race in races_series:
        races_dict[race] = races_dict.get(race, 0) + 1
    
    races = []
    counts = []
    for key, value in races_dict.items():
        races.append(key)
        counts.append(value)

    races_count_dict = {
        'races': races,
        'counts': counts
    }

    races_df = pd.DataFrame.from_dict(races_count_dict)
    races_df.set_index('races', inplace=True)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = races_df['counts']
    # print(race_count)

    # What is the average age of men?
    male_age_series = df[df.sex == 'Male']['age']
    average_age_men = round(male_age_series.mean(), 1)
    # print(average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    education_series = df['education']
    educations_count = {}
    for education in education_series:
        educations_count[education] = educations_count.get(education, 0) + 1
    
    bachelors_count = educations_count['Bachelors']
    total_education_count = sum(educations_count.values())
    
    percentage_bachelors = round((bachelors_count / total_education_count) * 100, 1)
    # print(percentage_bachelors)

    # What percentage of people with advanced education ('Bachelors', 'Masters', or 'Doctorate') make more than 50K?

    # bachelor_df = education_salary_df[education_salary_df.education == 'Bachelors']
    # masters_df = education_salary_df[education_salary_df.education == 'Masters']
    # doctorate_df = education_salary_df[education_salary_df.education == 'Doctorate']

    # higher_education_df = pd.concat([bachelor_df, masters_df, doctorate_df])
    # higher_education_salaries_df = higher_education_df[education_salary_df.salary == '>50K']
    # higher_education_rich = ((len(higher_education_salaries_df)) / (len(education_salary_df))) * 100
    # print(higher_education_rich)
    
    education_salary_df = df[['education', 'salary']]
    education_series = list(education_salary_df['education'])

    education_dict = {}
    for education in education_series:
        education_dict[education] = education_dict.get(education, 0) + 1
    #print(education_dict)

    education_list = list(education_dict.keys())
    # print(len(education_list))

    higher_educations = ['Bachelors', 'Masters', 'Doctorate']
    higher_education_df_list = []
    for higher_education in higher_educations:
        higher_education_df = education_salary_df[education_salary_df.education == higher_education]
        higher_education_df_list.append(higher_education_df)

    higher_educations_df = pd.concat(higher_education_df_list)
    # print(higher_educations_df)

    higher_education_salaries_df = higher_educations_df[education_salary_df.salary == '>50K']
    higher_education_rich = round(((len(higher_education_salaries_df)) / (len(higher_educations_df))) * 100, 1)
    # print(higher_education_rich)

    # What percentage of people without advanced education make more than 50K?
    lower_educations = []
    for education in education_list:
        if education not in higher_educations:
            lower_educations.append(education)
    # print(len(lower_educations))

    lower_educations_df = pd.DataFrame()
    lower_education_df_list = []

    for lower_education in lower_educations:
        lower_education_df = education_salary_df[education_salary_df.education == lower_education]
        lower_education_df_list.append(lower_education_df)
    
    lower_educations_df = pd.concat(lower_education_df_list)
    # print(lower_educations_df)
    
    lower_education_salaries_df = lower_educations_df[education_salary_df.salary == '>50K']
    lower_education_rich = round(((len(lower_education_salaries_df)) / (len(lower_educations_df))) * 100, 1)
    # print(lower_education_rich)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    work_hours_series = df['hours_per_week']
    min_work_hours = work_hours_series.min()
    # print(min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    hours_salary_df = df[['hours_per_week', 'salary']]
    min_work_hours_df = hours_salary_df[hours_salary_df.hours_per_week == min_work_hours]
    rich_min_work_hours_df = min_work_hours_df[min_work_hours_df.salary == '>50K']
    #print(rich_min_work_hours_df)  #len(min_work_hours_df)
    
    rich_percentage = round((len(rich_min_work_hours_df) / len(min_work_hours_df) * 100), 1)
    # print(rich_percentage)

    # What country has the highest percentage of people that earn >50K?
    countries_series = list(df['native_country'])

    country_salary_df = df[['native_country', 'salary']]
    rich_country_salary_df = country_salary_df[country_salary_df.salary == '>50K']

    country_salary_dict = {}
    for country in country_salary_df['native_country']:
        country_salary_dict[country] = country_salary_dict.get(country, 0) + 1
    
    rich_country_salary_dict = {}
    for country in rich_country_salary_df['native_country']:
        rich_country_salary_dict[country] = rich_country_salary_dict.get(country, 0) + 1

    rich_countries = rich_country_salary_dict.keys()
    rich_population_list = list(rich_country_salary_dict.items())

    new_rich_population_list = []
    for country, rich in rich_population_list:
        total_population = country_salary_dict[country]
        new_rich_population_list.append((country, rich, total_population))

    rich_country_dict = {}    
    for (country, rich, total) in new_rich_population_list:
        rich_country_dict[country] = round((rich / total) * 100, 1)
    
    highest_earning_country_percentage = max(rich_country_dict.values())
    for country, percentage in rich_country_dict.items():
        if percentage == highest_earning_country_percentage:
            highest_earning_country = country
    
    # Identify the most popular occupation for those who earn >50K in India.
    occupation_salary_df = df[['occupation', 'salary', 'native_country']]
    rich_occupation_salary_df = occupation_salary_df[occupation_salary_df.salary == '>50K']
    india_rich_occupation_salary_df = rich_occupation_salary_df[rich_occupation_salary_df.native_country == 'India']
    # print(india_rich_occupation_salary_df)

    india_rich_occupations = india_rich_occupation_salary_df['occupation']
    india_rich_occupations_dict = {}
    for occupation in india_rich_occupations:
        india_rich_occupations_dict[occupation] = india_rich_occupations_dict.get(occupation, 0) + 1

    max_IN_count = max(india_rich_occupations_dict.values())
    top_IN_occupation = ""
    for occupation, count in india_rich_occupations_dict.items():
        if count == max_IN_count:
            top_IN_occupation = occupation
        
    print(top_IN_occupation)

    # # DO NOT MODIFY BELOW THIS LINE

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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()