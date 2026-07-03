# Intrinsic Self-Correction (Self-Critique / Logit Shift)

## Overview
Internal parameter updates or token-level distribution adjustments where the model shifts probability outputs to self-correct during generation.

## Architecture & Workflow
```mermaid
flowchart LR
    A[Forward Pass Logits] --> B[Internal Self-Critique Model/Head]
    B --> C[Adjust Token Probabilities / Shift Logits]
    C --> D[Emit Corrected Next Token]
```

## Detailed Explanation
Self-correction enables AI agents and reasoning models to dynamically recover from computational or logical dead ends. In the context of **Intrinsic Self-Correction (Self-Critique / Logit Shift)**, this is achieved by continuously matching output metrics against defined constraints and executing correction paths.

### Core Mechanics
1. **Error Detection:** Verifying output structure using internal checkers or external validation pipelines.
2. **Backtracking:** Adjusting processing targets or memory pointers to pivot away from identified issues.
3. **Refinement:** Incorporating feedback directly into subsequent generation passes to establish a correct output path.

[← Back to README](../README.md)
