import base64
import hashlib
import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes

THREEMA_GATEWAY_URL = "https://msgapi.threema.ch"

def send_message(gateway_id, secret, private_key_path, recipient_id, message):
    """Send an end-to-end encrypted Threema message."""
    # Load private key
    with open(private_key_path, "rb") as key_file:
        private_key = RSA.import_key(key_file.read())

    # Get public key of recipient
    public_key = fetch_public_key(recipient_id, gateway_id, secret)

    # Encrypt message
    encrypted_message = encrypt_message(message, private_key, public_key)

    # Send message
    url = f"{THREEMA_GATEWAY_URL}/send_e2e"
    payload = {
        "from": gateway_id,
        "to": recipient_id,
        "secret": secret,
        "box": base64.b64encode(encrypted_message).decode()
    }

    response = requests.post(url, data=payload)
    return response.status_code == 200

def fetch_public_key(recipient_id, gateway_id, secret):
    """Fetch the public key of the recipient."""
    url = f"{THREEMA_GATEWAY_URL}/pubkeys/{recipient_id}"
    response = requests.get(url, auth=(gateway_id, secret))
    if response.status_code == 200:
        return base64.b64decode(response.text)
    else:
        raise Exception("Failed to fetch public key.")

def encrypt_message(message, private_key, public_key):
    """Encrypt the message for Threema."""
    rsa_cipher = PKCS1_OAEP.new(public_key)
    aes_key = get_random_bytes(16)
    encrypted_aes_key = rsa_cipher.encrypt(aes_key)

    cipher = AES.new(aes_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())

    return encrypted_aes_key + cipher.nonce + ciphertext + tag

