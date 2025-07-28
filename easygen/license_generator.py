import json
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def generate_license(user, hwid, expiry_date_str, private_key_path, output_path="license.lic"):
    license_data = {
        "user": user,
        "hwid": hwid,
        "expiry": expiry_date_str
    }

    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )

    license_json = json.dumps(license_data, sort_keys=True).encode()

    signature = private_key.sign(
        license_json,
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    license_data["signature"] = signature.hex()
    with open(output_path, "w") as f:
        json.dump(license_data, f, indent=2)

    print(f"License generated on '{output_path}'")
