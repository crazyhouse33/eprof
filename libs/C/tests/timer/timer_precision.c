// If you are tempted to put that at extern test because it is called by the timer test, dont do because remember extern test dont have access to normal code source
#include "timer.h"
#include "munit.h"
#include "stdio.h"

// need to handle valgrind cause it mess up precision tests

#ifdef VALGRIND
#include "valgrind/valgrind.h"
#endif

#define ALLOWED_MISPRESION 3
int main() {
  init_timer();
  unsigned long t1 = get_time_ns();
  unsigned long t2 = get_time_ns();

  // we print in order for an extern test to test that cross process timing is working as well
  printf("%lu %lu", t1, t2);
  unsigned long time = t2 - t1;
// testing precision
#ifdef VALGRIND
  if (RUNNING_ON_VALGRIND)
    return 0;
#endif
  munit_assert_ulong(time, <=, 1000);
  return 0;
}
