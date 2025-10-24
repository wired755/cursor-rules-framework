"""
Context initialization script for Cursor threads.
Run this at the start of any new thread to ensure proper context.
"""

import os
from pathlib import Path

def initialize_context():
    """
    Initializes context for Cursor threads by reading and processing documentation.
    Returns a dictionary of key context information.
    """
    docs_dir = Path(__file__).parent
    
    # Read core documentation
    with open(docs_dir / "PROJECT_CONTEXT.md") as f:
        project_context = f.read()
    
    with open(docs_dir / "PATTERNS.md") as f:
        patterns = f.read()
    
    with open(docs_dir / "QUICK_REFERENCE.md") as f:
        quick_ref = f.read()
    
    # Extract key patterns and responsibilities
    context = {
        "core_components": [
            "Django-based admin portal using django-jazzmin",
            "Mixin-based architecture for shared functionality",
            "Process status management system",
            "Bulk import/export system",
            "Resource-based data handling"
        ],
        
        "mixin_responsibilities": {
            "BulkImportMixin": [
                "Handles file upload and validation",
                "Manages import session state",
                "Provides import form and context",
                "Coordinates with resource for actual import"
            ],
            "AdminExportMixin": [
                "Handles secure export via direct links",
                "Supports filtered exports",
                "Manages export formats and filenames",
                "Logs export actions"
            ],
            "ProcessStatusMixin": [
                "Manages process state transitions",
                "Tracks session state",
                "Coordinates UI updates",
                "Handles process validation"
            ],
            "ReferentialIntegrityMixin": [
                "Validates foreign key references",
                "Preloads and caches reference data",
                "Manages validation errors",
                "Optimizes bulk operations"
            ]
        },
        
        "error_types": {
            "validation": {
                "row_number": "int",
                "field": "str",
                "value": "str",
                "type": "validation"
            },
            "processing": {
                "row_number": "int",
                "message": "str",
                "type": "processing"
            },
            "system": {
                "message": "str",
                "type": "system"
            }
        },
        
        "session_keys": [
            "comp_post_date",
            "loaded_date",
            "validated_date",
            "calculated_date",
            "closed_date",
            "closed_flg"
        ],
        
        "pii_fields": [
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
        ],
        
        "best_practices": {
            "code_organization": [
                "Keep UI logic in views, not mixins",
                "Use mixins for shared functionality",
                "Maintain consistent error handling",
                "Follow established patterns",
                "Document all changes"
            ],
            "performance": [
                "Use bulk operations where possible",
                "Cache reference data",
                "Optimize database queries",
                "Minimize session data"
            ],
            "security": [
                "Always validate user input",
                "Protect sensitive data",
                "Maintain audit trails",
                "Follow principle of least privilege"
            ]
        }
    }
    
    return context

def get_context_summary():
    """
    Returns a brief summary of the project context that can be pasted into Cursor.
    """
    context = initialize_context()
    
    summary = """# Project Context Summary

## Core Components
{}

## Mixin Responsibilities
{}

## Error Types
{}

## Best Practices
{}

For full context, refer to:
- docs/PROJECT_CONTEXT.md
- docs/PATTERNS.md
- docs/QUICK_REFERENCE.md
""".format(
        "\n".join(f"- {comp}" for comp in context["core_components"]),
        "\n".join(f"- {mixin}: {', '.join(resp)}" 
                 for mixin, resp in context["mixin_responsibilities"].items()),
        "\n".join(f"- {type_}: {fields}" 
                 for type_, fields in context["error_types"].items()),
        "\n".join(f"- {area}: {', '.join(practices)}" 
                 for area, practices in context["best_practices"].items())
    )
    
    return summary

if __name__ == "__main__":
    print(get_context_summary()) 