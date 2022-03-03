# Author: Tracy Vierra
# Date Created: 3/2/2022
# Date Modified: 3/2/2022

# Description:

# Usage:

from email_validator import validate_email, EmailNotValidError

testEmail = "examplestackabuse.com"

try:
    # Validating the `testEmail`
    emailObject = validate_email(testEmail)

    # If the `testEmail` is valid
    # it is updated with its normalized form
    testEmail = emailObject.email
    print(testEmail)
except EmailNotValidError as errorMsg:
    # If `testEmail` is not valid
    # we print a human readable error message
    print(str(errorMsg))

# from email_validator import validate_email

testEmail2 = "example@stackabuse.com"

emailObject = validate_email(testEmail2)
print(emailObject.email)