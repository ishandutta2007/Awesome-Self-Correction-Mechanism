# Copy-on-Write Block Tables

## Overview
Memory optimization strategy sharing KV cache pointers among multiple search paths and only cloning blocks when a path writes a unique token.

## Architecture & Workflow
```mermaid
flowchart TD
    A[Parent KV Cache Block] --> B[Search Branch A (Reads Parent)]
    A --> C[Search Branch B (Reads Parent)]
    B -->|Writes new token| D[Allocate new VRAM Page for A]
    C -->|Reads unchanged| A
```

## Detailed Explanation
Self-correction enables AI agents and reasoning models to dynamically recover from computational or logical dead ends. In the context of **Copy-on-Write Block Tables**, this is achieved by continuously matching output metrics against defined constraints and executing correction paths.

### Core Mechanics
1. **Error Detection:** Verifying output structure using internal checkers or external validation pipelines.
2. **Backtracking:** Adjusting processing targets or memory pointers to pivot away from identified issues.
3. **Refinement:** Incorporating feedback directly into subsequent generation passes to establish a correct output path.

[← Back to README](../README.md)
