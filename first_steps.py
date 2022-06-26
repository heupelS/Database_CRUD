#%% imports
import pandas as pd
import matplotlib.pyplot as plt

#%% read original data from .txt
def read_txt_file(datapath):
    dataframe = pd.read_csv(datapath, sep="	")
    dataframe = pd.DataFrame(dataframe)
    return dataframe

#%% write original data
def write_data(data):
    data.to_excel("Data/literature_review.xlsx")

#%% plotting functions

def plot_yearly_output(data):
    data.groupby('Jahr').size().plot(kind = 'bar')


#%%
if __name__ == "__main__":
    # Hier liegen die Daten
    original_data = "Data/Literature-data_TU-Darmstadt.txt"

    #Import data
    data = read_txt_file(original_data)
    
# %%
