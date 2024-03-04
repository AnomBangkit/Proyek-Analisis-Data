import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
sns.set(style="dark")

#load dataset
df = pd.read_csv(https://raw.githubusercontent.com/AnomBangkit/Proyek-Analisis-Data/main/Dashboard/Cleaned_hour_dataset.csv)
df["dteday"] = pd.to_datetime(df["dteday"])
st.set_page_config(page_title="Bike Sharing System EDA",
                   page_icon=":bike:",
                   layout="wide")


#helper function

def create_monthly_temp_df(df):
    monthly_temp_df=df.resample(rule="M", on="dteday").agg({
        "temp":"mean",
        "atemp": "mean",
        "cnt" : "mean"
    })
    monthly_temp_df.index = monthly_temp_df.index.strftime("%b-%y")
    monthly_temp_df = monthly_temp_df.reset_index()
    monthly_temp_df.rename(columns={
        'dteday':'month',
        'cnt':'total_rides',
        'temp': 'temperature (degC)',
        "atemp": "feel like temperature (degC)"
    }, inplace=True)
    return monthly_temp_df

def create_corr_df(df):
    corr_var=["cnt","temp", "atemp"]
    corr_df= df[corr_var]
    corr_df = corr_df.reset_index()
    corr_df.rename(columns={
        "cnt" : "total_rides",
        "temp": "temperature (degC)",
        "atemp": "feel like temperature (degC)"
    }, inplace=True)
    return corr_df


def create_monthly_users_df(df):
    monthly_users_df =df.resample(rule="M", on="dteday").agg({
        "casual": "sum",
        "registered" : "sum",
        "cnt" : "sum"
    })
    monthly_users_df.index = monthly_users_df.index.strftime('%b-%y')
    monthly_users_df = monthly_users_df.reset_index()
    monthly_users_df.rename(columns={
        "dteday" : "month",
        "cnt" : "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    }, inplace=True)

    return monthly_users_df

def create_seasonly_users_df(df):
    seasonly_users_df = df.groupby("season").agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    })
    seasonly_users_df = seasonly_users_df.reset_index()
    seasonly_users_df.rename(columns={
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    }, inplace=True)
    
    seasonly_users_df = pd.melt(seasonly_users_df,
                                      id_vars=['season'],
                                      value_vars=['casual_rides', 'registered_rides'],
                                      var_name='type_of_rides',
                                      value_name='count_rides')
    
    seasonly_users_df['season'] = pd.Categorical(seasonly_users_df['season'],
                                             categories=['Spring', 'Summer', 'Fall', 'Winter'])
    
    seasonly_users_df = seasonly_users_df.sort_values('season')
    
    return seasonly_users_df

def create_weekday_users_df(df):
    weekday_users_df = df.groupby("weekday").agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    })
    weekday_users_df = weekday_users_df.reset_index()
    weekday_users_df.rename(columns={
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    }, inplace=True)
    
    weekday_users_df = pd.melt(weekday_users_df,
                                      id_vars=['weekday'],
                                      value_vars=['casual_rides', 'registered_rides'],
                                      var_name='type_of_rides',
                                      value_name='count_rides')
    
    weekday_users_df['weekday'] = pd.Categorical(weekday_users_df['weekday'],
                                             categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    
    weekday_users_df = weekday_users_df.sort_values('weekday')
    
    return weekday_users_df

def create_hourly_users_df(df):
    hourly_users_df = df.groupby("hr").agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    })
    hourly_users_df = hourly_users_df.reset_index()
    hourly_users_df.rename(columns={
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    }, inplace=True)
    
    return hourly_users_df
  
#Main Page
st.header("Bike Sharing System App :bike:")
st.write ("The core data set is related to the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA")

#Sidebar
with st.sidebar :
    st.header("CAPITAL BIKESHARE")
    
    #make radio button
    page_names = ['Count Users', 'Data Distribution', "Temperature Plot"]
    page = st.radio('Navigation : ', page_names)
    
#Date picker
col1,col2 = st.columns((2))

#getting the min and max date
startDate = df["dteday"].min()
endDate = df["dteday"].max()

with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("End Date", endDate))

st.markdown("---")

main_df = df[(df["dteday"] >= date1) & (df["dteday"] <= date2)].copy()

monthly_temp_df = create_monthly_temp_df(main_df)
corr_df = create_corr_df(main_df)
monthly_users_df = create_monthly_users_df(main_df)
weekday_users_df = create_weekday_users_df(main_df)
seasonly_users_df = create_seasonly_users_df(main_df)
hourly_users_df = create_hourly_users_df(main_df)

