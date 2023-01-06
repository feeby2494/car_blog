import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]

df = pd.read_csv("./vocab_test_data/magic04.data", names=cols)
print(df.head())

df["class"] = (df["class"] == "g").astype(int)

print(df["class"].unique())

print(df.head())