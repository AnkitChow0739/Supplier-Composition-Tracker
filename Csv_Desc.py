#Supplier-composition-tracker 
import pandas as pd
import math as mt
import matplotlib as mp
import numpy as np
df = pd.read_csv(r"C:\Users\User\Desktop\Supplier-composition-tracker\data\synthetic-batches.csv")
List_of_colums = df.columns
Order = df.shape
Data_type = df.dtypes
count_missing_val = df.isna().sum()
print(f"List_of_colums:{List_of_colums}\n Data_types:\n{Data_type,Order}\n Missing values in each column:\n{count_missing_val}")
sum_column = df[['Fe_wt_pct',
       'Cr_wt_pct', 'Ni_wt_pct', 'Mn_wt_pct', 'C_wt_pct', 'Si_wt_pct',
       'P_wt_pct', 'S_wt_pct', 'Mo_wt_pct', 'N_wt_pct', 'Cu_wt_pct',
       'Ti_wt_pct']]
sum_tot_percentages = sum_column.sum(axis=1)
df["total_pct"] = 100 - sum_tot_percentages
print(f"Total = \n{df["total_pct"]}")