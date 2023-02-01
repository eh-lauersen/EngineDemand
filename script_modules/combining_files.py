# this should probably have been a loop, but I ran out of brainpower

import pandas as pd
import os


# path
path = os.path.join("..", "output", "processed_data")

# infiles
in330 = os.path.join(path, "A330_datetime.csv")
in340 = os.path.join(path, "A340_datetime.csv")
in350 = os.path.join(path, "A350_datetime.csv")
in380 = os.path.join(path, "A380_datetime.csv")

# dataframes
a330_datetime = pd.read_csv(in330)
a340_datetime = pd.read_csv(in340)
a350_datetime = pd.read_csv(in350)
a380_datetime = pd.read_csv(in380)

# combining dataframes
result = a330_datetime.append([a340_datetime, a350_datetime, a380_datetime])

# exporting file
outfile = os.path.join("..", "output", "processed_data", "allAircraft_datetime.csv")
result.to_csv(outfile, index=False)
