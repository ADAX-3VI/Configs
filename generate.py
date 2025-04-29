import uuid
import json

def generate_uuid():
    return str(uuid.uuid4())

def generate_v2ray_config():
    config = {
        "v": "2",
        "ps": "Auto Generated V2Ray Config",
        "add": "v2rayserver.com",
        "port": "443",
        "id": generate_uuid(),
        "aid": "64",
        "net": "tcp",
        "type": "none",
        "host": "v2rayserver.com",
        "path": "/v2ray",
        "tls": "true"
    }
    return config

configs = [generate_v2ray_config() for _ in range(5)]

with open("v2ray_configs.txt", "w") as file:
    for config in configs:
        file.write(json.dumps(config, indent=4) + "\n\n")

print("5 V2Ray configurations generated and saved!")
