import pandas as pd #import the pandas library for data manipulation

df = pd.read_csv('wetter.csv') #pd.read_csv() reads the CSV file 'wetter.csv' and stores it in a DataFrame called df
print(df.head())

#Calculate the overall average temperature.
avg_temp = df['Temperatur'].mean() #.mean() calculates the average of the 'Temperatur' column
print('Overall Average Temperature:', round(avg_temp, 2), '°C')

#Calculate the average temperature for the month of July.
df["Datum"] = pd.to_datetime(df["Datum"])
july_data = df[df['Datum'].dt.month == 7] #dt.month extracts the month from the datetime, == 7 filters for July
july_avg_temp = july_data['Temperatur'].dropna().mean() #dropna() removes any NaN values before calculating the mean, .mean() calculates the average
print(f'Average Temperature in July:', round(july_avg_temp, 2), '°C')
print(f'\nNumber of July-dates: {len(july_data)}')
print(f'\nYearly Average:')
print(july_data.groupby(july_data['Datum'].dt.year)['Temperatur'].mean().round(2))

#Compare whether the months of July and May differ significantly in their average temperature.
from scipy.stats import ttest_ind #import the t-test function from scipy.stats

df = pd.read_csv('wetter.csv') #read the CSV file again to ensure a fresh DataFrame
df["Datum"] = pd.to_datetime(df["Datum"])

July = df[df['Datum'].dt.month == 7]['Temperatur'].dropna() #filter for July and drop NaN values
May = df[df['Datum'].dt.month == 5]['Temperatur'].dropna() #filter for May and drop NaN values

print("Average July Temperature:", round(July.mean(), 2), "°C")
print("Average May Temperature:", round(May.mean(), 2), "°C")

t_stat, p_value = ttest_ind(July, May, equal_var=False) #perform the t-test assuming unequal variances, t-test measures if the means of two groups are statistically different (strength of the difference), p_value shows the significance level (if the difference is only coincidence)

print("T-statistic:", round(t_stat, 4))
print("P-value:", round(p_value, 4))

if p_value < 0.05: #if the p-value is less than 0.05, we reject the null hypothesis
    print("The difference in average temperatures between July and May is statistically significant.")
else:
    print("The difference in average temperatures between July and May is not statistically significant.")

print(f"P-value (exakt): {p_value:.20f}")