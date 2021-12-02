import pandas as pd
from itertools import chain
from check_names import check_names

def data_process(df_firm, df_collector):
    ## remover espaços vazios no nomes das colunas
    df_firm.columns = df_firm.columns.str.strip()
    df_collector.columns = df_collector.columns.str.strip()
    ## pegar colunas específicas
    collectorData = df_collector[['NOME PACIENTE', 'QTDE TOTAL ATENDIMENTOS', 'VALOR SESSÃO', 'TOTAL']]
    firmData= df_firm[['NOME PACIENTE', 'QTDE TOTAL ATENDIMENTOS','VALOR SESSÃO', 'TOTAL']]
    ## pegar todos os nomes e passar os dfs para formato de list
    def dfs_to_list(df_empresa, df_cobrador):
        ## pegar lista de nomes e transformar dfs das planilhas em listas
        names_list = df_empresa['NOME PACIENTE'].values.tolist()
        cobrador_names_list = df_cobrador['NOME PACIENTE'].values.tolist()
        list_empresa = df_empresa.values.tolist()
        list_cobrador = df_cobrador.values.tolist()
        return names_list, cobrador_names_list, list_empresa, list_cobrador

    names_list, cobrador_names_list, list_empresa, list_cobrador = dfs_to_list(firmData, collectorData)
    ## retornar nomes exclusivos de cada df
    new_names_list, cobrador_exclusivos, empresa_exclusivos = check_names(names_list, list_cobrador, list_empresa, cobrador_names_list)
    print(cobrador_exclusivos)
    def get_items_list(nomes, empresa, cobrador):
        new_list = list()
        for x in range(len(nomes)):
                ## chequear se nomes estão nas planilhas
            
                list_empresa_item_index = empresa.index(empresa[x])
                list_cobrador_item_index = cobrador.index(cobrador[x])

                empresa_item = empresa[list_empresa_item_index]
                cobrador_item = cobrador[list_cobrador_item_index]

                empresa_cobrador_item = empresa_item + cobrador_item
                new_list.append(empresa_cobrador_item)
        return new_list

    new_list = get_items_list(names_list, list_empresa, list_cobrador)

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

    new_df = checked_list_to_df(checked_list)
    return new_df