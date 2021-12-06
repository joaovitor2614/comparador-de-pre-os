
import pandas as pd


def clean_data(firm):
        firm.columns = firm.columns.str.strip()

        name_column = firm['NOME PACIENTE']
        names_list = name_column.values.tolist()
        for i in range(len(names_list)):
            current_name = names_list[i]
            new_value = current_name[9:]
            ## mudar para valores limpos
            firm['NOME PACIENTE'] = firm['NOME PACIENTE'].replace(firm['NOME PACIENTE'][i], new_value)
            
        

        return firm