#%% imports
import pandas as pd
import matplotlib.pyplot as plt

#%% read original data from .txt
def read_txt_file(datapath):
    dataframe = pd.read_csv(datapath, sep="	")
    dataframe = pd.DataFrame(dataframe)
    return dataframe

def read_csv_file(datapath):
    dataframe = pd.DataFrame(pd.read_csv(datapath, sep=';'))
    return dataframe

def read_xlsx_file(datapath):
    dataframe = pd.read_excel(datapath)
    dataframe = pd.DataFrame(dataframe)
    return dataframe


#%% Cleaning
def clean_data():
    original_data['Journal'] = original_data['Journal'].apply(str.upper)
    external_data['Title'] = external_data['Title'].astype(str)
    external_data['Title'] = external_data['Title'].apply(str.upper)


#%% Merge Dataframe

def merge_dfs(df1,df2):
    return pd.merge(df1,df2, left_on='Journal', right_on='Title', how='left')

#%% write original data
def write_data(data, name):
    data.to_excel(f"Data/{name}.xlsx")

#%% plotting functions

def plot_yearly_output(data):
    data.groupby('Jahr').size().plot(kind = 'bar')


#%%
if __name__ == "__main__":
    # Hier liegen die Daten
    original_data_path = "Data/Literature-data_TU-Darmstadt.txt"
    external_data_path = "Data/scimagojr-journal-2021.csv"

    #Import data
    original_data = read_txt_file(original_data_path)
    external_data= read_csv_file(external_data_path)

    
# %%
