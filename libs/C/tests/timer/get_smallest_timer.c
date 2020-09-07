// If you are tempted to put that at extern test because it is called by the timer test, dont do because remember extern test dont have access to normal code source
#include "stdio.h"
#include "timer.h"

int main() {
  init_timer();
  unsigned long t1 = get_time_ns();
  unsigned long t2 = get_time_ns();

  // we print in order for an extern test to test that cross process timing is working as well
  printf("%lu", t2 - t1);
  return 0;
}
