# Code Patterns

## Cursor Development Patterns

### Problem-Solving Guidelines

#### 1. Simplicity First Principle
- **Start with the simplest possible solution**: Always begin with the most direct fix
- **Question complexity**: Ask "Is this architectural change actually needed?"
- **YAGNI**: You Aren't Gonna Need It - don't build features you don't currently need
- **2-3 line fixes**: If the problem can be solved in 2-3 lines, do that first
- **Data format issues**: Usually require simple formatting changes, not architectural changes

#### 2. Problem Classification
- **Data Format Issues**: Usually require simple formatting changes, not architectural changes
- **Validation Errors**: Often just data format or field mapping issues
- **UI Issues**: Check templates and context before modifying backend
- **Performance Issues**: Only optimize after identifying actual bottlenecks

#### 3. Solution Validation
Before implementing any solution, ask:
- Can this be solved with a simple data format change?
- Is this actually a data flow problem or just a formatting problem?
- Would a 2-3 line fix work instead of a new function/class?
- Am I over-engineering a simple problem?

#### 4. Code Review Checklist
- [ ] Did I start with the simplest solution?
- [ ] Am I adding complexity that isn't needed?
- [ ] Could this be solved with a few lines instead of new functions?
- [ ] Am I following patterns just for the sake of following patterns?

## Troubleshooting Patterns

### Data Format Issues
- **Symptoms**: Validation errors, "not one of the available choices"
- **Root Cause**: Data sent in wrong format (comma-separated vs individual values)
- **Solution**: Simple data formatting change (2-3 lines)
- **Example**: `fields: selectedFields.join(',')` → proper individual field values

### UI Issues
- **Symptoms**: Missing data, incorrect display
- **Root Cause**: Template context issues, not backend problems
- **Solution**: Check templates first, add context if needed
- **Example**: Missing template variables vs backend logic issues

### Validation Errors
- **Symptoms**: Form validation failures
- **Root Cause**: Usually data format or field mapping
- **Solution**: Check data format before modifying validation logic
- **Example**: Field choices mismatch vs validation rule problems

## Anti-Patterns to Avoid

### Over-Engineering
- Creating new functions for simple data formatting
- Adding architectural layers for 2-3 line fixes
- Following patterns without questioning if they're needed
- Building "future-proof" solutions for current problems

### Assumption-Based Solutions
- Assuming data flow problems without checking format
- Assuming backend issues without checking templates
- Assuming architectural problems without checking simple fixes
- Assuming complexity is needed without trying simple solutions first

## Pre-Solution Validation Questions

1. **Is this actually a data format issue?**
2. **Can this be solved in 2-3 lines?**
3. **Am I over-engineering a simple problem?**
4. **Do I need new functions/classes for this?**
5. **Am I following patterns just because they exist?**
6. **What's the simplest possible solution?**
7. **Have I checked templates before backend?**
8. **Is this complexity actually needed?**

## Common Patterns
[Common patterns used in the codebase]

## Anti-Patterns to Avoid
[Patterns that should be avoided]

## Best Practices
[Best practices for this codebase]

## Code Examples
[Examples of good code patterns]

## Django-Specific Patterns
[Django-specific patterns used in this project]

## Security Patterns
[Security-related patterns and practices]

## Testing Patterns
[Testing patterns and practices]
