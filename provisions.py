import donnee
import pandas as pd


def chain_ladder_lambdas(table) -> list:
    lambdas = []
    cols = len(table.columns)
    for i in range(cols-1):
        currp = table.iloc[i].dropna()
        nextp = table.iloc[i+1].dropna()
        lambdas.append(currp[:len(nextp)].sum() / nextp.sum())   
    return lambdas

def chain_ladder_fill(table, lambdas) -> pd.DataFrame:
    cols = len(table.columns)
    for i in range(1, cols):
        prevp = table.iloc[i-1]
        currp = table.iloc[i]
        currp[currp.isna()] = prevp[currp.isna()] * lambdas[i-1]
    return table

def chain_ladder_reserve(table) -> list:
    reserves = []
    cols = len(table.columns)
    for i in reversed(range(cols)):
        currl = table.iloc[cols - i - 1]
        reserves.append(currl[cols-1] - currl[i])
        # left = currl[i]
        # right = currl[cols-1]
        # print(f"{right} - {left} = {right - left}")
    return reserves

lambdas = chain_ladder_lambdas(donnee.BDG)
filled = chain_ladder_fill(donnee.BDG.copy(deep=True), lambdas)
print(filled)
res = chain_ladder_reserve(filled)
print(sum(res))
