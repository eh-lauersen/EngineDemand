import pandas as pd
import os


def year_column(file: str, aircraft: str):
    
    """
    Creates a 'year' column with the year from 'f/f'.
    
    Input:
        file: CSV-file
        aircraft: type of aircraft
    
    Output:
        CSV-file
    """
    
    # infile
    infile = os.path.join("..", "output", "processed_data", file)
    df = pd.read_csv(infile)
    
    # datetime-function
    df["f/f"] = pd.to_datetime(df["f/f"])
    
    # year column
    df["year"] = df["f/f"].dt.year
    
    # outfile
    outfile = os.path.join("..", "output", "processed_data", f"{aircraft}_year.csv")
    df.to_csv(outfile, index=False)
    
    # user output
    print(f"File is processed: {aircraft}_year.csv")
    
    return None
