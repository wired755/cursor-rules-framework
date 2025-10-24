# MWA Django Testing Guide

This guide explains how to run Django tests for the MWA project using SQLite instead of Oracle to avoid RDS restrictions.

## Quick Start

### Run All Tests
```bash
# Navigate to project root
cd C:\Users\wired\DjangoProjects\mwa

# Run all tests with SQLite
python manage.py test --settings=test_settings

# Run all tests with verbose output
python manage.py test --settings=test_settings --verbosity=2

# Run all tests and keep database (faster for multiple runs)
python manage.py test --settings=test_settings --keepdb
```

### Run Specific Test Files
```bash
# Run Phase 4 security tests
python manage.py test mwa.tests.test_phase4_security --settings=test_settings

# Run logging tests
python manage.py test mwa.tests.test_logging_admin --settings=test_settings
python manage.py test mwa.tests.test_logging_integration --settings=test_settings
python manage.py test mwa.tests.test_logging_mixins --settings=test_settings
python manage.py test mwa.tests.test_logging_models --settings=test_settings

# Run Phase 2 and 3 tests
python manage.py test mwa.tests.test_phase2_logging --settings=test_settings
python manage.py test mwa.tests.test_phase3_logging --settings=test_settings
```

### Run Specific Test Classes or Methods
```bash
# Run specific test class
python manage.py test mwa.tests.test_phase4_security.Phase4SecurityTests --settings=test_settings

# Run specific test method
python manage.py test mwa.tests.test_phase4_security.Phase4SecurityTests.test_redaction_patterns_single_source --settings=test_settings
```

## Alternative Test Runner

You can also use the custom test runner script:

```bash
# Run all tests using the custom runner
python run_tests.py
```

## Test Settings Configuration

The `test_settings.py` file:
- Inherits all settings from your main `settings.py`
- Overrides only the database configuration to use SQLite
- Uses in-memory SQLite for faster testing
- Disables debug toolbar and other development tools
- Reduces logging verbosity during testing

## Key Features

### Database Configuration
- **SQLite in-memory**: Fastest testing with `:memory:` database
- **File-based SQLite**: Uncomment in `test_settings.py` for debugging
- **No Oracle dependencies**: Avoids RDS restrictions entirely

### Performance Optimizations
- **Faster password hashing**: Uses MD5 for testing
- **Reduced logging**: Warnings only during testing
- **Disabled middleware**: Removes debug toolbar and axes
- **Memory backend**: Uses local memory for email and cache

### Production Safety
- **Preserves all settings**: Only database configuration is overridden
- **No production impact**: Test settings are completely separate
- **Oracle compatibility**: Production Oracle settings remain unchanged

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **Settings Import Errors**: Make sure you're in the project root directory
   ```bash
   cd C:\Users\wired\DjangoProjects\mwa
   ```

3. **Test Database Issues**: Use `--keepdb` flag for faster subsequent runs
   ```bash
   python manage.py test --settings=test_settings --keepdb
   ```

### Debugging Tests

To inspect the test database, modify `test_settings.py`:
```python
# Change from in-memory to file-based
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
    }
}
```

## Test Coverage

To run tests with coverage:
```bash
# Install coverage
pip install coverage

# Run tests with coverage
coverage run --source='.' manage.py test --settings=test_settings
coverage report
coverage html  # Generate HTML report
```

## Best Practices

1. **Always use `--settings=test_settings`** for test commands
2. **Use `--keepdb`** for faster test runs during development
3. **Use `--verbosity=2`** for detailed test output
4. **Run specific tests** during development, all tests before commits
5. **Check test coverage** regularly to ensure comprehensive testing

## Test Structure

```
tests/
├── test_phase2_logging.py      # Phase 2 logging tests
├── test_phase3_logging.py      # Phase 3 logging tests
├── test_phase4_security.py     # Phase 4 security tests
├── test_logging_admin.py       # Admin logging tests
├── test_logging_integration.py # Integration tests
├── test_logging_mixins.py      # Mixin tests
└── test_logging_models.py      # Model tests
```

Each test file focuses on specific functionality and can be run independently.
