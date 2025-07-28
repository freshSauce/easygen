import tempfile
from datetime import datetime, timedelta
from easygen.license_generator import generate_license
from easygen.license_validator import validate_license
from easygen.utils import get_stable_hwid

PRIVATE_KEY = "private_key.pem"
PUBLIC_KEY = "public_key.pem"

def test_modified_hwid():
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".lic")
    expiry = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")

    generate_license(
        user="test_user",
        hwid="AA:BB:CC:DD:EE:FF",
        expiry_date_str=expiry,
        private_key_path=PRIVATE_KEY,
        output_path=temp_file.name
    )

    from json import load, dump
    with open(temp_file.name, "r") as f:
        lic = load(f)

    lic["hwid"] = get_stable_hwid()  # Simula cambio de HWID
    with open(temp_file.name, "w") as f:
        dump(lic, f)

    assert validate_license(temp_file.name, PUBLIC_KEY) is False
