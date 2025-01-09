# EDA / Data Analysis and Visualizations - Streamlit

Why Use Streamlit for Exploratory Data Analysis and Sharing Research?
Streamlit is an excellent tool for performing Exploratory Data Analysis (EDA) and creating interactive visualizations. Its simplicity allows researchers to quickly build applications to explore datasets, visualize trends, and gain insights without extensive front-end development experience. Moreover, Streamlit's ability to share apps with others by deploying them online ensures that research and analysis become actionable and accessible to collaborators and stakeholders. Whether it’s building interactive research dashboards, creating tools for students to learn STEM concepts, or simplifying workflows for common tasks, 
Streamlit bridges the gap between technical expertise and usability, making data-driven tasks easily shareable and engaging.

# Code Along

Introduction to Streamlit for STEM Researchers
Hi everyone! Today, I’ll guide you through setting up and using Streamlit, an amazing Python library that makes building interactive web apps easy and fun. Streamlit is especially great for STEM researchers like you, as it lets you turn your data and scripts into shareable, user-friendly apps without requiring extensive knowledge of web development.

1. Setting Up Streamlit Locally Using Conda
First, let’s talk about how to get Streamlit running on your local machine with Conda. Conda is a package manager that helps us create isolated environments for different projects, ensuring compatibility between dependencies. Here’s how we’ll get started:

Create a Conda Environment
I always recommend creating a new environment for each project. Run this command:

```
conda create -n streamlit_env python=3.9
```

Activate the Environment
Once the environment is created, activate it using:

```
conda activate streamlit_env
```

This switches your shell to the new environment, isolating any changes we make.

Install Streamlit
With the environment activated, we install Streamlit:

```
pip install streamlit
```

Although Conda manages environments, Streamlit itself is installed via pip because it’s not in the Conda repositories.

Verify the Installation
After installing, test it by running:

```
streamlit hello
```

This launches a sample Streamlit app in your default browser. If it works, you’re ready to dive in!

2. Exploring the Basics of Streamlit
Streamlit works by running Python scripts. Unlike Flask or Django, there’s no need to deal with HTML or JavaScript. You write Python code, and Streamlit handles the rest. Let’s go over some basic features:

Displaying Text
The st.write() function is the Swiss Army knife of Streamlit. You can use it to display text, data frames, charts, and more. For instance:

```
import streamlit as st
st.write("Hello, Streamlit!")
```

Adding Interactivity
Streamlit lets you create widgets like sliders, text inputs, and buttons with just a line of code. For example:

```
number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")
```

These widgets are automatically synchronized, meaning they update in real-time as you interact with them.

In Streamlit, you can add headings using the `st.title()`, `st.header()`, `st.subheader()`, and `st.markdown()` functions. Here is an example:

```
import streamlit as st

st.title("Title heading")

st.write("Hello, Streamlit!")

st.header("Number selection")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")


```

Visualizing Data
Streamlit integrates seamlessly with libraries like Matplotlib, Plotly, and Pandas. You can create beautiful, interactive visualizations directly in your app. For example:

```
# My Plot of data

import pandas as pd
import plotly.express as px
import streamlit as st

# Create sample data
data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

# Display the data in the Streamlit app
st.write(data)

# Create a Plotly figure
fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in the Streamlit app
st.plotly_chart(fig)

```

3. Building a Researcher Profile Page
Now, let’s build something practical—a Researcher Profile Page. This app will showcase a researcher’s details, including their name, field of study, publications, and an interactive section for exploring their work.

Here’s the full code, and I’ll walk you through it step by step:

```
import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Dr. Jane Doe"
field = "Astrophysics"
institution = "University of Science"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "jane.doe@example.com"
st.write(f"You can reach {name} at {email}.")
```

Breaking Down the App
Basic Inputs for Profile Details
The st.text_input() widget lets users enter their name, field of study, and institution. These inputs update the displayed profile dynamically.

Displaying Publications
The st.file_uploader() widget allows researchers to upload a CSV of their publications. We use Pandas to read the file and display it as a table with st.dataframe().

Filtering Publications
To add interactivity, we let users filter the publications by keyword. The apply() function searches for the keyword across all columns in the DataFrame, making it flexible for various data formats.

Visualizing Trends
If the uploaded CSV contains a "Year" column, we use Streamlit’s built-in st.bar_chart() to visualize the number of publications per year. This provides a quick way to analyze research output.

Contact Information
The app ends with a contact section, where researchers can share their email address.

## Data Vis - STEM sections

