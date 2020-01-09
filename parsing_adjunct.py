import pandas as pd
import seaborn as sns; sns.set()
import numpy as np
import csv
import matplotlib.pyplot as plt
import datetime as dt
import statistics

df_2016 = pd.read_csv("NYCAdjunctProfs_2016.csv")
#print(df_2016.head(5))

#print(df_2016['Total Pay'].dtypes)
df_2016['Total Pay'] = df_2016['Total Pay'].astype(str) #converts from object to string datatype
df_2016['Total Pay'] = df_2016['Total Pay'].str.replace(',','') #gets rid of commas in Total Pay
df_2016['Total Pay'] = df_2016['Total Pay'].str.replace('$','') #gets rid of $ in Total Pay
df_2016['Total Pay'] = df_2016['Total Pay'].astype(int) #converts from string to integer datatype
#print(df_2016['Total Pay'][0]+ df_2016['Total Pay'][1])
Total = df_2016['Total Pay'].sum()
#print(Total)

df_2017 = pd.read_csv("NYCAdjunctProfs_2017.csv")
df_2017['Total Pay'] = df_2017['Total Pay'].astype(str) #converts from object to string datatype
df_2017['Total Pay'] = df_2017['Total Pay'].str.replace(',','') #gets rid of commas in Total Pay
df_2017['Total Pay'] = df_2017['Total Pay'].str.replace('$','') #gets rid of $ in Total Pay
df_2017['Total Pay'] = df_2017['Total Pay'].astype(int) #converts from string to integer datatype
#print(df_2017['Total Pay'][0]+ df_2017['Total Pay'][1])
Total2 = df_2017['Total Pay'].sum()
#print(Total2)

df_2018 = pd.read_csv("NYCAdjunctProfs_2018.csv")
df_2018['Total Pay'] = df_2018['Total Pay'].astype(str) #converts from object to string datatype
df_2018['Total Pay'] = df_2018['Total Pay'].str.replace(',','') #gets rid of commas in Total Pay
df_2018['Total Pay'] = df_2018['Total Pay'].str.replace('$','') #gets rid of $ in Total Pay
df_2018['Total Pay'] = df_2018['Total Pay'].astype(int) #converts from string to integer datatype
#print(df_2018['Total Pay'][0]+ df_2018['Total Pay'][1])
Total3 = df_2018['Total Pay'].sum()
#print(Total3)

d_2016 = pd.read_csv("NYCProfessor_2016.csv")
d_2016['Total Pay'] = d_2016['Total Pay'].astype(str) #converts from object to string datatype
d_2016['Total Pay'] = d_2016['Total Pay'].str.replace(',','') #gets rid of commas in Total Pay
d_2016['Total Pay'] =d_2016['Total Pay'].str.replace('$','') #gets rid of $ in Total Pay
d_2016['Total Pay'] = d_2016['Total Pay'].astype(int) #converts from string to integer datatype
#print(df_2016['Total Pay'][0]+ df_2016['Total Pay'][1])
Total1_1 = d_2016['Total Pay'].sum()
#print(Total1_1)

d_2017 = pd.read_csv("NYCProfessor_2017.csv")
d_2017['Total Pay'] = d_2017['Total Pay'].astype(str) #converts from object to string datatype
d_2017['Total Pay'] = d_2017['Total Pay'].str.replace(',','') #gets rid of commas in Total Pay
d_2017['Total Pay'] = d_2017['Total Pay'].str.replace('$','') #gets rid of $ in Total Pay
d_2017['Total Pay'] = d_2017['Total Pay'].astype(int) #converts from string to integer datatype
#print(df_2016['Total Pay'][0]+ df_2016['Total Pay'][1])
Total2_1 = d_2017['Total Pay'].sum()
#print(Total2_1)

d_2018 = pd.read_csv("NYCProfessor_2018.csv")
d_2018['Total Pay'] = d_2018['Total Pay'].astype(str) #converts from object to string datatype
d_2018['Total Pay'] = d_2018['Total Pay'].str.replace(',','') #gets rid of commas in Total Pay
d_2018['Total Pay'] = d_2018['Total Pay'].str.replace('$','') #gets rid of $ in Total Pay
d_2018['Total Pay'] = d_2018['Total Pay'].astype(int) #converts from string to integer datatype
#print(df_2016['Total Pay'][0]+ df_2016['Total Pay'][1])
Total3_1 = d_2018['Total Pay'].sum()
#print(Total3_1)

