# Adjustments for 7/18/2023




import pandas as pd
df_2023_1 = pd.read_csv('/Users/niks/Desktop/USDA/Spring 2024/Data/2023 NxIrr_hyperspectral_txt/7-18-2023.csv', header=None) 


#For df_2023_1 Make element of first row first column "Wavelength". Make element of first column second row "Original Plotname"
df_2023_1.iloc[0,0] = "Wavelength"
df_2023_1.iloc[1,0] = "Original plotname"

#Drop first element of the dataframe


df_2023_1.iloc[0], df_2023_1.iloc[1] = df_2023_1.iloc[1].copy(), df_2023_1.iloc[0].copy()

#Make first row the header
df_2023_1.columns = df_2023_1.iloc[0]
df_2023_1 = df_2023_1[1:]

#Rename columns. Change second digit. If it is 2, change to 3, if it is 3 change to 5
import re

# Define a function to adjust the second digit of the column name
def adjust_second_digit(column_name):
    return re.sub(r'(?<=\w)(2|3)', lambda x: '3' if x.group(0) == '2' else '5', column_name)

# Apply the function to rename columns
df_2023_1.rename(columns=adjust_second_digit, inplace=True)

# Display the DataFrame
print(df_2023_1)


# Display the DataFrame
print(df_2023_1)

#Save the new dataframe 2023 (fixed).csv
df_2023_1.head().to_csv('/Users/niks/Desktop/USDA/Spring 2024/Data/2023 NxIrr_hyperspectral_txt/7-18-2023(fixed).csv', index=False)

