import streamlit as st
import pandas as pd
import base64
from data_process import data_process
from to_excel import to_excel


st.title('Comparador de valores')

st.markdown("""
Essa aplicação realiza uma simples checagem de valores através da diferença entre eles!

* **Tutorial de como usar:** (https://github.com/joaovitor2614/comparador-de-pre-os).
""")


# file uplodaers
uploaded_file = st.file_uploader("Empresa", type=['xlsx'])
uploaded_file2 = st.file_uploader("Cobrador", type=['xlsx'])


def filedownload(df):
  df_xlsx = to_excel(df)



  st.download_button(label='Resultado',
                                data=df_xlsx ,
                                file_name= 'resultado.xlsx')





if uploaded_file and uploaded_file2:
  if st.button("Processar"):
    firm = pd.read_excel(uploaded_file)
    collector = pd.read_excel(uploaded_file2)
    new_df = data_process(firm, collector)
 
    st.dataframe(new_df)
    st.markdown("""
    Downloads
    """)
    filedownload(new_df)
 
    


 
    
    
    




