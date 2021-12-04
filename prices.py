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


def filedownload(df, cobrador_exclusivos, empresa_exclusivos):
  df_xlsx = to_excel(df)

  df_cobrador_exclusivos = to_excel(cobrador_exclusivos)
  df_empresa_exclusivos = to_excel(empresa_exclusivos)
  



  st.download_button(label='Resultado',
                                data=df_xlsx ,
                                file_name= 'resultado.xlsx')
  st.download_button(label='items restantes - empresa',
                                data=df_empresa_exclusivos,
                                file_name= 'empresarestantes.xlsx')
  st.download_button(label='Items restantes - cobrador',
                                data=df_cobrador_exclusivos,
                                file_name= 'cobradorrestantes.xlsx')





if uploaded_file and uploaded_file2:
  if st.button("Processar"):
    firm = pd.read_excel(uploaded_file)
    collector = pd.read_excel(uploaded_file2)
    new_df, cobrador_exclusivos, empresa_exclusivos = data_process(firm, collector)
    st.subheader("Resultado análise")
    st.dataframe(new_df)
    st.subheader("Items restantes empresa")
    st.dataframe(empresa_exclusivos)
    st.subheader("Items restantes cobrador")
    st.dataframe(cobrador_exclusivos)
    st.markdown("""
    Downloads
    """)
    filedownload(new_df, cobrador_exclusivos, empresa_exclusivos)
 
    


 
    
    
    




