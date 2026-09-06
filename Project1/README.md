# DecodeLabs Data Analysis Project 1

## 📌 Project Overview

This project focuses on cleaning and transforming a raw e-commerce dataset to make it reliable, consistent, and ready for further data analysis.

The project demonstrates practical data-cleaning techniques using Python and Pandas, including identifying missing values, checking for duplicate records, validating data formats, and preparing the dataset for analysis.

## 🎯 Project Objective

The main objective of this project is to clean and transform a raw e-commerce dataset so that it becomes ready for analysis.

The project specifically focuses on:

- Identifying and handling missing values
- Finding and removing duplicate records
- Identifying and correcting incorrect data formats
- Ensuring the dataset contains no duplicate rows
- Ensuring dates are correctly formatted

## View PDF Report: [Cleaning.pdf](https://github.com/diopeter2020/DecodeLabs-Data-Analytics-Project/blob/main/Project1/Data_Cleaning.pdf )

## 🗂️ Dataset:

The dataset contains 1,200 rows and 14 columns

## 🛠️ Tools & Technologies

- Python
- Pandas
- Jupyter Notebook
- HTML

## 🔍 Data Cleaning Process

### 1. Missing Value Detection

The analysis identified approximately 309 missing values in the "CouponCode" column. 
The analysis asso shows that about 25% of the data is missing.

### 2. Handling Missing Values

Rather than removing records with missing coupon codes, the missing values were replaced with "NoCode".

This preserved the transaction records while providing a meaningful category for orders without a coupon code.

### 3. Duplicate Detection

Duplicate records were checked, and the result shows no duplicate rows.
Therefore, no duplicate rows were present after the cleaning process.
The project also checked duplicates based on "OrderID":
This helped ensure that each order was represented uniquely.

### 4. Data Validation

The dataset was inspected to ensure that important fields were represented correctly, including dates, quantities, prices, order status, payment methods, and coupon codes.

## ✅ Final Result

The raw e-commerce dataset was successfully cleaned and transformed.

The final dataset contains:

- No missing values
- No duplicate rows
- Cleaner coupon-code information
- Consistent data suitable for further analysis

The notebook confirms that the cleaned dataset is ready and fit for analysis.

## 📚 Key Skills Demonstrated

Through this project, I demonstrated practical skills in:

- Data cleaning
- Data preprocessing
- Missing-value handling
- Duplicate detection and removal
- Data validation
- Exploratory data inspection
- Python programming
- Pandas
- Data quality assurance

```
Data-Cleaning/
│
├──Cleaned_Data.csv
├── Data_Cleaning.pdf
└── README.MD
```

## 💡 Key Learning

This project reinforced the importance of data quality before analysis. Cleaning missing values, checking duplicates, and validating data formats helps ensure that subsequent analysis is based on accurate and reliable information.













 
