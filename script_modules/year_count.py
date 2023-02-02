import pandas as pd
import os


def year_count(file: str, aircraft: str):
    
    """
    Counting how many aircraft are built in each year of production. Use ***_year.csv files.
    
    Input: file: CSV-file; aircraft: type of aircraft
    Output: CSV-file
    """
    
    # infile
    infile = os.path.join("..", "output", "processed_data", file)
    df = pd.read_csv(infile)
    
    # grouping years and counting values per year
    grouped = df.groupby('year').size()
    
    # outfile
    outfile = os.path.join("..", "output", "processed_data", f"{aircraft}_year-count.csv")
    grouped.to_csv(outfile)
    
    # user output
    print(f"File processed: {grouped}")
    
    return None
