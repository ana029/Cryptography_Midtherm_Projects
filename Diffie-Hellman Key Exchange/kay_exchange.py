# Diffie-Hellman Key Exchange Simulation
# Public parameters (p and g)
p = 23    # prime number
g = 5     # generator
# Alice's private key (secret)
a = 6
# Bob's private key (secret)
b = 15
# Calculate public keys
A = pow(g, a, p)  # Alice's public key: g^a mod p
B = pow(g, b, p)  # Bob's public key: g^b mod p
print(" Public parameters:")
print(f"p (prime): {p}")
print(f"g (generator): {g}\n")
print("Public keys:")
print(f"Alice’s public key (A): {A}")
print(f"Bob’s public key (B): {B}\n")
# Compute the shared secret key
shared_key_alice = pow(B, a, p)  # (B^a mod p)
shared_key_bob = pow(A, b, p)    # (A^b mod p)
print(" Shared Secret Keys:")
print(f"Alice’s derived key: {shared_key_alice}")
print(f"Bob’s derived key: {shared_key_bob}\n")
# Verify if both shared keys are identical
if shared_key_alice == shared_key_bob:
    print(" Shared keys match! Secure channel established.")
else:
    print(" Keys do not match. Something went wrong.")
