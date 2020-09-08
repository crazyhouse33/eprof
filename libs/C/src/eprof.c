#include "eprof.h"
#include "file_lock.h"
#include "stdlib.h"
#include "timer.h"
#include <dirent.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>

#ifdef WIN32
#include <windows.h>
#define mkdir(dir, mode) _mkdir(dir)
#endif

bool rm_all_files(char *dir_name) {
  /*Delete all files of a directory at depth one*/
  struct dirent *cursor;
  DIR *dir = opendir(dir_name);
  char to_remove[1000];
  if (dir == NULL)
    return false;

  while (cursor = readdir(dir)) { /* On lit le premier répertoire du dossier. */

    snprintf(to_remove, 1000, "%s/%s", dir_name, cursor->d_name);
    int status = remove(to_remove);
  }

  closedir(dir);

  return true;
}

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
    rm_all_files(file_path);
  }
  mkdir(file_path, S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
  FILE *f_start = open_and_lock_fall_back(start_file, "a");
  if (!f_start) {
    perror("Can not create start file: ");
    exit(3);
  }
  FILE *f_end = open_and_lock_fall_back(end_file, "a");
  if (!f_end) {
    perror("Can not create end file: ");
    exit(3);
  }

  prof->start_file = f_start;
  prof->end_file = f_end;
  init_timer();

  return prof;
}

void __eprof_log(FILE *file, char *string, unsigned long time) { fprintf(file, "%s:%lu\n", string, time); }

unsigned long __eprof_print_and_time(FILE *file, char *string) {
  unsigned long time_res = get_time_ns();
  __eprof_log(file, string, time_res);
  return time_res;
}

void eprof_free() {}
