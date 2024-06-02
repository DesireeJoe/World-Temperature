import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress
import math
import io



# Seitenleiste
st.sidebar.markdown('<style>div.row-widget.stRadio div{color: black;}</style>', unsafe_allow_html=True)
# st.sidebar.write('<font color="black">Main Menu</font>', unsafe_allow_html=True)
page = st.sidebar.radio(" ", ["Home", "Introduction",
                              "Exploration Analysis - NASA",
                              "Exploration Analysis - OWID",
                              "Exploration Analysis - Surface Temperature Anomaly",
                              "Exploration Analysis - FAO",
                              "Modeling preparation",
                              "Machine Learning Models",
                              "Time-series modeling with SARIMA",
                              "Conclusion", "Credits"])



#####
if page == 'Home':
  
  
# Your Streamlit app content
  st.title("World Temperature")

  # Add the image to the home page
  st.image("world.png",  use_column_width=True)


# Inject custom CSS
st.markdown(
    """
    <style>
    .reportview-container {
        background: black;
        color: white;
    }
    .sidebar .sidebar-content {
        background: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)
if page == 'Introduction':

   st.write("## World Temperature: Effects of Greenhouse Gases on Gobal Temperatures")
   st.markdown("""
Understanding what impacts our planet's temperature changes over time is vital for understanding the dynamics of climate change. 

The goal of our project is to analyze the relationship between rising greenhouse gas emissions and their effect on global temperatures. 


This project dives into historical temperature records to uncover trends and patterns, using data from FAO, NASA and ‘Our World In Data”.

We want to understand how global warming has evolved over centuries and decades. We'll start by carefully looking at temperature data, going from the past to the present. Through detailed analysis and visualisation, we'll reveal how temperatures have changed across different parts of the world and over time.

Using data from FAO, NASA and ‘Our World In Data”, This project explores historical temperature records to try to uncover trends and patterns. We will highlight this data exploration in further detail in the next steps.
    """)
#################################################################################################################################

#Nasa Exploration#
if page ==  "Exploration Analysis - NASA":

# Title of the app
  st.title('Exploration Analysis - NASA')
# Display the logo
  st.image("nasa_x2.png", caption="", use_column_width=80)

# Introduction Section 
  st.markdown(
        """
        <style>
        .intro-box {
            border: 2px solid #0B3D91; 
            border-radius: 10px;
            background-color: #f9f9f9;
            padding: 15px;
            margin: 15px 0;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .intro-header {
            color: #0B3D91; 
            font-size: 22px;
            font-weight: bold;
        }
        .intro-text {
            font-size: 16px;
            line-height: 1.6;
            flex: 1;
        }
    
        </style>
        <div class="intro-box">
            <div class="intro-text">
                <div class="intro-header">Background, History and Updates</div>
                The GISS Surface Temperature Analysis version 4 - the GISTEMP v4 - is an estimate of global surface temperature change. Graphs and tables are updated around the middle of every month using current data files from NOAA GHCN v4 (meteorological stations) and also from ERSST v5 (ocean areas), combined as described in our publications Hansen et al. (2010) and Lenssen et al. (2019). These updated files incorporate reports for the previous month and also late reports and corrections for earlier months. Temperature change indicates deviations from the typical or expected temperature for a specific location and time. Tables of Global and Hemispheric Monthly Means and also Zonal Annual Means are available. We want to show a brief overview of the NASA temperature dataset, including descriptive statistics and basic properties.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
  
# Load data
  @st.cache
  def load_data():
    nasa = pd.read_csv("NASA_zonal.csv", encoding='latin1')
    return nasa

  nasa = load_data()

  # Show the data
  if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(nasa)
    
# Basic data info expander
  with st.expander("Properties and Descriptive statistics of the NASA dataset"):
      st.write("**Size of the DataFrame:**", nasa.shape)
      buffer = io.StringIO()
      nasa.info(buf=buffer)
      s = buffer.getvalue()
      st.text(s)
      st.markdown("**Variables:**")
      st.markdown("- The year of the measures\n"
                    "- 'Glob': This column represents the global average temperature anomaly. It provides the average temperature anomaly across the entire Earth, combining data from all latitudes and longitudes.\n"
                    "- 'NHem': This column represents the temperature anomaly for the Northern Hemisphere. It includes data from all latitudes in the Northern Hemisphere, from the equator (0 degrees latitude) to the North Pole (90 degrees latitude).\n"
                    "- 'SHem': This column represents the temperature anomaly for the Southern Hemisphere. It includes data from all latitudes in the Southern Hemisphere, from the equator (0 degrees latitude) to the South Pole (-90 degrees latitude).\n"
                    "- The rest of the variables represent latitude bands, indicating different regions of the Earth. E.g. the column '24N-90N' represents the latitude band from 24 degrees North to 90 degrees North, covering the Arctic region.")
      st.write("**Missing values per column:**", nasa.isna().sum())
      st.write("**Number of duplicates:**", nasa.duplicated().sum())
      st.write("**Data Description:**")
      st.write(nasa.describe())

  # Boxplot for distribution of variables
  st.markdown("#### Temperature anomalies in the different regions - Box-and-Whisker Plot")
  st.write('The following graph shows box-whisker plots for temperature anomalies in the different regions of the NASA data set. The analysis is essential to gain a better understanding of the distribution and dispersion of these data. Box-whisker plots provide a compact and informative representation of the statistical distribution and allow important aspects of the data to be grasped at a glance.')
  columns = ['Glob', 'NHem', 'SHem', "24N-90N", "24S-24N", "90S-24S", "64N-90N", "44N-64N", "24N-44N","EQU-24N", "24S-EQU", "44S-24S", "64S-44S", "90S-64S"]
  fig, ax = plt.subplots(figsize=(10, 6))
  nasa[columns].boxplot(ax=ax)
  ax.set_title('Temperature Anomalies - Box-and-Whisker Plot')
  ax.set_xlabel('Scope')
  ax.set_ylabel('Temperature Anomaly')
  plt.xticks(rotation=45)
  st.pyplot(fig)
  st.write('As a brief summary of the Box-and-Whisker Plot Observations and descriptive statistics in general it can be stated that the range of data (min-max) for most variables falls between -1 and 1. Only two variables (64N-90N, 90S-64S) exceed these boundaries. For 10 variables, the standard deviation is less than 0.5,  less than 1.0 for 3 variables, and less than 1.5 °C for 1 variable. In most variables, the mean and median values are closely aligned, indicating a low impact of extreme values on the mean. This is consistent with the box and whisker plot, where outliers are visible for Glob, NHem, 24-90N, 64N-90N, 24N-44N, 24S-EQU, and 90S-64S. For all other variables, the box-whisker plot does not show extreme values. For most variables (except 90S-64S), the spread from maximum to Q2 is larger than from minimum to Q2. Since Q2 is very close to 0 °C, this suggests that there are more temperature changes above average for that specific year. In the North Pole region (64N-90N), a greater variability in temperature change is observed. Anomaly values extend upwards to over +2 degrees Celsius (and sometimes even over +3 degrees Celsius), while the box extends downward to about -1.8 degrees Celsius')
  
  # Line plot for global temperature anomalies
  st.markdown("#### Global and Hemispheric Temperature Anomalies (1880-2023) - Lineplot")
  st.write('Visualising time series data with a line chart provide a clear view of the historical development of temperature anomalies on a global level and also in different geographic regions (here the north and the south Hemisphere). By visualising these data, we can see changes over time, identify seasonal variations, and analyse potential long-term trends.')
  fig, ax = plt.subplots(figsize=(12, 6))
  sns.lineplot(data=nasa, x='Year', y='Glob', label='Global', ax=ax)
  sns.lineplot(data=nasa, x='Year', y='NHem', label='North Hemisphere', ax=ax)
  sns.lineplot(data=nasa, x='Year', y='SHem', label='South Hemisphere', ax=ax)
  ax.set_title('Hemispheric Temperature Anomalies (1880-2023)')
  ax.set_xlabel('Year')
  ax.set_ylabel('Temperature Anomaly (°C)')
  st.pyplot(fig)
  st.write("""The Lineplot shows an increasing negative temperature change until 1910 (approx.) and increasing positive temperature change from approx. 1910 onwards until present. The graph indicates that temperature changes have been steadily increasing on average in recent years. This suggests that it is getting warmer on a global scale. Comparing temperature anomalies between the Northern and the Southern hemisphere shows that, especially since the year 2000, the temperature anomalies have been more positive in the Northern Hemisphere than in the Southern one. So the Temperature anomalies have been more positive in the Northern Hemisphere. This observation aligns with the overall understanding of climate change, as the Northern Hemisphere has been shown to experience more pronounced warming trends compared to the Southern Hemisphere. It could be attributed to various factors, including differences in land distribution, ocean currents, atmospheric circulation patterns, and human activities concentrated in the Northern Hemisphere. However, it is important to note that this interpretation is based on the assumption that the temperature anomalies are reliable and accurately represent the actual temperature changes in each hemisphere. Additionally, further analysis and examination of the data would be necessary to confirm the consistency and significance of these observed differences.""")

  # Climatic development with segmented color map
  from matplotlib.colors import LinearSegmentedColormap
  st.markdown("#### Climatic Development Over Years - Data Stripes")
  st.write("""The next data visualisation contains data stripes, which provide an intuitive way to visualise climate change and temperature trends. They offer a quick and clear representation of Earth's warming, making it easy to identify long-term temperature trends and point out differences between the earth zones/ latitudes.""")
  cmap = LinearSegmentedColormap.from_list('climate_stripes', ['turquoise', 'white', 'red'], N=256)
  years = nasa['Year']
  
  for column in columns:
      data = nasa[column]
      fig, ax = plt.subplots(figsize=(12, 1))
      norm = plt.Normalize(data.min(), data.max())
      colors = [cmap(norm(val)) for val in data]
      ax.bar(years, [1] * len(years), color=colors, width=1)
      ax.set_xlim(min(years), max(years))
      x_ticks = range(min(years), max(years), 20)
      ax.set_xticks(x_ticks)
      ax.set_xticklabels([str(year) for year in x_ticks])
      ax.set_yticklabels([])
      ax.set_xlabel('Year')
      ax.set_ylabel('Value')
      cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=cmap, norm=norm), ax=ax, orientation='horizontal', pad=0.60)
      cbar.set_label(f'Color for {column}')
      ax.set_title(f'Climatic development {column}')
      st.pyplot(fig)
  st.write('It appears that in recent decades, the majority of regions around the world have experienced predominantly positive temperature anomalies, especially since the 1980s / 1990s. However, there is an exception for the ‘90S-64S’ (South Pole) regions, where greater temperature variance is evident. Also the temperate zone in the south (64S-44S) shows earlier larger temperature changes since around 1970.')
  
  # Scatter plots with linear regression
  st.markdown("#### Relationship between years and temperature anomalies for different latitudes - Scatterplots")
  st.write('Another way of visualising the data is to use a scatter plot. These Scatter plots with linear regression lines provide visual insight into the relationship between years and temperature anomalies for different latitudes.')
  num_cols = len(nasa.columns) - 1
  num_rows = math.ceil(num_cols / 3)
  num_cols_subplot = min(num_cols, 3)
  fig, axes = plt.subplots(num_rows, num_cols_subplot, figsize=(15, 4 * num_rows))
  
  for i, column in enumerate(nasa.columns[1:]):
      row_idx = i // 3
      col_idx = i % 3
      ax = axes[row_idx, col_idx] if num_rows > 1 else axes[col_idx]
      ax.scatter(nasa['Year'], nasa[column], color='turquoise')
      ax.set_xlabel('Year')
      ax.set_ylabel(column)
      ax.set_title(f'Scatter Plot: Year vs. {column}')
      slope, intercept, r_value, p_value, std_err = linregress(nasa['Year'], nasa[column])
      line = slope * nasa['Year'] + intercept
      ax.plot(nasa['Year'], line, color='red')
      ax.text(0.8, 0.1, f'r = {r_value:.2f}\n p = {p_value:.4f}', transform=ax.transAxes)
  
  if num_cols_subplot < 3:
      for i in range(num_cols_subplot, 3):
          fig.delaxes(axes[row_idx, i])
  
  st.pyplot(fig)
  st.write('These graphs make it possible to identify trends, patterns, and correlations in temperature data. The linear regressions help quantify the direction and strength of these relationships and provide important insights into how climate has evolved in different regions over the years. To obtain a more profound comprehension of temperature variations over time across various latitudinal bands, a Pearson correlation analysis was performed for each latitude. Additionally, scatter plots were created to visualise the relationship between temperature change and the corresponding year. The plots reveal a consistent temperature increase over time, as all linear regression trends are positive. For the latitude 90S-64S (South Pole) plot, there is significant scatter, showing a more weak correlation. This suggests that while the South Pole has seen varied temperatures, using just the year is not enough to predict these anomalies. An also noticeable temperature dip occurred in approx. 1910 / 1920s and from the 1950s to 1980s (except in regions like SHem, 24S-24N, and 90S-64S). This non-uniform decrease hints at regional influences on temperature shifts, warranting further study.')
  
  ####

