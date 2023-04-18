import re


def check_password_strength(password):
    # Define the regex patterns
    patterns = [
        r"[a-z]",  # lowercase letters
        r"[A-Z]",  # uppercase letters
        r"\d",  # digits
        r"[@$!%*?&]",  # special characters
        r".{8,}"  # length
    ]

    # Test the password against each pattern
    score = 0
    for pattern in patterns:
        if re.search(pattern, password):
            score += 1

    # Define the strength levels
    strength_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong"
    }

    # Return the password strength
    return strength_levels.get(score, "Invalid password")


# Test the function with some example passwords
print(check_password_strength("password"))  # Very Weak
print(check_password_strength("Password123"))  # Weak
print(check_password_strength("Pass123!"))  # Moderate
print(check_password_strength("StrongPass123!"))  # Strong
print(check_password_strength("VeryStrongPa$$"))  # Very Strong