if page == 'Count Users' :
    #Subheader User Page
    st.subheader("Users")
    col1, col2, col3 = st.columns(3)

    with col1:
        total_all_rides = main_df['cnt'].sum()
        st.metric("Total Rides", value=total_all_rides)
    with col2:
        total_casual_rides = main_df['casual'].sum()
        st.metric("Total Casual Rides", value=total_casual_rides)
    with col3:
        total_registered_rides = main_df['registered'].sum()
        st.metric("Total Registered Rides", value=total_registered_rides)

    monthly_fig = px.line(monthly_users_df,
                 x='month',
                 y=['casual_rides', 'registered_rides', 'total_rides'],
                 markers=True, 
                 title="Monthly Count of Bikeshare Rides").update_layout(xaxis_title='', yaxis_title='Total Rides')
    st.plotly_chart(monthly_fig, use_container_width=True)

    col1, col2 = st.columns(2)
    seasonly_fig = px.bar(seasonly_users_df,
                 x='season',
                 y=['count_rides'],
                 color='type_of_rides',
                 title='Count of bikeshare rides by season').update_layout(xaxis_title='', yaxis_title='Total Rides')

    col1.plotly_chart(seasonly_fig, use_container_width=True)

    weekday_fig = px.bar(weekday_users_df,
                 x='weekday',
                 y=['count_rides'],
                 color='type_of_rides',
                 barmode='group',
                 title='Count of bikeshare rides by weekday').update_layout(xaxis_title='', yaxis_title='Total Rides')

    col2.plotly_chart(weekday_fig, use_container_width=True)

    hourly_fig = px.line(hourly_users_df,
                 x='hr',
                 y=['casual_rides', 'registered_rides'],
                 markers=True,
                 title='Count of bikeshare rides by hour of day').update_layout(xaxis_title='', yaxis_title='Total Rides')

    st.plotly_chart(hourly_fig, use_container_width=True)

elif page == 'Data Distribution':
    #Subheader Data Distribution
    st.subheader("Data Distribution")
    st.write("In this App we will se the correlation between temperature and total Rides before that we have to know Data distribution")
    #tables
    st.dataframe(corr_df.head(50), hide_index=True, use_container_width=True)
    st.divider()
    
    #chart
    st.subheader("Normal Distribution")
    st.write("This is the normal distribution plot")
    
    norm_dist, axs = plt.subplots(1, 3, figsize=(15,5))

    #make scatter plot
    sns.histplot(data=corr_df, x="temperature (degC)", ax=axs[0], kde=True, bins=10, color="red")
    sns.histplot(data=corr_df, x="feel like temperature (degC)", ax=axs[1], kde=True, bins=10, color="blue")
    sns.histplot(data=corr_df, x="total_rides", ax=axs[2], kde=True, bins=10, color="green")

    #set title
    axs[0].set_title("temperature (degC)")
    axs[1].set_title("feel like temperature (degC)")
    axs[2].set_title("total_rides")

    # give label
    for i in range(3):
        axs[i].set_xlabel("Temperature(C)")
    else:
        axs[i].set_xlabel("Total Rental Bikes")   
    
    st.pyplot(norm_dist.get_figure())
    st.divider()

    #make box plot
    st.subheader("Box Plot")
    st.write("This is the box plot")
    box_plt, axs = plt.subplots(1, 3, figsize=(15,5))
    sns.boxplot(data=corr_df, y="temperature (degC)", ax=axs[0], orient="v", color="red")
    sns.boxplot(data=corr_df, y="feel like temperature (degC)", ax=axs[1], orient="v", color="blue")
    sns.boxplot(data=corr_df, y="total_rides", ax=axs[2], orient="v", color="green")

    #set title
    axs[0].set_title("temperature (degC)")
    axs[1].set_title("feel like temperature (degC)")
    axs[2].set_title("total_rides")

    #give label
    for i in range(3):
        axs[i].set_ylabel("Temperature(C)")
    else:
        axs[i].set_ylabel("Total Rental Bikes")

    st.pyplot(box_plt.get_figure())

else :
    #Subheader Temp Plot
    st.subheader("Temparature vs Total Rides")
    scatt_fig, axs = plt.subplots(1, 2, figsize=(15,5))

    #make scatter plot
    sns.scatterplot(x="temperature (degC)", y="total_rides", data=corr_df, ax=axs[0], color="red")
    sns.scatterplot(x="feel like temperature (degC)", y="total_rides", data=corr_df, ax=axs[1], color="blue")

    #set title
    axs[0].set_title("total_rides vs temperature (degC)")
    axs[1].set_title("total_rides vs feel like temperature (degC)")

    #give label
    for i in range(2):
        axs[i].set_xlabel("Temperature(C)")
        axs[i].set_ylabel("Total Rental Bikes")

    st.pyplot(scatt_fig.get_figure())
    st.divider()
    
    #regression
    st.subheader("Monthly User Regression Analysis")
    reg_fig, axs = plt.subplots(1, 2, figsize=(15,5))

    #make scatter plot
    sns.regplot(x="temperature (degC)", y="total_rides", ax=axs[0], data=monthly_temp_df, color="blue")
    sns.regplot(x="feel like temperature (degC)", y="total_rides", ax=axs[1], data=monthly_temp_df, color="red")

    #title
    axs[0].set_title("temperature (degC) vs total_rides")
    axs[1].set_title("feel like temperature (degC) vs total_rides")

    #label
    for i in range(2):
        axs[i].set_xlabel("Temperature(C)")
        axs[i].set_ylabel("Total Rental Bikes")
    
    st.pyplot(reg_fig.get_figure())
    
    #heatmap
    st.write("heatmap correlation between variable")
    htmp_fig = plt.figure(figsize=(10,5))
    sns.heatmap(monthly_temp_df.corr(numeric_only=True), annot=True)
    st.pyplot(htmp_fig.get_figure())
    
st.markdown("---")


