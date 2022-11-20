#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import missingno as msno



def get_variables_names (variables_list = []):

    variables_names = np.array(range (0, len(variables_list)), dtype=np.dtype(object))
    
    for i in range (0, len(variables_list)):

        variables_names[i] = [x for x in globals() if globals()[x] is variables_list[i]][0]
        
    return variables_names    


def missed_values_count(df_list, normalize=True, visualize=True):
    
    missedvalues_df = pd.DataFrame()
    df_number = 0
    
    variables_names = get_variables_names(df_list)
    
    for df in df_list:
        
        totalvalues_in_row = df.shape[0]
    
        print('Total values in ', variables_names[df_number], ': ', totalvalues_in_row)
        
        for col in df.columns:
            
            if normalize:                
                missedvalues_df.loc[df_number, col] =  round(100 - (df[col].describe()[0] * 100) / totalvalues_in_row, 2)
                message_text = 'Missed values (%):'
            else:
                missedvalues_df.loc[df_number, col] = totalvalues_in_row - df[col].describe()[0]
                message_text = 'Missed values (counts):'
            
        df_number += 1    
    

    new_index = pd.Index(data=['DataFrame_Name']).append(missedvalues_df.columns)
    missedvalues_df['DataFrame_Name'] = variables_names
    
    missedvalues_df=missedvalues_df[new_index]
    
    print(message_text)
    
    if visualize:
        i = 0
        try:
            for df in df_list:
                msno.matrix(df, color=(0.0, 0.0, 0.99))
                i += 1
        except NameError:
            print('!!!! ------------------------------------------')
            print('Library missingno not installed!!!')
            print('https://github.com/ResidentMario/missingno')
            print('pip install missingno')
            print('import missingno as msno')
                    
    return missedvalues_df
