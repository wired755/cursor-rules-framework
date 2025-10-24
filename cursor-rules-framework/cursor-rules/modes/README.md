# Cursor Rules Prompts Directory

## Overview
This directory contains `.mdc` files for all Cursor prompt protocols. Each file defines a specific prompt with auto-execution sequences, context loading, and response templates.

## Prompt Files

### Core Prompts
- **`design.mdc`** - @DESIGN protocol for design document creation
- **`plan.mdc`** - @PLAN protocol for implementation planning
- **`plan_review.mdc`** - @PLAN-R protocol for plan feedback and revision
- **`plan_document.mdc`** - @PLAN-D protocol for plan documentation updates
- **`rca.mdc`** - @RCA protocol for root cause analysis
- **`simple_fix.mdc`** - @SIMPLE_FIX protocol for simple problem resolution

### Template Files
- **`templates.mdc`** - Response templates for all prompts
- **`README.md`** - This documentation file

## Usage

### Triggering Prompts
Each prompt is triggered by the `@` symbol followed by the prompt name:
- `@DESIGN <concept/requirement>`
- `@PLAN <design_name>`
- `@PLAN-R <plan_name> <feedback>`
- `@PLAN-D <plan_name> <document>`
- `@RCA <phase> <error>`
- `@SIMPLE_FIX <problem_description>`

### Auto-Execution Features
Each prompt includes:
- **Context Loading**: Automatic loading of relevant context files
- **Execution Sequence**: Step-by-step automated execution
- **Response Templates**: Consistent response formatting
- **Validation Checklists**: Built-in validation steps
- **Stop Points**: Explicit permission requirements

### MWA-Specific Features
All prompts include:
- HIPAA compliance requirements
- Oracle database considerations
- Django best practices within MWA constraints
- Session-based state management patterns
- MWA architectural patterns from app_patterns.md

## File Structure
```
.cursor/rules/prompts/
├── design.mdc              # @DESIGN protocol
├── plan.mdc                # @PLAN protocol
├── plan_review.mdc         # @PLAN-R protocol
├── plan_document.mdc       # @PLAN-D protocol
├── rca.mdc                 # @RCA protocol
├── simple_fix.mdc         # @SIMPLE_FIX protocol
├── templates.mdc           # Response templates
└── README.md               # This documentation
```

## Benefits
- **Modular Organization**: Each prompt is self-contained
- **Enhanced Functionality**: .mdc format provides advanced features
- **Consistent Execution**: Standardized protocols across all prompts
- **Easy Maintenance**: Individual prompt updates without affecting others
- **Clear Documentation**: Each prompt is well-documented and validated
