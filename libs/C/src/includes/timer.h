
/*Cross platform high resolution timer*/
//TODO Include get_intervall giving duration in between get_time_unspecified, for better precision (lesser boiler plate conversion during the timing)

#define NANOS_PER_SEC 1000000000UL
unsigned long get_time_ns();
/*Return time since unspecified starting point in nanoseconds*/


unsigned long get_time_unspecified();
/*Return time since get_time_unspecified starting point in unspecified unit. */

unsigned long init_timer();
/*Set the timer and return resolution*/

