import streamlit as st
import requests
import pandas as pd
# import plotly.express as px
from datetime import datetime, timedelta
from model_handler import make_local_request

# # Define API endpoint
# API_ENDPOINT = "https://accidents-app-8b4af04b640b.herokuapp.com/accidents-regression"
#
#
# # Function to make API requests
# def make_api_request(data):
#     response = requests.post(API_ENDPOINT, json=data)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         st.error(f"Failed to make API request. Status code: {response.status_code}")
#         return None


# Function to display numerical values
def display_numerical_values(data, title):
    st.subheader(title)
    st.write(data)


# Function to generate data points and make API requests
def generate_data(start_year, start_month, category, type):
    data_points = []

    # Generate 20 data points before and after the given date
    for i in range(-20, 21):
        current_date = datetime(start_year, start_month, 1) + timedelta(days=i)
        data_point = {'year': current_date.year, 'month': current_date.month, "category": category, "type": type}
        data_point['Value'] = make_local_request(data_point)
        data_point['Date'] = current_date
        data_points.append(data_point)

    # Create a DataFrame
    df = pd.DataFrame(data_points)

    return df


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


###############################################################################################

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


#######################################################################################################################

    # Section 1: Enter "Year", "Month", "Category", "Type"
    st.header("Section 1: Explore Specifics")
    st.subheader("Uncover Insights with Customized Analysis")
    st.markdown("""
        Dive into the details! Select a specific year, month, category, and type to uncover valuable insights 
        into Munich's traffic accidents. The power is in your hands to tailor your analysis.
    """)
    year = st.number_input("Enter Year", min_value=2000, max_value=2023, step=1)
    month = st.slider("Enter Month", 1, 12)
    category = st.selectbox("Select Category", ["Alcohol Accidents", "Escape Accidents", "Traffic Accidents"])
    accident_type = st.selectbox("Select Type", ["Total", "Injured and Killed", "With Personal Injury"])

    if st.button("Get Numerical Value and Line Graph"):
        data = {"year": year, "month": month, "category": category.lower(), "type": accident_type.lower()}
        result = make_local_request(data)
        if result:
            display_numerical_values(result, "Numerical Values")

            # df = generate_data(year, month, category, accident_type)
            # # Generate line graph for historical values and forecasts
            # generate_line_graph(df, "Historical and Forecasted Values")


#######################################################################################

    # Headings for different prediction options
    st.header("Prediction Options")

#######################################################################################

    # Section 2: Traffic Accidents
    st.subheader("Section 2: Traffic Accidents Analysis")
    st.markdown("""
        Predict and Visualize Traffic Accidents. Understand the patterns and trends in Munich's traffic accidents.
        Leverage predictive models to gain foresight and explore historical and forecasted values.
    """)
    section2_year = st.number_input("Enter Traffic Accidents Year", min_value=2000, max_value=2023, step=1)
    section2_month = st.slider("Enter Traffic Accidents Month", 1, 12)

    if st.button("Get Traffic Accidents Numerical Values and Line Graph"):
        section2_data_1 = {"year": section2_year, "month": section2_month,
                           "category": "traffic accidents", "type": "total"}
        section2_data_2 = {"year": section2_year, "month": section2_month,
                           "category": "traffic accidents", "type": "injured and killed"}
        section2_data_3 = {"year": section2_year, "month": section2_month,
                           "category": "traffic accidents", "type": "with personal injury"}
        result1 = make_local_request(section2_data_1)
        result2 = make_local_request(section2_data_2)
        result3 = make_local_request(section2_data_3)
        if result1:
            display_numerical_values(result1, "Traffic Accidents: Total")
        if result2:
            display_numerical_values(result2, "Traffic Accidents: Injured and Killed")
        if result3:
            display_numerical_values(result3, "Traffic Accidents: With Personal Injury")
            # Generate line graph for historical values and forecasts
            # df = pd.DataFrame(result['historical_forecast_data'])
            # generate_line_graph(df, "Traffic Accidents Historical and Forecasted Values")

