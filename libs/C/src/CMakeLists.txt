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


set(SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/eprof.c ${CMAKE_CURRENT_SOURCE_DIR}/includes/eprof.h ${CMAKE_CURRENT_SOURCE_DIR}/timer/aple_timer.c ${CMAKE_CURRENT_SOURCE_DIR}/timer/linux_timer.c ${CMAKE_CURRENT_SOURCE_DIR}/timer/windows_timer.c ${CMAKE_CURRENT_SOURCE_DIR}/timer/timer.c ${CMAKE_CURRENT_SOURCE_DIR}/includes/timer.h  ${CMAKE_CURRENT_SOURCE_DIR}/includes/file_lock.h ${CMAKE_CURRENT_SOURCE_DIR}/file-lock/file_lock.c )

set(ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

add_library(eprof STATIC ${SOURCES})

set_target_properties(eprof PROPERTIES VERSION ${version})
target_include_directories(eprof PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/includes)
set (headers ${SOURCES})
list(FILTER headers INCLUDE REGEX .*\.h)
message ("${headers}")
 

set_target_properties(eprof PROPERTIES PUBLIC_HEADER "${headers}")


include(GNUInstallDirs)
INSTALL(TARGETS eprof DESTINATION lib/eprof PUBLIC_HEADER DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/eprof"
)
 	


