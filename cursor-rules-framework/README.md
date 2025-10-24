# Cursor Rules Framework

A simplified, focused framework for Cursor AI assistant rules that follows the "Simplicity First" principle.

## Overview

The Cursor Rules Framework provides a modular, context-specific approach to organizing AI assistant rules. It separates universal rules from context-specific behaviors, optimizing for performance and maintainability while following research-backed patterns from 50+ successful implementations.

## Installation

### Copy Framework Files
Copy the `/cursor-rules/` directory to your project's `.cursor/` directory:

```
.cursor/
├── rules/
│   ├── rules.mdc              # Universal rules (3-5 alwaysApply max)
│   ├── project.mdc            # Project-specific context
│   ├── modes/
│   │   ├── rca.mdc            # RCA workflow
│   │   ├── design.mdc         # Design workflow
│   │   ├── plan.mdc           # Planning workflow
│   │   └── doc.mdc            # Documentation workflow
│   ├── behaviors/
│   │   ├── troubleshooting.mdc  # Troubleshooting behaviors
│   │   ├── designing.mdc         # Design behaviors
│   │   ├── planning.mdc          # Planning behaviors
│   │   └── documenting.mdc       # Documentation behaviors
│   └── tech/
│       └── django.mdc         # Technology-specific rules
```

### Cursor Setup
- Ensure Cursor is configured to read `.mdc` files
- Verify `.cursor/` directory is in your project root
- Test with `@rules.mdc` to confirm framework is loaded

## Quick Start

### Basic Usage
```bash
# Load universal rules
@rules.mdc

# Load specific workflow
@plan.mdc

# Load with behaviors
@rca.mdc @troubleshooting.mdc
```

### Expected Workflow
1. **Write**: Define your requirements
2. **Analyze**: AI analyzes and explains proposed solution
3. **Confirm**: AI asks for explicit permission with specific confirmation
4. **Validate**: AI verifies rule compliance before proceeding
5. **Implement**: Only after explicit "Yes" confirmation and compliance validation

### Rule Compliance System
The framework includes mandatory enforcement mechanisms:
- **Permission Gates**: Explicit permission required for all file modifications
- **Compliance Validation**: Pre-action rule compliance verification
- **Accountability**: Violation tracking and acknowledgment
- **No Override**: Rules cannot be bypassed by user requests

## Usage Guide

### Defining Project Context
Create `project.mdc` with your project-specific information:
```mdc
---
description: "Project-specific context and patterns"
---
# Project Context
- Technology stack: Django + Oracle + Terraform
- Architecture patterns: MVC, Repository pattern
- Coding standards: PEP 8, Django conventions
```

### Creating New Rules

#### Mode Rules (Workflows)
Create in `/modes/` directory:
```mdc
---
description: "Your custom workflow"
applyWhen: ["@your-mode.mdc"]
---
# Your Mode Workflow
## Workflow Steps
1. Step 1
2. Step 2
3. Step 3
```

#### Behavior Rules (Principles)
Create in `/behaviors/` directory:
```mdc
---
description: "Your custom behaviors"
applyWhen: ["@your-behaviors.mdc"]
---
# Your Behaviors
## Principles
- Principle 1
- Principle 2
```

#### Tech Rules (Technology-Specific)
Create in `/tech/` directory:
```mdc
---
description: "Your technology patterns"
applyWhen: ["@your-tech.mdc"]
---
# Your Technology Rules
## Patterns
- Pattern 1
- Pattern 2
```

### Rule Authoring Checklist
- [ ] Single responsibility per file
- [ ] Clear description in frontmatter
- [ ] Appropriate `applyWhen` or `alwaysApply` settings
- [ ] No more than 3-5 `alwaysApply: true` rules total
- [ ] Context-specific behaviors in `/behaviors/`
- [ ] Workflows in `/modes/`
- [ ] Tech-specific rules in `/tech/`
- [ ] Reference core rules instead of duplicating them
- [ ] Include enforcement mechanisms for critical rules
- [ ] Ensure accountability measures are in place

### Enforcement Architecture
The framework follows a single source of truth approach:
- **Core Rules**: All enforcement mechanisms in `rules.mdc`
- **Mode Files**: Reference core rules, don't duplicate them
- **Behavior Files**: Reference core rules, don't duplicate them
- **No Duplication**: Maintain consistency across all files
- **Centralized Control**: One place to update enforcement logic

### Naming Conventions
- **Files**: Use kebab-case (e.g., `user-profile.mdc`)
- **Modes**: Descriptive workflow names (e.g., `rca.mdc`, `design.mdc`)
- **Behaviors**: Context-specific names (e.g., `rca-behaviors.mdc`)
- **Tech**: Technology names (e.g., `django.mdc`, `react.mdc`)

## Best Practices

### For Using the Framework
- Start with `@rules.mdc` for universal rules
- Use specific mode files for workflows
- Reference behavior files when needed
- Keep project context in `project.mdc`

### For Writing Rules
- Follow the "Simplicity First" principle
- Write clear, actionable instructions
- Provide examples and anti-examples
- Test each rule individually
- Keep files under 100 lines

## Troubleshooting

### Common Issues

#### Rules Not Triggering
- Check file location in correct directory
- Verify frontmatter syntax
- Ensure `applyWhen` conditions are met
- Test with `@filename.mdc` directly

#### Performance Issues
- Limit `alwaysApply: true` rules to 3-5 maximum
- Use context-specific rules instead of universal ones
- Check for rule conflicts

#### Validation
```bash
# Test universal rules
@rules.mdc

# Test specific mode
@plan.mdc

# Test with behaviors
@rca.mdc @troubleshooting.mdc
```

## Contributing

For framework design decisions and implementation details, see `framework_design.mdc`.

To propose new rule types or workflows:
1. Create issue with use case
2. Provide example implementation
3. Reference framework design principles
4. Include performance impact analysis