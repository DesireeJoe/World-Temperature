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

   st.write("## World Temperature: Effects of Greenhouse Gasses on Gobal Temperatures")
   st.markdown("""
Understanding what impacts our planet's temperature changes over time is vital for understanding the dynamics of climate change. 

The goal of our project is to analyze the relationship between rising greenhouse gas emissions and their effect on global temperatures. 


This project dives into historical temperature records to uncover trends and patterns, using data from FAO, NASA and ‘Our World In Data”.

We want to understand how global warming has evolved over centuries and decades. We'll start by carefully looking at temperature data, going from the past to the present. Through detailed analysis and visualisation, we'll reveal how temperatures have changed across different parts of the world and over time.

Using data from FAO, NASA and ‘Our World In Data”, This project explores historical temperature records to try to uncover trends and patterns. We will highlight this data exploration in further detail in the next steps.
    """)
####

#Nasa Exploration#
if page ==  "Exploration Analysis - NASA":

# Title of the app
  st.title('Exploration Analysis - NASA')

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

  # Basic data info
  st.subheader('Basic Data Information')
  st.write(f"Size of the DataFrame: {nasa.shape}")
  buffer = io.StringIO()
  nasa.info(buf=buffer)
  s = buffer.getvalue()
  st.text(s)
  st.write(f"Missing values per column:\n{nasa.isna().sum()}")
  st.write(f"Number of duplicates: {nasa.duplicated().sum()}")
  st.write(f"Unique years: {nasa['Year'].unique()}")
  st.write(nasa.describe())

  # Boxplot for distribution of variables
  st.subheader('Temperature Anomalies - Box-and-Whisker Plot')
  columns = ['Glob', 'NHem', 'SHem', "24N-90N", "24S-24N", "90S-24S", "64N-90N", "44N-64N", "24N-44N","EQU-24N", "24S-EQU", "44S-24S", "64S-44S", "90S-64S"]
  
  fig, ax = plt.subplots(figsize=(10, 6))
  nasa[columns].boxplot(ax=ax)
  ax.set_title('Temperature Anomalies - Box-and-Whisker Plot')
  ax.set_xlabel('Scope')
  ax.set_ylabel('Temperature Anomaly')
  plt.xticks(rotation=45)
  st.pyplot(fig)
  
  # Line plot for global temperature anomalies
  st.subheader('Global Temperature Anomalies (1880-2023)')
  fig, ax = plt.subplots(figsize=(12, 6))
  sns.lineplot(data=nasa, x='Year', y='Glob', label='Glob', color='darkgreen', ax=ax)
  ax.set_title('Global Temperature Anomalies (1880-2023)')
  ax.set_xlabel('Year')
  ax.set_ylabel('Temperature Anomaly (°C)')
  st.pyplot(fig)
  
  # Line plot for hemispheric temperature anomalies
  st.subheader('Hemispheric Temperature Anomalies (1880-2023)')
  fig, ax = plt.subplots(figsize=(12, 6))
  sns.lineplot(data=nasa, x='Year', y='Glob', label='Global', ax=ax)
  sns.lineplot(data=nasa, x='Year', y='NHem', label='North Hemisphere', ax=ax)
  sns.lineplot(data=nasa, x='Year', y='SHem', label='South Hemisphere', ax=ax)
  ax.set_title('Hemispheric Temperature Anomalies (1880-2023)')
  ax.set_xlabel('Year')
  ax.set_ylabel('Temperature Anomaly (°C)')
  st.pyplot(fig)
  
  # Correlation heatmap
  st.subheader('Correlation Heatmap of Temperature Anomalies')
  correlation_matrix = nasa[columns].corr()
  fig, ax = plt.subplots(figsize=(8, 6))
  sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
  ax.set_title('Correlation Heatmap of Temperature Anomalies')
  st.pyplot(fig)
  
  # Climatic development with segmented color map
  st.subheader('Climatic Development Over Years')
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
  
  # Scatter plots with linear regression
  st.subheader('Scatter Plots with Linear Regression')
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
  ####

######
if page ==  "Exploration Analysis - OWID":

# Title of the app
  st.title('Exploration Analysis - OWID')

# Load data
  @st.cache
  def load_data():
    Co2 = pd.read_csv("owid-co2-data.csv", encoding='latin1')
    return Co2

  Co2 = load_data()

  # Show the data
  if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(Co2)

  # Basic data info
  st.subheader('Basic Data Information')
  st.write(f"Size of the DataFrame: {Co2.shape}")
  buffer = io.StringIO()
  Co2.info(buf=buffer)
  s = buffer.getvalue()
  st.text(s)
  st.write(f"Missing values per column:\n{Co2.isna().sum()}")
  st.write(f"Number of duplicates: {Co2.duplicated().sum()}")
  st.write(f"Unique years: {Co2['Year'].unique()}")
  st.write(Co2.describe())

#Credits#
####
if page == 'Credits':
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
