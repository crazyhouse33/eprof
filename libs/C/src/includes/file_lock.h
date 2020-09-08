#include <stdio.h>

FILE* open_and_lock(char* file_name, char* mode);
/*Open file if not previously locked. Return -1 if could not create/acquire the lock. Set errno. Return NULL if could not create the file and set errno. If you receive NULL, you should delete the lock yourself( the library dont do it to let you threat the errno of the file creation)*/
FILE* open_and_lock_fall_back(char* file_name, char* mode);
/*Open file if not locked. If failed because locked, try file-2, file-3 ...*/
int delete_lock(char* file_name);
/*Remove lock for a file, return -1 if error and set errno*/