Breaking Down the STEM Data Section
Dummy Data Creation

I created three DataFrames (physics_data, astronomy_data, weather_data) with sample data that mirrors real-world research contexts.
Physics data includes experimental results with energy levels and dates.
Astronomy data records celestial object observations with brightness levels and dates.
Weather data contains city-specific temperature, humidity, and recorded dates.
Tabbed Dataset Selection

Using st.selectbox(), we provide users the ability to choose which dataset to explore: Physics, Astronomy, or Weather. This keeps the interface clean and intuitive.
Interactive Widgets for Filtering

Physics: A slider (st.slider()) filters experiments based on energy levels.
Astronomy: Another slider lets users adjust the brightness range to focus on specific celestial objects.
Weather: Two sliders allow users to filter cities based on temperature and humidity ranges.
Real-Time Filtering

For each dataset, the app dynamically filters the DataFrame based on user input from the sliders. The filtered data is displayed immediately, demonstrating the power of real-time interactivity.
Why It’s Useful for STEM Researchers

This section showcases how researchers can quickly analyze and refine large datasets, focusing on specific attributes of interest without writing complex filtering code.

```
import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page with STEM Data")

# Collect basic information
name = "Dr. Jane Doe"
field = "Astrophysics"
institution = "University of Science"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add STEM Data Section
st.header("Explore STEM Data")

# Generate dummy data
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# Tabbed view for STEM data
st.subheader("STEM Data Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore", 
    ["Physics Experiments", "Astronomy Observations", "Weather Data"]
)

if data_option == "Physics Experiments":
    st.write("### Physics Experiment Data")
    st.dataframe(physics_data)
    # Add widget to filter by Energy levels
    energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
    filtered_physics = physics_data[
        physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
    ]
    st.write(f"Filtered Results for Energy Range {energy_filter}:")
    st.dataframe(filtered_physics)

elif data_option == "Astronomy Observations":
    st.write("### Astronomy Observation Data")
    st.dataframe(astronomy_data)
    # Add widget to filter by Brightness
    brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
    filtered_astronomy = astronomy_data[
        astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
    ]
    st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
    st.dataframe(filtered_astronomy)

elif data_option == "Weather Data":
    st.write("### Weather Data")
    st.dataframe(weather_data)
    # Add widgets to filter by temperature and humidity
    temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
    filtered_weather = weather_data[
        weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
        weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
    ]
    st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
    st.dataframe(filtered_weather)

# Add a contact section
st.header("Contact Information")
email = "jane.doe@example.com"
st.write(f"You can reach {name} at {email}.")
```

## Menu Bars

Features of the Sidebar Implementation
Navigation Menu

Added a radio button menu in the sidebar to navigate between the four sections: Researcher Profile, Publications, STEM Data Explorer, and Contact.
Section Segregation

Each menu selection displays only the relevant content, making the app more structured and less cluttered.
Sidebar Widgets for STEM Data

Moved the dataset selection dropdown into the sidebar for better accessibility and space utilization.
Consistent User Experience

Sidebar menus ensure users can switch between sections without scrolling.

```
import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "STEM Data Explorer", "Contact"],
)

# Dummy STEM data
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")
    
    # Collect basic information
    name = "Dr. Jane Doe"
    field = "Astrophysics"
    institution = "University of Science"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")
    
    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")

    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Physics Experiments", "Astronomy Observations", "Weather Data"]
    )

    if data_option == "Physics Experiments":
        st.write("### Physics Experiment Data")
        st.dataframe(physics_data)
        # Add widget to filter by Energy levels
        energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
        filtered_physics = physics_data[
            physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
        ]
        st.write(f"Filtered Results for Energy Range {energy_filter}:")
        st.dataframe(filtered_physics)

    elif data_option == "Astronomy Observations":
        st.write("### Astronomy Observation Data")
        st.dataframe(astronomy_data)
        # Add widget to filter by Brightness
        brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
        filtered_astronomy = astronomy_data[
            astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
        ]
        st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
        st.dataframe(filtered_astronomy)

    elif data_option == "Weather Data":
        st.write("### Weather Data")
        st.dataframe(weather_data)
        # Add widgets to filter by temperature and humidity
        temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
        humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
        filtered_weather = weather_data[
            weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
            weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
        ]
        st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
        st.dataframe(filtered_weather)

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "jane.doe@example.com"
    st.write(f"You can reach {name} at {email}.")

```

## ETL Pipeline

