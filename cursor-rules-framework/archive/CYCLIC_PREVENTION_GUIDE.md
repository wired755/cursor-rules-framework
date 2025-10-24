# Preventing Cyclic Changes in Cursor

## The Problem
Cursor sometimes makes changes that create cycles:
1. **Change A** → Breaks B
2. **Fix B** → Breaks A  
3. **Revert A** → Need the original change
4. **Repeat cycle**

## Your Framework's Existing Solutions

### 1. Permission-Based Workflow
Your `🚨 CRITICAL RULE 🚨` already prevents unauthorized changes:
- **STOP** - Don't make changes without permission
- **ANALYZE** - Provide root cause analysis first
- **EXPLAIN** - Describe the solution
- **WAIT** - Ask for explicit permission
- **CONFIRM** - Only proceed after user says "Yes"

### 2. Impact Analysis (from RCA mode)
Your RCA workflow includes:
- **Dependency Check**: What other code depends on this change
- **Side Effect Analysis**: Will this fix break other functionality
- **Related Feature Testing**: Check similar patterns that might be affected
- **Integration Validation**: Ensure fix works with existing code

### 3. Simplicity First Principle
Your framework forces simple solutions:
- **2-3 line fixes** before architectural changes
- **Data format issues** before complex logic
- **Template checks** before backend changes

## Additional Anti-Cyclic Strategies

### 1. Use the Anti-Cyclic Rule
Add `@anti-cyclic.mdc` to your prompts when making changes:
```
@anti-cyclic.mdc + @rca.mdc
```

### 2. Pre-Change Analysis
Before ANY change, ask:
- **What will this change break?**
- **What other changes will be needed?**
- **Will this require reverting previous changes?**
- **Are we fixing a symptom or the root cause?**

### 3. Change Validation Protocol
- **Check Dependencies**: What code depends on what you're changing
- **Verify Side Effects**: Will this change break other functionality
- **Test Integration**: Ensure change works with existing code
- **Document Impact**: Note what might be affected

## Common Cyclic Patterns to Avoid

### 1. The "Fix and Break" Cycle
- **Pattern**: Fix A → Breaks B → Fix B → Breaks A
- **Prevention**: Analyze all dependencies before making changes
- **Solution**: Fix both A and B together, or find a different approach

### 2. The "Feature Toggle" Cycle
- **Pattern**: Add feature → Breaks existing → Remove feature → Need feature
- **Prevention**: Test integration before adding features
- **Solution**: Implement feature properly from the start

### 3. The "Optimization" Cycle
- **Pattern**: Optimize → Breaks tests → Fix tests → Breaks optimization
- **Prevention**: Ensure optimization doesn't break functionality
- **Solution**: Optimize and update tests together

### 4. The "Refactor" Cycle
- **Pattern**: Refactor → Breaks integration → Revert → Need refactor
- **Prevention**: Plan refactoring carefully with integration testing
- **Solution**: Refactor incrementally with proper testing

## Implementation Strategy

### 1. Update Your Prompts
Add anti-cyclic awareness to your existing prompts:

**For RCA mode:**
```
@rca.mdc + @anti-cyclic.mdc
```

**For Design mode:**
```
@design.mdc + @anti-cyclic.mdc
```

**For Plan mode:**
```
@plan.mdc + @anti-cyclic.mdc
```

### 2. Enhanced Change Protocol
1. **Analyze Impact**: What will this change affect?
2. **Check Dependencies**: What depends on what you're changing?
3. **Plan Mitigation**: How to handle potential issues?
4. **Test Incrementally**: Verify each change before proceeding
5. **Document Changes**: Keep track of what was changed and why

### 3. Emergency Stop Conditions
Stop immediately if you detect:
- **Circular Dependencies**: Change A requires change B, which requires change A
- **Cascading Failures**: One change breaks multiple other things
- **Requirement Conflicts**: Change conflicts with existing requirements
- **Architecture Violations**: Change violates established patterns

## Best Practices

### 1. Root Cause First
- **Fix the real problem**: Don't just address symptoms
- **Understand the system**: Know how components interact
- **Question assumptions**: Verify what you think you know
- **Start simple**: Try the simplest solution first

### 2. Minimal Impact Changes
- **Change only what's necessary**: Don't modify unrelated code
- **Preserve existing functionality**: Don't break what works
- **Test incrementally**: Verify each change before proceeding
- **Document everything**: Keep track of what was changed

### 3. Dependency Awareness
- **Map the system**: Understand how components depend on each other
- **Check before changing**: Verify what depends on what you're changing
- **Plan for side effects**: Anticipate what might break
- **Have a rollback plan**: Know how to undo changes if needed

### 4. Integration Testing
- **Test the whole system**: Don't just test individual components
- **Verify end-to-end**: Ensure the change works in context
- **Check performance**: Ensure changes don't degrade performance
- **Validate assumptions**: Confirm the change works as expected

## Success Metrics

### Quantitative Metrics
- **Zero cyclic changes**: No changes that require reverting previous changes
- **Minimal side effects**: Changes don't break other functionality
- **Fast rollback**: Can quickly undo changes if needed
- **Stable system**: System remains functional throughout changes

### Qualitative Metrics
- **Clear dependencies**: Understand how components interact
- **Predictable behavior**: Changes have expected results
- **Maintainable code**: Changes don't make code harder to maintain
- **User satisfaction**: Changes solve problems without creating new ones

## Integration with Your Framework

Your existing framework already provides excellent foundations:

1. **Permission-based workflow** prevents unauthorized changes
2. **Impact analysis** in RCA mode checks dependencies
3. **Simplicity first** prevents over-engineering
4. **Template structure** ensures consistent behavior

The anti-cyclic rule (`@anti-cyclic.mdc`) adds:
- **Cyclic change detection** patterns
- **Pre-change analysis** requirements
- **Emergency stop conditions** for problematic changes
- **Integration testing** protocols

## Conclusion

Your framework already has strong anti-cyclic foundations. The additional `@anti-cyclic.mdc` rule provides:
- **Explicit cyclic change detection**
- **Pre-change impact analysis**
- **Emergency stop conditions**
- **Integration testing protocols**

This combination ensures Cursor makes thoughtful, well-analyzed changes that don't create cycles or require reverting previous work.