#Make sums into a list
Totals=[]
Totals.append(Total)
Totals.append(Total2)
Totals.append(Total3)
Totals2 = []
Totals2.append(Total1_1)
Totals2.append(Total2_1)
Totals2.append(Total3_1)

#Finding the median
finding = statistics.median(Totals)
print(finding)

finding2 = statistics.median(Totals2)
print(finding2)

#Create a line plot 
lineplt = pd.Series(Totals, name='Annual Salary of Adjuncts')
lineplt.index=pd.date_range('2016', '2018', freq='AS')
lineplt.plot(title = 'Annual Salary of Adjunct Professors in NYC', marker='o', markerfacecolor='blue', legend=True)
lineplt = pd.Series(Totals2, name='Annual Salary of Professors')
lineplt.index=pd.date_range('2016', '2018', freq='AS')
lineplt.plot(marker='', markerfacecolor='red', legend=True)
plt.ylabel('Total Pay')
plt.xlabel('Years')
plt.show()

#Create a bar plot
N = 3
ind = np.arange(N)
width = 0.3
ax = plt.subplot(111)
rects1 = ax.bar(ind, Totals, width, color = 'b', align = 'center')
rects2 = ax.bar(ind+width, Totals2, width, color= 'r', align='center', alpha=0.5)
#plt.bar(y_pos, Totals, align='center', alpha=0.5)
#plt.bar(y_pos, Totals2, align='center', alpha=0.5)
ax.set_title('Annual Salary of Adjunct Professors in NYC')
ax.set_xticks(ind+width/2)
ax.set_xticklabels(('2016', '2017', '2018'))
ax.set_ylabel('Total Pay')
ax.legend((rects1[0], rects2[0]), ('Adjuncts', 'Professors'))
def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.0*h, '%d'%int(h),
                ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
plt.show()

#Using seaborn to create a bar plot and then a lineplot
sns.set(style="darkgrid")
#years = np.array([2016, 2017, 2018])
years = ['2016', '2017', '2018']
monay = np.array(Totals)
lonay = np.array(Totals2)
d = {'years': years, 'Salary of Adjuncts': monay, 'Salary of Professors':lonay}
pdnumsqr = pd.DataFrame(d)
pdnumsqr['years'] = pd.Categorical(pdnumsqr['years'], ordered=True, categories = years)
data = pdnumsqr.melt('years', var_name='Salary', value_name='Average Total Pay')
bar = sns.barplot(x='years', y='Average Total Pay', hue='Salary', data = data, palette="Blues_d")
#ploot.set_xticklabels(ploot.get_xticklabels(), rotation=90
plt.savefig('Adjunct-Professor-Barplot.pdf')
plt.clf()

line = sns.lineplot(x='years', y='Average Total Pay', hue = 'Salary', data=data, palette="GnBu_d", marker= 'o')
fig5 = line.get_figure()
fig5.savefig('Adjunct-Professor-Lineplot.pdf')


#In seaborn- Adjuncts-Boxpot
sns.set_style("whitegrid")
remove_words = ['Adjunct']
pat = r'\b({})\b'.format('|'.join(remove_words))
flames = [df_2016, df_2017, df_2018]
flamboyant = pd.concat(flames)
flamboyant['School'] = flamboyant['School'].str.replace(pat, '')
flierprops = dict(marker='o', markersize=1)
bplot=sns.boxplot(y='Total Pay', x='Pay Year', 
                 data= flamboyant, 
                 palette="summer_r",
                  #hue = 'Pay Year',
                  linewidth=0.1,
                  flierprops=flierprops)
##bplot = sns.swarmplot(y='Total Pay', x='School', 
##                 data= flamboyant, 
##                 color='black',
##                 alpha=0.5,
##                 hue = 'Pay Year')
plt.yticks(fontsize=8)
plt.xticks(fontsize=8)
plt.tight_layout()
bplot.figure.savefig('boxplot-by-year-adjuncts.pdf',
                    format='pdf',
                    dpi=100)
plt.clf()

