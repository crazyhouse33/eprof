#ifndef GUARD_XXEPROF_C_GUARD_XX
#define GUARD_XXEPROF_C_GUARD_XX
#include <stdio.h>
#include <stdbool.h>

#define QUOTE_RES_(...) #__VA_ARGS__
#define QUOTE_RES(...) QUOTE_RES_(__VA_ARGS__)

typedef struct Eprof Eprof;
struct Eprof{
	FILE* start_file;
	FILE* end_file;
};

#define eprof_event_end(profiler, ...) \
__eprof_print_and_time(profiler->end_file, QUOTE_RES(__VA_ARGS__))
/*Mark all the given events end. Log time with internal timer*/

#define eprof_event_start(profiler, ...) \
__eprof_print_and_time(profiler->start_file, QUOTE_RES(__VA_ARGS__))
/*Mark all the given events start. Log time with internal timer*/

#define eprof_event_end_nt(profiler, time, ...) \
__eprof_log(profiler->end_file, QUOTE_RES(__VA_ARGS__), time)
/*Mark all the given events end. Log given time unstead of using the timer*/

#define eprof_event_start_nt(profiler, time, ...) \
__eprof_log(profiler->start_file, QUOTE_RES(__VA_ARGS__), time)
/*Mark all the given events start. Log given time unstead of using the timer*/

// fof tests
char* __eprof_get_file_loc(char* name, size_t len, char letter);

void __eprof_log(FILE* file, char* string, unsigned long time);
/*Internal function used by macro*/


unsigned long __eprof_print_and_time(FILE* file, char* string);
/*Internal function used by macro*/

Eprof* new_eprofiler(char* dir_path, bool append);
/*return eprof entitie loging event in the specified dir_path.*/ 
#endif
