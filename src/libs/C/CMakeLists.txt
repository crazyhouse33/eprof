message ("Building C library")
set( CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/libs)

set(SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/eprof.c ${CMAKE_CURRENT_SOURCE_DIR}/includes/eprof.h ${CMAKE_CURRENT_SOURCE_DIR}/timer/aple_timer.c ${CMAKE_CURRENT_SOURCE_DIR}/timer/linux_timer.c ${CMAKE_CURRENT_SOURCE_DIR}/timer/windows_timer.c ${CMAKE_CURRENT_SOURCE_DIR}/includes/timer.h )

include_subdirectories(${PROJECT_SOURCE_DIR}/extern/normal/src)
include_subdirectories(${CMAKE_CURRENT_SOURCE_DIR}/includes)

file(GLOB_RECURSE EXTERN_SOURCES CONFIGURE_DEPENDS ${PROJECT_SOURCE_DIR}/extern/normal/src/*.h ${PROJECT_SOURCE_DIR}/extern/normal/src/*.c)

#pretty printing sources for debuging build process
JOIN(";${SOURCES}" \n\t pretty)
message ("\nDetected internal sources in src:\n${pretty} ")

JOIN(";${EXTERN_SOURCES}" \n\t pretty)
message ("\nDetected external sources in extern/normal/src:\n${pretty}")


list (APPEND SOURCES ${EXTERN_SOURCES})

add_library(eprof STATIC ${SOURCES})

set_target_properties(eprof PROPERTIES VERSION ${version})
INSTALL(TARGETS eprof
        ARCHIVE DESTINATION ${PROJECT_SOURCE_DIR}/libs
        PUBLIC_HEADER DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/includes
)
target_include_directories(eprof PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/includes)

