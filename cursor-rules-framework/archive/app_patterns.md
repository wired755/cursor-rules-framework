# MWA Application Patterns

## MWA-Specific Patterns

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

## MWA Architecture Guidelines

### 1. Follow Existing Patterns
- **Mixins over Inheritance**: Use mixins for shared functionality (ProcessStatusMixin, CompensationMixin, etc.)
- **Session State Management**: Use request.session for process state, not database storage
- **Custom Admin Views**: Follow the pattern of @admin.site.admin_view decorators
- **Resource Classes**: Use CommonResource base class for all import/export resources

### 2. Model Conventions
- **Always specify db_column**: All model fields must have explicit db_column mappings
- **Use verbose_name**: All fields require verbose_name for admin display
- **Follow legacy naming**: Maintain existing table and column naming conventions (e.g., COMP_POST_DT)
- **Audit fields**: Include created_date, updated_date, created_by, updated_by where applicable
- **Thin Models**: Business logic in mixins, not models

### 3. Admin Interface Rules
- **Extend CommonModelAdmin**: All admin classes should inherit from CommonModelAdmin
- **Use BulkImportExportMixin**: For models with import/export functionality
- **Register with mwa_admin_site**: Always use the custom admin site, not default
- **Implement get_comp_post_date**: For models with compensation post dates

### 4. Import/Export Patterns
- **Extend CommonResource**: All resource classes must inherit from CommonResource
- **Implement get_field_metadata**: Define comprehensive field metadata for all resources
- **Use file_headers**: Define file_headers tuple for headerless import files
- **Validate referential integrity**: Check foreign key relationships during import

## MWA Application Workflows

### Process Status Workflow
1. **Initialize Process Status**: Always call init_process_status before process operations
2. **Update Session Atomically**: Use update_session method for process state changes
3. **Clear Session on Errors**: Implement proper cleanup for failed operations
4. **Handle State Transitions**: Manage state flow through Data Loading → Validation → Calculation → Period Closing

### Import/Export Workflow
1. **Preprocess File**: Validate file format and structure
2. **Validate in Dry-Run Mode**: Check data integrity before import
3. **Bulk Create on Success**: Use bulk operations for performance
4. **Handle Errors**: Provide clear error messages and recovery options
5. **Log Actions**: Maintain audit trail for all operations

### Security Workflow
1. **Validate User Permissions**: Check user.is_staff for administrative operations
2. **Sanitize Inputs**: Validate all form inputs and file uploads
3. **Protect PII Data**: Use sanitize_data function for sensitive information
4. **Maintain Audit Trail**: Log all security events for compliance
5. **Follow HIPAA Guidelines**: Ensure healthcare data protection

### Error Handling Workflow
1. **Use Consistent Error Structure**: Follow established error response format
2. **Provide Clear Messages**: Give specific guidance for failed validation
3. **Maintain Audit Trail**: Log all errors for debugging and compliance
4. **Handle Edge Cases**: Ensure all error scenarios are covered
