# Pymaceuticals

While your data companions rushed off to jobs in finance and government, you remained adamant that science was the way for you. Staying true to your mission, you've joined Pymaceuticals Inc., a burgeoning pharmaceutical company based out of San Diego. Pymaceuticals specializes in anti-cancer pharmaceuticals. In its most recent efforts, it began screening for potential treatments for squamous cell carcinoma (SCC), a commonly occurring form of skin cancer.
As a senior data analyst at the company, you've been given access to the complete data from their most recent animal study. In this study, 249 mice identified with SCC tumor growth were treated through a variety of drug regimens. Over the course of 45 days, tumor development was observed and measured. The purpose of this study was to compare the performance of Pymaceuticals' drug of interest, Capomulin, versus the other treatment regimens. You have been tasked by the executive team to generate all of the tables and figures needed for the technical report of the study. The executive team also has asked for a top-level summary of the study results.

### Observations and Insights:

1) When looking at the different drug regimens, the only treatments that significantly outperformed the placebo group was the Capomulin and the Ramicane. These were also the drugs regimens with the highest use in the study.

![Alt text](/Matplotlib_Challenge/treatments.png?raw=true"Number of Times the Drug was Tested")

2) If we were to extrapoliate the data from our line plot focusing on the one mouse (j246) and the summary data table, the Capomulin regimen provides one the largest reduction in tumor volume and we can see that the biggest reduction in tumor volume occurs between days 25 and 30

![Alt text](/Matplotlob_Challenge/tumor.png?raw=true"Tumor Volume Over Time")

3) Based on the correlation coefficient that was calculated, we can conclude that there is a very strong relationship between the volume of the tumor and the weight of the mouse

! [Alt text](/Matplotlob_Challenge/volume.png?raw=true"Tumor Volume (mm3) vs Weight of Mouse (g)")
