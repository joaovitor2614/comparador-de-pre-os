import streamlit as st
import pandas as pd
import base64
from clean_data import clean_data
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
  df_xlsx, df_cobrador_exclusivos, df_empresa_exclusivos = to_excel(df), to_excel(cobrador_exclusivos), to_excel(empresa_exclusivos) 
  col1, col2, col3 = st.columns([1,1,1])
  with col1:
    
      st.download_button(label='Resultado', data=df_xlsx , file_name= 'resultado.xlsx')
  with col2:
     st.download_button(label='Items restantes - empresa', data=df_empresa_exclusivos, file_name= 'empresa-restantes.xlsx')
  with col3:
     st.download_button(label='Items restantes - cobrador', data=df_cobrador_exclusivos, file_name= 'cobrador-restantes.xlsx')


  



 
 





if uploaded_file and uploaded_file2:
  if st.button("Processar"):
    ## ler arquivos de excel com pandas
    firm, collector = pd.read_excel(uploaded_file), pd.read_excel(uploaded_file2)
    firm = clean_data(firm)
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
 
    


 
    
    
    




