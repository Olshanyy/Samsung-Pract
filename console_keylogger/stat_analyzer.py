import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kstest, chisquare, skew, kurtosis


uni, bio, trio = "self_data/Olshanyy_uni.csv", "self_data/Olshanyy_bio.csv", "self_data/Olshanyy_trio.csv"

uni = pd.read_csv(uni)
uni.drop(uni.columns[0:1], axis=1, inplace=True)

bio = pd.read_csv(bio)
bio.drop(bio.columns[0:1], axis=1, inplace=True)

trio = pd.read_csv(trio)
trio.drop(trio.columns[0:1], axis=1, inplace=True)


print("=========UNI=========")
print(uni)
print()

print("=========BIO=========")
print(bio)
print()

print("=========TRIO=========")
print(trio)
print()

for symbol in uni.columns:
    print(f"{symbol}:")
    print(f"Mean: {uni[symbol].mean()}")
    print(f"STD: {uni[symbol].std()}")
    print(f"Variance: {uni[symbol].var()}")
    print(f"Skewness: {skew(uni[symbol])}")
    print(f"Kurtosis: {kurtosis(uni[symbol])}")
    print()

for symbol in bio.columns:
    print(f"{symbol}:")
    print(f"Mean: {bio[symbol].mean()}")
    print(f"STD: {bio[symbol].std()}")
    print(f"Variance: {bio[symbol].var()}")
    print(f"Skewness: {skew(bio[symbol])}")
    print(f"Kurtosis: {kurtosis(bio[symbol])}")
    print()

for symbol in trio.columns:
    print(f"{symbol}:")
    print(f"Mean: {trio[symbol].mean()}")
    print(f"STD: {trio[symbol].std()}")
    print(f"Variance: {trio[symbol].var()}")
    print(f"Skewness: {skew(trio[symbol])}")
    print(f"Kurtosis: {kurtosis(trio[symbol])}")
    print()

for symbol in uni.columns:
    print(f"{symbol}: ")
    print(kstest(uni[symbol], "norm"))
    print(chisquare(uni[symbol]))
    print()

for symbols in bio.columns:
    print(f"{symbols}: ")
    print(kstest(bio[symbols], "norm"))
    print(chisquare(bio[symbols]))
    print()

for symbols in trio.columns:
    print(f"{symbols}: ")
    print(kstest(trio[symbols], "norm"))
    print(chisquare(trio[symbols]))
    print()
