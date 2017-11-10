[![Docker Repository on Quay](https://quay.io/repository/wehouse/house-price-estimator/status "Docker Repository on Quay")](https://quay.io/repository/wehouse/house-price-estimator)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Home Price Estimator

## Introduction
By using a well known public data set from Kaggle (King County Home Prices Sold Data[1]) which contains 21613 observations of
real home sales prices, we will explore different regression techniques and demonstrate their productionization in real life.

## Dataset
We are using Kaggle/Harlfoxem's house sold in 2014 and 2015 [1] pertaining to King County in USA. This dataset consists of 21613 data points that contain 19 data points
for each observation including price, bathrooms, bedrooms and lot sizes as well as build/maintenance year among others.

## Data Pre-processing
Dataset generously contributed by Pang and Lee is quite high quality in its completeness. Data quality is very high and we 
found no missing data points. We had to employ hotencoding to zipcodes as that was a non-comparable datapoint, all else had
comparable relationships so we used them as-is. SKLearn library we choose for the task and the model (LinearRegression) has
in-built ability to 

## Models
In order to analyze any dataset, we first need to have a model of explanation in mind. Each model has its strengths and
weaknesses which must be carefully evaluated.

In order of implementation, we used the following models:
1. Multiple Linear Regression

## Results
In order to compare results of multiple models, we will be using the Adjusted R^2 in order to evaluate test vs pred
accuracy. We will introduce other techniques of comparison.

### Multiple Linear Regression
Adj R^2 value is 0.805

## How to deploy and run?
### From Code
Install requirements from requirements.txt via 
```
pip install -r requirements.txt
```
Afterwards
```
gunicorn app:api
```
Port 8000 u will have it launched that will only address 127.0.0.1 requests and can be accessed using the postman collection in repo.

### From Docker
Docker image is provided via Quay, its launch instructions are here:
[Container Registry](https://quay.io/repository/wehouse/house-price-estimator)

postman collection in repo again will be the primary way to use it.

## References
1. https://www.kaggle.com/harlfoxem/housesalesprediction/data