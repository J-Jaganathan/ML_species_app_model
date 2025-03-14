import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title('Penguin Species Classifier')
st.info('This is the web-app that Predicts Output of classification of Species of penguin using a ML model')
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
#Input Features
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
  gender = st.selectbox('Gender',('male','female'))
  bill_length_mm = st.slider('Bill length (mm)',32.1,52.6,41.9)
  bill_depth_mm = st.slider('Bill Depth (mm)',13.1,21.5,17.2)
  flipper_length_mm = st.slider('Flipper length (mm)',172.0,231.0,201.0)
  body_mass_g = st.slider("Body mass (g)",2700.00, 6300.0, 4267.0)

  data = {'island': island,
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm':bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'sex': gender}
  input_df = pd.DataFrame(data, index =[0])
  input_penguins = pd.concat([input_df,X], axis=0)
with st.expander('Input Features'):
  st.write("**Input Penguins**")
  input_df
  st.write("**Combined penguins data**")
  input_penguins
#Data Preparation
#X encoded
encode = ['island','sex']
df_penguins = pd.get_dummies(input_penguins,prefix=encode)
xx = df_penguins[1:]
input_row = df_penguins[:1]
#Y encoded
target_mapper = {'Adelie' : 0,
                 'Chinstrap': 1,
                 'Gentoo': 2}
def target_encode(val):
  return target_mapper[val]

y = Y.apply(target_encode)

with st.expander("Data Preparation"):
  st.write("**Encoded X(input penguin)**")
  input_row
  st.write("**Encoded y**")
  y

#Model training and inference
## Train the ML model
clf = RandomForestClassifier()
clf.fit(xx,y)

##Apply model to make predictions
prediction = clf.predict(input_row)
prediction_proba = clf.predict_proba(input_row)
df_prediction_proba = pd.DataFrame(prediction_proba)
df_prediction_proba.columns = ['Adelie','Chinstrap','Gentoo']
df_prediction_proba.rename(columns={0: 'Adelie', 1:'Chinstrap', 2: 'Gentoo'})

##Result Displayer
st.subheader('Predicted Species')
st.dataframe(df_prediction_proba,
             column_config={'Adelie':st.column_config.ProgressColumn('Adelie',format="%f",width='medium',min_value=0,max_value=1),
                                                 'Chinstrap':st.column_config.ProgressColumn('Chinstrap',format="%f",width='medium',min_value=0,max_value=1),
                                                 'Gentoo':st.column_config.ProgressColumn('Gentoo',format="%f",width='medium',min_value=0,max_value=1),},
             hide_index=True)
penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])
st.success(str(penguins_species[prediction[0]]))
