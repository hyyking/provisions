""" Projet actuariat M1 ISF Léo DURET & Nicolas Moine """

import pandas as pd
import numpy as np

import donnee

def chain_ladder_lambdas(table: pd.DataFrame) -> list:
    """ compute chain ladder lambda coefs """
    lambdas = []
    for i in range(len(table.columns) - 1):
        currp = table[i].dropna()
        nextp = table[i + 1].dropna()
        lambdas.append(nextp.sum() / currp[: len(nextp)].sum())
    return lambdas


def chain_ladder_fill(table: pd.DataFrame, lambdas: list) -> pd.DataFrame:
    """ fill triangle using chain ladder method """
    for i in range(1, len(table.columns)):
        table[i][table[i].isna()] = table[i - 1][table[i].isna()] * lambdas[i - 1]
    return table


# -------------------------------------------------------------------------------


def london_chain_coefs(table: pd.DataFrame) -> list:
    """ compute london chain regression coefficients """
    coefs = []
    size = len(table.columns)
    # compute N-2 terms
    for i in range(size - 2):
        currp = table[i][table[i + 1].notna()]  # mask the overlapping lines
        nextp = table[i + 1].dropna()  # match the previous length

        beta = currp.cov(nextp) / currp.var()
        alpha = nextp.mean() - beta * currp.mean()
        coefs.append((alpha, beta))

    # compute N - 1
    # we set alpha = 0
    # so lambda = avg(S_n) / avg(S_n-1) = S_n / S_n-1 (single term in both)
    coefs.append((table[size - 1][0] / table[size - 2][0], 0))
    return coefs


def london_chain_fill(table, lambdas) -> pd.DataFrame:
    """ fill triangle using london chain method """
    for i in range(1, len(table.columns)):
        prevp, currp = table.loc[:, i-1], table.loc[:, i]
        alpha, beta = lambdas[i - 1]
        currp[currp.isna()] = alpha + beta * prevp[currp.isna()]
    return table


# -------------------------------------------------------------------------------


def bf_gammas(table: pd.DataFrame) -> list:
    """ compute acutalisation coefs """
    # compute proportions of the ultimate charge
    return (table.iloc[0] / table.iloc[0, -1]).values


def bf_fill(table: pd.DataFrame, sp_ratio: float, primes: pd.Series, gammas: list) -> pd.DataFrame:
    """ fill triangle using Bornhuetter-Ferguson method """
    size = len(table.index)
    for i in range(1, size):
        currl = table.iloc[i]
        lgam = gammas[size - i - 1]  # gamma of last value
        lval = currl[size - i - 1]  # last value

        for j in range(size - i, size):
            currl[j] = lval + (gammas[j] - lgam) * sp_ratio * primes.iloc[i]
    return table


# -------------------------------------------------------------------------------


def provisions(table: pd.DataFrame) -> list:
    """ get expected provisions for filled table """
    reserves = []
    size = len(table.columns)
    for i in reversed(range(size)):
        currl = table.iloc[size - i - 1]
        reserves.append(currl[size - 1] - currl[i])
    return reserves


if __name__ == "__main__":
    OUTPUT = "actuariat.xls"

    def chain_ladder():
        """ ex3 """
        lambdas = chain_ladder_lambdas(donnee.BDG)
        filled = chain_ladder_fill(donnee.BDG.copy(deep=True), lambdas)
        res = provisions(filled)

        filled["Provisions"] = res
        filled["Coefs"] = lambdas + [np.nan]

        print(filled)
        return filled

    def london_chain():
        """ ex3 """
        lambdas = london_chain_coefs(donnee.BDG)
        filled = london_chain_fill(donnee.BDG.copy(deep=True), lambdas)
        res = provisions(filled)

        filled["Provisions"] = res

        reprf = lambda t: (round(t[0], 4), round(t[1], 4))
        filled["Coefs"] = list(map(reprf, lambdas)) + [np.nan]

        print(filled)
        return filled

    def ratio_sinistre_prime():
        """ ex4 """
        return chain_ladder().iloc[:, -3] / donnee.PRIMES["prime"].values

    def bornhuetter_ferguson():
        """ ex7 """
        gammas = bf_gammas(donnee.BDG)
        filled = bf_fill(donnee.BDG.copy(deep=True), 0.97, donnee.PRIMES, gammas)
        res = provisions(filled)

        filled["Provisions"] = res
        filled["Coefs"] = gammas

        print(filled)
        return filled


    with pd.ExcelWriter(OUTPUT) as writer:
        chain_ladder().to_excel(writer, sheet_name="chain_ladder")
        london_chain().to_excel(writer, sheet_name="london_chain")
        ratio_sinistre_prime().to_excel(writer, sheet_name="ratio SP")

        bornhuetter_ferguson().to_excel(writer, sheet_name="bf")
