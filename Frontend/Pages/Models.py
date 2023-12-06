import streamlit as st
import os


def visualize_images(image_folder):
    st.markdown("""
        <h1 style='text-align: center;'>Visualisations</h1>
    """, unsafe_allow_html=True)
    st.write("Welcome to the Visualisations page! Here, images obtained during Exploratory Data Analysis are displayed.")

    # Image descriptions
    image_descriptions = [
        "Image 1: ARIMA Auto-Correlation Plot",
        "Image 2: ARIMA Partial Auto-Correlation Plot",
        """Image 3: LightGBM Model | Root Mean Squared Error (RMSE): 178.9579 | R-squared (R2) Score: 0.9788""",
        """Image 4: Linear Regression Model | Linear Regression RMSE: 652.3649192609317 | 
        Linear Regression R2 Score: 0.7182540867105955""",
        """Image 5: Multi-Layer Perceptron Model | Root Mean Squared Error (RMSE): 1228.6881 | 
        R-squared (R2) Score: 0.0006""",
        """Image 6: Poisson Regression Model | Root Mean Squared Error: 216.49672043877882 |
        R-squared: 0.9689701932188256""",
        "Image 7: Prophet Model for Alcohol Accidents",
        "Image 8: Prophet Components of Alcohol Model",
        "Image 9: Prophet Model for Escape Accidents",
        "Image 10: Prophet Components of Escape Model",
        "Image 11: Prophet Model for Traffic Accidents",
        "Image 12: Prophet Components of Traffic Model",
        "Image 13: SARIMAX Model",
        "Image 14: AutoARIMA Using Sktime",
        "Image 15: XGBRegressor for Time Series",
        """Image 16: XGBoost | Root Mean Squared Error (RMSE): 179.2515 |
        R-squared (R2) Score: 0.9787""",
    ]

    image_files = sorted(os.listdir(image_folder))

    # Display each image and its description
    for i, image_file in enumerate(image_files, start=1):
        image_path = os.path.join(image_folder, image_file)
        st.image(image_path, caption=image_descriptions[i-1], use_column_width=True)


images_folder = """../Frontend/models"""

# Run the app
if __name__ == "__main__":
    visualize_images(images_folder)
