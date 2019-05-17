###############################################################################
# "Housing data" example
###############################################################################
#  Objectives:
#
#  Source:
#   https://github.com/ageron/handson-ml/blob/master/02_end_to_end_machine_learning_project.ipynb
###############################################################################

# -----------------------------------------------------------------------------
# Instructions and other information
# -----------------------------------------------------------------------------
# Download the data from:
#   https://github.com/ageron/handson-ml/tree/master/datasets/housing
# Pandas API:
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/
# CMaps:
#   https://matplotlib.org/tutorials/colors/colormaps.html
# -----------------------------------------------------------------------------

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Import required libraries
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
import scipy
import sklearn
import pandas as pd
#%matplotlib inline

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Setup data path
DATA_PATH = "../data/extracted/housing/"
DATA_FILE = "housing.csv"
FULL_PATH = DATA_PATH + DATA_FILE

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Read the CSV file into a data frame
data = pd.read_csv(FULL_PATH)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Get information about our dataframe
data.head(10)
data.info()
headers = list(data)
print(headers)

data["ocean_proximity"]
data["ocean_proximity"].value_counts()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Get some basic statistics and plots
data.describe()
data.hist(bins=50, figsize=(20, 15))
#plt.show()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Create a test set
def splitTrain(data, ratio):
    ixShuffle = np.random.permutation(len(data))
    testSetSize = int(len(data) * ratio)
    ixTest = ixShuffle[:testSetSize]
    ixTrain = ixShuffle[testSetSize:]
    return (data.iloc[ixTrain], data.iloc[ixTest])

(train,test) = splitTrain(data, .05)
test

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Plotting
data.plot(kind="scatter", x="longitude", y="latitude")
data.plot(kind="scatter", x="longitude", y="latitude", alpha=.2)
data.plot(
    kind="scatter", x="longitude", y="latitude",
    alpha=.15, s=data["population"]/100, figsize=(10,7), label="population",
    c="median_house_value", cmap=plt.get_cmap("RdPu"), colorbar=True
)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Correlation (Pearson)
data.corr()
