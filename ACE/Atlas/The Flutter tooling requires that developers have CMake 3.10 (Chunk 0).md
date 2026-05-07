---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:22:46.867243'
id: ddb7a420
links: []
modified: '2026-05-07T20:22:46.867243'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: The Flutter tooling requires that developers have CMake 3.10 (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: b92800c85cf9
source: CMakeLists.txt
page: 0
title: The Flutter tooling requires that developers have CMake 3.10 (Chunk 0)
keywords: ['Flutter tooling', 'CMake 3.10']
created: 2026-05-08 01:52:46
tree_path: linux > Page 0 > The Flutter tooling requires that developers have 
---

# The Flutter tooling requires that developers have CMake 3.10 or later # installed. You should not increase this version, as doing so will cause # the plugin to fail to compile for some customers of the plugin. cmake_minimum_required(VERSION 3.10) set(PROJECT_NAME "jni") project(${PROJECT_NAME} LANGUAGES CXX) add_subdirectory("${CMAKE_CURRENT_SOURCE_DIR}/../src" "${CMAKE_CURRENT_BINARY_DIR}/shared") if (TARGET jni) set(jni_bundled_libraries $<TARGET_FILE:jni> PARENT_SCOPE ) else() set(jni_bundled_libraries "" PARENT_SCOPE ) endif()

### Related Concepts
- [[Flutter tooling]]
- [[CMake 3.10]]
