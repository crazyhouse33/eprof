#putting test in bin/test
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin/test_binaries)

set(list_lazy_tests )
set(list_mandatory_tests )



file(GLOB_RECURSE EXTERN_SOURCES_TEST CONFIGURE_DEPENDS ${PROJECT_SOURCE_DIR}/extern/test/src/*.h ${PROJECT_SOURCE_DIR}/extern/test/src/*.c)

file(GLOB_RECURSE TESTS_SOURCES ${PROJECT_SOURCE_DIR}/tests/shared-codebase/*.c ${PROJECT_SOURCE_DIR}/tests/shared-codebase/*.h)

# Removing garbage among external sources
list(REMOVE_ITEM EXTERN_SOURCES_TEST ${PROJECT_SOURCE_DIR}/extern/test/src/munit/example.c )

JOIN(";${TESTS_SOURCES}" \n\t pretty)
message ("\nDetected sources for test build in test/shared-codebase:\n ${pretty}")

JOIN(";${EXTERN_SOURCES_TEST}" \n\t pretty)
message ("\nDetected external sources for test build in extern/test/src:\n ${pretty}")

include_subdirectories(${PROJECT_SOURCE_DIR}/tests/shared-codebase)
include_subdirectories(${PROJECT_SOURCE_DIR}/extern/test/src)
list(APPEND SOURCES ${TESTS_SOURCES})
list (APPEND SOURCES ${EXTERN_SOURCES_TEST})



message("Test discovery and building:\n")
file(GLOB_RECURSE CTESTS ${PROJECT_SOURCE_DIR}/tests/*.c)
list(FILTER CTESTS EXCLUDE REGEX ${PROJECT_SOURCE_DIR}/tests/ext-tests/.*) # every .c in test excecpt the one in ext-test is to be compiled as a test
list(FILTER CTESTS EXCLUDE REGEX ${PROJECT_SOURCE_DIR}/tests/shared-codebase/.*) #Those are not to compile
foreach(file ${CTESTS})
  get_filename_component (name_without_extension ${file} NAME_WE)
  add_executable(${name_without_extension} ${SOURCES} ${file})
  add_test(NAME ${name_without_extension} COMMAND ${name_without_extension} WORKING_DIRECTORY ${EXECUTABLE_OUTPUT_PATH})
  if (file MATCHES ${PROJECT_SOURCE_DIR}/tests/lazy/*)

	  message("\t${file} detected as a lazy test")
	  #listing test->executable test for the python script to let him check modification date of exe
	  list(APPEND list_lazy_tests "${name_without_extension} ${EXECUTABLE_OUTPUT_PATH}/${name_without_extension}")
  else()
	message("\t${file} detected as a mandatory test")
	  list(APPEND list_mandatory_tests "${name_without_extension} ${EXECUTABLE_OUTPUT_PATH}/${name_without_extension}")
  endif()

endforeach()


#compile ext-test ones
file(GLOB_RECURSE TEST_DEPENDENCIES ${PROJECT_SOURCE_DIR}/tests/ext-tests/*.c)
foreach(file ${TEST_DEPENDENCIES})
	message ("\t${file} detected as necessary compile target for tests")
	get_filename_component (name_without_extension ${file} NAME_WE)
  	add_executable(${name_without_extension} ${file})
endforeach()

target_link_libraries(eprof_lib_test eprof)

#listing dependencies of test (we should have done it automatically in the name)

set(list_lazy_tests ${list_lazy_tests} PARENT_SCOPE)
set(list_mandatory_tests ${list_mandatory_tests} PARENT_SCOPE)








