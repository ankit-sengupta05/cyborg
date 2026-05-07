---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:23:04.314640'
id: dee7d424
links: []
modified: '2026-05-07T20:23:04.314640'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: The Flutter tooling requires that developers have a version  (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: d5c61f7adcea
source: CMakeLists.txt
page: 0
title: The Flutter tooling requires that developers have a version  (Chunk 0)
keywords: ['Flutter tooling', 'Visual Studio', 'CMake']
created: 2026-05-08 01:53:04
tree_path: windows > Page 0 > The Flutter tooling requires that developers have 
---

# The Flutter tooling requires that developers have a version of Visual Studio # installed that includes CMake 3.14 or later. You should not increase this # version, as doing so will cause the plugin to fail to compile for some # customers of the plugin. cmake_minimum_required(VERSION 3.14) set(PROJECT_NAME "jni") project(${PROJECT_NAME} LANGUAGES CXX) add_subdirectory("${CMAKE_CURRENT_SOURCE_DIR}/../src" "${CMAKE_CURRENT_BINARY_DIR}/shared") if (TARGET jni) set(jni_bundled_libraries $<TARGET_FILE:jni> PARENT_SCOPE ) else() set(jni_bundled_libraries "" PARENT_SCOPE ) endif()

### Related Concepts
- [[Flutter tooling]]
- [[CMake]]
- [[Visual Studio]]
