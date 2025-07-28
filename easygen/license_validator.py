import json
from datetime import datetime
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from easygen.utils import get_stable_hwid

def validate_license(license_path, public_key_path):
    with open(license_path, "r") as f:
        license_data = json.load(f)

    signature = bytes.fromhex(license_data.pop("signature"))

    license_json = json.dumps(license_data, sort_keys=True).encode()

    with open(public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())

    try:
        public_key.verify(
            signature,
            license_json,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
    except Exception as e:
        print("Invalid signature.")
        return False

    expiry = datetime.strptime(license_data["expiry"], "%Y-%m-%d").date()
    if expiry < datetime.now().date():
        print("Expired signature.")
        return False

    current_hwid = get_stable_hwid()
    if license_data["hwid"] != current_hwid:
        return False

    print("Licencia válida.")
    return True