#######################################################################################

    # Section 3: Escape Accidents
    st.subheader("Section 3: Escape Accidents Unveiled")
    st.markdown("""
        Predict and Analyze Escape Accidents. Gain insights into incidents involving escape scenarios. 
        Uncover patterns and forecasts for enhanced understanding.
    """)
    section3_year = st.number_input("Enter Escape Accidents Year", min_value=2000, max_value=2023, step=1)
    section3_month = st.slider("Enter Escape Accidents Month", 1, 12)

    if st.button("Get Escape Accidents Numerical Values and Line Graph"):
        section3_data_1 = {"year": section3_year, "month": section3_month,
                           "category": "escape accidents", "type": "total"}
        section3_data_2 = {"year": section3_year, "month": section3_month,
                           "category": "escape accidents", "type": "injured and killed"}
        section3_data_3 = {"year": section3_year, "month": section3_month,
                           "category": "escape accidents", "type": "with personal injury"}
        result1 = make_local_request(section3_data_1)
        result2 = make_local_request(section3_data_2)
        result3 = make_local_request(section3_data_3)
        if result1:
            display_numerical_values(result1, "Escape Accidents: Total")
        if result2:
            display_numerical_values(result2, "Escape Accidents: Injured and Killed")
        if result3:
            display_numerical_values(result3, "Escape Accidents: With Personal Injury")

            # Generate line graph for historical values and forecasts
            # df = pd.DataFrame(result['historical_forecast_data'])
            # generate_line_graph(df, "Escape Accidents Historical and Forecasted Values")

#######################################################################################

    # Section 4: Alcohol Accidents
    st.subheader("Section 4: Delving into Alcohol-Related Incidents")
    st.markdown("""
        Explore and Forecast Alcohol-Related Accidents. Analyze the impact and trends associated with alcohol-related incidents 
        in Munich. Predict and visualize the future based on historical data.
    """)
    section4_year = st.number_input("Enter Alcohol Accidents Year", min_value=2000, max_value=2023, step=1)
    section4_month = st.slider("Enter Alcohol Accidents Month", 1, 12)

    if st.button("Get Alcohol Accidents Numerical Values and Line Graph"):
        section4_data_1 = {"year": section4_year, "month": section4_month,
                           "category": "escape accidents", "type": "total"}
        section4_data_2 = {"year": section4_year, "month": section4_month,
                           "category": "escape accidents", "type": "injured and killed"}
        section4_data_3 = {"year": section4_year, "month": section4_month,
                           "category": "escape accidents", "type": "with personal injury"}
        result1 = make_local_request(section4_data_1)
        result2 = make_local_request(section4_data_2)
        result3 = make_local_request(section4_data_3)
        if result1:
            display_numerical_values(result1, "Escape Accidents: Total")
        if result2:
            display_numerical_values(result2, "Escape Accidents: Injured and Killed")
        if result3:
            display_numerical_values(result3, "Escape Accidents: With Personal Injury")


            # # Generate line graph for historical values and forecasts
            # df = pd.DataFrame(result['historical_forecast_data'])
            # generate_line_graph(df, "Alcohol Accidents Historical and Forecasted Values")

#######################################################################################

    st.sidebar.title("Acknowledgment & Contributor")
    st.sidebar.write("""
        This app is part of the AI engineer task at Digital Product School.

        **Created by:** Diksha Shrivastava
        - [LinkedIn](https://www.linkedin.com/in/diksha-shrivastava-2aa3bb221/)
        - [Twitter](https://twitter.com/Diksha1713)
        - [GitHub](https://github.com/diksha-shrivastava13)
        - [CV](https://drive.google.com/file/d/1W3QEudAk5WU-vojh3JEyvsUz0ut0wIKH/view?usp=sharing)
        - [Website](http://diksha-shrivastava13.xyz/)

        For more details, check out the [GitHub repository](https://github.com/diksha-shrivastava13/Traffic-Accidents-Model).
    """)


# Run the app
if __name__ == "__main__":
    main()
