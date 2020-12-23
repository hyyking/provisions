from provisions import chain_ladder_lambdas, chain_ladder_fill, provisions

from pandas import Timestamp, DataFrame
import numpy as np

TD = DataFrame({
    Timestamp("2007"): [5946, 9668, 10563, 10771, 10978, 11040],
    Timestamp("2008"): [6346, 9593, 10316, 10468, 10536, np.nan],
    Timestamp("2009"): [6269, 9245, 10092, 10355, np.nan, np.nan],
    Timestamp("2010"): [5863, 8546, 9268, np.nan, np.nan, np.nan],
    Timestamp("2011"): [5778, 8524, np.nan, np.nan, np.nan, np.nan],
    Timestamp("2012"): [6184, np.nan, np.nan, np.nan, np.nan, np.nan,],
}).T


if __name__ == "__main__":
    lambdas = chain_ladder_lambdas(TD)
    print(lambdas)
    filled = chain_ladder_fill(TD.copy(deep=True), lambdas)
    print(filled)
    res = provisions(filled)
    print(res)
    print(sum(res))
