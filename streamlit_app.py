import streamlit as st
import pandas as pd
st.title('🎈 App Name')
st.info('This is the app that builds a machine learning model')
with st.expander('Data'):
  st.write('Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

  st.write('xxXxx');
  X = df.drop('species',axis=1)
  X

  st.write('xxYxx');
  Y = df.species
  Y
