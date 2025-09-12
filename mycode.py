import pandas as pd
import os



# Defining Data

data={'Name':['Rituraj','Rahul','Rakesh'],
    'Age':[31,32,33],
    'City':['vasai',"Nsp","virar"]}

df=pd.DataFrame(data)


#adding New Data
new_df={'Name':'Payal','Age':30,'City':"Bsr"}
df.loc[len(df.index)]=new_df

#adding second new_data
# new_df1={'Name':'Sikha','Age':28,'City':"Vasai"}
# df.loc[len(df.index)]=new_df1

# making a Folder Named Data 
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file, including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")

