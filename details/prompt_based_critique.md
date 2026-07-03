# Prompt-Based Critique (Self-Refine)

## Overview
An external programmatic wrapper directing a single LLM to generate, critique, and refine its own output via specialized prompt sequences.

## Architecture & Workflow
```mermaid
flowchart TD
    A[Generate Initial Draft] --> B[Generate Critique Prompt]
    B --> C[Evaluate Draft for Errors]
    C --> D[Generate Refined Output Prompt]
    D --> E[Rewrite and Refine Output]
```

## Detailed Explanation
Self-correction enables AI agents and reasoning models to dynamically recover from computational or logical dead ends. In the context of **Prompt-Based Critique (Self-Refine)**, this is achieved by continuously matching output metrics against defined constraints and executing correction paths.

### Core Mechanics
1. **Error Detection:** Verifying output structure using internal checkers or external validation pipelines.
2. **Backtracking:** Adjusting processing targets or memory pointers to pivot away from identified issues.
3. **Refinement:** Incorporating feedback directly into subsequent generation passes to establish a correct output path.

[← Back to README](../README.md)
