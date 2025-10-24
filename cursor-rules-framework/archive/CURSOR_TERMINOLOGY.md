# Cursor Framework Terminology

## Clear Distinctions for Cursor Understanding

### PROTOCOLS
**Definition**: Specific, executable procedures triggered by user commands
**Location**: `.cursorrules` → CURSOR MACRO PROTOCOLS section
**Characteristics**:
- Atomic operations with clear start/stop points
- Triggered by specific user commands (DESIGN, PLAN, RCA, etc.)
- Include validation checklists
- Have explicit permission requirements
- Are step-by-step procedures

**Examples**:
- `DESIGN <concept>` - Creates design documents
- `PLAN <design_name>` - Creates implementation plans
- `RCA <phase> <error>` - Root cause analysis
- `SIMPLE_FIX <problem>` - Simple problem resolution

### WORKFLOWS
**Definition**: Broader development processes and methodologies
**Location**: `docs/context/workflows.md`
**Characteristics**:
- General approaches to development tasks
- Provide context and guidance
- May reference protocols when appropriate
- Represent ongoing development processes
- Are methodological approaches

**Examples**:
- Feature Development Workflow
- Bug Fixing Workflow
- Code Review Workflow
- Testing Workflow
- Documentation Workflow

## How They Work Together

1. **Workflows** provide the overall approach and context
2. **Protocols** are specific procedures that can be invoked within workflows
3. **Workflows** may reference protocols (e.g., "Use RCA macro protocol")
4. **Protocols** are triggered by user commands
5. **Workflows** guide general development practices

## Usage Guidelines for Cursor

- **When user gives specific command** (DESIGN, PLAN, etc.) → Use PROTOCOL
- **When providing general development guidance** → Reference WORKFLOW
- **When troubleshooting** → Use RCA PROTOCOL within Bug Fixing WORKFLOW
- **When creating documents** → Use DESIGN/PLAN PROTOCOLS
- **When fixing simple issues** → Use SIMPLE_FIX PROTOCOL

## File References

- **Protocols**: `.cursorrules` → CURSOR MACRO PROTOCOLS
- **Workflows**: `docs/context/workflows.md`
- **Application Patterns**: `docs/context/app_patterns.md`
- **Development Patterns**: `docs/context/patterns.md`
