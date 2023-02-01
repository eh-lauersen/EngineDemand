import pandas as pd
import os


def aircraft_year_only(infile: str, aircraft: str):
    
    """
    Will make a CSV-file containing only one column with only the year that an aircraft had its first flight.

    Input:
        file: the CSV-file for an aircraft
        aircraft: the type of aircraft
    
    Output:
        file with only one column containing only the year that an aircraft was produced
    """
    
    # creating paths
    path = os.path.join("..", "data")
    data = os.path.join(path, infile)
    
    # loading dataset
    df = pd.read_csv(data)
    
    # extracting year
    year_only = df["f/f"].str[6:]
    
    # outfile
    outfile = os.path.join(path, "aircraftYearOnly", f"{aircraft}year.csv")
    year_only.to_csv(outfile, index=False)
    
    # user output
    print(f"File processed")
    
    return None


aircraft_year_only()
