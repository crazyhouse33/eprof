# Protection to not mess up sources
if ( ${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_BINARY_DIR} )
	message( FATAL_ERROR "In-source builds not allowed. Run cmake .. into the build directory. You need to remove CMakeFiles and CMakeCache.txt as it can not be done automatically inside the CMakeList. run:
	rm CMakeCache.txt
	rm -rf CMakeFiles	
	" )
	# Does not work
    file(REMOVE_RECURSE CMakeFiles)
    file(REMOVE CMakeCache.txt)
endif()

cmake_minimum_required(VERSION 3.7)

set (version 0.0)
project(eproflibc C)

include (CTest)
set(CMAKE_C_FLAGS_DEBUG "-ggdb3 -fdiagnostics-color=always")

# Building main executable
add_subdirectory(src)


if(CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME AND BUILD_TESTING)
    add_subdirectory(tests)
endif()

