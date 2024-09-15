import streamlit as st
import pandas as pd
import plotly.express as px
from constants import Color

def read_data():
    df = pd.read_csv("supahcoolsoft.csv", index_col=0, parse_dates=[0])
    df.columns = df.columns.str.strip()
    return df

def layout():
    df = read_data()
    st.markdown("# Company Executive Dashboard")
    st.markdown("This is a simple dashboard about our company and the employees.")
    st.markdown("## Raw Data")
    st.dataframe(df)

    numeric_columns = df.select_dtypes(include='number').columns
    Column = st.selectbox("Choose Column", numeric_columns)
    
    
    df_stats = df[Column].describe()
    cols = st.columns(4)
    stats = ["min", "mean", "max", "count"]
    labels = ["Min", "Average", "Max", "Total Count"]
    
    for col, stat, label in zip(cols, stats, labels):       
        with col:
            st.metric(label=label, value=df_stats[stat])
        
    if 'Department' in df.columns:
        
        df_count = df['Department'].value_counts().reset_index()
        df_count.columns = ['Department', 'Count']
        
        
        fig = px.bar(
            data_frame=df_count,
            x='Department',
            y='Count',
            title='Bar Chart of Employees Count by Department'
        )
        st.plotly_chart(fig)
    else:
        st.error("The 'Department' column is not present in the DataFrame.")
    fig = px.histogram(
        data_frame= df , 
        x = 'Salary_SEK',
        nbins = 20,
        title= 'Histogram of salary Distribution',
    )
    st.plotly_chart(fig)

    df_salary_department = df[["Department" , "Salary_SEK"]]

    fig = px.box(
        data_frame= df_salary_department , 
        x = 'Department',
        y = 'Salary_SEK',
        title= 'Box Chart of the Salaries in different Departments'
    )
    st.plotly_chart(fig)

    fig = px.histogram(
        data_frame= df,
        x = 'Age',
        nbins= 20,
        title= 'History Of Age Distribution',
    )
    st.plotly_chart(fig)
    df_age_Department = df[['Department' , 'Age']]

    fig = px.box(
        data_frame= df_age_Department ,
        x = 'Department',
        y = 'Age',
        title= 'History of distribution of ages in departments',
    )
    st.plotly_chart(fig)


    fig.update_layout(
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        paper_bgcolor= Color.BACKGROUND,
        plot_bgcolor= Color.BACKGROUND,
    )
    st.plotly_chart(fig)

    read_css()



def read_css():
    with open('style.css') as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True,
        )

if __name__ == "__main__":
    layout()
