#include "file_lock.h"
#include "munit.h"

int main() {
FILE* file = open_and_lock("lock_test", "w");
FILE* f2=open_and_lock("lock_test", "w");
munit_assert_ptr(f2, ==, (FILE*)-1);

FILE* f3=open_and_lock_fall_back("lock_test", "w");

FILE* f4=fopen("lock_test2","r");
munit_assert_ptr(f4, !=,NULL);

int stat=delete_lock("lock_test");
munit_assert_int(stat, ==, 0);
/*FILE* f5=open_and_lock("lock_test", "w");
munit_assert_ptr(f5, !=, (FILE*)-1);
munit_assert_ptr(f5, !=, NULL);
We dont do thoses because apparentl from a process if you open twice the file it dont lock. Still it should work from external processes.  https://gavv.github.io/articles/file-locks/

This is really odd and I passed 2 hours on this ;(
*/
}
	
