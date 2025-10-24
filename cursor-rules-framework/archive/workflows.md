# Development Workflows
**Definition**: Broader development processes and methodologies that provide context and guidance. These reference protocols when appropriate and represent ongoing development approaches.

## Cursor Development Workflows

### Feature Development Workflow
1. **Analyze Requirements**: Review design documents and requirements
2. **Check Existing Patterns**: Look for similar implementations in codebase
3. **Follow MWA Patterns**: Use established mixin and resource patterns from `docs/context/app_patterns.md` (see MWA Architecture Guidelines section)
4. **Implement Security**: Apply HIPAA compliance and PII protection
5. **Test Implementation**: Verify functionality and security
6. **Update Documentation**: Maintain project documentation

### Bug Fixing Workflow
1. **Identify Root Cause**: Use RCA macro protocol (see `.cursorrules` CURSOR MACRO PROTOCOLS)
2. **Check Templates First**: Verify template context before backend changes
3. **Apply Simple Fix**: Start with 2-3 line solutions (use SIMPLE_FIX protocol if needed)
4. **Test Fix**: Verify solution works
5. **Update Documentation**: Document changes

### Code Review Workflow
1. **Review for Patterns**: Ensure code follows MWA patterns
2. **Check Security**: Verify HIPAA compliance and PII protection
3. **Validate Architecture**: Ensure mixin and resource patterns
4. **Test Coverage**: Verify adequate testing
5. **Documentation**: Ensure documentation is updated

### Testing Workflow
1. **Unit Tests**: Test individual components
2. **Integration Tests**: Test complete workflows
3. **Security Tests**: Test HIPAA compliance and PII protection
4. **Performance Tests**: Test with large datasets
5. **Documentation**: Update test documentation

### Documentation Workflow
1. **Follow Templates**: Use established document templates
2. **Apply Standards**: Follow documentation workflow rules
3. **Update Context**: Keep context files current
4. **Review Content**: Ensure accuracy and completeness
5. **Maintain Consistency**: Follow established patterns

## Development Rules
[Development workflow rules]

## Code Review Workflows
[Code review workflow rules]

## Testing Workflows
[Testing workflow rules]

## Deployment Workflows
[Deployment workflow rules]

## Documentation Workflows
[Documentation workflow rules]

## Security Workflows
[Security workflow rules]

## Maintenance Workflows
[Maintenance workflow rules]

## Emergency Workflows
[Emergency workflow rules]
