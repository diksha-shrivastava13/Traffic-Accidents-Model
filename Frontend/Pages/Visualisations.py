import streamlit as st
import os


def visualize_images(image_folder):
    st.markdown("""
        <h1 style='text-align: center;'>Visualisations</h1>
    """, unsafe_allow_html=True)
    st.write("Welcome to the Visualisations page! Here, images obtained during Exploratory Data Analysis are displayed.")

    # Image descriptions
    image_descriptions = [
        """Image 1: Bar Plot Displaying the Different Characteristics of Accidents 
        (Injured and Killed or Personal Injury or Total) for Each Category of Accident.""",
        "Image 2: Line Plot of Change from Previous Month Percentage",
        "Image 3: Line Plot of Accidents Involving Alcohol Plotted Against Time",
        "Image 4: Line Plot of Each Category of Accidents (Traffic, Alcohol, or Escape) Plotted Against Time.",
        "Image 5: Line Plot of Escape Accidents Plotted Against Time",
        "Image 6: Line Plot of Escape Accidents Plotted Against Time",
        "Image 7: Twelve Months Mean Trend of Accidents",
        "Image 8: Accidents Comparison of Current vs Previous Year's Month",
        "Image 9: Accidents Comparison of Current vs Previous Year."
    ]

    image_files = os.listdir(image_folder)

    # Display each image and its description
    for i, image_file in enumerate(image_files, start=1):
        image_path = os.path.join(image_folder, image_file)
        st.image(image_path, caption=image_descriptions[i-1], use_column_width=True)


images_folder = """/Users/DELL/PycharmProjects/Traffic-Accidents-Model/Frontend/Visualisations"""

# Run the app
if __name__ == "__main__":
    visualize_images(images_folder)
