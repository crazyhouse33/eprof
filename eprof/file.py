from collections import defaultdict
from eprof.file_event_entry import Event_entry
import os 
from kvhf.file import KVH_file
import heapq
import re
regexp_start= re.compile(r".*S\d?$")
regexp_end= re.compile(r".*E\d?$")
start_type=0
end_type=1



def read_file_until(f, delim='\n', bufsize=65536):
    prev = ''
    buf = "1"
    if type(f)==str:
        need_to_close=True
        f=open(f)
    while buf:
        buf = f.read(bufsize)
        split = buf.split(delim)
        if len(split) > 1:
            yield prev + split[0]  # appending first the the tail
            prev = ''
            for part in split[1:-1]:  # Threat everything in  between
                yield part
        prev += split[-1]  # adding rest
    if need_to_close==True:
        f.close()

class line_reader():
    def __init__(self, f, delim, bufsize=65536, name='',type=0):
        self.gen= read_file_until(f, delim, bufsize)
        self.line=0
        self.name=name
        self.type=type

    def read_line(self):
        try:
            line = next(self.gen)
            self.line+=1
            return line
        except StopIteration:
            return None



class Event_file:

    def __init__(self, path=None):
        self.dictionnary_events = defaultdict(Event_entry)
        self.time_end_sep = '\n'
        self.event_sep = ','
        self.time_begin_sep = ':'
        if path is None:
            return
        elif isinstance(path, str):
            self.parse_dir(path)
        else:
            raise TypeError(
                "Init argument must be nothing, None, or a path to an eprof directory (str), not " + str(type(path)))

    def get_readers(self,dir_path):
        res={}
        files = [dir_path + '/'+ file for file in os.listdir(dir_path) if os.path.isfile(dir_path+'/'+file)]
        start_files= [ file for file in files if regexp_start.match(file)]
        end_files=[ file for file in files if regexp_end.match(file)]

        for file in start_files:
            reader=line_reader(file, self.time_end_sep,name=file, type=start_type)
            res[file]=reader

        for file in end_files:
            reader=line_reader(file, self.time_end_sep,name=file, type=end_files)
            res[file]=reader

        return res 



    def parse_dir(self, dir_path):
        #This parse a dir respecting timeline and being memory friendly
        #Creating heap
        readers= self.get_readers(dir_path)
        lines=[]
        for key, reader in list(readers.items()):
            line = reader.read_line()
            if line ==None:
                del readers[key]
                continue
            heapq.heappush(lines, (self.parse_line(line, reader.name, reader.line), reader))

        while readers:

            line, reader = heapq.heappop(lines)
            time, ev_names  = line

            #Processing the minimum line
            for name in ev_names:
                entry = self.dictionnary_events[name]
                if reader.type == start_type:
                    entry.add_event_start(time)
                else :
                    entry.add_event_end(time)

            #Adding next line to the heap
            next_line= reader.read_line()
            if next_line ==None:#reader is done
                del readers[reader.name]
            else:
                heapq.heappush(lines, (self.parse_line(next_line, reader.name, reader.line), reader))


    def parse_line(self, line, path="", lineno=-1):
        try:
            partition = line.partition(self.time_begin_sep)
            return float(partition[2]), [name.strip() for name in partition[0].split(
                self.event_sep)] 
        except Exception as e:
            raise ValueError("Parsing error on file \"{}\":{}".format(path, lineno)) from e

    def to_kvh_file(self):
        kvhf_dic = {}
        for key, value in self.dictionnary_events.items():
            event = value.event
            kvhf_entry = event.to_kvhf()
            kvhf_dic[key] = kvhf_entry
        return KVH_file(kvhf_dic)
