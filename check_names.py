import pandas as pd

## check if name in the both list
def check_names(names_list, cobrador_list, empresa_list, cobrador_names):

    empresa_exclusivos = list()
    cobrador_exclusivos = list()
    ## pegar lista de nomes da empresa antes de qualquer item ser deletado
    names_list_original = names_list
    ### iterar lista da empresa e vê se algum valor não está na lista do cobrador 
    ### e deletar da lista dos nomes esse valor
    for i in range(len(empresa_list)):
       
        if empresa_list[i][0] not in cobrador_names:
            empresa_exclusivos.append(empresa_list[i])
            names_list.remove(empresa_list[i][0])
    ### iterar lista do cobrador e vê se algum valor não está na lista da empresa
    ### e deletar da lista do cobrador esse valor
    for i in range(len(cobrador_list)):
        
        if cobrador_list[i][0] not in names_list_original:
            cobrador_exclusivos.append(cobrador_list[i]) 
     

    return names_list, cobrador_exclusivos, empresa_exclusivos

