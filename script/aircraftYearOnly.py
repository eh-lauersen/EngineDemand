import pandas as pd
import os

def aircraftYearOnly (infile: str, aircraft: str):
    
    """
    Will make a CSV-file containing only one column with only the year that an aircraft had its first flight.
    
    Input:
        file: the CSV-file for an aircraft
        aircraft: the type of aircraft
    
    Output:
        file with only one column containing only the year that an aircraft was produced
    """
    
    # creating paths
    path = os.path.join("data", "cleanData")
    data = os.path.join(path, infile)
    
    # loading dataset
    df = pd.read_csv(data)
    
    # extracting year
    yearonly = df["f/f"].str[6:]
    
    # outfile
    outfile = os.path.join(path, "aircraftYearOnly", f"{aircraft}year.csv")
    yearonly.to_csv(outfile, index = False)
    
    # user output
    print(f"File processed")
    
    return None