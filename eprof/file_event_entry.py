from collections import deque
from eprof.event import Event

class Event_entry:
    def __init__(self):
        self.event= Event()
        self.queue= deque()
        self.end_queue=deque() #Since we read start and end same time, end can correspond to a future start, so we need to stock it

    def add_occurence(self, start, finish):
        time= finish - start
        self.event.add_occurence(time)

    def add_event_start(self,time):
        self.queue.append(time)
        if self.end_queue:
            finish_time= self.end_queue.popleft()
            self.add_occurence(time, finish_time)

    def add_event_end(self,time):
        try: 
            start= self.queue.popleft()
        except IndexError:
            return self.end_queue.append(time)
        self.add_occurence(start, time)
 

