import pandas as pd
import os

def tableClean (infile: str, aircraft: str):
    
    """
    A function for tidying up aircraft tables.
    It will get the relevant columns from the CSV-file, remove irrelevant data, and export it in a new CSV-file.
    
    Input:
        infile: name of the raw-data CSV-file in the data-folder
        aircraft: the type of aircraft in the table (will be used for naming)
    
    Output:
        CSV-file containing the cleaned dataset
        A file containing a list of original operators of the produced aircraft
    """
    
    # loading dataset
    rawFile = os.path.join("data", infile)
    data = pd.read_csv(rawFile, usecols= ["c/n", "f/f", "operator", "type", "St"])
    
    # tidying table
    
    ## removing aircraft operator-changes by filtering out NaN in first-flight date
    ffCleaned = data.dropna(subset=["f/f"])
    
    ## filtering out planes made for Airbus
    airbusCleaned = ffCleaned[ffCleaned["operator"].str.contains("Airbus") == False]
    
    ## filtering out freighters
    cleanTable = airbusCleaned[airbusCleaned["type"].str.contains("F") == False]
    
    # making a dataframe for operators
    operatorsList = cleanTable["operator"].unique().tolist()
    operatorsDF = pd.DataFrame(operatorsList, columns = ["operators"])
    
    # making outfiles
    outfileTable = os.path.join("data", "cleanData", f"{aircraft}.csv")
    outfileList = os.path.join("data", "cleanData", f"operator{aircraft}.csv")
    
    cleanTable.to_csv(outfileTable, index = False)
    operatorsDF.to_csv(outfileList, index = False)
    
    # user output
    print(f"Data is processed. Operators are: {operatorsList}")
    
    return None