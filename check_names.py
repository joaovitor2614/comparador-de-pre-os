import pandas as pd

## check if name in the both list
def check_names(names_list, cobrador_list, empresa_list, cobrador_names):
 
    empresa_exclusivos = list()
    cobrador_exclusivos = list()
    names_list_original = names_list
    for i in range(len(empresa_list)):
       
        if empresa_list[i][0] not in cobrador_names:
            empresa_exclusivos.append(empresa_list[i])
    for i in range(len(cobrador_list)):
        
        if cobrador_list[i][0] not in names_list_original:
            cobrador_exclusivos.append(cobrador_list[i])
        
    for i in range(len(names_list)):
        if names_list[i] not in cobrador_names:

             names_list = names_list.remove(names_list[i])
 
     
  
    return names_list, cobrador_exclusivos, empresa_exclusivos




"""
  df_cobrador = to_excel(cobrador_exclusivos)
  df_empresa = to_excel(empresa_exclusivos)
  st.download_button(label='Items exclusivos cobrador',
                                data=df_cobrador ,
                                file_name= 'cobrador-exclusivos.xlsx')
  st.download_button(label='Items exclusivos empresa',
                                data=df_empresa ,
                                file_name= 'empresa-exclusivos.xlsx')
"""