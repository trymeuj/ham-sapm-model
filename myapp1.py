import streamlit as st
import joblib

model_nb = joblib.load('spam-ham')

st.title("spam or ham let's check")
ip = st.text_input("enter ur text")

op = model_nb.predict([ip])
if st.button('DO_PREDICT'):
  st.title(op[0])
  
  
  
  
         
