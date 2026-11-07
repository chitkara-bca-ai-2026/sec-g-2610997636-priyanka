print("Input:")
print(" Username: student_user")
print(" Password: Secure@123")

username = input("\nEnter your username: ")
password = input("Enter your password: ")

print("\n=================================================")
print("PASSWORD VALIDATION REPORT")
print("==================================================")

print("Username:", username)
print("Password:", "*" * len(password))
print("\n--- Validation Rules ---")

if len(password) >= 8:
    print("[PASS] Minimum 8 characters (" + str(len(password)) + " characters)")
    length_valid = True
else:
    print("[FAIL] Minimum 8 characters")
    length_valid = False

if any(char.isdigit() for char in password):
    print("[PASS] At least one digit")
    digit_valid = True
else:
    print("[FAIL] At least one digit")
    digit_valid = False

if any(char.isupper() for char in password):
    print("[PASS] At least one uppercase letter")
    uppercase_valid = True
else:
    print("[FAIL] At least one uppercase letter")
    uppercase_valid = False

print("\n--- Result ---")

if length_valid and digit_valid and uppercase_valid:
    print("Password is VALID!")
    print("Account created successfully for " + username + "!")
else:
    print("Password is INVALID.")
    print("Account registration failed for " + username + "!")

print("\n==========================================")



