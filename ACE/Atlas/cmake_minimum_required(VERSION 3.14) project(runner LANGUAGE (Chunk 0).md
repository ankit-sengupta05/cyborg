---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:25:32.460730'
id: 5791a500
links: []
modified: '2026-05-07T20:25:32.460730'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: cmake_minimum_required(VERSION 3.14) project(runner LANGUAGE (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: a42f3723f5a7
source: CMakeLists.txt
page: 0
title: cmake_minimum_required(VERSION 3.14) project(runner LANGUAGE (Chunk 0)
keywords: ['CMake', 'C++', 'Application Target', 'flutter run', 'flutter_window.cpp', 'main.cpp', 'utils.cpp', 'win32_window.cpp', 'flutter_window.cpp', 'Runner.rc', 'runner.exe.manifest', 'BINARY_NAME', 'FLUTTER_VERSION', 'FLUTTER_VERSION_MAJOR', 'FLUTTER_VERSION_MINOR', 'FLUTTER_VERSION_PATCH', 'NOMINMAX', 'flutter', 'flutter_wrapper_app', 'dwmapi.lib', 'CMAKE_SOURCE_DIR', 'flutter_assemble']
created: 2026-05-08 01:55:32
tree_path: runner > Page 0 > cmake_minimum_required(VERSION 3.14) project(runne
---

cmake_minimum_required(VERSION 3.14) project(runner LANGUAGES CXX) # Define the application target. To change its name, change BINARY_NAME in the # top-level CMakeLists.txt, not the value here, or `flutter run` will no longer # work. # # Any new source files that you add to the application should be added here. add_executable(${BINARY_NAME} WIN32 "flutter_window.cpp" "main.cpp" "utils.cpp" "win32_window.cpp" "${FLUTTER_MANAGED_DIR}/generated_plugin_registrant.cc" "Runner.rc" "runner.exe.manifest" ) # Apply the standard set of build settings. This can be removed for applications # that need different build settings. apply_standard_settings(${BINARY_NAME}) # Add preprocessor definitions for the build version. target_compile_definitions(${BINARY_NAME} PRIVATE "FLUTTER_VERSION=\"${FLUTTER_VERSION}\"") target_compile_definitions(${BINARY_NAME} PRIVATE "FLUTTER_VERSION_MAJOR=${FLUTTER_VERSION_MAJOR}") target_compile_definitions(${BINARY_NAME} PRIVATE "FLUTTER_VERSION_MINOR=${FLUTTER_VERSION_MINOR}") target_compile_definitions(${BINARY_NAME} PRIVATE "FLUTTER_VERSION_PATCH=${FLUTTER_VERSION_PATCH}") target_compile_definitions(${BINARY_NAME} PRIVATE "FLUTTER_VERSION_BUILD=${FLUTTER_VERSION_BUILD}") # Disable Windows macros that collide with C++ standard library functions. target_compile_definitions(${BINARY_NAME} PRIVATE "NOMINMAX") # Add dependency libraries and include directories. Add any application-specific # dependencies here. target_link_libraries(${BINARY_NAME} PRIVATE flutter flutter_wrapper_app) target_link_libraries(${BINARY_NAME} PRIVATE "dwmapi.lib") target_include_directories(${BINARY_NAME} PRIVATE "${CMAKE_SOURCE_DIR}") # Run the Flutter tool portions of the build. This must not be removed. add_dependencies(${BINARY_NAME} flutter_assemble)

### Related Concepts
- [[FLUTTER_VERSION]]
- [[flutter_wrapper_app]]
- [[main.cpp]]
- [[FLUTTER_VERSION_MINOR]]
- [[BINARY_NAME]]
- [[CMake]]
- [[flutter_assemble]]
- [[utils.cpp]]
- [[CMAKE_SOURCE_DIR]]
- [[win32_window.cpp]]
- [[NOMINMAX]]
- [[C++]]
- [[runner.exe.manifest]]
- [[FLUTTER_VERSION_MAJOR]]
- [[flutter_window.cpp]]
- [[Runner.rc]]
- [[FLUTTER_VERSION_PATCH]]
- [[dwmapi.lib]]
- [[Application Target]]
- [[flutter run]]
- [[flutter]]
