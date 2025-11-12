# ==========================================================
# Task 2A + 2B: Elliptic Curve Cryptography (ECC)
# Curve: prime256v1 (also known as secp256r1)
# Libraries required: cryptography
# Install with: pip install cryptography
# ==========================================================

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric.utils import encode_dss_signature, decode_dss_signature

# ----------------------------------------------------------
# TASK 2A: Generate ECC Keys
# ----------------------------------------------------------

#  Generate ECC private key using the prime256v1 curve
private_key = ec.generate_private_key(ec.SECP256R1())

#  Derive the corresponding public key
public_key = private_key.public_key()

# Save the private key to a PEM file
with open("ecc_private_key.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

# Save the public key to a PEM file
with open("ecc_public_key.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

print(" ECC private and public keys have been generated and saved.\n")

# ----------------------------------------------------------
# TASK 2B: Sign and Verify a Message
# ----------------------------------------------------------

# Create a message file
with open("ecc.txt", "w") as f:
    f.write("Elliptic Curves are efficient.")

#  Read the message content as bytes
with open("ecc.txt", "rb") as f:
    message = f.read()

#  Load the private key from the file for signing
with open("ecc_private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# Sign the message using ECDSA with SHA-256
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

# Save the signature to a binary file
with open("signature.bin", "wb") as f:
    f.write(signature)

print(" Message signed successfully. Signature saved as 'signature.bin'.\n")

#  Load the public key from the file for verification
with open("ecc_public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

#  Verify the signature using the public key
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print(" Signature verification successful! The message is authentic and untampered.\n")
except Exception as e:
    print(" Signature verification failed:", e)

# ----------------------------------------------------------
# End of Script
# ----------------------------------------------------------
