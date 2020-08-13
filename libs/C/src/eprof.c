#include "eprof.h"
#include "stdlib.h"
#include "timer.h"
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>

#ifdef WIN32
#include <windows.h>
#define mkdir(dir, mode) _mkdir(dir)
#endif

// Used by tests and thus not static
char *__eprof_get_file_loc(char *name, size_t len, char letter) {
  char *start_file = malloc(sizeof(char) * (len + 3));
  memcpy(start_file, name, sizeof(char) * len);
  start_file[len] = '/';
  start_file[len + 1] = letter;
  start_file[len + 2] = 0;
  return start_file;
}

Eprof *new_eprofiler(char *file_path, bool append) {
  Eprof *prof = malloc(sizeof(Eprof));
  size_t len = strlen(file_path);
  char *start_file = __eprof_get_file_loc(file_path, len, 'S');
  char *end_file = __eprof_get_file_loc(file_path, len, 'E');

  if (!append) {
    remove(start_file);
    remove(end_file);
  }
  mkdir(file_path, S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
  FILE *f_start = open_and_lock(start_file, "a");
  if (!f_start) {
    perror("Can not create start file: ");
    exit(3);
  }
  FILE *f_end = open_and_lock(end_file, "a");
  if (!f_end) {
    perror("Can not create end file: ");
    exit(3);
  }
  if (append){
	  char* buffer = malloc(sizeof(char)*);
  	setvbuf( f_start, NULL, _IOFBF, sizeof( buf ) )
  }
  prof->start_file = f_start;
  prof->end_file = f_end;
  return prof;
}

void __eprof_log(FILE *file, char *string, unsigned long time) { fprintf(file, "%s:%lu\n", string, time); }

unsigned long __eprof_print_and_time(FILE *file, char *string) {
  unsigned long time_res = get_time_ns();
  __eprof_log(file, string, time_res);
  return time_res;
}

void eprof_free(){
	
}
