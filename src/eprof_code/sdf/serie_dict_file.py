import matplotlib.pyplot as pyplot
class Serie_dict:
    def __init__(self, file_or_dico=None, key_sep=':', value_sep=' '):
        """Create a super dict from a normal dict, or a file. Empty super dict if nothing"""
        self.key_sep=key_sep;
        self.value_sep=value_sep;
        if not file_or_dico:
            self.dico = dictdefault(list)  
        else if isinstance(file_or_dico,dict):
            self.dico = file_or_dico
        else:
            self.dico = parse_file(file_or_dico)

    
    def dump_to_file(self, file, keys=None, key_sep=None, value_sep=None):
        """Serialize subset of keys (default all) to given path"""
        if keys == None:
            keys= self.dico.keys()
        if key_sep == None:
            key_sep= self.key_sep

        if value_sep == None:
            value_sep= self.key_sep

        with open(file) as f:
            for key in keys:
                print("{}{}{}".format(key, key_sep, value_sep.join(self.dico[key])),file=f)

    def parse_file(file, key_sep, value_sep):
        """Parse a file and return a super dict"""
        dico=Serie_dict()
        with open(file) as f:
            for line in f.read().split('\n'):
                key, sep, values= line.partition(key_sep)
                dico[key]= values.split(value_sep)
        return dico

    def merge_vertical(self,dico2, keys=None):
        """Add entries of dico 2 corresponding to keys (by default all). If key is allready present, the new value replace the old one"""
        if keys == None:
            keys = dico2.dico.keys()

        for key in keys:
            self.dico[key]= dico2.dico[key]

    def merge_horizontal(self, dico2):
        """Add entries of dico2 corresponding to keys (by default all). If key is allready present, append the values of the second dico the existing one"""
        if keys== None:
            keys = dico2.dico.keys()

        for key in keys:
            self.dico[key].extend(dico2.dico[key])

    def plot(self, keys=None):
        """Plot on same graph every values of given keys (all by default)"""
        if  keys==None:
            keys= self.dico.keys()

        for key in keys:
            pyplot.plot(self.dico[key], label=key)
        pyplot.legend()

    def plot_pie(self, keys=None)):
        """Plot pie chart of last values of given keys (all by default)"""
        if keys ==None:
            keys=self.dico.keys()

        values = [self.dico[key][-1] for key in keys]
        pyplot.pie(values, labels=keys)






