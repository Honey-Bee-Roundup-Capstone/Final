# <a name="top"></a>Honey Bee Round-up
![]()

by: Dashiell Bringhurst, Rajesh Lamichhane, and Jennifer Lewis

<p>
  <a href="https://github.com/dashbringhurst" target="_blank">
    <img alt="Dashiell" src="https://img.shields.io/github/followers/dashbringhurst?label=Follow_Dashiell&style=social" />
  </a>
   <a href="https://github.com/rajeshlamichhane04" target="_blank">
    <img alt="Rajesh" src="https://img.shields.io/github/followers/rajeshlamichhane04?label=Follow_Rajesh&style=social" />
  </a>
   <a href="https://github.com/JenniferMLewis" target="_blank">
    <img alt="Jennifer" src="https://img.shields.io/github/followers/JenniferMLewis?label=Follow_Jenn&style=social" />
  </a>
</p>


***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___

<img src="https://cdn.discordapp.com/attachments/415980182021603329/1035270460373483610/eric-ward-qFAEHxevxVE-unsplash.jpg">

## <a name="project_description"></a>Project Description:
[[Back to top](#top)]

***
## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]

### Project Outline:


        
### Hypothesis



### Target variable


### Need to haves (Deliverables):



### Nice to haves (With more time):



***

## <a name="findings"></a>Key Findings:
[[Back to top](#top)]




***

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

### Data Used
<p>
Originally Data was found on <a href = "https://data.world/finley/bee-colony-statistical-data-from-1987-2017">Data.World</a>, then up-to-date data was pull from the Original Souces, and we narrowed down to the Bee Colony Loss Data from <a href = "https://bip2.beeinformed.org/loss-map/">BeeInformed.org</a>
</p>

#### Starting DataFrame:

---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| year | Year Survey Data was reported for. | [DATETIME] |
| state | State Survey Data was reported for. | [OBJ64] |
| total_annual_loss | Percentage (%) of bees lost among all colonies in the reported state. | |
| average_loss | Average Level of Bee Loss Experience by a Bee Keeper in the reported state. | |
| starting_colonies | Number of Colonies at the start of the reporting period for the reported state. | |
| colonies_lost | Number of Colonies lost at the end of the reporting period for the reported state. (Note: Loss rates should not be interpreted as a change in population size because beekeepers can replace lost colonies throughout the year. Therefore, colony loss rates are best interpreted as a turn-over rate, as high levels of losses do not necessarily result in a decrease in the total number of colonies managed in the United States.) | |
| ending_colonies | Number of Colonies at the end of the reporting peroid for the reported state. | |
| beekeepers| Number of Bee Keepers with Colonies who operate in the reported state. | |
| beekeepers_exclusive_to_state | Percentage (%) of Bee Keepers with Colonies ONLY in the reported state. (Keepers with colonies in more than one state have their numbers added to all states they operate in.) | |
| colonies | Number of Colonies belonging to keepers who operate in the reported state.| |
| colonies_exclusive_to_state | Percentage (%) of Colonies kept by Bee Keepers who ONLY operate in the reported state.  | |

#### Final DataFrame:

***

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]
<p>
Data was originally found on Data.World, and further traced back to it's source to pull the most up-to-date data on Bees.
<ul>Of the original 3 Data sets:
<li> After assessement Census Data from the USDA was deemed not to have pertinent information to the current population of bees or health of hives, as well as the fact that it is reported in 5 year gaps, was removed from our initial data set.</li>
<li> Survey Data by State from the USDA was also deemed as having less pertinent information on the trend in population of bees or health of their hives, and was left for further exploration as time permits due to a small amount of data on the environmental area of the colonies.</li>
<li> The Bee Colony Loss Data from BeeInformed.org has the most relevant data regarding current number of colonies, number of bee keepers, and loss of bees and colonies, so was the data set we initially focused on.
  <ul><li> However, due to this privacy stipulation "For the protection of privacy, losses are reported as N/A if 10 or fewer beekeepers responded in that state. These beekeepers' losses are included in the national statistics." we decided to drop all records where the number of beekeepers were 10 or less, as most of the data was Null, and therefore not contributing towards our goal. </li></ul></li></ul>

![]()


### Wrangle steps: 


*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - wrangle.py 
    - explore.py
    - modeling.py


### Takeaways from exploration:


***

## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]

### Stats Test 1: ANOVA Test: One Way

Analysis of variance, or ANOVA, is a statistical method that separates observed variance data into different components to use for additional tests. 

A one-way ANOVA is used for three or more groups of data, to gain information about the relationship between the dependent and independent variables: in this case our clusters vs. the log_error, respectively.

To run the ANOVA test in Python use the following import: \
<span style="color:green">from</span> scipy.stats <span style="color:green">import</span> f_oneway

- f_oneway, in this case, takes in the individual clusters and returns the f-statistic, f, and the p_value, p:
    - the f-statistic is simply a ratio of two variances. 
    - The p_vlaue is the probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is
- The alternate hypothesis (H<sub>1</sub>) is 

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:


#### Summary:


### Stats Test 2: T-Test: One Sample, Two Tailed
- A T-test allows me to compare a categorical and a continuous variable by comparing the mean of the continuous variable by subgroups based on the categorical variable
- The t-test returns the t-statistic and the p-value:
    - t-statistic: 
        - Is the ratio of the departure of the estimated value of a parameter from its hypothesized value to its standard error. It is used in hypothesis testing via Student's t-test. 
        - It is used in a t-test to determine if you should support or reject the null hypothesis
        - t-statistic of 0 = H<sub>0</sub>
    -  - the p-value:
        - The probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct
- We wanted to compare the individual clusters to the total population. 
    - Cluster1 to the mean of ALL clusters
    - Cluster2 to the mean of ALL clusters, etc.

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is 
- The alternate hypothesis (H<sub>1</sub>) is 

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05


#### Results:


#### Summary:

***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation:

### Baseline
    
- Baseline Results: 
    

- Selected features to input into models:
    - features = []

***

### Models and R<sup>2</sup> Values:
- Will run the following regression models:

    

- Other indicators of model performance with breif defiition and why it's important:

    
    
#### Model 1: Linear Regression (OLS)


- Model 1 results:



### Model 2 : Lasso Lars Model


- Model 2 results:


### Model 3 : Tweedie Regressor (GLM)

- Model 3 results:


### Model 4: Quadratic Regression Model

- Model 4 results:


## Selecting the Best Model:

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Validation/Out of Sample RMSE | R<sup>2</sup> Value |
| ---- | ----| ---- |
| Baseline | 0.167366 | 2.2204 x 10<sup>-16</sup> |
| Linear Regression (OLS) | 0.166731 | 2.1433 x 10<sup>-3</sup> |  
| Tweedie Regressor (GLM) | 0.155186 | 9.4673 x 10<sup>-4</sup>|  
| Lasso Lars | 0.166731 | 2.2204 x 10<sup>-16</sup> |  
| Quadratic Regression | 0.027786 | 2.4659 x 10<sup>-3</sup> |  


- {} model performed the best


## Testing the Model

- Model Testing Results

***

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]


***
###### ReadMe template by: <a href="https://github.com/mdalton87" target="_blank">Mathew Dalton</a>
</p>
