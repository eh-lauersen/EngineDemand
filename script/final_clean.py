import pandas as pd
import os


def final_clean(file: str, aircraft: str):
    
    """
    Final clean of tables.
    Keeps only year in "f/f" column and only overall type of aircraft in "type".
    Also changes name of "f/f" to "f/f_year".
    
    Input:
        filename: name of CSV file
        aircraft: type of aircraft
    
    Output:
        a new file with only the completely cleaned data
    """
    
    # input file
    infile = os.path.join("..", "data", file)
    df = pd.read_csv(infile)
    
    # cleaning type
    df["type"] = df["type"].str[:3]
    
    # cleaning f/f
    df["f/f"] = df["f/f"].str[6:]
    
    # renaming f/f
    df.rename(columns={'f/f': 'f/f_year'}, inplace=True)
    
    # exporting dataframe
    outfile = os.path.join("..", "output", "processed_data", f"{aircraft}.csv")
    df.to_csv(outfile, index=False)
    
    # user output
    print("File processed")
    
    return None


final_clean("A380.csv", "A380")
