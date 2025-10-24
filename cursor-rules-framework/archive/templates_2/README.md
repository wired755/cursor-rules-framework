# Documentation Templates

## Overview
This directory contains enhanced documentation templates for generating structured documents in the MWA project. These templates are used by the prompt protocols to create comprehensive design documents and implementation plans.

## Templates

### Design Document Template
- **File**: `design_template.mdc`
- **Purpose**: Generate structured design documents
- **Usage**: `@DESIGN -D <concept>` or `@DESIGN <concept>` (default includes both)
- **Features**:
  - HIPAA compliance requirements
  - Security requirements
  - Audit requirements
  - User experience requirements
  - Architecture decisions
  - Implementation approach
  - Risk assessment

### Implementation Plan Template
- **File**: `plan_template.mdc`
- **Purpose**: Generate structured implementation plans
- **Usage**: `@PLAN -D <design_name>` or `@PLAN <design_name>` (default includes both)
- **Features**:
  - Phase-based planning
  - Task breakdown
  - Dependencies tracking
  - Deliverables definition
  - Timeline estimation
  - Risk assessment
  - Resource requirements

## Usage with Flags

### Design Flags
- `@DESIGN <concept>` - Default: Thread response + design document
- `@DESIGN -D <concept>` - Design document only
- `@DESIGN -T <concept>` - Thread response only

### Plan Flags
- `@PLAN <design_name>` - Default: Thread response + implementation plan
- `@PLAN -D <design_name>` - Implementation plan only
- `@PLAN -T <design_name>` - Thread response only

## Benefits

1. **Structured Output**: Consistent document format across all designs and plans
2. **Comprehensive Coverage**: Includes all necessary sections for MWA project
3. **Compliance Ready**: Built-in HIPAA, security, and audit requirements
4. **Flexible Usage**: Flags allow for different output types
5. **Enhanced Functionality**: .mdc format provides advanced features

## Integration

These templates integrate with the prompt protocols to provide:
- Auto-loading of relevant context
- Conditional execution based on flags
- Enhanced template functionality
- MWA-specific requirements and patterns
