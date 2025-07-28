import uuid
import platform
import hashlib

def get_stable_hwid():
    base = (
        str(uuid.getnode()) +                     # MAC address
        platform.node() +                         # Hostname
        platform.system() + platform.machine()    # OS info
    )
    hwid = hashlib.sha256(base.encode()).hexdigest()
    return hwid
