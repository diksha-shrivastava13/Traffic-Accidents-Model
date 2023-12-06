import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Define API endpoint
API_ENDPOINT = "https://your-api-endpoint"


# Function to make API requests
def make_api_request(data):
    response = requests.post(API_ENDPOINT, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to make API request. Status code: {response.status_code}")
        return None


# Function to display numerical values
def display_numerical_values(data, title):
    st.subheader(title)
    st.write(data)


# Function to generate line graph for historical values and forecasts
def generate_line_graph(df, title):
    fig = px.line(df, x='Date', y='Value', labels={'Value': title}, title=title)
    st.plotly_chart(fig)


# Function to create the main app
def main():
    # Configure Streamlit page layout
    st.set_page_config(
        page_title="Munich Traffic Accidents",
        page_icon=":car:",
        layout="centered",
    )

    # Centered title
    st.markdown("""
        <h1 style='text-align: center;'>Explore Monthly Traffic Accidents in Munich 🚗🚦</h1>
    """, unsafe_allow_html=True)

    # Introduction text
    st.markdown("""
         Explore and analyze monthly traffic accidents in Munich using this interactive tool.
         Customize your analysis by leveraging the options below, enabling in-depth scrutiny of both numerical 
         values and dynamic line graphs.

         Discover insights through various prediction options, each offering a unique perspective on Munich's traffic landscape:

         - **Section 1: Explore Specifics:** Dive into the details! Select a specific year, month, category, and type to uncover valuable insights into Munich's traffic accidents.

         - **Section 2: Traffic Accidents Analysis:** Predict and visualize traffic accidents. Understand patterns, trends, and historical data to make informed decisions.

         - **Section 3: Escape Accidents Unveiled:** Predict and analyze escape accidents. Gain insights into incidents involving escape scenarios. Uncover patterns and forecasts for enhanced understanding.

         - **Section 4: Delving into Alcohol-Related Incidents:** Explore and forecast alcohol-related accidents. Analyze the impact and trends associated with alcohol-related incidents in Munich. Predict and visualize the future based on historical data.

         Check out what the data looks like and the performance of different models at **Models and Visualization**.
     """)

    # Section 1: Enter "Year", "Month", "Category", "Type"
    st.header("Section 1: Explore Specifics")
    st.subheader("Uncover Insights with Customized Analysis")
    st.markdown("""
        Dive into the details! Select a specific year, month, category, and type to uncover valuable insights 
        into Munich's traffic accidents. The power is in your hands to tailor your analysis.
    """)
    year = st.number_input("Enter Year", min_value=2000, max_value=2023, step=1)
    month = st.slider("Enter Month", 1, 12)
    category = st.selectbox("Select Category", ["Category A", "Category B", "Category C"])
    accident_type = st.selectbox("Select Type", ["Type 1", "Type 2", "Type 3"])

    if st.button("Get Numerical Value and Line Graph"):
        data = {"year": year, "month": month, "category": category, "type": accident_type}
        result = make_api_request(data)
        if result:
            display_numerical_values(result, "Numerical Values")

            # Generate line graph for historical values and forecasts
            df = pd.DataFrame(result['historical_forecast_data'])
            generate_line_graph(df, "Historical and Forecasted Values")

    # Headings for different prediction options
    st.header("Prediction Options")

    # Section 2: Traffic Accidents
    st.subheader("Section 2: Traffic Accidents Analysis")
    st.markdown("""
        Predict and Visualize Traffic Accidents. Understand the patterns and trends in Munich's traffic accidents.
        Leverage predictive models to gain foresight and explore historical and forecasted values.
    """)
    section2_year = st.number_input("Enter Traffic Accidents Year", min_value=2000, max_value=2023, step=1)
    section2_month = st.slider("Enter Traffic Accidents Month", 1, 12)

    if st.button("Get Traffic Accidents Numerical Values and Line Graph"):
        section2_data = {"year": section2_year, "month": section2_month}
        result = make_api_request(section2_data)
        if result:
            display_numerical_values(result, "Traffic Accidents Numerical Values")

            # Generate line graph for historical values and forecasts
            df = pd.DataFrame(result['historical_forecast_data'])
            generate_line_graph(df, "Traffic Accidents Historical and Forecasted Values")

    # Section 3: Escape Accidents
    st.subheader("Section 3: Escape Accidents Unveiled")
    st.markdown("""
        Predict and Analyze Escape Accidents. Gain insights into incidents involving escape scenarios. 
        Uncover patterns and forecasts for enhanced understanding.
    """)
    section3_year = st.number_input("Enter Escape Accidents Year", min_value=2000, max_value=2023, step=1)
    section3_month = st.slider("Enter Escape Accidents Month", 1, 12)

    if st.button("Get Escape Accidents Numerical Values and Line Graph"):
        section3_data = {"year": section3_year, "month": section3_month}
        result = make_api_request(section3_data)
        if result:
            display_numerical_values(result, "Escape Accidents Numerical Values")

            # Generate line graph for historical values and forecasts
            df = pd.DataFrame(result['historical_forecast_data'])
            generate_line_graph(df, "Escape Accidents Historical and Forecasted Values")

    # Section 4: Alcohol Accidents
    st.subheader("Section 4: Delving into Alcohol-Related Incidents")
    st.markdown("""
        Explore and Forecast Alcohol-Related Accidents. Analyze the impact and trends associated with alcohol-related incidents 
        in Munich. Predict and visualize the future based on historical data.
    """)
    section4_year = st.number_input("Enter Alcohol Accidents Year", min_value=2000, max_value=2023, step=1)
    section4_month = st.slider("Enter Alcohol Accidents Month", 1, 12)

    if st.button("Get Alcohol Accidents Numerical Values and Line Graph"):
        section4_data = {"year": section4_year, "month": section4_month}
        result = make_api_request(section4_data)
        if result:
            display_numerical_values(result, "Alcohol Accidents Numerical Values")

            # Generate line graph for historical values and forecasts
            df = pd.DataFrame(result['historical_forecast_data'])
            generate_line_graph(df, "Alcohol Accidents Historical and Forecasted Values")

    st.sidebar.title("Acknowledgment & Contributor")
    st.sidebar.write("""
        This app is part of the AI engineer task at Digital Product School.

        **Contributor:** XYZ
        - [LinkedIn](https://www.linkedin.com/in/xyz/)
        - [Twitter](https://twitter.com/xyz/)
        - [GitHub](https://github.com/xyz/)
        - [CV](https://link-to-cv.com/)

        For more details, check out the [GitHub repository](https://github.com/xyz/dps-ai-engineer-task).
    """)


# Run the app
if __name__ == "__main__":
    main()
