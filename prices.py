import streamlit as st
import pandas as pd


uploaded_file = st.file_uploader("Upload Planilha 1", type=['csv'])
uploaded_file2 = st.file_uploader("Upload Planilha 2", type=['csv'])

if st.button("Processar"):
    Plan_1 = pd.read_csv(uploaded_file, encoding='cp1252')
    Plan_2 = pd.read_csv(uploaded_file2, encoding='cp1252')
    print(Plan_1)
 
    
    
    




