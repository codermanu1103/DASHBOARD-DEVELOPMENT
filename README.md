# DASHBOARD-DEVELOPMENT

COMPANY NAME - CODTECH IT SOLUTIONS

NAME - Manthan Gupta

INTERN ID - CT06DG1412

DOMAIN NAME - DATA ANALYSIS

DURATION - 6 WEEKS(June 14th 2025 to July 29th 2025)

MENTOR - NEELA SANTHOSH KUMAR

Description:

Titanic Survival Dashboard
This project creates an interactive dashboard using Dash and Plotly to explore Titanic passenger data by embarkation port. It displays:
🚹 Survival rate by gender
📊 Age distribution of passengers

1. Library Imports
dash, dcc, html – for building the web interface.
Input, Output – for reactive user inputs.
plotly.express – for visualizations.
pandas – for data manipulation.
seaborn – for loading the Titanic dataset.

2. Dataset Loading & Cleaning
Loads the Titanic dataset using sns.load_dataset('titanic').
Removes rows with missing values in:
age
embarked (port)
sex
pclass
survived
Resulting dataset is clean and ready for visualization.

3. Dash App Initialization
Creates a Dash app using dash.Dash(__name__).
Sets the title to "Titanic Survival Dashboard".

4. App Layout Components
The layout is composed of the following:
Header: "🚢 Titanic Survival Dashboard" (centered).
Dropdown Menu:
Filters passengers by embarked port (values: S, C, Q).
Non-clearable with default value 'S'.
Two Graphs:
survival-bar: Bar chart showing survival rate by gender.
age-histogram: Histogram of age distribution based on survival.

5. Callback Function for Interactivity
Triggered when the dropdown value (embarked port) changes:
@app.callback([Output(...), Output(...)], [Input(...)])
Inside the callback:
Data Filtering: Filters passengers based on selected port.
Survival Rate Bar Chart:
Groups by sex, computes mean of survived.
Plots a bar chart using plotly.express.bar.
Age Distribution Histogram:
Shows age distribution with survival status as color.
Uses plotly.express.histogram.

6. App Execution
if __name__ == '__main__':
    app.run(debug=True)
Launches the Dash web server locally.
debug=True enables auto-refresh and error tracing.

📌 What This Dashboard Offers
Interactive filtering by port (C, Q, S).
Visual insights on survival rate across genders.
Age-based survival patterns shown through histograms.
Useful for exploratory data analysis or presentations.

Output:

<img width="1464" height="196" alt="Image" src="https://github.com/user-attachments/assets/d9a8345b-8870-4fc8-87a4-307b9aaf6799" />

<img width="1858" height="786" alt="Image" src="https://github.com/user-attachments/assets/a690eb43-d3a3-4cd9-a52f-faad5d4dbdf3" />

<img width="1892" height="584" alt="Image" src="https://github.com/user-attachments/assets/431e5e6f-ef08-462f-b1c8-635b4fd83e47" />

<img width="1837" height="744" alt="Image" src="https://github.com/user-attachments/assets/b17d62bb-25e9-4268-ba71-4018c3faf9da" />

<img width="1868" height="579" alt="Image" src="https://github.com/user-attachments/assets/e3c41607-7adc-43f7-bcae-0ae252defe0f" />

<img width="1853" height="746" alt="Image" src="https://github.com/user-attachments/assets/4dd18052-aa70-4744-8936-8d58817d6eb3" />

<img width="1863" height="513" alt="Image" src="https://github.com/user-attachments/assets/cc4a1d3e-131f-4659-9594-8cb18fa6dcc9" />
