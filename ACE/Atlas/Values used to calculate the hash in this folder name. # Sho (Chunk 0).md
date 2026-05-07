---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:21:16.059939'
id: '14497569'
links: []
modified: '2026-05-07T20:21:16.059939'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: 'Values used to calculate the hash in this folder name. # Sho (Chunk 0)'
type: knowledge_chunk
---

---
chunk_id: 259229bb9d56
source: hash_key.txt
page: 0
title: Values used to calculate the hash in this folder name. # Sho (Chunk 0)
keywords: ['AGP', 'NDK', 'NDK version', 'PROJECT path', 'ABI', 'HASH value', 'CMAKE', 'Ninja']
created: 2026-05-08 01:51:16
tree_path: 6q3s5v3j > Page 0 > Values used to calculate the hash in this folder n
---

# Values used to calculate the hash in this folder name. # Should not depend on the absolute path of the project itself. # - AGP: 8.11.1. # - $NDK is the path to NDK 28.2.13676358. # - $PROJECT is the path to the parent folder of the root Gradle build file. # - $ABI is the ABI to be built with. The specific value doesn't contribute to the value of the hash. # - $HASH is the hash value computed from this text. # - $CMAKE is the path to CMake 3.22.1. # - $NINJA is the path to Ninja. -HC:/Users/ankit/AppData/Local/Pub/Cache/hosted/pub.dev/jni-1.0.0/src -DCMAKE_SYSTEM_NAME=Android -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_SYSTEM_VERSION=21 -DANDROID_PLATFORM=android-21 -DANDROID_ABI=$ABI -DCMAKE_ANDROID_ARCH_ABI=$ABI -DANDROID_NDK=$NDK -DCMAKE_ANDROID_NDK=$NDK -DCMAKE_TOOLCHAIN_FILE=$NDK/build/cmake/android.toolchain.cmake -DCMAKE_MAKE_PROGRAM=$NINJA -DCMAKE_LIBRARY_OUTPUT_DIRECTORY=C:/Users/ankit/Projects/Android/CyborgAI-main/build/jni/intermediates/cxx/Debug/$HASH/obj/$ABI -DCMAKE_RUNTIME_OUTPUT_DIRECTORY=C:/Users/ankit/Projects/Android/CyborgAI-main/build/jni/intermediates/cxx/Debug/$HASH/obj/$ABI -DCMAKE_BUILD_TYPE=Debug -BC:/Users/ankit/AppData/Local/Pub/Cache/hosted/pub.dev/jni-1.0.0/android/.cxx/Debug/$HASH/$ABI -GNinja

### Related Concepts
- [[ABI]]
- [[Ninja]]
- [[NDK]]
- [[AGP]]
- [[PROJECT path]]
- [[CMAKE]]
- [[NDK version]]
- [[HASH value]]
