#include "file_lock.h"
#include <fcntl.h>
#include <errno.h>
#include <sys/file.h>
#include <stdlib.h>
#include <string.h>
extern int errno;

int fopen_mode_to_open(char* mode){
	int oflag;
	switch (*mode) {
		case 'r':
			oflag = O_RDONLY;
			break;

		case 'w':
			oflag = O_WRONLY | O_CREAT | O_TRUNC;
			break;

		case 'a':
			oflag = O_WRONLY | O_CREAT | O_APPEND;
			break;

		default:
			errno = EINVAL;
			return -1;
	}

	while (*++mode) {
		switch (*mode) {
			case '+':
				oflag |= O_RDWR;
				oflag &= ~(O_RDONLY | O_WRONLY);
				break;

#if defined(O_TEXT) && defined(O_BINARY)
			case 't':
				oflag &= ~(O_TEXT | O_BINARY);
				oflag |= O_TEXT;
				break;
#endif

#if defined(O_TEXT) && defined(O_BINARY)
			case 'b':
				oflag &= ~(O_TEXT | O_BINARY);
				oflag |= O_BINARY;
				break;
#endif

			case 'c':
			case 'n':
				break;

#ifdef O_SEQUENTIAL
			case 'S':
				oflag |= O_SEQUENTIAL;
				break;
#endif


#ifdef O_RANDOM
			case 'R':
				oflag |= O_RANDOM;
				break;
#endif

#ifdef O_SHORT_LIVED
			case 'T':
				oflag |= O_SHORT_LIVED;
				break;
#endif

#ifdef O_TEMPORARY
			case 'D':
				oflag |= O_TEMPORARY;
				break;
#endif

			case ' ':
				// Ignore
				break;

			default:
				errno = EINVAL;
				return -1;
		}
	}

	return oflag;

}
FILE* open_and_lock(char* file, char* mode){
	int fd = open(file,fopen_mode_to_open(mode), S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH);//This is necessary to open with good modes. To not create file if user did not want to or crash if the file did not exist...
	int status= flock(fd, LOCK_NB | LOCK_EX);

	
	if (status ==-1){
		return (FILE*) -1;
	}
	return fopen(file, mode);
}

static size_t  __change_name(char** file_name,size_t name_len, size_t* mem, int cpt){
	char to_append[100];
	size_t append_len= snprintf(to_append, 100,"%d", cpt);
	size_t total_size= append_len + name_len+1;
	size_t new_size=total_size;
	if (*mem<total_size){
		new_size+=5;
		*file_name=realloc(*file_name, sizeof(char)*new_size);
		*mem=new_size;
	}
	memcpy(*file_name+name_len, to_append, sizeof(char)*(append_len+1));
	return total_size;

}

FILE* open_and_lock_fall_back(char* file_name, char* mode){
	FILE* res;
	int cpt=2;
	size_t len= strlen(file_name);
	char* new_file= strdup(file_name);
	size_t mem= len+1;

	res= open_and_lock(new_file, mode);

	while (res==(FILE*)-1 && errno== EWOULDBLOCK){
		len= __change_name(&new_file, len, &mem,cpt++);
		res=open_and_lock(new_file, mode);
	}

	return res;

}

int delete_lock(char* file_name){
	int fd = open(file_name, O_RDONLY, S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH);
	int status= flock(fd, LOCK_UN);
	return status;
}

