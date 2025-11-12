import hashlib
import hmac

# Step 1: Create data.txt
original_text = "Never trust, always verify."
file_name = "data.txt"

with open(file_name, "w") as f:
    f.write(original_text)

print(f"File '{file_name}' created with content:\n{original_text}\n")

# Task 3A: SHA-256 Hash
with open(file_name, "rb") as f:
    file_data = f.read()

sha256_hash = hashlib.sha256(file_data).hexdigest()
print(f"SHA-256 hash of '{file_name}':\n{sha256_hash}\n")

# Task 3B: HMAC using SHA-256
key = b"secretkey123"  # HMAC key must be bytes
hmac_hash = hmac.new(key, file_data, hashlib.sha256).hexdigest()
print(f"HMAC-SHA256 of '{file_name}' with key '{key.decode()}':\n{hmac_hash}\n")

# Task 3C: Integrity Check
# Change one letter in the file
modified_text = "Never trust, always verity."  # Changed 'f' to 'i' in 'verify'
with open(file_name, "w") as f:
    f.write(modified_text)

print(f"File '{file_name}' modified to:\n{modified_text}\n")

# Recompute HMAC
with open(file_name, "rb") as f:
    modified_file_data = f.read()

new_hmac_hash = hmac.new(key, modified_file_data, hashlib.sha256).hexdigest()
print(f"New HMAC-SHA256 after modification:\n{new_hmac_hash}\n")

# Explain what happens
if new_hmac_hash != hmac_hash:
    print("HMACs are different! The file was modified.")
else:
    print("HMACs are identical! The file was not modified.")

