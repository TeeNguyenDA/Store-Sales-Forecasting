# Store-Sales-Forecasting

## About this project

The goal of this project to predict total daily sales of products sold at Favorita stores located in Ecuador. The training data includes dates, store and product information, whether that item was being promoted, as well as the sales numbers. Additional files include supplementary information that may be useful in building the models. Data was adapted from Kaggle.

This project encompasses a comprehensive range of tasks typically encountered in a data science workflow, including data acquisition, feature engineering, data transformation, data visualization & EDA, hypothesis testing, model development, and Tableau deployment.

**User Path**:
* [data](https://github.com/TeeNguyenDA/Store-Sales-Forecasting/tree/main/data): Includes: 1) [store_sales_raw.csv](https://github.com/TeeNguyenDA/Store-Sales-Forecasting/blob/main/data/store_sales_raw.csv), 2) [holidays_events.csv](https://github.com/TeeNguyenDA/Store-Sales-Forecasting/blob/main/data/holidays_events.csv), 3) [stores.csv](https://github.com/TeeNguyenDA/Store-Sales-Forecasting/blob/main/data/stores.csv)
* [notebooks](https://github.com/TeeNguyenDA/Store-Sales-Forecasting/tree/main/notebooks): Includes: 1) [store_sales_forecast.ipynb](https://github.com/TeeNguyenDA/Store-Sales-Forecasting/blob/main/notebooks/store_sales_forecast.ipynb)
* [models](https://github.com/TeeNguyenDA/Store-Sales-Forecasting/tree/main/models): Includes: 1) [sarima_model.joblib](https://github.com/TeeNguyenDA/Store-Sales-Forecasting/blob/main/models/sarima_model.joblib), 2) [prophet_model.joblib](https://github.com/TeeNguyenDA/Store-Sales-Forecasting/blob/main/models/prophet_model.joblib)
* [outputs](https://github.com/TeeNguyenDA/Store-Sales-Forecasting/tree/main/outputs): Includes: 1) [SARIMA_sales_forecast.xlsx](https://github.com/TeeNguyenDA/Store-Sales-Forecasting/blob/main/outputs/SARIMA_sales_forecast.xlsx), 2) [prophet_sales_forecast.xlsx](https://github.com/TeeNguyenDA/Store-Sales-Forecasting/blob/main/outputs/prophet_sales_forecast.xlsx)

## Applications 

Through this project, we can automate the sales forecasting using the SARIMA and Facebook Prophet models for the Favorita stores located in Ecuador. New data time series sales data from this store with similar characteristics can leverage the .joblib models to fit again and forecast the sales.

## Context
This project was part of my final capstone project for the Data Science diploma at Lighthouse Labs (Canada), aiming to deliver an end-to-end project.

## Process in the main [Jupyter Notebook](https://github.com/TeeNguyenDA/Store-Sales-Forecasting/blob/main/notebooks/store_sales_forecast.ipynb)

### Part 1: Introduction
Output mapping: The [**store_sales_forecast.ipynb**](/notebooks/store_sales_forecast.ipynb) notebook

### Part 2: Data Prepping & EDA
Output mapping: The [**store_sales_forecast.ipynb**](/notebooks/store_sales_forecast.ipynb) notebook

1. Load the dataset

2. Data Prepping - Converting into Datetime format for all dataframes

3. EDA on 'holidays_df' and 'store_df'

4. Data Prepping and EDA for the main dataframe 'store_sales_df'

5. Decompose the series to see the trend, seasonal, and residual components

6. The augmented Dicky-Fuller test for stationarity

7. Autocorrelation plots (ACF), partial autocorrelation plots (PACF) and Weekly Differencing

8. Train-test split after confirming the data is stationary with D = 1, m = 7

### Part 3: SARIMA and Facebook Prophet Models with Model-specific Prepping
Output mapping: The [**store_sales_forecast.ipynb**](/notebooks/store_sales_forecast.ipynb) notebook, the [**[sarima_model.joblib]**](/models/sarima_model.joblib) model, the [**[SARIMA_sales_forecast.xlsx]**](/outputs/SARIMA_sales_forecast.xlsx) forecast outputs, the [**[prophet_model.joblib]**](/models/prophet_model.joblib) model, the [**[prophet_sales_forecast.xlsx]**](/outputs/prophet_sales_forecast.xlsx) forecast outputs.

1. SARIMA Model

2. Facebook Prophet Model

3. Compare the RMSE of both Models

### Part 4: Conclusion
Output mapping: The [**store_sales_forecast.ipynb**](/notebooks/store_sales_forecast.ipynb) notebook

## Results & Findings

* Prophet is known to handle seasonality and holiday effects well. Our data have a certain degree of effects from the EDA, thus it explains the better performance of Prophet model than the SARIMA model. Given the results, we might favor using the Prophet model or similar models that capture the data patterns of seasonality of grocery sales well. However, if there is new data with different characteristics, the model's performance should be re-evaluated.

* Business implications: As we mentioned Part 3 of each model, the forecasted sales of SARIMA are mostly higher than the actual sales in our investigated scenarios (totalling sales daily, weekly and monthly). Reversedly, Facebook's Prophet gives a more accurate forecasted sales yet mostly on the lower end compared to actual. Depending on the business strategy of forecasting and performance tracking, we might consider: Using SARIMA's sales forecast results in case of an optimistic business scenario or focusing on setting a high target; whereas using Prophet's sales forecasting for a realistic business scenario or low-target setting.

* Considerations for Improvement: While Prophet is performing better than SARIMA model, there's still a significant error that we might want to reduce. This could involve hyperparameter tuning, incorporating external variables, or trying different transformations of the data. For now, we're just focusing the time series of the total sales per period.

## Author

(Tee) Thanh Nguyen

## Credits

The dataset was extracted and adapted from [kaggle](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/overview). The code was also developed based on knowledge from: Kaggle, Analyics Vidhya, THI LAN ANH NGUYEN, SATOSHI_S, IRENE A. GYEBI, SHI LONG ZHUANG, TER HUICHEE, FRANCISCO JAVIER GALLEGO, SHRUTI SAXENA, TUSHAR GOEL, MOHAMED EL-SROGY, HOWOO JANG, EKREM BAYAR.