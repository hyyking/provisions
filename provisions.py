import donnee
import pandas as pd


def chain_ladder_lambdas(table) -> list:
    lambdas = []
    cols = len(table.columns)
    for i in range(cols-1):
        currp = table[i].dropna()
        nextp = table[i+1].dropna()
        lambdas.append(nextp.sum() / currp[:len(nextp)].sum())   
    return lambdas

def chain_ladder_fill(table, lambdas) -> pd.DataFrame:
    cols = len(table.columns)
    for i in range(1, cols):
        prevp = table[i-1]
        currp = table[i]
        currp[currp.isna()] = prevp[currp.isna()] * lambdas[i-1]
    return table

def reserve(table) -> list:
    reserves = []
    cols = len(table.columns)
    for i in reversed(range(cols)):
        currl = table.iloc[cols - i - 1]
        reserves.append(currl[cols-1] - currl[i])
    return reserves



def london_chain_coefs(table) -> list:
    coefs = []
    cols = len(table.columns)
    # compute N-2 terms
    for i in range(cols - 2):
        currp = table[i][table[i+1].notna()] # mask the overlapping lines
        nextp = table[i+1].dropna() # match the previous length
        l = currp.cov(nextp) / currp.var()
        a = nextp.mean() - l * currp.mean()
        coefs.append((l, a))

    # compute N - 1
    # we set alpha = 0
    # so lambda = avg(S_n) / avg(S_n-1) = S_n / S_n-1 (single term in both)
    coefs.append((table[cols-1][0] / table[cols-2][0], 0))
    return coefs

def london_chain_fill(table, lambdas) -> pd.DataFrame:
    cols = len(table.columns)
    for i in range(1, cols):
        prevp = table[i-1]
        currp = table[i]
        l, alpha = lambdas[i-1]
        currp[currp.isna()] = alpha + l * prevp[currp.isna()]
    return table

def bf_gammas(table) -> list:
    return (table.iloc[0] / table.iloc[0, -1]).values

def bf_fill(table, sp, primes, gammas):
    size = len(table.index)
    for i in range(1, size):
        currl = table.iloc[i] 
        lidx = size - i - 1
        lg = gammas[lidx] # gamma of last value
        lv = currl[lidx] # last value

        for j in range(size - i, size):
            currl[j] = lv + (gammas[j] - lg) * sp * primes.iloc[i]
    return table

if __name__ == "__main__":
    def chain_ladder():
        lambdas = chain_ladder_lambdas(donnee.BDG)
        print(lambdas)
        filled = chain_ladder_fill(donnee.BDG.copy(deep=True), lambdas)
        print(filled)
        res = reserve(filled)
        print(sum(res))
    # chain_ladder()

    def london_chain():
        lambdas = london_chain_coefs(donnee.BDG)
        print(lambdas)
        filled = london_chain_fill(donnee.BDG.copy(deep=True), lambdas)
        print(filled)
        res = reserve(filled)
        print(sum(res))
    # london_chain()

    def bf():
        gammas = bf_gammas(donnee.BDG)
        print(gammas)
        filled = bf_fill(donnee.BDG.copy(deep=True), 0.97, donnee.PRIMES, gammas)
        print(filled)
        res = reserve(filled)
        print(sum(res))
    bf()

