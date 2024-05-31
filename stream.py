import streamlit as st

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

   st.write("## World Temperature: Effects of Greenhouse Emissions on Gobal Temperatures")
   st.markdown("""
Understanding what impacts our planet's temperature changes over time is vital for understanding the dynamics of climate change. 

The goal of our project is to analyze the relationship between rising greenhouse gas emissions and their effect on global temperatures. 


This project dives into historical temperature records to uncover trends and patterns, using data from FAO, NASA and ‘Our World In Data”.

We want to understand how global warming has evolved over centuries and decades. We'll start by carefully looking at temperature data, going from the past to the present. Through detailed analysis and visualisation, we'll reveal how temperatures have changed across different parts of the world and over time.

Using data from FAO, NASA and ‘Our World In Data”, This project explores historical temperature records to try to uncover trends and patterns. We will highlight this data exploration in further detail in the next steps.
    """)
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
    
######################################################
######
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
  
  st.dataframe(Co2)

    # Expandable section for descriptive statistics
    with st.expander("Descriptive statistics of the OWID dataset"):
        st.dataframe(Co2.describe())
        st.markdown('**Looking at the OWID dataset, the summary statistics indicate various things:**')

    with st.expander("Properties of the OWID dataset"):
        st.markdown("###### Dimensions")
        st.markdown(f"- Number of Rows: {Co2.shape[0]}\n"
                    f"- Number of Columns: {Co2.shape[1]}\n")
        st.markdown("")
        st.markdown("###### Data types")
        st.markdown("- 71 variables are of data type float\n"
                    "- 1 variable is of dtype integer\n"
                    "- 2 variables are of dtype object\n")
        st.markdown("")
        st.markdown("###### Missing values")
        st.markdown("- Exist in almost all of the variables in the dataset\n"
                    "- Vary greatly in share of total entries among variables\n")
        st.markdown("")
        st.markdown("###### Variables")
        st.markdown("- The dataset consists mainly of numerical variables on CO2 emissions with different scopes like emissions per emission source and the scope of aggregation (like total, shared, cumulative, per capita)\n"
                    "- Other context metrics like year, population, country and GDP\n"
                    "- For an in-detail description see [OWID CO2 Data GitHub](https://github.com/owid/co2-data)\n")

    st.markdown("***")

    # Missing values analysis
    st.markdown("#### Missing values")

    # Function to calculate missing values
    def missing_values_table(df):
        mis_val = df.isnull().sum()
        mis_val_percent = 100 * mis_val / len(df)
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        mis_val_table_ren_columns = mis_val_table.rename(columns={0: 'Missing Values', 1: '% of Total Values'})
        mis_val_table_ren_columns = mis_val_table_ren_columns[mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values('% of Total Values', ascending=False).round(1)
        return mis_val_table_ren_columns
    
    # Calculate the missing values table
    missing_table = missing_values_table(Co2)

    # Display the missing values table
    st.dataframe(missing_table)
    st.write('<span style="font-size: 12px;">*Click on the column heading to sort in ascending / descending order.</span>', unsafe_allow_html=True)

    st.write('**Having a more in-detail look at the amount of missing values in the dataset shows that:**')
    st.markdown('  * There is a large amount of missing values in the dataset, accumulating to 56.62% of all values in the dataset.')
    st.markdown('  * The amount of missing values varies greatly across variables.')
    st.markdown('  * Some variables have a comparably low percentage of missing values and are below 1/3 of all entries (e.g., `share_global_luc_co2`, `co2`).')
    st.markdown('  * Some variables have missing values exceeding 90% of entries (e.g., `consumption_co2`, `other_industry_co2`).')

    st.write('The high share of missing values across a large part of the variables in the OWID dataset (ranging from 15.3% to 94.9% across variables) poses some challenges to data selection and preprocessing that might influence interpretability of the results further down the road.')

    st.markdown("***")

#################################################################################################################################################################33
if page ==  "Exploration Analysis - Surface Temperature Anomaly":

# Title of the app
  st.title('Exploration Analysis - Surface Temperature Anomaly')

# Load data
  @st.cache
  def load_data():
    sta = pd.read_csv("hadcrut-surface-temperature-anomaly.csv", encoding='latin1')
    return sta

  sta = load_data()

  # Show the data
  if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(sta)

  # Basic data info
  st.subheader('Basic Data Information')
  st.write(f"Size of the DataFrame: {sta.shape}")
  buffer = io.StringIO()
  sta.info(buf=buffer)
  s = buffer.getvalue()
  st.text(s)
  st.write(f"Missing values per column:\n{sta.isna().sum()}")
  st.write(f"Number of duplicates: {sta.duplicated().sum()}")
  st.write(sta.describe())
####
