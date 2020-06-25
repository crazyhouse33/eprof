
def read_file_until(f, delim='\n', bufsize=65536):
    prev = ''
    buf="1"
    while buf:
        buf = f.read(bufsize)
        split = buf.split(delim)
        if len(split)>1:
            yield prev + split[0]# appending first the the tail
            for part in split[1:-1]:# Threat everything in betwen between
                yield part
        prev += split[-1]#adding rest 


class Event_parser:

    def __init__(self, ):
        self.dictionnary_events=defaultdict(Event_entry)
        self.time_end_sep='\n'
        self.event_sep=','
        self.time_begin_sep=':'


    def parse_dir(self,dir_path):
        with open(dir_path+"/S") as f_start: 
            with open(dir_path+"/E") as f_end:
                startline="1"
                endline="1"
                while startline or endline:
                    if startline:
                        startline = read_file_until(f_start, self.time_sep):
                        ev_starts, time_start= self.parse_line(startline)
                        for start in ev_starts:
                        entry= self.dictionnary_events[start]
                        entry.add_event_start(time_start)
                    
                    if endline:
                        endline = read_file_until(f_end, self.time_sep)
                        ev_ends, time_end= self.parse_line(endline)
                        for end in ev_ends:
                            entry= self.dictionnary_events[end]
                            entry.add_event_end(time_end)

    def parse_line(self, line):
        partition= line.partition(self.time_begin_sep)
        return partition[0].split(self.event_sep) partition[2]

    def parser_get_result(self):
        super_dict=Super_dict()
        for key, value in self.dictionnary_events.items():
            small_dict = Super_dict(value.event.as_dict(key))
            super_dict.merge_vertical(small_dict)
        return super_dict
