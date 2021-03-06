#include <eprof.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

unsigned long t = 0;

int main(int argc, char **argv) {
  if (argc < 2) {
    printf("Plz run with a number of iteration to run. Give one more to activate append mode");
    exit(1);
  }
  bool append= argc >2;

  int it = atoi(argv[1]);
  Eprof *profiler = new_eprofiler("eprof_test", append);

  eprof_event_start(profiler, whole);
  for (int j = 0; j < it; j++) {
    eprof_event_start(profiler, ext_for);

    for (int i = 0; i < 10; i++) {
      eprof_event_start(profiler, in_for);
      eprof_event_end(profiler, in_for);
    }
    eprof_event_end(profiler, ext_for);
  }
  eprof_event_end(profiler, whole);
  return 0;
}
