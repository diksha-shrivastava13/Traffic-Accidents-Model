import streamlit as st
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def display_model_results(model_name):
    st.subheader(f"Results for {model_name}")
    # Assuming you have saved images for each model with the name "model_name.png"
    image_path = f"model_results/{model_name}.png"
    if os.path.exists(image_path):
        img = mpimg.imread(image_path)
        st.image(img, caption=model_name, use_column_width=True)
    else:
        st.warning(f"No image found for {model_name}")


def display_data_analysis_visualizations(visualization_name):
    st.subheader(f"Data Analysis Visualization: {visualization_name}")
    # Assuming you have saved images for data analysis with the name "visualization_name.png"
    image_path = f"data_analysis_visualizations/{visualization_name}.png"
    if os.path.exists(image_path):
        img = mpimg.imread(image_path)
        st.image(img, caption=visualization_name, use_column_width=True)
    else:
        st.warning(f"No image found for {visualization_name}")


def main():
    st.title("Models and Visualization")

    st.header("Model Results")

    # List of models tested
    models_list = [
        "Model 1", "Model 2", "Model 3", "Model 4",
        "Model 5", "Model 6", "Model 7", "Model 8",
        "Model 9", "Model 10", "Model 11", "Model 12"
    ]

    # Display results for each model
    for model in models_list:
        display_model_results(model)

    st.header("Data Analysis Visualizations")

    # List of data analysis visualizations
    visualizations_list = [
        "Visualization 1", "Visualization 2", "Visualization 3",
        "Visualization 4", "Visualization 5", "Visualization 6",
        "Visualization 7", "Visualization 8", "Visualization 9", "Visualization 10"
    ]

    # Display visualizations for data analysis
    for visualization in visualizations_list:
        display_data_analysis_visualizations(visualization)


if __name__ == "__main__":
    main()
