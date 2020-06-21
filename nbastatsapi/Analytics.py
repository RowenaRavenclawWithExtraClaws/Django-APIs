
class Calculations():
    def __init__(self, stat_abb, stats):
        self.stat_abb = stat_abb
        self.stats = stats

    def fgPercent(self, fg_made, fg_att):
        fg = fg_made / fg_att
        return round(fg, 2)

    def threesPercent(self, threes_made, threes_att):
        threes = threes_made / threes_att
        return round(threes, 2)

    def ftPercent(self, ft_made, ft_att):
        ft = ft_made / ft_att
        return round(ft, 2)

    def calcAll(self):
        player_name = self.stats[0][self.stat_abb.index('Starters')]
        minutes_played = int(self.stats[0][self.stat_abb.index('MP')][:2])
        fg_made = int(self.stats[0][self.stat_abb.index('FG')])
        fg_att = int(self.stats[0][self.stat_abb.index('FGA')])
        threes_made = int(self.stats[0][self.stat_abb.index('3P')])
        threes_att = int(self.stats[0][self.stat_abb.index('3PA')])
        ft_made = int(self.stats[0][self.stat_abb.index('FT')])
        ft_att = int(self.stats[0][self.stat_abb.index('FTA')])
        orb = int(self.stats[0][self.stat_abb.index('ORB')])
        drb = int(self.stats[0][self.stat_abb.index('DRB')])
        ast = int(self.stats[0][self.stat_abb.index('AST')])
        stl = int(self.stats[0][self.stat_abb.index('STL')])
        blk = int(self.stats[0][self.stat_abb.index('BLK')])
        tov = int(self.stats[0][self.stat_abb.index('TOV')])
        pf = int(self.stats[0][self.stat_abb.index('PF')])
        pts = int(self.stats[0][self.stat_abb.index('PTS')])
        pm = int(self.stats[0][self.stat_abb.index('+/-')])

        analytics = {}

        analytics['Player name'] = player_name
        analytics['FG%'] = self.fgPercent(fg_made, fg_att)
        analytics['3P%'] = self.threesPercent(threes_made, threes_att)
        analytics['FT%'] = self.ftPercent(ft_made, ft_att)

        return analytics
