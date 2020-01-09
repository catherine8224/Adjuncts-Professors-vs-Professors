import pandas as pd
import seaborn as sns; sns.set()
import numpy as np
import csv
import matplotlib.pyplot as plt
import datetime as dt
import statistics
from pandas.api.types import is_numeric_dtype

#Adjunct Professors 2016
df_2016 = pd.read_csv("editors2016A.csv", header=None)
df_2016.columns = ['Name', 'Agency', 'Total Pay', 'School','School1','Title','Rate of Pay', 'Pay Year','Pay Basis','Branch/Major Category']
df_2016['Total Pay'] = df_2016['Total Pay'].str.replace(',','') #gets rid of commas in Total Pay
df_2016['Total Pay'] = df_2016['Total Pay'].str.replace('$','') #gets rid of $ in Total Pay
df_2016['Total Pay'] = df_2016['Total Pay'].astype(int) #converts from string to integer datatype
Total = df_2016['Total Pay'].sum()
Total = Total/(df_2016.shape[0]) #finds average salary
grouped = df_2016.groupby(['School','Pay Year'], as_index=False)["Total Pay"].mean()

'''
#sns.set(font_scale = 0.5)
p = sns.barplot(data=grouped, x='New', y='Total Pay')
#_ = plt.setp(p.get_xticklabels(), rotation=90)
plt.xticks(fontsize=8, rotation=90)
plt.title("Adjuncts")
plt.xlabel('Schools', fontsize=10)
plt.ylabel('Total Pay', fontsize=10)
plt.tight_layout()
plt.show()

#Normalization
occupation_counts = (df_2016.groupby(['Total Pay'])["School"].value_counts(normalize=True, sort=False).rename('percentage').mul(100).reset_index().sort_values('School'))
remove_words = ['Adjunct']
pat = r'\b({})\b'.format('|'.join(remove_words))
grouped['New'] = grouped['School'].str.replace(pat, '')
replace_words = ['Community College'] 
pat = r'\b({})\b'.format('|'.join(replace_words))
grouped['New'] = grouped['New'].str.replace(pat, 'CC')
p = sns.barplot(x="School", y="percentage", data = occupation_counts)
_ = plt.setp(p.get_xticklabels(), rotation=90)
plt.title("Adjuncts-Normalization")
plt.xticks(fontsize=8, rotation=90)
plt.xlabel('Schools', fontsize=10)
plt.ylabel('Percentage', fontsize=10)
plt.tight_layout()
plt.show()
'''
#Adjunct Professors 2017
df_2017 = pd.read_csv("editors2017A.csv")
#df_2017.columns = ['Name', 'Agency', 'Total Pay', 'School', 'School1','Title','Rate of Pay', 'Pay Year','Pay Basis','Branch/Major Category']
df_2017['Total Pay'] = df_2017['Total Pay'].str.replace(',','') 
df_2017['Total Pay'] = df_2017['Total Pay'].str.replace('$','')
df_2017['Total Pay'] = df_2017['Total Pay'].astype(int) 
Total2 = df_2017['Total Pay'].sum()
Total2 = Total2/(df_2017.shape[0])
grouped2 = df_2017.groupby(['School','Pay Year'], as_index=False)[['Total Pay']].mean()

#Adjunct Professors 2018
df_2018 = pd.read_csv("editors2018A.csv")
df_2018['Total Pay'] = df_2018['Total Pay'].str.replace(',','') 
df_2018['Total Pay'] = df_2018['Total Pay'].str.replace('$','') 
df_2018['Total Pay'] = df_2018['Total Pay'].astype(int) 
Total3 = df_2018['Total Pay'].sum()
Total3 = Total3/(df_2018.shape[0])
grouped3 = df_2018.groupby(['School','Pay Year'], as_index=False)[['Total Pay']].mean()

#Professors 2016
d_2016 = pd.read_csv("editors2016.csv", header = None)
d_2016.columns = ['Name', 'Agency', 'Total Pay', 'School', 'School1','Title','Rate of Pay', 'Pay Year','Pay Basis','Branch/Major Category']
d_2016['Total Pay'] = d_2016['Total Pay'].str.replace(',','') 
d_2016['Total Pay'] =d_2016['Total Pay'].str.replace('$','') 
d_2016['Total Pay'] = d_2016['Total Pay'].astype(int)
d_2016['Pay Year'] = d_2016['Pay Year'].round()
Total1_1 = d_2016['Total Pay'].sum()
Total1_1 = Total1_1/(d_2016.shape[0])
grouped1_1 = d_2016.groupby(['School','Pay Year'], as_index=False)[['Total Pay']].mean()

