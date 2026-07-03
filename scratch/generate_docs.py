import os

details_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Self-Correction-Mechanism\details"
os.makedirs(details_dir, exist_ok=True)

concepts = [
    {
        "id": "human_in_the_loop_steering",
        "title": "Human-in-the-Loop Steering",
        "desc": "Traditional conversational steering where humans manually audit and guide error correction in a multi-turn chat window.",
        "diagram": """flowchart LR
    A[LLM Outputs Code/Text] --> B[Human Audits Output]
    B -->|Finds Error| C[Human Sends Corrective Prompt]
    C --> A
    B -->|No Error| D[Output Finalized]"""
    },
    {
        "id": "prompt_based_critique",
        "title": "Prompt-Based Critique (Self-Refine)",
        "desc": "An external programmatic wrapper directing a single LLM to generate, critique, and refine its own output via specialized prompt sequences.",
        "diagram": """flowchart TD
    A[Generate Initial Draft] --> B[Generate Critique Prompt]
    B --> C[Evaluate Draft for Errors]
    C --> D[Generate Refined Output Prompt]
    D --> E[Rewrite and Refine Output]"""
    },
    {
        "id": "native_rl_thinking",
        "title": "Native Reinforcement-Learned Thinking (o1/R1)",
        "desc": "Models trained via large-scale RL to natively produce internal thinking traces, allowing them to search, backtrack, and correct reasoning errors at test-time.",
        "diagram": """flowchart TD
    A[Input Prompt] --> B[Generate Thought Token Stream]
    B --> C{Evaluate Intermediate Logic}
    C -->|Error Detected| D[Backtrack & Try Alternative Path]
    C -->|Logic Correct| E[Continue Reasoning Trace]
    E --> F[Generate Final Output Tokens]
    D --> B"""
    },
    {
        "id": "intrinsic_self_correction",
        "title": "Intrinsic Self-Correction (Self-Critique / Logit Shift)",
        "desc": "Internal parameter updates or token-level distribution adjustments where the model shifts probability outputs to self-correct during generation.",
        "diagram": """flowchart LR
    A[Forward Pass Logits] --> B[Internal Self-Critique Model/Head]
    B --> C[Adjust Token Probabilities / Shift Logits]
    C --> D[Emit Corrected Next Token]"""
    },
    {
        "id": "extrinsic_programmatic_self_correction",
        "title": "Extrinsic Programmatic Self-Correction (Compiler-in-the-Loop)",
        "desc": "Hardcoded environments like Python sandboxes or theorem provers executing model code and returning compilation traces directly back to the context window.",
        "diagram": """flowchart TD
    A[LLM Generates Code] --> B[Execute in Sandboxed Container]
    B --> C{Execution Status}
    C -->|Success| D[Finalize Code]
    C -->|Failure / Crash| E[Feed Stack Trace to LLM Context]
    E --> A"""
    },
    {
        "id": "reward_model_guided_correction",
        "title": "Reward-Model Guided Correction (PRM Steering)",
        "desc": "Secondary process-supervised reward models auditing each reasoning token block and halting generation if the confidence score drops.",
        "diagram": """flowchart TD
    A[Model Generates Step N] --> B[PRM Evaluates Step N]
    B --> C{Score > Threshold?}
    C -->|Yes| D[Proceed to Step N+1]
    C -->|No| E[Discard Step N and Re-generate]"""
    },
    {
        "id": "token_level_backtracking",
        "title": "Token-Level Backtracking Vectors",
        "desc": "Dynamic KV cache manipulation allowing the inference engine to prune incorrect branches and restart generation from a previous logical node.",
        "diagram": """flowchart TD
    A[Inference KV Cache] --> B[Identify Bad Logic Step]
    B --> C[Rewind KV Cache Pointer to Branch Point]
    C --> D[Generate Alternate Token Sequence]"""
    },
    {
        "id": "copy_on_write_block_tables",
        "title": "Copy-on-Write Block Tables",
        "desc": "Memory optimization strategy sharing KV cache pointers among multiple search paths and only cloning blocks when a path writes a unique token.",
        "diagram": """flowchart TD
    A[Parent KV Cache Block] --> B[Search Branch A (Reads Parent)]
    A --> C[Search Branch B (Reads Parent)]
    B -->|Writes new token| D[Allocate new VRAM Page for A]
    C -->|Reads unchanged| A"""
    },
    {
        "id": "token_inflation_vram_crisis",
        "title": "Token Inflation and VRAM Cache Satiation Crisis",
        "desc": "The engineering challenge of rapidly depleting GPU memory due to massive context requirements of verbose internal reasoning traces.",
        "diagram": """flowchart TD
    A[Verbose Thinking Traces] --> B[Massive KV Cache Accumulation]
    B --> C[GPU VRAM Satiation]
    C --> D[System Out-of-Memory / Latency Spikes]
    D --> E[MLA & PagedAttention Mitigation]"""
    },
    {
        "id": "infinite_reasoning_loops",
        "title": "The High Cost of Infinite Reasoning Trapping",
        "desc": "A failure mode where the LLM repeats identical incorrect correction cycles indefinitely, consuming test-time compute budget without making progress.",
        "diagram": """flowchart TD
    A[Generate Solution] --> B[Compiler Errors out]
    B --> C[Parse Error]
    C --> D[Regenerate Identical Failure]
    D --> B
    D -->|Step Cap reached| E[Scaffolding Aborts / Reroutes]"""
    },
    {
        "id": "autonomous_swe_solvers",
        "title": "Autonomous Software Engineering & Sandbox Maintenance",
        "desc": "Deploying self-correcting agents to clone codebases, run test suites, inspect system logs, and iteratively refactor until all tests pass.",
        "diagram": """flowchart TD
    A[Clone Repo] --> B[Identify Issue]
    B --> C[Edit Code]
    C --> D[Run Test Suite]
    D --> E{Tests Pass?}
    E -->|No| F[Analyze Log & Refactor]
    F --> C
    E -->|Yes| G[Git Commit / PR]"""
    },
    {
        "id": "financial_auditing_sql_generation",
        "title": "Automated Financial Auditing & SQL Query Generation",
        "desc": "Using self-correction to handle complex SQL joins and schema structures, adjusting queries dynamically when databases return optimization or syntax errors.",
        "diagram": """flowchart TD
    A[Generate Complex SQL Join] --> B[Database Engine Execution]
    B --> C{Execution Result}
    C -->|Optimization/Syntax Error| D[Analyze DB Trace & Schema]
    D --> E[Re-map Join Macro]
    E --> B
    C -->|Data Ready| F[Format Audit Report]"""
    },
    {
        "id": "aerospace_chip_verification",
        "title": "Mission-Critical Aerospace and Chip Hardware Verification",
        "desc": "Generating formal specifications and proofs (Verilog assertions, Lean 4) where automated provers provide compile feedback for syntax correction.",
        "diagram": """flowchart TD
    A[Translate Requirements to assertions/proof] --> B[Lean 4 / Verilog Compiler]
    B --> C{Proof Status}
    C -->|Proof Incomplete / Error| D[Extract Syntax & Rule Mappings]
    D --> E[Iteratively Refine Proof]
    E --> B
    C -->|Compiled Flawlessly| F[Verified System Assurance]"""
    }
]

for idx, c in enumerate(concepts):
    filename = f"{c['id']}.md"
    filepath = os.path.join(details_dir, filename)
    
    content = f"""# {c['title']}

## Overview
{c['desc']}

## Architecture & Workflow
```mermaid
{c['diagram']}
```

## Detailed Explanation
Self-correction enables AI agents and reasoning models to dynamically recover from computational or logical dead ends. In the context of **{c['title']}**, this is achieved by continuously matching output metrics against defined constraints and executing correction paths.

### Core Mechanics
1. **Error Detection:** Verifying output structure using internal checkers or external validation pipelines.
2. **Backtracking:** Adjusting processing targets or memory pointers to pivot away from identified issues.
3. **Refinement:** Incorporating feedback directly into subsequent generation passes to establish a correct output path.

[← Back to README](../README.md)
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Generated 13 detail files successfully.")
