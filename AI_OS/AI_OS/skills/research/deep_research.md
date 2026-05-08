# Deep Research Skill

## Overview
Conducts comprehensive research across the knowledge base using vector similarity search, graph traversal, and multi-hop reasoning.

## Capabilities
- Semantic search across all vault content
- Graph-based relationship discovery
- Multi-document synthesis
- Confidence scoring and provenance tracking

## Parameters
- query: Research question or topic
- depth: Research depth (1-5, default: 3)
- sources: Maximum sources to consider (default: 10)

## Execution Flow
1. Vector search for initial relevant chunks
2. Graph traversal for related concepts
3. Content synthesis with confidence scoring
4. Result formatting with source citations

## Dependencies
- Vector index for semantic search
- Knowledge graph for relationship traversal
- Chunk registry for content access

## Metrics
- Execution count: 45
- Success rate: 92%
- Average latency: 2340ms