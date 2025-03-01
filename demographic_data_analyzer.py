import pandas as pd

def demographic_data_analyzer():
    # Load dataset
    df = pd.read_csv("adult.data.csv")

    # 1. Count of each race
    race_count = df['race'].value_counts()
    
    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # 3. Percentage of people with a Bachelor's degree
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)
    
    # 4. Percentage of people with advanced education making >50K
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1)
    
    # 5. Percentage of people without advanced education making >50K
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = round((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1)
    
    # 6. Minimum hours worked per week
    min_work_hours = df['hours-per-week'].min()
    
    # 7. Percentage of people working min hours who earn >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)
    
    # 8. Country with highest percentage of people earning >50K
    country_salary_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total_counts = df['native-country'].value_counts()
    country_percentages = (country_salary_counts / country_total_counts * 100).dropna()
    highest_earning_country = country_percentages.idxmax()
    highest_earning_country_percentage = round(country_percentages.max(), 1)
    
    # 9. Most popular occupation for those earning >50K in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]
    
    # Return results as a dictionary
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

if __name__ == "__main__":
    results = demographic_data_analyzer()
    for key, value in results.items():
        print(f"{key}: {value}")
