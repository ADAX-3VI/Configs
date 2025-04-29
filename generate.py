import random
import uuid

def generate_uuid():
    return str(uuid.uuid4())

def generate_v2ray_config():
    uuid_value = generate_uuid()
    config = f"""
    {{
        "v": "2",
        "ps": "Auto Generated V2Ray Config",
        "add": "v2rayserver.com",
        "port": "443",
        "id": "{uuid_value}",
        "aid": "64",
        "net": "tcp",
        "type": "none",
        "host": "v2rayserver.com",
        "path": "/v2ray",
        "tls": "true"
    }}
    """
    return config

configs = []
for _ in range(5):
    configs.append(generate_v2ray_config())

with open("v2ray_configs.txt", "w") as file:
    for config in configs:
        file.write(config + "\n\n")

print("5 V2Ray configurations generated and saved!")
