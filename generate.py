import uuid
import json
import random

def generate_uuid():
    return str(uuid.uuid4())

def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

def generate_random_port():
    return random.randint(1000, 65535)

def generate_random_path():
    paths = ["/v2ray", "/path1", "/path2", "/custom-path"]
    return random.choice(paths)

def generate_v2ray_config():
    config = {
        "v": "2",
        "ps": "Auto Generated V2Ray Config",
        "add": generate_random_ip(),
        "port": str(generate_random_port()),
        "id": generate_uuid(),
        "aid": "64",
        "net": "tcp",
        "type": "none",
        "host": generate_random_ip(),
        "path": generate_random_path(),
        "tls": "true"
    }
    return config

configs = []

for _ in range(5):
    configs.append(generate_v2ray_config())

with open("v2ray_configs.json", "w") as file:
    for config in configs:
        try:
            json.dump(config, file, indent=4)
            file.write("\n\n")
        except ValueError as e:
            print(f"Error writing config: {e}")

print("5 V2Ray configurations generated and saved!")
