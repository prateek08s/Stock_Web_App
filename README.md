# Stock WebApp
Here's the updated `README.md` file with the link to the web app included:

---

# Stock Forecast App

## Overview

The **Stock Forecast App** is a web application designed to provide stock price predictions using advanced time series forecasting techniques. Built with Streamlit, Prophet, and Plotly, this app allows users to select stocks, specify prediction parameters, and visualize both historical and forecasted stock data.

You can access the live web app [here](https://stockwebappp.streamlit.app/).

## Features

- **Stock Selection**: Choose from a list of popular stocks for analysis.
- **Date Range Input**: Specify the start and end dates for the data to be analyzed.
- **Prediction Slider**: Select the number of years for which predictions are required.
- **Data Visualization**: View raw and forecasted data with interactive Plotly charts.
- **Forecast Plot**: Visualize future stock prices with Prophet's forecasting capabilities.
- **Forecast Components**: Analyze the components contributing to the forecast.

## Technologies Used

- **Streamlit**: A fast framework for building interactive web applications.
- **Prophet**: A forecasting tool by Facebook for time series data.
- **Plotly**: A graphing library for creating interactive plots.
- **yfinance**: A library to download historical market data from Yahoo Finance.

## Installation

To run this app locally, you need to set up your environment with the following dependencies:

```bash
pip install streamlit yfinance prophet plotly
```

## Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/prateek08s/Stock_Web_App.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd Stock_Web_App
   ```

3. **Run the Streamlit App**

   ```bash
   streamlit run Main.py
   ```

4. **Access the App**

   Open your web browser and go to `http://localhost:8501` to view the app.

   Alternatively, you can view the live app at [this link](https://stockwebappp.streamlit.app/).

## Customization

You can customize the app's appearance by modifying the custom CSS provided in the `Main.py` file. The CSS styles include:

- Background color and font for the body
- Styling for the title and subtitle
- Container styles for dataframes and charts
- Sidebar color and widget styling

## Troubleshooting

If you encounter issues with the dependencies, ensure you have the correct versions installed. For example, Prophet has compatibility issues with certain versions of NumPy. You might need to adjust the version of Prophet or NumPy accordingly.

## Contributing

Feel free to fork the repository and submit pull requests with improvements or fixes. 


## Contact

For questions or support, please reach out to [prateek08s](https://github.com/prateek08s).

---

