---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:17:57.064861'
id: b29d8606
links: []
modified: '2026-05-07T20:17:57.064861'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: cmake_minimum_required(VERSION 3.13) project(runner LANGUAGE (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: bd81b55faef8
source: CMakeLists.txt
page: 0
title: cmake_minimum_required(VERSION 3.13) project(runner LANGUAGE (Chunk 0)
keywords: ['CMake', 'C++', 'Application Target', 'main.cc', 'my_application.cc', 'flutter', 'APPLICATION_ID', 'dependency libraries']
created: 2026-05-08 01:47:57
tree_path: runner > Page 0 > cmake_minimum_required(VERSION 3.13) project(runne
---

cmake_minimum_required(VERSION 3.13) project(runner LANGUAGES CXX) # Define the application target. To change its name, change BINARY_NAME in the # top-level CMakeLists.txt, not the value here, or `flutter run` will no longer # work. # # Any new source files that you add to the application should be added here. add_executable(${BINARY_NAME} "main.cc" "my_application.cc" "${FLUTTER_MANAGED_DIR}/generated_plugin_registrant.cc" ) # Apply the standard set of build settings. This can be removed for applications # that need different build settings. apply_standard_settings(${BINARY_NAME}) # Add preprocessor definitions for the application ID. add_definitions(-DAPPLICATION_ID="${APPLICATION_ID}") # Add dependency libraries. Add any application-specific dependencies here. target_link_libraries(${BINARY_NAME} PRIVATE flutter) target_link_libraries(${BINARY_NAME} PRIVATE PkgConfig::GTK) target_include_directories(${BINARY_NAME} PRIVATE "${CMAKE_SOURCE_DIR}")

### Related Concepts
- [[Application Target]]
- [[CMake]]
- [[main.cc]]
- [[APPLICATION_ID]]
- [[dependency libraries]]
- [[C++]]
- [[flutter]]
- [[my_application.cc]]
