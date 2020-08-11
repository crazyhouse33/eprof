#include "timer.h"
#include "munit.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() {

  long res = init_timer();

  for (int i = 0; i < 10; i++) {

    FILE *fp;
    char out[1035];

    long start = get_time_ns();

    fp = popen("../../build/bin/timer_precision", "r");
    if (fp == NULL) {
      printf("Failed to run command\n");
      exit(1);
    }

    char *placeholder;
    fread(out, sizeof(char), 1035, fp);
    char *space = strchr(out, ' ');
    *space = 0;
    unsigned long start_proc = strtoul(out, &placeholder, 0);
    unsigned long end_proc = strtoul(space + 1, &placeholder, 0);
    int ret_status = pclose(fp);
    long end = get_time_ns();

    munit_assert_ulong(start_proc, >=, start);
    munit_assert_ulong(start_proc, <=, end);
    munit_assert_ulong(end_proc, <=, end);
    munit_assert_ulong(end_proc, >=, start);
    munit_assert_ulong(end_proc, >=, start_proc);

    start = start_proc;
    end = end_proc;

    munit_assert_int(ret_status, ==, 0);
  }
}
