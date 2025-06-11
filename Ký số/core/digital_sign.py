from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class DigitalSigner:
    def __init__(self):
        self.private_key = None
        self.certificate = None
    
    def load_private_key(self, key_path, password=None):
        with open(key_path, "rb") as key_file:
            self.private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=password.encode() if password else None,
                backend=default_backend()
            )
    
    def sign_file(self, file_path, output_path=None):
        if not self.private_key:
            raise ValueError("Private key not loaded")
        
        if not output_path:
            output_path = file_path + ".sig"
        
        with open(file_path, "rb") as f:
            data = f.read()
        
        signature = self.private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        with open(output_path, "wb") as f:
            f.write(signature)
        
        return output_path
    
    def verify_signature(self, file_path, signature_path, public_key):
        # Implementation for verification
        pass