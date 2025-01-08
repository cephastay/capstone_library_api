import re

from django.core.exceptions import ValidationError

def validate_email_address(email):
    """
    This function checks if a valid email has been provided 
    matching it against a standard regular expression
    Only two domains are allowed. `gmail` and `outlook`
    """
    e_pattern = r'^[a-zA-Z0-9._%+-]+@(outlook\.com|gmail\.com)$'
    if not re.match(pattern=e_pattern, string=email):
        raise ValidationError(f"{email} is not a valid email address")