from runstats import Statistics

class Event_statistic:
    def __init__(self,want_max=True, want_mean=True, want_variance= True, want_min=False):
           self.stat=Statistics()
           self.want_max=want_max
           self.want_mean= want_mean
           self.want_variance= want_variance
           self.want_min=want_min

    def as_dict(self, name):
        res = dicdefault(list) 
        if self.want_min:
            res[name + " min"] = self.stat.minimum() 

        if self.want_max:
            res[name + " max"] = self.stat.maximum() 

        if self.want_variance:
            res[name + " variance"] = self.stat.variance()

        if self.want_mean:
            res[name + " mean"] = self.stat.mean()
        return res

    def add_occurence(self, time):
        self.stat.push(time)


