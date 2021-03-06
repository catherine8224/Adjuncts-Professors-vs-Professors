# Adjuncts-Professors-vs-Professors

This project is comparing the salary of Adjunct Professors vs. Professors (from 2016-2018) using the website
<ul>
  <li><a href= "www.seethroughny.net/payrolls"> SeeThroughNY </a></li>
  <li><a href = "openpayrolls.com"> OpenPayrolls </a></li>
</ul>

![](SeeThrough.gif)

Since <a href= "www.seethroughny.net/payrolls"> SeeThroughNY </a> does not provide Excel sheet of the data, I first did webscraping on the SeeThroughNY website, focusing mainly on Professors located in the NYC area, and the same for Adjunct Professors. The python script is providing under webscraping*.py

I then saved the data in editor*.csv. I then parsed the data based on the data I needed.

I generated many graphs (boxplots and bargraphs) for the different years:

<b> Bar Graphs </b> 
**Annual Salary for Adjunct Professors vs Full Time Professors from 2016 to 2018**

![GitHub Logo](/Adjunct-Prof-Barplot_inmatplotlib.png)

**Annual Salary for Adjuncts per School**
![Next Logo](/Adjuncts-Barplot.png)

**Annual Salary for Professors per School**
![Nextnext Logo](/Professor-Barplot.png)

<b> BoxPlot </b>
![Boxplot1](boxplot-horiz-all.png)

![Boxplot2](boxplot-horizontal-all.png)


**Boxplot- Annual Salary of Adjunct Professors**
![Boxplot3](boxplot-by-year-adjuncts.png)

**Boxplot- Annual Salary of Full Time Professors**
![Boxplot4](boxplot-by-year-profs.png)
