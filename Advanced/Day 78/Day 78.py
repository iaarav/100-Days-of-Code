import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

clean_df = df.dropna()
print(clean_df)
print()

col = clean_df["Mid-Career 90th Percentile Salary"].subtract(clean_df["Mid-Career 10th Percentile Salary"])

clean_df.insert(1, 'Spread', col)
lowRisk = clean_df.sort_values("Spread")

print(lowRisk)
print()

groupedDf = clean_df.groupby('Group')[[
    'Starting Median Salary', 'Mid-Career Median Salary', 'Mid-Career 10th Percentile Salary',
    'Mid-Career 90th Percentile Salary']].mean()
print(groupedDf)
