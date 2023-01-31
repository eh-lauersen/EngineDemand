# this should probably have been a loop, but I ran out of brainpower

import pandas as pd
import os


# path
path = os.path.join("..", "output", "processed_data")

# infiles
in330 = os.path.join(path, "A330.csv")
in340 = os.path.join(path, "A340.csv")
in350 = os.path.join(path, "A350.csv")
in380 = os.path.join(path, "A380.csv")

# dataframes
a330 = pd.read_csv(in330)
a340 = pd.read_csv(in340)
a350 = pd.read_csv(in350)
a380 = pd.read_csv(in380)

# combining dataframes
result = a330.append([a340, a350, a380])

# exporting file
outfile = os.path.join("..", "output", "processed_data", "allAircraft.csv")
result.to_csv(outfile)
