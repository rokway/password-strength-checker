import re

def check_password_strength(password):
    """Evaluate the strength of a password and provide feedback."""
    score = 0
    recommendations = []

    # Check length
    if len(password) >= 12:
        score += 1
    else:
        recommendations.append("Make the password at least 12 characters long.")

    # Check for uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        recommendations.append("Include both uppercase and lowercase letters.")

    # Check for numbers
    if re.search(r'\d', password):
        score += 1
    else:
        recommendations.append("Add at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        recommendations.append("Add at least one special character (e.g., !, @, #).")

    # Check for common patterns
    common_patterns = ['password', '1234', 'qwerty', 'letmein', 'admin']
    if any(pattern in password.lower() for pattern in common_patterns):
        recommendations.append("Avoid common patterns like 'password' or '1234'.")
    else:
        score += 1

    # Overall evaluation
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, recommendations


# Main script
if __name__ == "__main__":
    print("Welcome to the Password Strength Checker!")
    user_password = input("Enter a password to check its strength: ")

    strength, feedback = check_password_strength(user_password)
    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("Recommendations:")
        for suggestion in feedback:
            print(f"- {suggestion}")
