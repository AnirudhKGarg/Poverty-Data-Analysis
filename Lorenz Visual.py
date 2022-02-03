#Import libraries
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = "Git/Poverty-Data-Analysis/Income Dataset.csv"

dfDist = pd.read_csv(path, index_col=0, skiprows=[0])

dfDist.rename(columns = {"Unnamed: 1": "Households", "Unnamed: 6": "Top 5%"}, inplace=True)


print(dfDist)