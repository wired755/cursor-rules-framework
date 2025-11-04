# Top 10 Best Practices for Writing Cursor Rules

Based on comprehensive review of the Cursor Rules Framework repository, including archive files and implementation patterns.

---

## 1. **Simplicity First - Start with the Simplest Solution**

**Principle**: Always begin with the simplest solution that works before adding complexity.

**Implementation**:
- Start with 2-3 line fixes before architectural changes
- Question whether additional complexity is actually needed
- YAGNI (You Aren't Gonna Need It) - don't build features you don't currently need
- Check data format issues before assuming architectural problems
- Verify template context before modifying backend logic

**Why it matters**: Over-engineering is the most common mistake. The framework's own migration reduced from 15+ files to 5 files while maintaining all essential functionality.

**Evidence**: Found in `GENERAL_BEST_PRACTICES.md`, `patterns.md`, `troubleshooting.mdc`, and `01-general.mdc`.

---

## 2. **Explicit Permission Gates - Never Make Changes Without Consent**

**Principle**: Require explicit user permission for ALL file modifications using a standardized approval phrase.

**Implementation**:
- Use a single standard approval phrase: **"APPROVE"** (case-insensitive)
- Follow the mandatory 5-step protocol: STOP → ANALYZE → EXPLAIN → WAIT → CONFIRM
- Implement session boundary enforcement (no permission carryover between requests)
- Track permission state: NONE → REQUESTED → GRANTED
- Complete pre-action audit checklist before any file modification

**Why it matters**: Prevents unauthorized changes and ensures user control. The framework includes sophisticated permission state tracking and accountability systems.

**Evidence**: Found in `00-rules.mdc`, `rules.mdc`, `NO_CHANGES_FIRST.mdc`, and `GENERAL_BEST_PRACTICES.md`.

---

## 3. **Limit Universal Rules - Maximum 1-3 `alwaysApply: true` Rules**

**Principle**: Keep universal rules to an absolute minimum (1-3 maximum) to optimize performance and prevent conflicts.

**Implementation**:
- Use `alwaysApply: true` sparingly - only for truly universal rules
- Prefer context-specific rules loaded via `@filename.mdc` syntax
- Place universal rules in a single file (e.g., `00-rules.mdc`)
- Each `alwaysApply` rule consumes tokens on every request
- Research shows 3-5 maximum across entire framework, but 1-3 is ideal

**Why it matters**: Too many universal rules create contradictory instructions, degrade performance, and dilute important rules. The framework evolved from allowing 3-5 to recommending 1-3.

**Evidence**: Found in `GENERAL_BEST_PRACTICES.md`, `framework_design.mdc`, and `MIGRATION_GUIDE.md`.

---

## 4. **Single Responsibility Per File - One Purpose Per Rule File**

**Principle**: Each rule file should have a single, well-defined responsibility.

**Implementation**:
- Mode files (workflows): One workflow per file (e.g., `rca.mdc` for RCA workflow)
- Behavior files: One set of behaviors per file (e.g., `troubleshooting.mdc` for troubleshooting behaviors)
- Stack files: One technology per file (e.g., `django.mdc` for Django patterns)
- Universal rules: All enforcement in one file (`00-rules.mdc`)
- Keep files under 100 lines (ideally 50-80 lines)

**Why it matters**: Maintainability, clarity, and performance. Single responsibility makes files easier to understand, modify, and load selectively.

**Evidence**: Found in `GENERAL_BEST_PRACTICES.md`, `framework_design.mdc`, and `MIGRATION_GUIDE.md`.

---

## 5. **Separate Behaviors from Workflows - Use Modular Architecture**

**Principle**: Separate behavioral principles (how to think) from workflow processes (what to do).

**Implementation**:
- **Behaviors** (`behaviors/*.mdc`): Reusable principles that can be shared across modes
- **Workflows** (`modes/*.mdc`): Step-by-step processes for specific tasks
- Behaviors cannot override core permission gates from universal rules
- Mode files reference behaviors, don't duplicate them
- Technology patterns in separate `stack/` directory

**Why it matters**: Enables reusability, maintainability, and clear separation of concerns. Change behavior once, affects all relevant workflows.

**Evidence**: Found in `GENERAL_BEST_PRACTICES.md`, `framework_design.mdc`, and `RULES.md`.

---

## 6. **Use Direct File Tagging - `@filename.mdc` Syntax**

**Principle**: Use direct file references instead of complex context loading systems.

**Implementation**:
- Use `@filename.mdc` syntax (e.g., `@rca.mdc`, `@plan.mdc`)
- Avoid complex auto-execution sequences or prompt resolution systems
- Load maximum 1-2 files per prompt to avoid context overload
- Make file names descriptive and clear
- No ambiguity about which files are loaded

**Why it matters**: Simplicity, performance, and predictability. Direct references eliminate ambiguity and reduce processing overhead.

**Evidence**: Found in `framework_design.mdc`, `MIGRATION_GUIDE.md`, and `RULES.md`.

---

## 7. **Implement Session Boundary Enforcement - No Permission Carryover**

**Principle**: Each new user request requires fresh explicit permission; previous permissions do not apply.

**Implementation**:
- Reset permission state to NONE at start of each new request
- Explicitly state "This is a NEW request requiring fresh permission"
- Do not assume permission from previous requests
- Track permission state transitions explicitly
- Document permission source for each specific action

**Why it matters**: Prevents permission assumption errors and ensures user control over every action. Critical for safety and accountability.

**Evidence**: Found in `00-rules.mdc`, `rules.mdc`, `GENERAL_BEST_PRACTICES.md`, and mode files.

---

## 8. **Include Pre-Action Audit Checklists - Verify Before Acting**

**Principle**: Complete a mandatory checklist before any file modification to ensure rule compliance.

**Implementation**:
- Verify `rules.mdc` is loaded
- Confirm permission gates are understood
- Check for explicit "APPROVE" from user
- Quote exact user statement granting permission
- Verify permission state is GRANTED
- Confirm this is a new request (not carrying over permission)

**Why it matters**: Prevents rule violations and ensures accountability. The framework includes sophisticated compliance validation mechanisms.

**Evidence**: Found in `00-rules.mdc`, `rules.mdc`, mode files, and `GENERAL_BEST_PRACTICES.md`.

---

## 9. **Research-Driven Design - Base Rules on Proven Patterns**

**Principle**: Base rule design decisions on analysis of successful implementations rather than theoretical approaches.

**Implementation**:
- Follow patterns from 50+ real-world cursor rules implementations
- Test incrementally and measure effectiveness
- Avoid theoretical approaches without practical validation
- Use proven patterns (e.g., checkpoint pattern superior to state machines for LLM context)
- Iterate based on actual usage patterns

**Why it matters**: Practical validation ensures rules actually work. The framework's evolution from 15+ files to 5 files came from analyzing what actually worked in practice.

**Evidence**: Found in `GENERAL_BEST_PRACTICES.md`, `framework_design.mdc`, and `RULES.md`.

---

## 10. **Centralized Enforcement - Single Source of Truth for Core Rules**

**Principle**: Place all enforcement mechanisms in one universal rules file; other files reference, don't duplicate.

**Implementation**:
- Universal rules file (`00-rules.mdc`) contains all enforcement mechanisms
- Mode files reference core rules, don't duplicate them
- Behavior files cannot override permission gates from universal rules
- Gate verification templates standardized across all mode files
- No duplication of enforcement logic

**Why it matters**: Maintainability and consistency. Update enforcement once, applies everywhere. Prevents rule conflicts and inconsistencies.

**Evidence**: Found in `GENERAL_BEST_PRACTICES.md`, `framework_design.mdc`, behavior files (which explicitly state they cannot override gates), and mode files.

---

## Additional Critical Patterns

### File Organization
- Use numbered prefixes for organization: `00-rules.mdc`, `01-general.mdc`, `10-project.mdc`, `20-XX.mdc` (modes), `30-XX.mdc` (behaviors)
- Keep files in appropriate directories: `modes/`, `behaviors/`, `stack/`

### Avoid Anti-Patterns
- **Over-engineering**: Complex hierarchical systems with multiple layers
- **Meta-frameworks**: Creating frameworks for frameworks
- **Circular references**: Complex interdependencies
- **Permission lying**: AI claiming permission without explicit confirmation
- **Rule skipping**: Bypassing mandatory workflow steps

### Performance Optimization
- Limit total file count: 8-12 files per project (evolved from 5-7)
- Optimize token usage through selective file loading
- Maximum 1-2 files loaded per prompt
- Keep individual files to 50-120 lines (ideally 50-80)

---

## Summary

These 10 best practices form the foundation of effective Cursor Rules:

1. **Simplicity First** - Start simple, add complexity only when needed
2. **Explicit Permission Gates** - Never make changes without "APPROVE"
3. **Limit Universal Rules** - Maximum 1-3 `alwaysApply: true` rules
4. **Single Responsibility** - One purpose per file
5. **Separate Behaviors from Workflows** - Modular architecture
6. **Direct File Tagging** - Use `@filename.mdc` syntax
7. **Session Boundary Enforcement** - No permission carryover
8. **Pre-Action Audit Checklists** - Verify before acting
9. **Research-Driven Design** - Base on proven patterns
10. **Centralized Enforcement** - Single source of truth

These practices are derived from analysis of 100+ successful cursor rules implementations and validated through the framework's own evolution and migration experiences.

