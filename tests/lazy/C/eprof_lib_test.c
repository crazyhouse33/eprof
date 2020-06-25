#include "munit.h"
#include <eprof.h>
#include <stdio.h>

unsigned long t=0;


int main() {
  Eprof *profiler = new_eprofiler("eprof_test", false);
  eprof_event_start(profiler, FOR, whole);
  for (int i = 0; i < 5; i++) {
    eprof_event_start(profiler, in_for);
    eprof_event_end(profiler, in_for);
  }
  unsigned long last_t = eprof_event_end(profiler, FOR);
  eprof_event_end_nt(profiler, last_t, whole);
} 
