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
project(eproflib C)

#Common use functions
include(build-helpers/cmakefunc)

#Setting compilation options
set(CMAKE_BUILD_TYPE Debug)
#fdiagnostics for ninja that have trouble with color otherwise
set(CMAKE_C_FLAGS_DEBUG "-ggdb3 -fdiagnostics-color=always")
#allow C programs to get the version
add_definitions(-DAUTHBREAK_VERSION="${version}")
include(build-helpers/cmake_dependencies_set_up) # Finding necessary standard libs and seting up path in the code


#TODO put it separate file
#if we are not in master, we need to us templates to fill some files for master
set ( CONFIGURE_DIR ${CMAKE_SOURCE_DIR}/dev/push_release_to_master)
if(EXISTS "${CONFIGURE_DIR}")
	configure_file(${CONFIGURE_DIR}/eprof.py.cmake_template ${CMAKE_BINARY_DIR}/eprof.py)#give python version number

configure_file(${CONFIGURE_DIR}/README.md.cmake_template ${CMAKE_SOURCE_DIR}/README.md)#give readme version number

endif()


# Building libraries
add_subdirectory(src/libs)

##### TEST 
include (CTest)


# Building tests
add_subdirectory(tests)

#Adittional targets
include(build-helpers/cmake_lazy_testing_targets) # need to be after test discovery
