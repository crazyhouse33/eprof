#putting test in bin/test
#detecting valgrind
include(CheckIncludeFile)
check_include_file("valgrind/valgrind.h" HAVE_VALGRIND)
if(HAVE_VALGRIND)
	add_definitions(-D VALGRIND=1)
endif()


set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)
if(NOT DEFINED PRODUCT_NUM_IT)
	SET(PRODUCT_NUM_IT 10000)

endif()

message("Test discovery and building:\n")
#include_subdirectories(${CMAKE_PROJECT_SOURCE_DIR}/extern/test/src)
#file(GLOB_RECURSE TESTS_EXT_SRC CONFIGURE_DEPENDS ${CMAKE_PROJECT_SOURCE_DIR}/extern/test/src/*.c ${CMAKE_PROJECT_SOURCE_DIR}/extern/test/src/*.h)
file(GLOB_RECURSE TESTS ${CMAKE_CURRENT_SOURCE_DIR}/*.c)
file(GLOB_RECURSE MUNIT_SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/extern/munit/*.c ${CMAKE_CURRENT_SOURCE_DIR}/extern/munit/*.h)
list (REMOVE_ITEM TESTS ${MUNIT_SOURCES})
list (REMOVE_ITEM MUNIT_SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/extern/munit/example.c)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/extern/munit)




foreach(file ${TESTS})
  get_filename_component (name_without_extension ${file} NAME_WE)
  add_executable(${name_without_extension} ${file} ${MUNIT_SOURCES})
  target_link_libraries(${name_without_extension} eprof)
  add_test(NAME ${name_without_extension} COMMAND ${name_without_extension} ${PRODUCT_NUM_IT} WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/out)
  message("\t-Found ${file}. Will be build as ${EXECUTABLE_OUTPUT_PATH}/${name_without_extension}")
endforeach()


#compile ext-test ones
file(GLOB_RECURSE TEST_DEPENDENCIES ${CMAKE_CURRENT_SOURCE_DIR}/ext-tests/*.c)
foreach(file ${TEST_DEPENDENCIES})
	message ("\t${file} detected as necessary compile target for tests")
	get_filename_component (name_without_extension ${file} NAME_WE)
  	add_executable(${name_without_extension} ${file})
endforeach()

#listing dependencies of test (we should have done it automatically in the name)

add_dependencies (timer_test timer_precision)# timer call timer prcision


