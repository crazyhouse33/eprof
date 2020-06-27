from runstats import Statistics
from kvhf.history_entry import  Serie_stats

class Event_statistic:
    def __init__(self,want_max=True, want_mean=True, want_stdev= True, want_min=False):
           self.stat=Statistics()
           self.want_max=want_max
           self.want_mean= want_mean
           self.want_stdev= want_stdev
           self.want_min=want_min


    def to_kvhf(self, name):
        mins= self.stat.minimum() if self.want_min else []
        mins= self.stat.maximum() if self.want_max else []
        stdevs= self.stat.stddev() if self.want_stdev else []
        means= self.stat.mean if self.want_mean else []
        return Serie_stats(means=means, mins=mins, maxs=maxs, stdevs=stdevs)
        

    def add_occurence(self, time):
        self.stat.push(time)

    def get_occurence_num(self):
        return len(self.stat)


