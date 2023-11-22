# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:32:10 2023

@author: Mehdi Hasan Rafi
PhD Researcher at MIST
"""

import os
import pandas as pd

input_folder = r'D:\Datasets\ENTLN\2021\folder'
output_folder = input_folder

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through all the CSV files in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith('.csv'):
        file_path = os.path.join(input_folder, file_name)

        # Read the CSV file using pandas
        data = pd.read_csv(file_path)

        # Filter the data according to the 'icheight' column values
        CG = data[data['icheight'] == 0]
        CC = data[data['icheight'] > 0]

        # Save the filtered data to separate CSV files
        base_name, ext = os.path.splitext(file_name)
        CG.to_csv(os.path.join(output_folder, f"CG_{base_name}{ext}"), index=False)
        CC.to_csv(os.path.join(output_folder, f"CC_{base_name}{ext}"), index=False)

print("CSV files separated and saved in the output folder.")
