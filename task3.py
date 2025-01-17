import re

def check_password_strength(password):
  """
  Checks the strength of a password based on various criteria.

  Args:
    password: The password to be checked.

  Returns:
    A string describing the password strength (Weak, Medium, Strong).
  """

  # Define criteria for different strength levels
  length_criteria = 8  # Minimum length
  uppercase_criteria = re.search(r'[A-Z]', password)  # Presence of uppercase letter
  lowercase_criteria = re.search(r'[a-z]', password)  # Presence of lowercase letter
  number_criteria = re.search(r'\d', password)  # Presence of a digit
  special_char_criteria = re.search(r'[!@#$%^&*()_+\=\[\]{};\'\\:"|,.<>\/?]', password)  # Presence of a special character

  # Calculate the strength level
  if len(password) < length_criteria:
    return "Weak"
  elif any([uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria]) and len(password) >= length_criteria:
    return "Medium"
  elif all([uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria]) and len(password) >= length_criteria:
    return "Strong"
  else:
    return "Weak"

# Get password input from the user
password = input("Enter a password: ")

# Check and display the strength level
strength = check_password_strength(password)
print(f"Password strength: {strength}")