#include "timer.h"

unsigned long init_timer() {
  unsigned long res = _init_timer();
  get_time_ns();
  return res;
}
