# Data Science Salary Estimation: Overview 
* Created a tool t estimate data science salaries (MAE~$11k) to help in negotiating their income.
* Scraped over 100 jop description from glassdoor using python and selenium
* The text of job descrption to quantify the value  companies put on python, R ,excel, aws and spark.
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flash.

## Code and Resources Used
* Python version: 3.8.3
* Packages: pandas, numpy, sklearn, matplotlip, seaborn, flask, json, pickle
* For web Framework Requirements: '''pip install -r requirements.txt'''
* Scraper Github: https://github.com/arapfaik/scraping-glassdoor-selenium
* Flask Production: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Web Scraping 

Used web scraper github repo (mentioned above) to scrape 1000 job postion fromm glassdoor

* Job title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Headquarters
* Company Size
* Company Founded Date
* Type of Ownership
* Industry
* Revenue
* Competitors

## Data CLeaning

After scraping the data,the following changes and created the following variables:

* Parsed numeric data out of salary
* Made columns for employer provided salary and hourly wages
* Removed rows without salary
* Parsed rating out of company text
* Made a new column for company state
* Added a column for if the job was at the company’s headquarters
* Transformed founded date into age of company
* Made columns for if different skills were listed in the job description:
  * Python
  * R
  * Excel
  * AWS
  * Spark
* Column for simplified job title and Seniority
* Column for description length


## Model Building

Tried three different models and evaluated them using Mean Absolute Error. 
Three different models:
* Multiple Linear Regression 
* Lasso Regression 
* Random Forest


## Model performance

The Random Forest model far outperformed the other approaches on the test and validation sets.
* Random Forest : MAE = 15.07



## Productionization
Built a flask API endpoint .The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.
