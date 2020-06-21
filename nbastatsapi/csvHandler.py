import pandas as pd


def process(file):
    data = pd.read_csv(file)
    statAbb = data.columns.values.tolist()  # stat abbriviation
    stats = data.to_numpy()  # actual stats
    '''fgPercentage = int(stats[0][statAbb.index(
        'FG')]) / int(stats[0][statAbb.index('FGA')])
    return round(fgPercentage, 2)'''
