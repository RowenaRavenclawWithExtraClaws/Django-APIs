
class Calculations():
    def __init__(self, stat_abb, stats):
        self.stat_abb = stat_abb
        self.stats = stats

    def fgPercent(self, fg_made, fg_att):
        if fg_att == 0:
            return 'undefined'
        fg = fg_made / fg_att
        return round(fg, 2)

    def threesPercent(self, threes_made, threes_att):
        if threes_att == 0:
            return 'undefined'
        threes = threes_made / threes_att
        return round(threes, 2)

    def ftPercent(self, ft_made, ft_att):
        if ft_att == 0:
            return 'undefined'
        ft = ft_made / ft_att
        return round(ft, 2)

    def tsPercent(self, pts, fg_att, ft_att):
        ts_att = fg_att + 0.44 * ft_att
        if ts_att == 0:
            return 'undefined'
        ts = pts / (2 * ts_att)
        return round(ts, 2)

    def efgPercent(self, fg_made, threes_made, fg_att):
        if fg_att == 0:
            return 'undefined'
        efg = (fg_made + 0.5 * threes_made) / fg_att
        return round(efg, 2)

    def thressRate(self, threes_att, fg_att):
        if fg_att == 0:
            return 'undefined'
        threes_rate = threes_att / fg_att
        return round(threes_rate)

    def ftRate(self, ft_att, fg_att):
        if fg_att == 0:
            return 'undefined'
        ft_rate = ft_att / fg_att
        return round(ft_rate, 2)

    def tovPercent(self, tov, fg_att, ft_att):
        if fg_att == 0 and ft_att == 0 and tov == 0:
            return 'undefined'
        tov_percentage = (100 * tov) / (fg_att + 0.44 * ft_att + tov)
        return round(tov_percentage, 2)

    def gmScore(self, pts, fg_made, fg_att, ft_att, ft_made, orb, drb, stl, ast, blk, pf, tov):
        gm_score = pts + 0.4 * fg_made - 0.7 * fg_att - 0.4 * \
            (ft_att - ft_made) + 0.7 * orb + 0.3 * drb + \
            stl + 0.7 * ast + 0.7 * blk - 0.4 * pf - tov
        return round(gm_score, 2)

    def calcAll(self):
        individual_stats = None
        analytics = []

        for indx in range(len(self.stats)):
            player_name = self.stats[indx][self.stat_abb.index('Starters')]
            minutes_played = int(
                self.stats[indx][self.stat_abb.index('MP')][:2])
            fg_made = int(self.stats[indx][self.stat_abb.index('FG')])
            fg_att = int(self.stats[indx][self.stat_abb.index('FGA')])
            threes_made = int(self.stats[indx][self.stat_abb.index('3P')])
            threes_att = int(self.stats[indx][self.stat_abb.index('3PA')])
            ft_made = int(self.stats[indx][self.stat_abb.index('FT')])
            ft_att = int(self.stats[indx][self.stat_abb.index('FTA')])
            orb = int(self.stats[indx][self.stat_abb.index('ORB')])
            drb = int(self.stats[indx][self.stat_abb.index('DRB')])
            ast = int(self.stats[indx][self.stat_abb.index('AST')])
            stl = int(self.stats[indx][self.stat_abb.index('STL')])
            blk = int(self.stats[indx][self.stat_abb.index('BLK')])
            tov = int(self.stats[indx][self.stat_abb.index('TOV')])
            pf = int(self.stats[indx][self.stat_abb.index('PF')])
            pts = int(self.stats[indx][self.stat_abb.index('PTS')])
            pm = int(self.stats[indx][self.stat_abb.index('+/-')])

            individual_stats = {}

            individual_stats['Player name'] = player_name
            individual_stats['FG%'] = self.fgPercent(fg_made, fg_att)
            individual_stats['3P%'] = self.threesPercent(
                threes_made, threes_att)
            individual_stats['FT%'] = self.ftPercent(ft_made, ft_att)
            individual_stats['TS%'] = self.tsPercent(pts, fg_att, ft_att)
            individual_stats['eFG%'] = self.efgPercent(
                fg_made, threes_made, fg_att)
            individual_stats['3PAr'] = self.thressRate(threes_att, fg_att)
            individual_stats['FTr'] = self.ftRate(ft_att, fg_att)
            individual_stats['TOV%'] = self.tovPercent(tov, fg_att, ft_att)
            individual_stats['GmSc'] = self.gmScore(
                pts, fg_made, fg_att, ft_att, ft_made, orb, drb, stl, ast, blk, pf, tov)

            analytics.append(individual_stats)

        return analytics
