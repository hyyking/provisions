import numpy as np
import pandas as pd

BDG = pd.DataFrame({
    pd.Timestamp("2002"): [41034, 46461, 46488, 46487, 46486, 46486, 46488, 46484, 46484, 46484, 46483, 46483, 46483, 46483, 46483],
    pd.Timestamp("2003"): [42873, 48824, 48828, 48824, 48824, 48820, 48820, 48819, 48819, 48818, 48817, 48817, 48817, 48817, np.nan],
    pd.Timestamp("2004"): [39678, 45224, 45241, 45242, 45240, 45239, 45238, 45239, 45239, 45238, 45238, 45238, 45237, np.nan, np.nan],
    pd.Timestamp("2005"): [39182, 44744, 44764, 44763, 44764, 44763, 44762, 44762, 44762, 44762, 44761, 44761, np.nan, np.nan, np.nan],
    pd.Timestamp("2006"): [41389, 47020, 47055, 47094, 47093, 47093, 47092, 47091, 47090, 47090, 47090, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2007"): [40785, 46680, 46867, 46869, 46871, 46870, 46868, 46868, 46868, 46868, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2008"): [42943, 49465, 49638, 49639, 49635, 49633, 49632, 49631, 49631, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2009"): [48021, 54681, 54741, 54728, 54726, 54725, 54725, 54725, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2010"): [51940, 59405, 59450, 59452, 59451, 59452, 59451, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2011"): [50147, 56704, 56732, 56734, 56733, 56732, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2012"): [48820, 55081, 55115, 55115, 55112, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2013"): [53186, 60070, 60091, 60086, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2014"): [51141, 58314, 58332, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2015"): [53877, 60965, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2016"): [54984, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
}).T


RBDG = pd.DataFrame({
    pd.Timestamp("2002"): [39693, 46427, 46473, 46478, 46478, 46479, 46477, 46477, 46477, 46477, 46477, 46477, 46477, 46477, 46477],
    pd.Timestamp("2003"): [42103, 48785, 48809, 48810, 48810, 48808, 48808, 48807, 48806, 48806, 48806, 48806, 48806, 48805, np.nan],
    pd.Timestamp("2004"): [38820, 45192, 45222, 45226, 45225, 45225, 45225, 45225, 45225, 45225, 45225, 45225, 45225, np.nan, np.nan],
    pd.Timestamp("2005"): [38358, 44713, 44744, 44745, 44747, 44747, 44747, 44747, 44747, 44747, 44747, 44747, np.nan, np.nan, np.nan],
    pd.Timestamp("2006"): [40445, 46991, 47035, 47074, 47075, 47075, 47075, 47075, 47075, 47075, 47075, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2007"): [39831, 46655, 46848, 46851, 46854, 46853, 46853, 46853, 46853, 46853, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2008"): [42288, 49422, 49615, 49617, 49614, 49614, 49614, 49613, 49613, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2009"): [47231, 54648, 54719, 54712, 54712, 54712, 54712, 54712, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2010"): [51324, 59373, 59433, 59439, 59439, 59440, 59440, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2011"): [49463, 56676, 56714, 56716, 56716, 56716, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2012"): [48095, 55057, 55085, 55086, 55084, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2013"): [52664, 60041, 60068, 60064, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2014"): [50682, 58276, 58308, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2015"): [53329, 60926, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    pd.Timestamp("2016"): [54188, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
}).T


PRIMES = pd.DataFrame({
    "annee": [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016],
    "prime": [50000, 60000, 55000, 50000, 50000, 45000, 47000, 48000, 50000, 54000, 55000, 56000,  53000,  55000, 56000],
}).set_index("annee", drop=True)


ANNEE2017 = pd.DataFrame({
    "Garantie": ["Incendie","Incendie","Incendie","Incendie","Incendie","Incendie","Incendie"],
    "Exercice": [pd.Timestamp("2010"), pd.Timestamp("2011"), pd.Timestamp("2012"), pd.Timestamp("2013"), pd.Timestamp("2014"), pd.Timestamp("2015"), pd.Timestamp("2016")],
    "CNRU": [78738, 69630, 62561, 62607, 56345, 56047, 57809]
})

SINISTRES2018 = pd.DataFrame({
    "Année de declaration": [2018] * 28,
    "Année de survenance": [2017, 2016, 2016, 2015, 2014, 2014, 2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2015, 2015, 2015, 2014, 2013, 2016, 2016, 2016, 2017, 2017, 2017, 2017],
    "Reglements": [50000, 35000, 40000, 22000, 20000, 18000, 15000, 14000, 10000, 9000, 7000, 4000, 2000, 1000, 4000, 2000, 6000, 4500, 3000, 1000, 40000, 3000, 2000, 3000, 4500, 2500, 1500, 3000],
})
