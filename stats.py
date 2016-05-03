import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''


data = data.splitlines()

data = [i.split(',') for i in data]

column_names = data[0]
data_rows = data[1:]

df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print("The mean of Alcohol and Tobacco dataset is: {0}, {1}".format(df['Alcohol'].mean(), df['Tobacco'].mean()))
print("The median of Alcohol and Tobacco is: {0}, {1}".format(df['Alcohol'].median(), df['Tobacco'].median()))
print("The Range of Alcohol and Tobacco is: {0}, {1}".format(max(df['Alcohol'])-min(df['Alcohol']), max(df['Tobacco'])-
                                                             min(df['Tobacco'])))
print("The Variance of Alcohol and Tobacco is: {0}, {1}".format(df['Alcohol'].var(), df['Tobacco'].var()))
print("The SD of Alcohol and Tobacco is:  {0}, {1}".format(df['Alcohol'].std(), df['Tobacco'].std()))


