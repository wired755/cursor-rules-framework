# Cursor Rules Framework

## Overview

This framework provides structured, consistent AI assistant behavior for software development workflows. It implements research-backed patterns from 100+ successful cursor rules implementations.

## Quick Start

### Core Files (Always Applied)
- **`00-rules.mdc`** - Core permission gates and enforcement
- **`01-general.mdc`** - General operational rules and problem-solving guidelines

### Mode Files (Conditional Loading)
- **`20-rca.mdc`** - Root cause analysis workflow (`@rca.mdc`)
- **`21-plan.mdc`** - Implementation planning workflow (`@plan.mdc`)
- **`22-design.mdc`** - Architectural design workflow (`@design.mdc`)
- **`23-rule.mdc`** - Rule creation workflow (`@rule.mdc`)
- **`24-doc.mdc`** - Documentation workflow (`@doc.mdc`)

### Behavior Files (Context-Specific)
- **`30-planning.mdc`** - Planning behaviors (`@planning.mdc`)
- **`31-troubleshooting.mdc`** - RCA behaviors (`@troubleshooting.mdc`)
- **`32-designing.mdc`** - Design behaviors (`@designing.mdc`)
- **`33-documenting.mdc`** - Documentation behaviors (`@documenting.mdc`)

### Tech Stack Files (Auto-Loaded by File Type)
- **`stack/django.mdc`** - Django patterns (loads for `.py` files)

### Project Context
- **`10-project.mdc`** - Project-specific context (`@project.mdc`)

## Key Features

### 🔒 Permission Gates
- **Standard Approval Phrase**: Only "APPROVE" is accepted
- **Session Isolation**: Fresh permission required for each new request
- **Pre-Action Audit**: Mandatory checklist before any file modifications
- **Permission State Tracking**: NONE → REQUESTED → GRANTED

### 🚦 Workflow Checkpoints
- **Gate Checkpoints**: Integrated at critical workflow steps
- **Mode-Specific Workflows**: Tailored processes for each development task
- **Behavior Integration**: Context-specific guidance within workflows

### 🛡️ Violation Prevention
- **Immediate Halt Protocol**: 5-step acknowledgment for violations
- **Cross-File Enforcement**: Behavior files cannot override gates
- **Accountability System**: Violation tracking and acknowledgment

## Usage Examples

### Basic Workflow
1. User requests task: "Fix the login bug"
2. AI loads appropriate mode: `@rca.mdc`
3. AI follows workflow with gate checkpoints
4. AI presents solution and requests: "Type APPROVE to proceed"
5. User types: "APPROVE"
6. AI implements changes

### Mode Activation
```
@rca.mdc - Root cause analysis
@plan.mdc - Implementation planning  
@design.mdc - Architectural design
@rule.mdc - Create new rules
@doc.mdc - Documentation creation
```

### Behavior Loading
```
@planning.mdc - Planning-specific behaviors
@troubleshooting.mdc - RCA-specific behaviors
@designing.mdc - Design-specific behaviors
@documenting.mdc - Documentation behaviors
```

## File Structure

```
cursor-rules/
├── 00-rules.mdc              # Core gates (always applied)
├── 01-general.mdc            # General rules (always applied)
├── 10-project.mdc            # Project context
├── behaviors/                 # Context-specific behaviors
│   ├── 30-planning.mdc
│   ├── 31-troubleshooting.mdc
│   ├── 32-designing.mdc
│   └── 33-documenting.mdc
├── modes/                    # Workflow definitions
│   ├── 20-rca.mdc
│   ├── 21-plan.mdc
│   ├── 22-design.mdc
│   ├── 23-rule.mdc
│   └── 24-doc.mdc
└── stack/                    # Tech-specific patterns
    └── django.mdc
```

## Research Foundation

This framework is based on analysis of 100+ successful cursor rules implementations, incorporating:

- **Explicit Approval Keywords**: Single standardized confirmation phrase
- **Session-Based Permissions**: No permission carryover between requests
- **Pre-Action Validation**: Mandatory checklists before modifications
- **Checkpoint Pattern**: Superior to state machines for LLM context
- **Centralized Gates**: Single source of truth for enforcement
- **Modular Architecture**: Conditional loading via globs and manual triggers

## Success Metrics

- **Consistency**: Identical gate verification across all modes
- **Enforceability**: No workflow can bypass gates
- **Clarity**: User always knows when "APPROVE" is required
- **Accountability**: Violations trigger immediate acknowledgment
- **Session Isolation**: Permission never carries over between requests
- **Performance**: Maximum 2 always-applied rules for optimal token usage

## Getting Help

- **Gate Issues**: Check `00-rules.mdc` for core permission requirements
- **Workflow Questions**: Reference specific mode files (`20-rca.mdc`, etc.)
- **Behavior Guidance**: See behavior files in `behaviors/` directory
- **Tech Patterns**: Check `stack/` directory for framework-specific rules

---

*This framework follows research-backed best practices for cursor rules implementation, ensuring consistent, secure, and effective AI assistant behavior.*