#Professors 2017
d_2017 = pd.read_csv("editors2017.csv")
d_2017['Total Pay'] = d_2017['Total Pay'].str.replace(',','') #gets rid of commas in Total Pay
d_2017['Total Pay'] = d_2017['Total Pay'].str.replace('$','') #gets rid of $ in Total Pay
d_2017['Total Pay'] = d_2017['Total Pay'].astype(int) #converts from string to integer datatype
Total2_1 = d_2017['Total Pay'].sum()
Total2_1 = Total2_1/(d_2017.shape[0]) #finds average salary
grouped2_1 = d_2017.groupby(['School', 'Pay Year'], as_index=False)[['Total Pay']].mean()
#print(grouped2_1)

#Professors 2018
d_2018 = pd.read_csv("editors2018.csv")
d_2018['Total Pay'] = d_2018['Total Pay'].str.replace(',','') #gets rid of commas in Total Pay
d_2018['Total Pay'] = d_2018['Total Pay'].str.replace('$','') #gets rid of $ in Total Pay
d_2018['Total Pay'] = d_2018['Total Pay'].astype(int) #converts from string to integer datatype
Total3_1 = d_2018['Total Pay'].sum()
Total3_1 = Total3_1/(d_2018.shape[0]) #finds average salary
grouped3_1 = d_2018.groupby(['School','Pay Year'], as_index=False)[['Total Pay']].mean()

#Make sums into a list
Totals=[]
Totals.append(Total)
Totals.append(Total2)
Totals.append(Total3)
Totals2 = []
Totals2.append(Total1_1)
Totals2.append(Total2_1)
Totals2.append(Total3_1)


#Skewed Distribution and Log Transformation of a Skewed Distribution

##'''Adjunct Professors 2016'''
##sdis= df_2016.hist(column='Total Pay', bins=28)
##plt.show()
##print('Skew:', df_2016['Total Pay'].skew(axis=0, skipna=True))
##result = df_2016['Total Pay'].kurtosis(skipna = True) 
##print("Kurtosis:", result)
##
###df_2016["Total Pay"].apply(np.log).hist(log=True, bins=28)
###plt.show()
###df_2016["Total Pay"].apply(np.log).hist(log=True, bins=28)
##
##'''Professors 2016'''
##sdis= d_2016.hist(column='Total Pay', bins=28)
##plt.show()
##print('Skew:', d_2016['Total Pay'].skew(axis=0, skipna=True))
##result = d_2016['Total Pay'].kurtosis(skipna = True) 
##print("Kurtosis:", result)
##
##'''Adjunct Professors 2017'''
##df_2017.hist(column='Total Pay', bins=30)
##plt.show()
####print('Skew:', df_2017['Total Pay'].skew(axis=0, skipna=True))
####result = df_2017['Total Pay'].kurtosis(skipna = True) 
####print('Kurtosis:', result)
###df_2017["Total Pay"].apply(np.log).hist(log=True, bins=30)
###plt.show()
###d_2017["Total Pay"].apply(np.log).hist(log=True, bins=30)
###plt.show()
##'''Professors 2017'''
##d_2017.hist(column='Total Pay', bins=30)
##plt.show()
##print('Skew:', d_2017['Total Pay'].skew(axis=0, skipna=True))
##result = d_2017['Total Pay'].kurtosis(skipna = True) 
##print("Kurtosis:", result)
##
##'''Adjunct Professors 2018'''
##df_2018.hist(column='Total Pay', bins=28)
##plt.show()
####print('Skew:', df_2018['Total Pay'].skew(axis=0, skipna=True))
####result = df_2018['Total Pay'].kurtosis(skipna = True) 
####print('Kurtosis:', result)
###df_2018["Total Pay"].apply(np.log).hist(log=True, bins=28)
###plt.show()
###d_2018["Total Pay"].apply(np.log).hist(log=True, bins=28)
###plt.show()
##'''Professors 2018'''
##d_2018.hist(column='Total Pay', bins=30)
##plt.show()
##print('Skew:', d_2018['Total Pay'].skew(axis=0, skipna=True))
##result = d_2018['Total Pay'].kurtosis(skipna = True) 
##print("Kurtosis:", result)

#In seaborn-Professors-BoxPlot
##flames = [d_2018, df_2018, d_2017, df_2017, d_2016, df_2016]
##flamboyant = pd.concat(flames)
##flierprops = dict(markersize=1)
##bplot=sns.boxplot(y='Pay Year', x='Total Pay', 
##                 data= flamboyant,
##                  orient='h', 
##                 palette="winter_r",
##                  hue = 'Title',
##                  linewidth=0.1,
##                  flierprops=flierprops
##                  )
##plt.yticks(fontsize=8)
##plt.xticks(fontsize=8)
##plt.tight_layout()
##bplot.figure.savefig('boxplot-horiz-all.pdf',
##                    format='pdf',
##                    dpi=100)
##plt.show()
##plt.clf()
df_2016.columns = ['Name', 'Agency', 'Total Pay', 'School','School1','Title','Rate of Pay', 'Pay Year','Pay Basis','Branch/Major Category']
#if d_2016['Pay Basis'] == 'Annual':

print(d_2016)

