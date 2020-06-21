
class Calculations():
    def __init__(self, statAbb, stats):
        self.statAbb = statAbb
        self.stats = stats

    def fgPercent(self, fgMade, fgAttempt):
        fg = fgMade / fgAttempt
        return round(fg, 2)

    def threesPercent(self, threesMade, threesAttempt):
        threes = threesMade / threesAttempt
        return round(threes, 2)

    def ftPercent(self, ftMade, ftAttempt):
        ft = ftMade / ftAttempt
        return round(ft, 2)
