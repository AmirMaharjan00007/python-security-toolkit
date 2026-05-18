import re

# Common weak passwords (you can extend this list)
COMMON_PASSWORDS = [
    "123456", "password", "123456789", "qwerty", "abc123", "password1",
    "111111", "12345678", "123123", "admin", "letmein", "welcome",
    "monkey", "dragon", "baseball", "football",
]

def check_length(password):
    length = len(password)
    if length < 8:
        return 0, "Too short (less than 8 characters)"
    elif length < 12:
        return 1, "Medium length"
    else:
        return 2, "Good length"

def has_uppercase(password):
    if re.search(r"[A-Z]", password):
        return 1, "Has uppercase letters"
    return 0, "No uppercase letters"

def has_lowercase(password):
    if re.search(r"[a-z]", password):
        return 1, "Has lowercase letters"
    return 0, "No lowercase letters"

def has_digit(password):
    if re.search(r"\d", password):
        return 1, "Has digits"
    return 0, "No digits"

def has_symbol(password):
    if re.search(r"[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]", password):
        return 2, "Has symbols"
    return 0, "No symbols"

def is_common_password(password):
    pw_clean = password.strip().lower()
    if pw_clean in [p.lower() for p in COMMON_PASSWORDS]:
        return True, "Commonly used / weak password"
    return False, "Not in common password list"

def rate_strength(score, is_common):
    if is_common:
        return "Very Weak"
    if score < 3:
        return "Weak"
    elif score < 5:
        return "Medium"
    else:
        return "Strong"

def suggest_improvements(password):
    suggestions = []

    if len(password) < 12:
        suggestions.append("Use at least 12 characters.")

    if not re.search(r"[A-Z]", password):
        suggestions.append("Add uppercase letters.")

    if not re.search(r"[a-z]", password):
        suggestions.append("Add lowercase letters.")

    if not re.search(r"\d", password):
        suggestions.append("Add at least one digit.")

    if not re.search(r"[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]", password):
        suggestions.append("Add special symbols.")

    if suggestions:
        return "Suggestions: " + " ".join(suggestions)
    return "Password looks strong."

def check_password_strength(password):
    # Check each component
    len_score, len_msg = check_length(password)
    upper_score, upper_msg = has_uppercase(password)
    lower_score, lower_msg = has_lowercase(password)
    digit_score, digit_msg = has_digit(password)
    symbol_score, symbol_msg = has_symbol(password)
    is_common, common_msg = is_common_password(password)

    # Compute total score (0–7)
    total_score = len_score + upper_score + lower_score + digit_score + symbol_score

    # Strength rating
    strength = rate_strength(total_score, is_common)

    # Display results
    print("\n" + "="*50)
    print("PASSWORD STRENGTH CHECKER")
    print("="*50)
    print(f"Password: {'*' * len(password)}  ({len(password)} characters)")
    print(f"Length:          {len_msg}")
    print(f"Uppercase:       {upper_msg}")
    print(f"Lowercase:       {lower_msg}")
    print(f"Digits:          {digit_msg}")
    print(f"Symbols:         {symbol_msg}")
    print(f"Common:          {common_msg}")
    print(f"Strength rating: {strength} ({total_score}/7)")
    print("\n" + suggest_improvements(password))

def main():
    print("Password Strength Checker")
    password = input("Enter password: ").strip()
    if not password:
        print("Password cannot be empty.")
        return

    check_password_strength(password)

if __name__ == "__main__":
    main()


  
#Notes
#You can expand COMMON_PASSWORDS to load from a file (e.g., rockyou.txt in development only).
#For production, never store or log real user passwords; only hash comparisons or rules‑based checks.
  
