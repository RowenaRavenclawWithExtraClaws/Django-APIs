import pandas as pd
from .Analytics import Calculations


def process(file):
    data = pd.read_csv(file)
    stat_abb = data.columns.values.tolist()  # stat abbriviation
    stats = data.to_numpy()  # actual stats
    calc = Calculations(stat_abb, stats)
    analytics = calc.calcAll()
    return {'analytics': analytics}
