<a name="top"></a>
# Kaggle Product Failure


- [Project Description](#project_desc)  
    - Steps to reproduce
    - Goals/ Scenario
- [Project Planning](#plan)  
    - Data Acquisition 
    - Initial Hypothesis
    - Deliverables
- [Data Exploration](#explore)  
    - Data Dictionary
    - Key Findings



<a name="project_desc"></a>
# About the project 

This project is meant to produce a set of predictions for entry into a kaggle competition.  This particular competition is a classification problem using ROC Area Under Curve as the target metric.


## Steps to reproduce
You can download a copy of the data from [Kaggle](https://www.kaggle.com/competitions/tabular-playground-series-aug-2022/data). This project assumes that the data will be stored with the main files in their own directory `'./data'`.

- `'./data/train.csv'` 
    - Includes the data where failure is labeled.  This is the data that will be used to train, evaluate, and select the model to use on the competition data.
- `'./data/test.csv'`
    - This is the competition data.  In this dataset failure is not labeled, so I will not be able to evaluate our predictions ourselves.  However, I will receive a score after submitting our predictions to the kaggle competition.

## Goals / Scenario
The fictional company **Keep It Dry** wants to improve its main product `Super Soaker`. The product is used in factories to absorb spills and leaks.

The company has data for several existing versions of the products and the failure results for those tests.  The goal is to use the data from those results to predict the failure for a new line of products.

<div style="background-color: #f44336; color: white; border-radius: 25px; padding: 15px; width: 80%">
 <strong>Warning!</strong>

  A model only performs well for the world in which it was trained.  Since the product codes available for training are different than those that can be predicted on, there is not a reasonable expectation for a good model performance.
</div>


## Deliverables

- **submission.csv**: A CSV file containing the predictions made from `test.csv`. It consists of two columns:
    - `id` : the id of the row being predicted
    - `failure` : the predicted probability of failure.

[[Back to top](#top)]

<a name="plan"></a>
# Planning

## Data wrangling
Collection of the data is straight-forward since this is a kaggle competition.  All I needed to do is download the appropriate csv files.  Upon further inspection of these files there are some null values that will need to be addressed.  The most likely method of null-handling will be to impute the values with the mean (in the case of continuous variables) or the mode (in the case of categorical variables).

## Initial Hypothesis
My initial hypothesis for this problem is that I might be able to find a pattern or cluster using two or three variables that shows a division or concentration of failed tests.


<a name="explore"></a>
# Exploration:

## Data Dictionary
| Attribute | Data Type | Definition |
| ----- | ----- | ----- |
| product_code | Category | Version of product |
| loading | Continuous | Amount of liquid poured for test |
| failure | Category | Failure state of the test |
| attribute_x | Category | Descriptive categories. Attribute combinations are unique for each product_code |
| measurement_x | Continuous | Unkown. Assumed to be a value that describes something that was measured |

## Key Findings

**product_code**: Product code was the single strongest predictor I was able to find for failure.  However, I did not realize that the product codes differed betweend datasets, so this is a wasted discovery.

**attribute_0 / attribute_1**: These attributes describe a material used in the product.  It was not as strong as a predictor as product_code, but was still a predictor.  Unfortunately, the materials used here are also not consistent across datasets.

[[Back to top](#top)]