import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('To analyse the iris data set')
data=pd.read_csv('data/Iris.csv')
st.write(data)
st.header('Columns names')
col=data.columns
st.write(col)
options=st.selectbox('select the chart',['Barchart','Histogram','CountPlot'])
if options=='Barchart':
    st.bar_chart(data[['SepalLengthCm','PetalLengthCm']])
if options=='Histogram':
    sns.histplot(data=data, x="PetalLengthCm")
    plt.show()
    st.pyplot()
if options=='CountPlot':
    sns.countplot(data=data, x="PetalLengthCm")
    plt.show()
    st.pyplot()

