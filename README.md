# Supermarket_Sales

This Python script creates an interactive web-based application using Streamlit to analyze sales data. It employs several libraries:

Streamlit: Facilitating the creation of the web app interface.
Pandas: Handling and structuring the sales data.
Plotly Express: Generating visualizations like charts to represent the data.
The program operates in distinct phases:

Data Loading and Preparation:

Loads sales data from a CSV file into a structured table (DataFrame).
Converts the 'Date' column to a date format and arranges the data chronologically.
Derives 'Year' and 'Month' columns from the date for improved data segmentation.
User Interaction:

Employs a sidebar interface allowing users to filter the data by selecting a specific month or viewing the entire dataset ('All' option).
Data Visualization:

Showcases various graphical representations:
Depicts daily and product-specific sales through bar charts.
Presents city-wise billing, exhibiting total sales per city with numeric values embedded within the bars.
Illustrates payment distribution via a pie chart.
Displays city evaluation with average ratings, again integrating values within the bars.
Data Presentation:

Furnishes a tabular display at the application's conclusion, exhibiting the filtered dataset based on the user's month selection or the comprehensive dataset if 'All' is chosen.

For this specific analysis, we've chosen a dataset from Kaggle's Dataset Free repository.

Dashboard link: https://21112023supermarketsales-hn2ungks5e7lxywsvz2ttr.streamlit.app/