#In seaborn-Professors-BoxPlot
flames = [d_2018, df_2018]
flamboyant = pd.concat(flames)
flierprops = dict(markersize=1)
bplot=sns.boxplot(y='Total Pay', x='Pay Year', 
                 data= flamboyant, 
                 palette="winter_r",
                  hue = 'Title',
                  linewidth=0.1,
                  flierprops=flierprops)
##bplot = sns.stripplot(y='Total Pay', x='School', 
##                 data= flamboyant, 
##                 color='black',
##                 alpha=0.5)
plt.yticks(fontsize=8)
plt.xticks(fontsize=8)
plt.tight_layout()
bplot.figure.savefig('boxplot-2018.pdf',
                    format='pdf',
                    dpi=100)
plt.clf()

#Create a line plot 
lineplt = pd.Series(Totals, name='Annual Salary of Adjuncts')
#lineplt.index=pd.date_range('2016', '2018', freq='AS')
lineplt.plot(title = 'Annual Salary of Adjunct Professors in NYC', marker='o', markerfacecolor='blue', legend=True)
lineplt = pd.Series(Totals2, name='Annual Salary of Professors')
#lineplt.index=pd.date_range('2016', '2018', freq='AS')
lineplt.index= ['2016', '2017', '2018']
lineplt.plot(marker='', markerfacecolor='red', legend=True)
plt.ylabel('Total Pay')
plt.xlabel('Years')
plt.tight_layout()
plt.savefig('Adjunct-Prof-Lineplot_inmatplotlib', format='png', dpi=200)
plt.clf()

#Create a bar plot
N = 3
ind = np.arange(N)
width = 0.3
ax = plt.subplot(111)
rects1 = ax.bar(ind, Totals, width, color = 'b', align = 'center')
rects2 = ax.bar(ind+width, Totals2, width, color= 'r', align='center', alpha=0.5)
#plt.bar(y_pos, Totals, align='center', alpha=0.5)
#plt.bar(y_pos, Totals2, align='center', alpha=0.5)
ax.set_title('Annual Salary of Adjuncts/Professors in NYC')
ax.set_xticks(ind+width/2)
ax.set_xticklabels(('2016', '2017', '2018'))
ax.set_ylabel('Total Pay')
ax.legend((rects1[0], rects2[0]), ('Adjuncts', 'Professors'))
def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.0*h, '%d'%int(h),
                ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
plt.tight_layout()
plt.savefig('Adjunct-Prof-Barplot_inmatplotlib', format='png', bbox_inches='tight', transparent=True, dpi=200)
plt.clf()

#Creating a boxplot for Adjuncts 2016 in matplotlib
slice = df_2016.iloc[:,[2,3]]
bp = slice.boxplot(column='Total Pay', by='School')
#axes=plt.gca()
axes = plt.subplot(111)
axes.set_ylim([0,60000])
plt.show()
plt.clf()


#Making barplot for all 3 years for Professors
frames = [grouped1_1, grouped2_1, grouped3_1]
result = pd.concat(frames, keys=['2016', '2017', '2018'])
p = sns.barplot(data=result, x='School', y='Total Pay', hue='Pay Year')
plt.xticks(fontsize=8, rotation=90)
plt.title('Professors')
plt.xlabel('Schools', fontsize=10)
plt.ylabel('Average Salary', fontsize=10)
plt.tight_layout()
plt.savefig('Professor-Barplot.pdf')
plt.clf()

#Making barplot for all 3 years for Adjuncts
remove_words = ['Adjunct']
pat = r'\b({})\b'.format('|'.join(remove_words))
grouped['School'] = grouped['School'].str.replace(pat, '')
grouped2['School'] = grouped2['School'].str.replace(pat, '')
grouped3['School'] = grouped3['School'].str.replace(pat, '')
frames = [grouped, grouped2, grouped3]
result = pd.concat(frames, keys=['2016', '2017', '2018'])

p = sns.barplot(data=result, x='School', y='Total Pay', hue='Pay Year')
plt.xticks(fontsize=8, rotation=90)
plt.title('Adjuncts')
plt.xlabel('Schools', fontsize=10)
plt.ylabel('Total Pay', fontsize=10)
plt.tight_layout()
plt.savefig('Adjuncts-Barplot.pdf')
plt.clf()