Here’s a guide to extending the Streamlit app to include a simple ETL (Extract, Transform, Load) data pipeline using one of the dummy STEM datasets as an example.
We’ll allow users to upload a CSV file, apply a transformation to add an extra column, and display the transformed data in both tabular and visual formats.

Step-by-Step Guide to Building an ETL Data Pipeline in Streamlit
1. Introduce the ETL Pipeline Concept
Start by explaining the ETL process:

Extract: Read or upload data (e.g., from a CSV file).
Transform: Apply a data manipulation or transformation.
Load: Display the final data, which could include visualizations or saving the results.
We’ll build a pipeline for STEM researchers to upload a CSV, add a derived column, and view the updated dataset alongside a simple plot.

```
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sidebar menu for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a Page", ["Home", "ETL Pipeline"])

if page == "Home":
    st.title("Welcome to the STEM Research Dashboard")
    st.write(
        "Use this dashboard to upload data, perform analysis, and visualize results. "
        "Switch to the ETL Pipeline tab in the sidebar to start transforming your data!"
    )

elif page == "ETL Pipeline":
    st.title("ETL Data Pipeline")
    st.write(
        "This tool demonstrates a simple ETL pipeline for STEM datasets. "
        "You can upload a CSV file, transform the data by adding a new column, and visualize the results."
    )

    # Step 1: Extract (Upload CSV)
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)
        st.write("### Original Data")
        st.write(df)

        # Step 2: Transform (Add a new column)
        st.write("### Transformation: Add a Derived Column")
        column_choice = st.selectbox("Select a column to base the new column on:", df.columns)
        multiplier = st.slider("Choose a multiplier for the new column", 1, 10, 2)

        # Adding a new column
        df[f"{column_choice}_Transformed"] = df[column_choice] * multiplier
        st.write("### Transformed Data")
        st.write(df)

        # Step 3: Load (Display Data and Plot)
        st.write("### Visualization")
        plot_type = st.radio("Select a plot type", ["Bar Plot", "Line Plot"])

        if plot_type == "Bar Plot":
            st.write(f"Bar Plot of {column_choice}_Transformed")
            fig, ax = plt.subplots()
            df[[column_choice, f"{column_choice}_Transformed"]].plot.bar(ax=ax)
            st.pyplot(fig)
        elif plot_type == "Line Plot":
            st.write(f"Line Plot of {column_choice}_Transformed")
            fig, ax = plt.subplots()
            df[[column_choice, f"{column_choice}_Transformed"]].plot(ax=ax)
            st.pyplot(fig)

```

CSV data:

```
Star,Distance_Light_Years,Apparent_Magnitude,Temperature_Kelvin
Sirius,8.6,-1.46,9940
Canopus,310,-0.72,7350
Alpha Centauri,4.37,-0.01,5790
Arcturus,36.7,-0.05,4286
Vega,25,0.03,9602
Capella,42.9,0.08,4970
Rigel,860,0.12,12100
Betelgeuse,642,0.42,3500
Aldebaran,65.3,0.85,3910
Antares,554,0.96,3200

```

Detailed Explanation of the Code
1. Sidebar for Navigation
The st.sidebar.radio widget provides a simple menu for switching between the "Home" and "ETL Pipeline" pages. This keeps the interface clean and organized.
2. Extract Data
The st.file_uploader widget allows users to upload a CSV file.
Once uploaded, the file is read into a Pandas DataFrame using pd.read_csv().
The raw data is displayed using st.write().
3. Transform Data
Users select a column from the DataFrame via the st.selectbox widget.
A transformation is applied by multiplying the selected column by a user-defined value from the st.slider widget.
The resulting DataFrame is displayed with the new derived column.
4. Load Data
The transformed data is visualized using Matplotlib.
Users can toggle between a bar plot and a line plot using st.radio.
The plot is generated using the transformed column, displayed with st.pyplot().
How It Looks in Action
Upload CSV: The user uploads a cleaned CSV file (e.g., physics or weather data).
Apply Transformation: Select a column (e.g., temperature) and apply a multiplier to generate a new column.
View Results: The app displays the new data table and allows the user to view a plot of the transformation.
Extending the Pipeline
Save the Transformed Data: Add an option to download the updated dataset.
Data Filtering: Include additional widgets to filter rows or apply conditional logic.
Advanced Plots: Incorporate more sophisticated visualizations using libraries like Seaborn or Plotly.
This ETL pipeline example demonstrates how Streamlit can simplify the process of working with data, enabling STEM researchers to build actionable insights from their datasets with minimal effort.


# Github Streamlit



