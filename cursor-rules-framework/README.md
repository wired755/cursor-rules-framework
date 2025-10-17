# Cursor Rules Structure

## Overview
This directory contains organized Cursor rules that separate general operational rules from project-specific requirements. The structure is designed to be reusable across different projects.

## Directory Structure

```
.cursor/rules/
├── general.mdc                    # Core Cursor operational rules
├── frameworks/                    # Framework-specific rules
│   └── django.mdc                 # Django best practices
├── project/                       # Project-specific rules
│   ├── project.mdc                # MWA project context
│   ├── architecture.mdc           # MWA architectural patterns
│   ├── patterns.mdc               # MWA implementation patterns
│   └── testing.mdc                # MWA-specific testing
└── prompts/                       # Cursor prompt protocols
    ├── design.mdc
    ├── plan.mdc
    ├── rca.mdc
    └── simple_fix.mdc
```

## File Descriptions

### General Rules
- **`general.mdc`**: Core Cursor operational rules that apply to any project
  - Critical operational rules
  - Problem-solving guidelines
  - Common problem patterns
  - Development rules
  - Anti-patterns to avoid
  - Emergency stop checklist
  - Response templates

### Framework Rules
- **`frameworks/django.mdc`**: Django-specific best practices
  - Django best practices integration
  - Error handling
  - Security & permissions
  - Performance optimization
  - Testing integration
  - Convention over configuration

### Project Rules
- **`project/project.mdc`**: MWA project context and requirements
  - Project overview
  - Core technologies & patterns
  - Session management
  - Frontend guidelines
  - File organization
  - Documentation requirements
  - Common pitfalls

- **`project/architecture.mdc`**: MWA architectural patterns
  - Architecture guidelines
  - Model conventions
  - Admin interface rules
  - Import/export patterns
  - Architectural decision record

- **`project/patterns.mdc`**: MWA implementation patterns
  - Specific implementation guidelines
  - Code examples
  - MWA-specific anti-patterns
  - Project-specific pitfalls

- **`project/testing.mdc`**: MWA-specific testing requirements
  - Oracle database testing
  - Healthcare compliance testing
  - MWA process flow testing
  - Performance testing

### Prompt Protocols
- **`prompts/`**: Cursor prompt protocols for specific workflows
  - Design protocol
  - Plan protocol
  - Root cause analysis
  - Simple fix protocol

## Usage

### For This Project (MWA)
All rules are automatically loaded by Cursor. The structure provides:
- General operational guidance
- Django-specific best practices
- MWA-specific requirements and patterns

### For Other Projects
To reuse this structure for another project:
1. Copy the directory structure
2. Update `project/` files with project-specific content
3. Keep `general.mdc` and `frameworks/` unchanged
4. Update prompt protocols as needed

## Benefits

### 1. Clear Separation
- **General Rules**: Apply to any Cursor usage
- **Framework Rules**: Apply to specific frameworks
- **Project Rules**: Apply only to the current project

### 2. Reusability
- Structure can be used for any project type
- Easy to migrate to new projects
- Consistent organization across projects

### 3. Maintainability
- Clear boundaries between rule types
- Easy to update specific rule categories
- Modular organization for better management

### 4. Scalability
- Easy to add new frameworks
- Simple to add new project-specific rules
- Clear structure for team collaboration

## Migration from .cursorrules

This structure replaces the monolithic `.cursorrules` file with:
- Better organization
- Clear separation of concerns
- Enhanced functionality with .mdc format
- Improved maintainability
- Reusable structure for other projects
