import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f8f9fa;
        color: #212529;
        font-family: 'Roboto', sans-serif;
    }
    .title-container {
        text-align: center;
        padding: 30px;
        background-color: #007bff;
        border-radius: 15px;
        margin-bottom: 30px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }
    .title-container h1 {
        font-size: 40px;
        color: #ffffff;
        margin: 0;
    }
    .title-container h2 {
        font-size: 26px;
        color: #e0e0e0;
        margin-top: 10px;
    }
    .chart-container, .dataframe-container {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        height: 100%;
    }
    .dataframe-container {
        max-width: 100%;
        overflow-x: auto;
    }
    .col-container {
        padding: 25px;
        border: 2px solid #007bff;
        border-radius: 10px;
        margin-top: 20px;
        background-color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #007bff;
        color: #ffffff;
    }
    .sidebar .sidebar-content .widget {
        color: #ffffff;
    }
    .sidebar .widget label {
        color: #ffffff;
    }
    .loading-spinner {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    .equal-height {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }
    .equal-height > div {
        flex: 1;
        margin: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Display title and subtitle with custom styling
st.markdown("""
    <div class="title-container">
        <h1>Stock Forecast App</h1>
        <h2>Explore stock predictions with Prophet and Plotly!</h2>
    </div>
    """, unsafe_allow_html=True)

# Sidebar for inputs with custom color
st.sidebar.header("User Input")
stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
selected_stock = st.sidebar.selectbox('Select dataset for prediction', stocks)
n_years = st.sidebar.slider('Years of prediction:', 1, 8)
start_date = st.sidebar.date_input("Start date", value=date(2015, 1, 1))
end_date = st.sidebar.date_input("End date", value=date.today())

# Calculate period for forecasting
period = n_years * 365

@st.cache_data
def load_data(ticker, start_date, end_date):
    data = yf.download(ticker, start_date, end_date)
    data.reset_index(inplace=True)
    return data

# Loading spinner
with st.spinner('Loading data...'):
    data = load_data(selected_stock, start_date, end_date)

# Create columns for displaying data and plots with equal heights
col1, col2 = st.columns(2)

with col1:
    st.subheader('Raw Data')
    st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
    st.dataframe(data.tail(), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.subheader('Forecast Data')
    st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
    st.dataframe(data.tail(), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Plot raw data with a specified height
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="Stock Open", line=dict(color='royalblue')))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Stock Close", line=dict(color='firebrick')))
    fig.update_layout(
        title='Time Series Data with Rangeslider',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_rangeslider_visible=True,
        template='plotly_white',
        autosize=True
    )
    st.plotly_chart(fig, use_container_width=True, height=600)  # Set a specific height

st.subheader('Time Series Data')
with st.container():
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    plot_raw_data()
    st.markdown('</div>', unsafe_allow_html=True)

# Predict forecast with Prophet
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show forecast plot and components in expandable sections
with st.expander('Forecast Plot', expanded=True):
    fig1 = plot_plotly(m, forecast)
    fig1.update_layout(
        title='Forecast Plot',
        template='plotly_white',
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff'
    )
    st.plotly_chart(fig1, use_container_width=True)

with st.expander('Forecast Components'):
    fig2 = m.plot_components(forecast)
    st.pyplot(fig2)  # Display matplotlib figure
