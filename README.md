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

Technical Goals:

Our technical goals are to analyze honeybee colony data from the USDA to determine if there is a statistically significant amount of loss among colonies over time, and to develop a machine learning model that accurately predicts honeybee colony loss based on significant environmental and human-driven features. We can use these predictions to make recommendations to stakeholders to minimize colony loss and improve outcomes.

Business Goals:

Honeybees pollinate $15 billion worth of crops in the United States each year, including more than 130 types of fruits, nuts, and vegetables. Honeybees also produce honey, worth about $3.2 million in 2017 according to USDA-National Agricultural Statistics Service (NASS).

We want to provide stakeholders with an accurate model for predicting colony loss over time, which factors affect colony loss, and which areas are most conducive to colony production and preservation. We also want to provide a way for stakeholders to test outcomes based on actions they take (or not take) to mitigate colony loss. Our overarching business goal is to influence stakeholders to make responsible and proactive decisions to help honeybees thrive.

        
### Hypothesis

Our initial hypothesis is that honeybee colony loss has increased over time and will continue to increase year over year if no measures are taken to mitigate or reverse this outcome. Some initial questions we have are:

How much have honeybee colonies diminished over time? Is this loss compounded year over year?

What significant features drive honeybee colony loss?

What time of year is the biggest loss?

What state/area suffers heaviest loss and primary factors attributing to that?

Does summer or winter have the largest loss?

Does the beekeeper to colony ratio have an effect on colony loss?

### Target variable

Our target variable is honeybee colony loss. We trained and evaluated several machine learning models to predict future colony loss based on significant features. We selected the best-performing model for testing unseen data.

### Need to haves (Deliverables):

Final Notebook: Full pipeline, hypotheses, statistical testing, markdown, code comments wrangle.py explore.py modeling.py Three models including time series Slide deck 7-10 minute presentation to a mixed technical and non-tech audience.

### Nice to haves (With more time):

Interactive map

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

### Stats Test 1: Correlation Test

Correlation tests are used to check if two samples are related. They are often used for feature selection and multivariate analysis in data preprocessing and exploration.


To run the Correlation test in Python use the following import: \
<span style="color:green">from</span> scipy.stats <span style="color:green">import</span> pearsonr

- pearsonr, in this case, takes in the  and returns the correlation coefficient, corr, and the p_value, p:
    - the correlation coefficient is a unitless continuous numerical measure between -1 and 1, where 1= perfect correlation and -1 = perfect negative correlation. 
    - The p_value is the probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct.

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is there is no relationship between the number of colonies lost annually and the beekeeper to colony ratio.
- The alternate hypothesis (H<sub>1</sub>) is there is a relationship between the number of colonies lost annually and the beekeeper to colony ratio.

#### Confidence level and alpha value:
- I established a 95% confidence level 
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:

corr = 0.765
p = 3.51e-57

#### Summary:

We can reject the null hypothesis that there is no relationship between the number of colonies lost annually and the beekeeper to colony ratio.

### Stats Test 2: T-Test: Two Samples, Two Tailed
- A T-test allows me to compare a categorical and a continuous variable by comparing the mean of the continuous variable by subgroups based on the categorical variable
- The t-test returns the t-statistic and the p-value:
    - t-statistic: 
        - Is the ratio of the departure of the estimated value of a parameter from its hypothesized value to its standard error. It is used in hypothesis testing via Student's t-test. 
        - It is used in a t-test to determine if you should support or reject the null hypothesis
        - t-statistic of 0 = H<sub>0</sub>
    -  - the p-value:
        - The probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct
- We wanted to compare colony loss in the summer to colony loss in the winter. 

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is there is no difference between the number of colonies lost in the summer and the number of colonies lost in the winter.
- The alternate hypothesis (H<sub>1</sub>) is a difference between the number of colonies lost in the summer and the number of colonies lost in the winter.

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05


#### Results:

t = 4.322
p = 1.840e-5

#### Summary:

We can reject the null hypothesis that there is no difference in colony loss between summer and winter.

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
