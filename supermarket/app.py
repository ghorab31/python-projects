import pandas as pd
import streamlit as st
import plotly.express as px
df=pd.read_csv("supermarket_sales - Sheet1.csv",index_col=0)   
st.markdown("<h1 style='text-align: center;color: white;'>Super Market Analysis</h1>",unsafe_allow_html=True)

page=st.sidebar.radio('pages',['Dataset','univariant','bivariant','multivariant'])
df['Date']=pd.to_datetime(df['Date'])
df['Month_Name']=df['Date'].dt.month_name()
df['Month']=df['Date'].dt.month.astype('object')
City=df['City'].unique()
Gender=df['Gender'].unique()
Customertype=df['Customer type'].unique()
start_date=st.sidebar.date_input("StartDate", value=df.Date.min(),min_value=df.Date.min(),max_value=df.Date.max())
end_Date=st.sidebar.date_input("EndDate", value=df.Date.min(),min_value=df.Date.min(),max_value=df.Date.max())
CustomerType=st.sidebar.multiselect('Customer type',df['Customer type'].unique(),default=Customertype)
Cityside=st.sidebar.multiselect('City',df.City.unique(),default=City)
Genderside=st.sidebar.multiselect('Gender',df.Gender.unique(),default=Gender)
df_filtered=df[(df.Date>=str(start_date))&(df.Date<=str(end_Date))]
df_filtered= df_filtered[df_filtered['City'].isin(Cityside)]
df_filtered=df_filtered[df_filtered['Gender'].isin(Genderside)]
df_filtered=df_filtered[df_filtered['Customer type'].isin(CustomerType)]
if page=='Dataset':
    st.dataframe(df_filtered)
elif page=='univariant':
    col=st.selectbox('select Column',df.columns)
    chart=st.selectbox('select Chart',['Histogram','box','pie'])
    if chart =='Histogram':
        st.plotly_chart(px.histogram(data_frame=df_filtered,x=col,title=col,width=400))
    elif chart=='box':
         st.plotly_chart(px.box(data_frame=df_filtered,y=col,title=col))
    elif chart=='pie':
        st.plotly_chart(px.pie(data_frame=df_filtered,names=col,title=col))
elif page == "bivariant":
    col1 = st.selectbox('Select Column for X-axis', df.columns, key='col1')
    col2 = st.selectbox('Select Column for Y-axis', df.columns, key='col2')
    colorr = st.selectbox('Select Column for Color', df.columns, key='colorr')
    chart=st.selectbox('select Chart',['bar','line','scatter'])
    if chart=='bar':
        st.plotly_chart(px.bar(data_frame=df_filtered,x=col1,y=col2,color=colorr,title=f'{col1} vs {col2}',facet_col=colorr).update_layout(barmode='group'))
    elif chart=='line':
        st.plotly_chart(px.line(data_frame=df_filtered,x=col1,y=col2,title=f'{col1} vs {col2}'))
    st.markdown("<h1 style='text-align: center;color: white;'>BiVariant analysis</h1>",unsafe_allow_html=True)
    genderdf=df_filtered.groupby(['Payment','Gender'])['gross income'].mean().reset_index().sort_values(ascending=False,by='gross income')
    st.plotly_chart(px.bar(data_frame=genderdf,x='Gender',y='gross income',barmode='group',color='Payment',text_auto=True,title="Payment"))
    gross_city_month=df_filtered.groupby(['City','Month_Name','Month'])['gross income'].sum().reset_index().round(2).sort_values(by='Month')
    st.plotly_chart(px.bar(data_frame=gross_city_month,x='Month_Name',y='gross income',color='City',barmode='group',facet_col='City'))

elif page=="multivariant":
    dfcor=df.corr(numeric_only=True)
    dfcor.drop(index='gross margin percentage',columns="gross margin percentage",inplace=True,)
    st.plotly_chart(px.imshow(dfcor,width=1200,height=600,text_auto=True,title="Correlation Matrix between columns"))



