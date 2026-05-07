---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:25:02.738195'
id: 5ffb400b
links: []
modified: '2026-05-07T20:25:02.738195'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: cmake_minimum_required(VERSION 3.15) project(runner LANGUAGE (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: 917639eb7a12
source: CMakeLists.txt
page: 0
title: cmake_minimum_required(VERSION 3.15) project(runner LANGUAGE (Chunk 0)
keywords: ['CMake', 'Version 3.15', 'Project Runner', 'Binary Name', 'flutter_window.cpp', 'main.cpp', 'run_loop.cpp', 'win32_window.cpp', 'Runner.rc', 'runner.exe.manifest', 'flutter', 'flutter_wrapper_app']
created: 2026-05-08 01:55:02
tree_path: runner > Page 0 > cmake_minimum_required(VERSION 3.15) project(runne
---

cmake_minimum_required(VERSION 3.15) project(runner LANGUAGES CXX) add_executable(${BINARY_NAME} WIN32 "flutter_window.cpp" "main.cpp" "run_loop.cpp" "utils.cpp" "win32_window.cpp" "${FLUTTER_MANAGED_DIR}/generated_plugin_registrant.cc" "Runner.rc" "runner.exe.manifest" ) apply_standard_settings(${BINARY_NAME}) target_compile_definitions(${BINARY_NAME} PRIVATE "NOMINMAX") target_link_libraries(${BINARY_NAME} PRIVATE flutter flutter_wrapper_app) target_include_directories(${BINARY_NAME} PRIVATE "${CMAKE_SOURCE_DIR}") add_dependencies(${BINARY_NAME} flutter_assemble)

### Related Concepts
- [[CMake]]
- [[runner.exe.manifest]]
- [[flutter_wrapper_app]]
- [[Version 3.15]]
- [[main.cpp]]
- [[flutter_window.cpp]]
- [[run_loop.cpp]]
- [[Runner.rc]]
- [[win32_window.cpp]]
- [[Binary Name]]
- [[Project Runner]]
- [[flutter]]
