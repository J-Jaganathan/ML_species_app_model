import streamlit as st
import pandas as pd
st.title('🎈 App Name')
st.info('This is the app that builds a machine learning model')
with st.expander('Data'):
  st.write('Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

  st.write('**X**');
  X = df.drop('species',axis=1)
  X

  st.write('**Y**');
  Y = df.species
  Y

with st.expander('Data Visualization'):
  st.scatter_chart(data=df,x = 'bill_length_mm', y='body_mass_g', color='species')

with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
  gender = st.selectbox('Gender',('male','female'))
  bill_length = st.slider('bill length (mm)',32.1,52.6,41.9)
