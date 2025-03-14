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
  bill_length_mm = st.slider('Bill length (mm)',32.1,52.6,41.9)
  bill_depth_mm = st.slider('Flipper Length (mm)',13.1,21.5,17.2)
  flipper_length_mm = st.slider('Flipper length (mm)',172.0,231.0,201.0)
  body_mass_g = st.slider("Body mass (g)",2700.00, 6300.0, 4267.0)
  gender = st..selected
  data = ('island': island,
          'bill_length_mm': bill_length_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'gender': gender)
  input_df = pd.DataFrame(data, index =[0])
  input_penguins = pd.concat([input_df,X], axis=0)
input_penguins
