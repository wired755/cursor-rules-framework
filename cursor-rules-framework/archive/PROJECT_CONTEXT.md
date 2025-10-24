# MWA Project Context

## Architecture Overview

### Core Components
- Django-based admin portal using django-jazzmin
- Mixin-based architecture for shared functionality
- Process status management system
- Bulk import/export system
- Resource-based data handling

### Key Technologies
- Django Admin with Jazzmin UI
- django-import-export for data operations
- Session-based state management
- Event-driven process status system

## Core Patterns

### Mixin Pattern
Mixins are used to share functionality across admin classes while maintaining separation of concerns:

1. **BulkImportMixin**
   - Handles file upload and validation
   - Manages import session state
   - Provides import form and context
   - Coordinates with resource for actual import

2. **AdminExportMixin**
   - Handles secure export via direct links
   - Supports filtered exports
   - Manages export formats and filenames
   - Logs export actions

3. **ProcessStatusMixin**
   - Manages process state transitions
   - Tracks session state
   - Coordinates UI updates
   - Handles process validation

4. **ReferentialIntegrityMixin**
   - Validates foreign key references
   - Preloads and caches reference data
   - Manages validation errors
   - Optimizes bulk operations

### Resource Pattern
Resources handle data import/export operations with optimized performance:

1. **BulkImportResourceMixin**
   - Optimizes bulk imports using bulk_create
   - Handles preprocessing and validation
   - Manages referential integrity
   - Coordinates with ProcessStatus

2. **CommonResource**
   - Base resource with shared functionality
   - Field metadata management
   - Validation utilities
   - Date handling

### Process Status Pattern
State management through a structured process:

1. **State Flow**
   - Data Loading
   - Validation
   - Calculation
   - Period Closing

2. **State Management**
   - Session-based tracking
   - ProcessStatus model updates
   - UI state synchronization
   - Event-driven transitions

## Common Patterns

### Error Handling
Consistent error response structure across the application:

1. **Error Types**
   ```python
   # Validation Errors
   {
       "row_number": int,
       "field": str,
       "value": str,
       "type": "validation"
   }

   # Processing Errors
   {
       "row_number": int,
       "message": str,
       "type": "processing"
   }

   # System Errors
   {
       "message": str,
       "type": "system"
   }
   ```

2. **Error Display**
   - Scrollable error lists
   - Type-specific formatting
   - Consistent summary information
   - Clear error messages

### State Management
Session-based state tracking with process status:

1. **Session Keys**
   ```python
   SESSION_KEYS = [
       "comp_post_date",
       "loaded_date",
       "validated_date",
       "calculated_date",
       "closed_date",
       "closed_flg"
   ]
   ```

2. **State Transitions**
   - Validation prerequisites
   - State update methods
   - UI synchronization
   - Error handling

### Security
Comprehensive security measures:

1. **Data Protection**
   - PII field redaction
   - CSRF protection
   - Permission checks
   - Audit logging

2. **PII Fields**
   ```python
   PII_FIELDS = [
       "patient_name",
       "account_id",
       "ssn",
       "email",
       "phone",
       "address",
       "transaction_id",
       "trans_amt",
       "provider",
       "locums_provider"
   ]
   ```

## Best Practices

### Code Organization
1. Keep UI logic in views, not mixins
2. Use mixins for shared functionality
3. Maintain consistent error handling
4. Follow established patterns
5. Document all changes

### Performance
1. Use bulk operations where possible
2. Cache reference data
3. Optimize database queries
4. Minimize session data

### Security
1. Always validate user input
2. Protect sensitive data
3. Maintain audit trails
4. Follow principle of least privilege

### Testing
1. Test all state transitions
2. Verify validation rules
3. Check error handling
4. Ensure UI updates correctly

## Implementation Guidelines

### Adding New Features
1. Review existing patterns
2. Follow established error handling
3. Maintain state management
4. Update documentation

### Modifying Existing Code
1. Understand current patterns
2. Maintain backward compatibility
3. Update affected components
4. Document changes

### Error Handling
1. Use consistent error types
2. Provide clear messages
3. Maintain audit trail
4. Handle all edge cases

### State Management
1. Update both session and model
2. Maintain UI consistency
3. Handle transitions properly
4. Log state changes 