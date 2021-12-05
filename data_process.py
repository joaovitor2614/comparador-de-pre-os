import pandas as pd
from itertools import chain
from check_names import check_names

def data_process(df_firm, df_collector):
    ## remover espaços vazios no nomes das colunas
    df_firm.columns, df_collector.columns  = df_firm.columns.str.strip(), df_collector.columns.str.strip()
    ## pegar colunas específicas
    columns_to_select = ['NOME PACIENTE', 'QTDE TOTAL ATENDIMENTOS', 'VALOR SESSÃO', 'TOTAL']
    collectorData, firmData = df_collector[columns_to_select], df_firm[columns_to_select]

    ## pegar todos os nomes e passar os dfs para formato de list
    def dfs_to_list(df_empresa, df_cobrador):
        ## pegar lista de nomes e transformar dfs das planilhas em listas
        column = 'NOME PACIENTE'
        names_list, cobrador_names_list = df_empresa[column].values.tolist(), df_cobrador[column].values.tolist()
        list_empresa, list_cobrador = df_empresa.values.tolist(), df_cobrador.values.tolist()
         
        return names_list, cobrador_names_list, list_empresa, list_cobrador

    names_list, cobrador_names_list, list_empresa, list_cobrador = dfs_to_list(firmData, collectorData)
    ### função para filtrar dados únicos em cada planilha e delete-los da lista de nomes
    new_names_list, cobrador_exclusivos, empresa_exclusivos = check_names(names_list, list_cobrador, list_empresa, cobrador_names_list)
    ## pegar items na duas planilhas e juntar os valores
    def get_items_list(nomes, empresa, cobrador):
        new_list = list()
        for x in range(len(nomes)):
                list_empresa_item_index, list_cobrador_item_index = empresa.index(empresa[x]), cobrador.index(cobrador[x])
                empresa_item, cobrador_item = empresa[list_empresa_item_index], cobrador[list_cobrador_item_index]
                ## juntar os dois valores em uma lista
                empresa_cobrador_item = empresa_item + cobrador_item
                new_list.append(empresa_cobrador_item)
        return new_list

    new_list = get_items_list(new_names_list, list_empresa, list_cobrador)
    ### subtrair valores da lista do cobrador por valores da lista da empresa
    def check_values(items_list):
        checked_list = list()
        for i in range(len(items_list)):
            current_value = items_list[i]
            total_amount_check = int(current_value[7]) - int(current_value[3])
            total_calls_check = int(current_value[5]) - int(current_value[1])
            total_calls_sessions_check = int(current_value[6]) - int(current_value[2])
   
         


            checked_item = [current_value[0], total_amount_check, total_calls_check, total_calls_sessions_check]
            checked_list.append(checked_item)
        return checked_list

    checked_list = check_values(new_list)
    def checked_list_to_df(checked):
        new_df = pd.DataFrame(checked, columns=['NOME DO PACIENTE', 'DIF-PREÇO TOTAL', 'DIF-ATENDIMENTOS', 'DIF-VALOR ATEND'])
        return new_df
    ## retornar nomes exclusivos de cada df
    
    new_df = checked_list_to_df(checked_list)
    column_exclusive = ['NOME DO PACIENTE', 'ATENDIMENTOS', 'VALOR-ATEND', 'VALOR TOTAL']
    cobrador_exclusivos = pd.DataFrame(cobrador_exclusivos, columns=column_exclusive)
    empresa_exclusivos = pd.DataFrame(empresa_exclusivos, columns=column_exclusive)
    return new_df, cobrador_exclusivos, empresa_exclusivos
