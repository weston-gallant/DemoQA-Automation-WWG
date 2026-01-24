"""Test data specifically for DemoQA Practice Forms page"""

# Default user for required field validation
PRACTICE_FORM_DEFAULT_USER = {
    "first_name": "Weston",
    "last_name": "Gallant",
    "email": "DJWestyOwn@test.com",
    "phone": "1234567890"
}

# Additional test users for data-driven scenarios
PRACTICE_FORM_TEST_USERS = [
    PRACTICE_FORM_DEFAULT_USER,
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@test.com", 
        "phone": "9876543210"
    },
    {
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane.smith@test.com",
        "phone": "5551234567"
    }
]
