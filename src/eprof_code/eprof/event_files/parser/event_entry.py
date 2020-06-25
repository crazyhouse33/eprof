from collections import deque

class Event_entry:
    def __init__(self):
        self.event= Event_statistics()
        self.queue=deque()

    def add_event_start(self,time):
        self.queue.append(self.time)

    def add_event_end(self,time):
        start= self.queue.popleft()
        time = time - start
        self.event.add_occurence(time)

