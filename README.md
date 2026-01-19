# Bike-Sharing
Exploratory Data Analysis of Washington D.C. bike rental data (2011–2012)

Exploratory Data Analysis:-

1) Import the dataset into a pandas dataframe. Ensure that the date column is in Pandas' datetime format.
2) Check the data type of each column. How many rows are in the dataset? Does the dataset contain any missing values ?
3) Using the date column, create new columns for: year, month, day of the week and hour of the day.
4) Rename the values in the season column to spring, summer, fall and winter.
5) Calculate the total number of casual and registered bikes rented in the years 2011 and 2012.
6) Calculate the mean of the hourly total rental count by season. Which season has the highest mean?
7) Are more bikes rented by registered users on working or non-working days ?  Does the answer differ for non-registered users? Is the answer the same for both years?
8) Which months in the year 2011 have the highest and the lowest total number of bikes rented? Repeat for the year 2012.
9) Which type of weather has the highest and lowest mean of the hourly total rental count?
10) Calculate the correlation between the hourly total rental count and all the numerical columns in the dataset. Which column has the highest correlation with the total rental count?
11) Create a new categorical column called day_period, which can take four possible values: night, morning, afternoon and evening. These values correspond to the following binning of the hour column: 0-6: night, 6-12: morning, 12-6: afternoon, 6-24: evening.
12) Generate a pivot table for the mean of the hourly total rental count, with the index set to the dday andthe column set to the working day column. What can you observe from the table?
