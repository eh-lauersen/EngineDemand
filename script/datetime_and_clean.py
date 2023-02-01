import pandas as pd
import os


def datetime_clean(file: str, aircraft: str):
    
    """
    Converts the "f/f" column into a datetime column with pandas datetime-function.
    Also cleans the "type" column to only the overall type of aircraft (removing -***)
    
    Input:
        infile: CSV-file to be processed
        aircraft: type of aircraft (will be used for title of outfile)
    Output: 
        CSV-file
    """
    
    # loading dataframe
    infile = os.path.join("..", "data", file)
    df = pd.read_csv(infile)
    
    # datetime
    df["f/f"] = pd.to_datetime(df["f/f"])
    
    # cleaning "type"
    df["type"] = df["type"].str[:3]
    
    # outfile
    outfile = os.path.join("..", "output", "processed_data", f"{aircraft}_datetime.csv")
    df.to_csv(outfile, index=False)
    
    # user output
    print(f"File is processed.")
    
    return None

datetime_clean("A380.csv", "A380")