################################################################################################################################################################################################

if page ==  "Exploration Analysis - OWID":
# Title of the app
  st.title('Exploration Analysis - OWID')
if page == "Exploration Analysis - OWID":
    st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<h1 class="centered-title">Exploration Analysis - OWID</h1>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.write('Exploratory analyses are used to gain initial insight into the data, identify data quality issues, discover patterns and generate hypotheses. They are the starting point for further analyses and research in which specific questions are answered or models are developed.')
    st.write('Various representations and visualisations of the dataset now follow.')

    st.markdown("#### The OWID Dataset")

    st.write('**Intro**')
    st.write('The CO2 and Greenhouse Gas Emissions dataset is a collection of key metrics maintained by Our World in Data. It is updated regularly and includes data on CO2 emissions (annual, per capita, cumulative and consumption-based), other greenhouse gasses, energy mix, and other relevant metrics.')
    st.write('Overview of the OWID dataset, including statistics and basic properties: This step provides a first insight into the dataset, including the available variables and the general structure.')

    # Load Data
    @st.cache
    def load_data():
        Co2 = pd.read_csv("owid-co2-data.csv", encoding='latin1')
        return Co2

    Co2 = load_data()

      # Show the data
    if st.checkbox('Show raw data'):
       st.subheader('Raw data')
       st.write(Co2)

     # Expandable section for descriptive statistics
    with st.expander("Descriptive statistics of the OWID dataset"):
         st.dataframe(Co2.describe())
         st.markdown('**Looking at the OWID data set, the summary statistics indicate various things:**')
         st.markdown('*  In various variables, the mean and median value differ substantially (e.g. co2: 379.98 mean vs 3.10 median. This mismatch could 1) indicate the presence of outliers skewing the value distribution')
         st.markdown('*  A high number of missing values denoted as "0", skewing the distribution')
         st.markdown('*  The large difference between the Q3 and Q4 and the max value in various variables (e.g. co2, total_ghg) indicates the existence of very high outlier values')


    with st.expander("Properties of the OWID dataset"):
         st.markdown("###### Dimensions")
         st.markdown(f"- Number of Rows: {Co2.shape[0]}\n"
                     f"- Number of Columns: {Co2.shape[1]}\n")
         st.markdown("")
         st.markdown("###### Data types")
         st.markdown("- 71 variables are of data type float\n"
                    "- 1 variable is of dtype integer\n"
                    "- 2 variables are of dtype object\n"
                    "- This dataset is basically from the year 1880-2022 and shows the year wise values of CO2 emissions across different countries for every year\n")

         st.markdown("")
         st.markdown("###### Missing values")
         st.markdown("- There are missing values in almost every variable of the dataset\n"
                     "-  There are almost 31 columns with more than 50% of missing values\n")
         st.markdown("")
         st.markdown("###### Variables")
         st.markdown("- The dataset consists mainly of numerical variables on CO2 emissions with different scopes like emissions per emission source and the scope of aggregation (like total, shared, cumulative, per capita)\n"
                    "- Other context metrics like year, population, country and GDP\n"
                    "- Total countries in the dataset is around 231\n"
                    "- The values of carbon dioxide emissions are calculated in million tonnes\n"
                    "- For an in-detail description see [OWID CO2 Data GitHub](https://github.com/owid/co2-data)\n")

         st.markdown("***")

    # Total missing values
         mis_val = Co2.isnull().sum()
    
    # Percentage of missing values
         mis_val_percent = 100 * mis_val / len(Co2)
    
    # Make a table with the results
         mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    
    # Rename the columns
         mis_val_table_ren_columns = mis_val_table.rename(columns={0: 'Missing Values', 1: '% of Total Values'})
    
    # Sort the table by percentage of missing descending and filter out columns with no missing values
         mis_val_table_ren_columns = mis_val_table_ren_columns[mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values('% of Total Values', ascending=False).round(1)

    # Display the missing values table using Streamlit
    st.markdown("<h2 style='text-align: center;'>CO2 Dataset Missing Values Analysis</h2>", unsafe_allow_html=True)
    st.write("Below is the table showing the count and percentage of missing values for each column in the CO2 dataset:")
    st.dataframe(mis_val_table_ren_columns)
    
    st.write('**Having a more in detail look at the amount of missing values in the data set shows that:**')
    st.markdown('  * There is a large amount of missing values in the data set, accumulating to 56,62% of all values in the data set.')
    st.markdown('  * The amount of missing values varies a great deal across variables,')
    st.markdown('  * Some variables have a comparably low percentage of missing values and are below 1/3 of all entries (e.g. share_global_luc_co2, co2),')
    st.markdown('  * While others with amount of missing values exceed 90% of entries (e.g. consumption_co2, other_industry_co2)')
    
    st.markdown('  * The high share of missing values across a large part of the variables in the OWID data set (ranging from 15.3% to 94.9% across variables) poses some challenges to data selection and data preprocessing that might influence interpretability of the results further down the road.')

    st.markdown("***")
if page ==  "Exploration Analysis - OWID":
#Plots
#Barplot of different categories of C02 emissions

# CO2 categories
 categories = [
    'CO2',
    'Flaring CO2',
    'Other Industry CO2',
    'Methane',
    'Nitrous Oxide',
    'Oil CO2',
    'Gas CO2',
    'Coal CO2',
    'Cement CO2',
    'Total GHG',
    'Land Use Change CO2'
 ]

# Corresponding sum values for the selected categories
 co2_values = [
    11858676.647999998,
    90882.134,
    45375.86899999999,
    956622.5999999999,
    342210.54,
    2835551.222,
    1286208.5720000002,
    3935870.717,
    216475.77999999997,
    5022398.451,
    4609805.573
 ]

# Calculate percentages
 total_co2 = sum(co2_values)
 percentages = [(value / total_co2) * 100 for value in co2_values]

# Streamlit Title
 st.markdown("<h2 style='text-align: center;'>Barplot Representing the Distribution of CO2 Emissions Across Different Categories</h2>", unsafe_allow_html=True)
 st.write("This barplot provides a graphical representation of the percentage contribution of each category to the total CO2 emissions.")

# Create bar plot with percentages
 plt.figure(figsize=(12, 8))
 plt.bar(categories, percentages, color='skyblue')
 plt.title('CO2 Emissions by Category', fontsize=14)
 plt.xlabel('Category', fontsize=12)
 plt.ylabel('Percentage of Total CO2 Emissions', fontsize=12)
 plt.xticks(rotation=45, ha='right')
 plt.tight_layout()

# Display the plot in Streamlit
 st.pyplot(plt)
 st.markdown("***")

if page ==  "Exploration Analysis - OWID":
# Description of the plot
  st.markdown("### Description of the CO2 Emissions Distribution")
  st.write("""
  - **CO2 emissions** constitute the largest portion, representing **38%** of the total emissions.
  - **Land Use Change CO2** follows closely, accounting for **14.8%** of the total emissions, indicating the significant impact of land use practices on CO2 levels.
  - **Total GHG (Total Greenhouse Gases)** contribute **16.1%** to the emissions, emphasizing the collective impact of all greenhouse gases.
  - **Coal CO2** is a significant contributor at **12.6%**, indicating the role of coal in CO2 emissions from energy production.
  - **Oil CO2** accounts for **9.1%** of emissions, highlighting the contribution of oil-based activities.
  - **Gas CO2** represents **4.1%** of emissions, indicating the contribution of gas-related activities.
  - While categories like **Flaring CO2** and **Other Industry CO2** individually contribute smaller percentages, they still contribute to the overall emissions profile.
  - The bar chart underscores the diverse sources of CO2 emissions and the importance of addressing each category in mitigation strategies.
  """)

#Line plot for Global Co2 emissions by emission sources 
# Convert the 'year' column to an integer
  Co2['year'] = Co2['year'].astype(int)

# Filter data for years from 1880 onwards
  Co2 = Co2[Co2['year'] >= 1880]
# Select relevant columns for CO2 emissions by different sources
  emission_sources = ['flaring_co2', 'other_industry_co2', 'methane', 'nitrous_oxide',
                    'oil_co2', 'gas_co2', 'coal_co2', 'cement_co2', 'total_ghg', 'land_use_change_co2']

# Aggregate data by summing over years
  emission_data = Co2.groupby('year')[emission_sources].sum()

# Mapping variable names to custom legend labels
  legend_labels = {
    'flaring_co2': 'Flaring CO2',
    'other_industry_co2': 'Other Industry CO2',
    'methane': 'Methane',
    'nitrous_oxide': 'Nitrous Oxide',
    'oil_co2': 'Oil CO2',
    'gas_co2': 'Gas CO2',
    'coal_co2': 'Coal CO2',
    'cement_co2': 'Cement CO2',
    'total_ghg': 'Total GHG',
    'land_use_change_co2': 'Land Use Change CO2'
  }

# Title and Introduction
  st.markdown("<h2 style='text-align: center;'>Global CO2 Emissions by Emission Sources</h2>", unsafe_allow_html=True)
  st.write("The line plot illustrates global CO2 emissions over time, categorized by various emission sources. Each line in the plot represents the trend of CO2 emissions from a specific source, such as flaring, industrial processes, methane, nitrous oxide, oil, gas, coal, cement production, land use changes, and the total greenhouse gas emissions.")

# Plotting
  plt.figure(figsize=(12, 6))

  for source in emission_sources:
     plt.plot(emission_data.index, emission_data[source], label=legend_labels[source])

  plt.title('Global CO2 Emissions by Emission Sources', fontsize=14)
  plt.xlabel('Year', fontsize=12)
  plt.ylabel('CO2 Emissions (million tonnes)', fontsize=12)
  plt.legend()
  plt.grid(True)
  plt.tight_layout()  # Adjust layout to prevent overlapping elements

# Display the plot in Streamlit
  st.pyplot(plt)

# Description of the plot
  st.markdown("### Description of the CO2 Emissions Distribution")
  st.write("""
  - The contributions of different emission sources to the total CO2 emissions vary over time.
  - Some sources might show increasing trends, while others may exhibit fluctuations or decreasing patterns.
  - Certain emission sources, such as coal, oil, and gas, might stand out as major contributors to CO2 emissions due to their relatively higher emission levels.
  - The plot might unveil temporal patterns or anomalies in CO2 emissions from specific sources over time, indicating potential shifts in energy usage, industrial activities, or environmental policies.
  - Land use change CO2 emissions show distinct patterns, reflecting alterations in land use practices like deforestation, afforestation, or changes in agricultural land management.
  - The plot includes a line for total greenhouse gas emissions, which provides an overview of the cumulative impact of all emission sources considered, with an initial steady rise and then a sudden rise from around the 1990s till the 2020s, followed by a sudden decline.
  - The sudden decline can also be attributed to missing values that have not yet been addressed.
  - Observing the lines collectively can help in understanding the interrelation between different emission sources and their combined effect on global CO2 levels.
  """)
  st.markdown("***")
  
if page ==  "Exploration Analysis - OWID":
  # Convert the 'year' column to an integer
    Co2['year'] = Co2['year'].astype(int)

    # Filter data to exclude entries that are not individual countries
    excluded_entries = ['World', 'Asia', 'Africa', 'Europe', 
                    'North America', 'Oceania', 'South America', 'High-income countries', 
                    'Low-income countries', 'Lower-middle-income countries', 
                    'Upper-middle-income countries']

    Co2 = Co2[~Co2['country'].isin(excluded_entries)]

# Calculate total methane emissions for each country
    country_methane_emissions = Co2.groupby('country')['methane'].sum()

# Sort countries based on methane emissions and select top 5
    top_5_countries_methane = country_methane_emissions.nlargest(5)

# Extract data for the top 5 countries
    top_5_countries_data = Co2[Co2['country'].isin(top_5_countries_methane.index)]

#pivot the values 
    methane_pivot = top_5_countries_data.pivot(index='year', columns='country', values='methane')

# Title and Introduction
    st.markdown("<h2 style='text-align: center;'>Top 5 Countries with Highest CO2 Emissions from Methane</h2>", unsafe_allow_html=True)
    st.write("The line plot illustrates the trend of methane emissions over time for the top 5 countries with the highest total methane emissions. Each line represents the methane emissions trajectory for one of the top 5 countries, namely China, the United States, India, Russia, and the European Union. The plot enables a comparative analysis of methane emission patterns among these nations, offering insights into their respective contributions to global methane emissions.")

# Plotting
    plt.figure(figsize=(12, 6))
    methane_pivot.plot()

    plt.title('Methane Emissions for Top 5 Countries', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Methane Emissions (million tonnes)', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

# Display the plot in Streamlit
    st.pyplot(plt)

# Description of the plot
    st.markdown("### Description of Methane Emissions Distribution")
    st.write("""
      - China consistently exhibits high levels of methane emissions over the years, likely due to its extensive agricultural activities, coal mining, and rapidly growing industrial sector.
      - The United States also shows a notable presence in methane emissions, attributed to its diverse economy, including agriculture, oil and gas production, and waste management practices.
      - India's methane emissions exhibit an upward trend, reflecting its growing population, agricultural practices, and expanding industrial base, which heavily relies on coal for energy production.
      - Russia's methane emissions may stem from various sources such as natural gas production, agricultural activities, and landfills, reflecting the country's vast territory and resource-intensive industries.
      - The European Union, representing a collective of countries, demonstrates efforts to curb methane emissions over time, possibly driven by regulatory measures, technological advancements, and increased awareness of environmental issues.
      """)
#####################################################################################################################################################################
 
if page ==  "Exploration Analysis - Surface Temperature Anomaly":
# Title of the app
     st.title('Exploration Analysis - Surface Temperature Anomaly')
     st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
     )
     st.markdown('<h1 class="centered-title">Exploration Analysis - Surface Temperature Analysis</h1>', unsafe_allow_html=True)
     st.markdown("<br><br>", unsafe_allow_html=True)

     st.markdown("#### The Surface Temperature Anomaly Dataset")

     st.write('**Intro**')
     st.write('Surface temperature anomaly, measured in degrees Celsius The temperature anomaly is relative to the 1951-1980 global average temperature. Data is based on the HadCRUT analysis from the Climatic Research Unit (University of East Anglia) in conjunction with the Hadley Centre (UK Met Office).')
     st.write('Overview of the Surface Temperature Anomaly dataset, including statistics and basic properties: This step provides a first insight into the dataset, including the available variables and the general structure.')

    # Load Data
     @st.cache
     def load_data():
       sta = pd.read_csv("hadcrut-surface-temperature-anomaly.csv", encoding='latin1')
       return sta

     sta = load_data()

      # Show the data
     if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(sta)

     # Expandable section for descriptive statistics
     with st.expander("Descriptive statistics of the Surface Temperature Anomaly dataset"):
          st.dataframe(sta.describe())
          st.markdown('* The Entity is the country variable and the code is the country codes')
          st.markdown('* The Year variables is from 1850-2017 and the surface temperature anomaly is measured for every country every year')
          st.markdown('* The Surface temperature anomaly dataframe in total has 4 columns')

     with st.expander("Properties of the Surface Temperature Anomaly dataset"):
          st.markdown("###### Dimensions")
          st.markdown(f"- Number of Rows: {sta.shape[0]}\n"
                      f"- Number of Columns: {sta.shape[1]}\n")
          st.markdown("")
          st.markdown("###### Data types")
          st.markdown("- 1 variables are of data type float\n"
                      "- 1 variable is of dtype integer\n"
                      "- 2 variables are of dtype object\n")
          st.markdown("")
          st.markdown("###### Missing values")
          st.markdown("- Exist only in the Code variable in the dataset\n")
                      
          st.markdown("")
          st.markdown("###### Variables")
          st.markdown("- The dataset consists only 4 columns: The Year from 1850-2017, the surface temeprature measured in different countries every year over the mentioned time period and the country codes\n"
                      "- For an in-detail description see [Surface Temeprature Anomaly Data](https://ourworldindata.org/grapher/hadcrut-surface-temperature-anomaly)\n")

          st.markdown("***")
         
          st.markdown("#### Missing values")

    # Total missing values
          mis_val = sta.isnull().sum()
    
    # Percentage of missing values
          mis_val_percent = 100 * mis_val / len(sta)
    
    # Make a table with the results
          mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    
    # Rename the columns
          mis_val_table_ren_columns = mis_val_table.rename(columns={0: 'Missing Values', 1: '% of Total Values'})
    
    # Sort the table by percentage of missing descending and filter out columns with no missing values
          mis_val_table_ren_columns = mis_val_table_ren_columns[mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values('% of Total Values', ascending=False).round(1)

    # Display the missing values table using Streamlit
          st.write("Below is the table showing the count and percentage of missing values for each column in the Surface temperature anomaly dataset:")
          st.dataframe(mis_val_table_ren_columns)
    
          st.write('**Having a more in detail look at the amount of missing values in the data set shows that:**')
          st.markdown('  * The column of Code had missing values of 164 about 0.55%')
          st.markdown('  * But when checked it was observed that there was an entry Micronesia in the code column')
          st.markdown('  * So we removed this entry and now the dataset has no missing values for the further computation and analysis')
         
          st.markdown("***")

if page ==  "Exploration Analysis - Surface Temperature Anomaly":
   top_countries = ['Afghanistan', 'Chad', 'Uganda', 'Romania', 'Belarus']
   surface_temp_top_countries = sta[sta['Entity'].isin(top_countries)]

   # Title and Introduction
   st.markdown("<h2 style='text-align: center;'>Surface Temperature Anomaly in Top 5 Countries </h2>", unsafe_allow_html=True)
   st.write("The plot illustrates the surface temperature anomaly trends in the top 5 countries (Afghanistan, Chad, Uganda, Romania, and Belarus) from the years 1880 to 2017.")

    # Plotting
   plt.figure(figsize=(10, 6))

   for country in top_countries:
       country_data = surface_temp_top_countries[surface_temp_top_countries['Entity'] == country]
       plt.plot(country_data['Year'], country_data['Surface temperature anomaly'], label=country)
   plt.xlabel('Year')
   plt.ylabel('Surface Temperature Anomaly')
   plt.title('Surface Temperature Anomaly in Top 5 Countries (1880-2017)')
   plt.legend()
   plt.grid(True)
   plt.tight_layout()

    # Display the plot in Streamlit
   st.pyplot(plt)

    # Description of the plot
   st.markdown("### Description of Surface Temperature Anomaly Trends")
   st.write("""
   - The plot allows for a visual comparison of surface temperature anomalies across the top 5 countries over the available time period.
   - Each country's data spans a different time period: Afghanistan from 1947 to 2017, Chad from 1946 to 2017, Uganda from 1901 to 2017, and Romania and Belarus from 1850 to 2017.
   - There have been significant fluctuations in temperature anomaly trends over the centuries.
   - Until around 1975, the trends remained relatively constant across most countries.
   - Belarus shows a sudden drop in surface temperature anomaly around 1945, possibly due to natural variations caused by increased industrial activities during World War II.
   - All the countries have exhibited an increasing trend in surface temperature anomalies after 1975 until 2017.
   - Uganda shows the highest surface temperature anomaly, reaching around 3.8 degrees Celsius around 2015.
   - An interesting observation is the falling trend in surface temperature anomaly for Afghanistan around 2017, indicating a deviation from the overall increasing trend observed in other countries.
   - This anomaly might warrant further investigation into the factors influencing temperature patterns in Afghanistan.
    """)     
   st.markdown("***")

if page ==  "Exploration Analysis - Surface Temperature Anomaly":
      sns.set_style("whitegrid")
      
      @st.cache
      def load_data():
        merged_data = pd.read_csv("merged_data.csv", encoding='latin1')
        return merged_data
      merged_data = load_data()    
  
# Title and Plot Title Description
      st.markdown("<h2 style='text-align: center;'>CO2 Emissions and Surface Temperature Anomalies Over Years</h2>", unsafe_allow_html=True)
      st.write("The Line plot represents two line plots on the same graph. The first line plot depicts the trend of surface temperature anomaly over the years from 1850 to 2017. The second line plot illustrates the trend of CO2 emissions over the years from 1880 to 2022.")

# Create a figure and axis object
      fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot CO2 emissions on the primary y-axis
      sns.lineplot(data=merged_data, x='Year', y='co2', color='red', ax=ax1, label='CO2 Emissions')

# Set the y-label for CO2 emissions
      ax1.set_ylabel('CO2 Emissions (Tonnes)', color='red')
 
# Create a secondary y-axis for Surface Temperature Anomaly
      ax2 = ax1.twinx()
      sns.lineplot(data=merged_data, x='Year', y='Surface temperature anomaly', color='blue', ax=ax2, label='Surface Temperature Anomaly')

# Set the y-label for Surface Temperature Anomaly
      ax2.set_ylabel('Surface Temperature Anomaly (°C)', color='blue')

# Set labels and title
      ax1.set_xlabel('Year')
      plt.title('CO2 Emissions and Surface Temperature Anomaly Over Years')

# Show legend
      lines1, labels1 = ax1.get_legend_handles_labels()
      lines2, labels2 = ax2.get_legend_handles_labels()
      ax1.legend(lines1, ['CO2 Emissions'], loc='upper left')
      ax2.legend(lines2, ['Surface Temperature Anomaly'], loc='upper right') 

# Rotate x-axis labels for better readability
      plt.xticks(rotation=45)

# Show the plot
      st.pyplot(fig)

# Description of the plot
      st.markdown("### Description of CO2 Emissions and Surface Temperature Anomalies Trends")
      st.write("""                                                                                                                                  
    - Both line plots show an overall increasing trend over the respective time periods.
    - The surface temperature anomaly exhibits a steady increase from 1850 to 2017, while CO2 emissions show a rising trend from 1880 to 2022.
    - Despite the general upward trajectory, both plots also exhibit periods of fluctuations and variability.
    - These fluctuations may result from various factors such as natural climate variability, human activities, and external events.
    - The simultaneous increase in both surface temperature anomaly and CO2 emissions suggests a potential relationship between the two variables.
    - This observation aligns with the scientific understanding that increasing CO2 emissions contribute to global warming, leading to rising surface temperatures.
    - In recent years, there appears to be a steeper increase in both surface temperature anomaly and CO2 emissions.
    - This observation suggests a potential acceleration in global warming and underscores the urgency of addressing climate change mitigation efforts. 
    """)
      st.markdown("***")

if page ==  "Exploration Analysis - Surface Temperature Anomaly":
    import streamlit as st
    import plotly.express as px
    import pandas as pd


    # Plotly Choropleth Map with a different color scale
    fig = px.choropleth(
          sta,
          locations='Entity',
          color='Surface temperature anomaly',
          hover_name='Entity',
          animation_frame='Year',
          projection='natural earth',
          title='Surface Temperature Anomaly Over Time',
          color_continuous_scale='Viridis'  # Change the color scale to Viridis
     )

    # Customize the layout
    fig.update_layout(
        coloraxis_colorbar=dict(
        title='Surface Temperature Anomaly (°C)'
    ),
    coloraxis_colorbar_thickness=25,
    coloraxis_colorbar_len=0.5
    )

# Display the map in Streamlit
    st.plotly_chart(fig)
#########################################################################################################################################################
if page == "Exploration Analysis - FAO" : 
  st.write("### Exploration of FAO Datasets")
  st.write("##### Food and Agriculture Orginization of the United Nations")

# Load data
  @st.cache
  def load_data():
    FAO_Continent = pd.read_csv("FAO_merged.csv", sep=',', encoding='latin1')
    FAO_global = pd.read_csv("FAO_Global.csv", sep=',', encoding='latin1')

    return FAO_Continent, FAO_global

  FAO_Continent, FAO_global = load_data()

    
  with st.expander("Full description of data"):
     st.markdown("""
                **Data description:**
The FAOSTAT Temperature change on land domain disseminates statistics of mean surface temperature change by country, with annual updates. 
The current dissemination covers the period 1961–2023. Statistics are available for monthly, seasonal and annual mean temperature anomalies, 
i.e., temperature change with respect to a baseline climatology, corresponding to the period 1951–1980.
                The standard deviation of the temperature change of the baseline methodology is also available. Data are based on the publicly available GISTEMP data, the Global Surface Temperature Change data distributed by the National Aeronautics and Space Administration Goddard Institute for Space Studies (NASA-GISS)
\n\n
**Statistical concepts and definitions:**    Statistical standards: Data in the Temperature Change on land domain are not an explicit SEEA variable. Nonetheless, country and regional calculations employ a definition of “Land area” consistent with SEEA Land Use definitions, specifically SEEA CF Table 5.11 “Land Use Classification” and SEEA AFF Table 4.8, “Physical asset account for land use.” The Temperature Change domain of the FAOSTAT Agri-Environmental Indicators section is compliant with the Framework for the Development of Environmental Statistics (FDES 2013), contributing to FDES Component 1: Environmental Conditions and Quality, Sub-component 1.1: Physical Conditions, Topic 1.1.1: Atmosphere, climate and weather, Core set/ Tier 1 statistics a.1    
 \n\n
  **Reference area:**    Reference area: Area of all the Countries and Territories of the world. In 2023: 198 countries and 39 territories.&nbsp; | Code - reference area: FAOSTAT, M49, ISO2 and ISO3 (https://www.fao.org/faostat/en/#definitions).CHAR(13)CHAR(10)CHAR(13)CHAR(10)FAO Global Administrative Unit Layer (GAUL National level – reference year 2014. FAO Geospatial data repository GeoNetwork. Permanent address: https://www.fao.org:80/geonetwork?uuid=f7e7adb0-88fd-11da-a88f-000d939bc5d8
 \n\n

**Time coverage:** 1961-2023 | Periodicity: Monthly, Seasonal, Yearly
 \n\n
**Base period:** 1951-1980
""")

     st.dataframe(FAO_global, height=400)

     fao_merged_filt = FAO_Continent[FAO_Continent['Months'] == 'Meteorological year']

# Filter for 5 continents
     fao_merged_filt = fao_merged_filt[fao_merged_filt['Area'].isin(['Americas', 'Europe', 'Asia', 'Africa', 'Oceania'])]

    # Slider for year range selection
  st.write("#### Temperature changes from 1961 - 2019")
  year_range = st.slider(
    "Select the year range",
    int(fao_merged_filt['Year'].min()), int(fao_merged_filt['Year'].max()), 
   (int(fao_merged_filt['Year'].min()), int(fao_merged_filt['Year'].max())), 
        step=1
    )

# Filter the data based on the selected year range
  filtered_data = fao_merged_filt[(fao_merged_filt['Year'] >= year_range[0]) & (fao_merged_filt['Year'] <= year_range[1])]

# Create subplots
fig, axs = plt.subplots(5, 1, figsize=(10, 20))

# Plot temperature against years for each area
for i, area in enumerate(filtered_data['Area'].unique()):
    area_data = filtered_data[filtered_data['Area'] == area]
    axs[i].plot(area_data['Year'], area_data['Temperature change'], marker='o', label=area)
    axs[i].set_xlabel('Years')
    axs[i].set_ylabel('Temperature (°C)')
    axs[i].set_title(f'Temperature change (°C) for {area}')
    axs[i].legend()
    axs[i].grid(True)
    axs[i].set_ylim(-1.5, 2.5)  # Set y-axis limits from -2 to 2

# Adjust layout to prevent overlap
fig.tight_layout(pad=3.0)

st.pyplot(fig)

#All continents graph
fig, ax = plt.subplots()

ax.plot(FAO_Continent.query("Area == 'Europe'")['Year'], FAO_Continent.query("Area == 'Europe'")['Temperature change'], marker='o', color='blue', label='Europe')
ax.plot(FAO_Continent.query("Area == 'Asia'")['Year'], FAO_Continent.query("Area == 'Asia'")['Temperature change'], marker='x', color='green', label='Asia')
ax.plot(FAO_Continent.query("Area == 'Africa'")['Year'], FAO_Continent.query("Area == 'Africa'")['Temperature change'], marker='s', color='red', label='Africa')
ax.plot(FAO_Continent.query("Area == 'Americas'")['Year'], FAO_Continent.query("Area == 'Americas'")['Temperature change'], marker='^', color='orange', label='Americas')
ax.plot(FAO_Continent.query("Area == 'Oceania'")['Year'], FAO_Continent.query("Area == 'Oceania'")['Temperature change'], marker='D', color='purple', label='Oceania')

ax.set_xlabel('Years')
ax.set_ylabel('Temperature')
ax.set_title('Temperature Variation for Different Continents')
ax.legend()
ax.grid(True)

st.pyplot(fig)

import plotly.express as px

# Plotly Choropleth Map with a different color scale
fig = px.choropleth(
    FAO_global,
    locations='ISO3 Code',
    color='Temperature change',
    hover_name='Area',
    animation_frame='Year',
    projection='natural earth',
    title='Temperature Change Over Time',
    color_continuous_scale='Viridis'  # Change the color scale to Viridis
)

# Customize the layout
fig.update_layout(
    coloraxis_colorbar=dict(
        title='Temperature Change (°C)'
    ),
    coloraxis_colorbar_thickness=25,
    coloraxis_colorbar_len=0.5
)

# Display the map in Streamlit
st.plotly_chart(fig)

###
###########################################################################################################################################################################################################################

if page ==  "Machine Learning Models":
  # Title of the app
     st.title('Machine Learning Models')
     st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
     )
     st.markdown('<h1 class="centered-title">Machine Learning Models</h1>', unsafe_allow_html=True)
     st.markdown("<br><br>", unsafe_allow_html=True)

############################################################################################################################################################################################################################
if page ==  "Credits":
   st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        .linkedin-logo {
            width: 30px;
            height: 30px;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
st.markdown('<h1 class="centered-title">Credits</h1>', unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
   
with col1:
     st.write("**Members of the project team:**")
     st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
     st.write("**Resources:**")
     st.markdown("<br><br><br><br><br><br><br>", unsafe_allow_html=True)
     #st.write("**Project report: uploaden?**") # upload report
   
with col2:
     st.write("Manasi Deshpande")
     st.write("Desireé Jörke")
     st.write("Fiona Murphy")
     st.markdown("<br>", unsafe_allow_html=True)
     st.write("Tarik Anour (Tutor)")
     st.markdown("<br>", unsafe_allow_html=True)
     st.write("[NASA GISTEMP Data](https://data.giss.nasa.gov/gistemp/)")
     st.write("[OWID CO2 Data](https://github.com/owid/co2-data)")
     st.write("[Surface Temperature Anomaly Data](https://ourworldindata.org/grapher/hadcrut-surface-temperature-anomaly)")
     st.write("[FAO Annual Surface Temperature Change dataset](https://www.fao.org/faostat/en/#data/ET)")
        
with col3:     
     linkedin_icon = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"

     st.markdown(
        f'<a href="https://www.linkedin.com/in/manasi-deshpande-b68730191/" target="_blank">'
        f'<img class="linkedin-logo" src="{linkedin_icon}" alt="LinkedIn" width="100" height="100" />'
        f'</a>', 
        unsafe_allow_html=True
        )


st.markdown(
         f'<a href="https://www.linkedin.com/in/desireé-jörke-7ba6321a3/" target="_blank">'
         f'<img class="linkedin-logo" src="{linkedin_icon}" alt="LinkedIn" />'
         f'</a>', 
         unsafe_allow_html=True
         )

st.markdown(
         f'<a href="https://www.linkedin.com/in/fionamurphy90//" target="_blank">'
         f'<img class="linkedin-logo" src="{linkedin_icon}" alt="LinkedIn" />'
         f'</a>', 
         unsafe_allow_html=True
         )

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<span style='font-size: 12px;'>\*For each member of the group, specify the level of expertise around the problem addressed:</span>  \n<span style='font-size: 12px;'>   None of the members have prior knowledge with respect to in-depth climate data analysis.</span>", unsafe_allow_html=True)

# linkedIn logo 1 https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Logo.svg.original.svg
# linkedIn logo 2 https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg

