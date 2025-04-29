import uuid
import json

def generate_uuid():
    return str(uuid.uuid4())

def generate_v2ray_config():
    config = {
        "v": "2",  # مقدار به صورت رشته و درست
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

configs = []
for _ in range(5):
    try:
        configs.append(generate_v2ray_config())
    except ValueError as e:
        print(f"Error generating config: {e}")

# ذخیره‌سازی فایل
with open("v2ray_configs.txt", "w") as file:
    for config in configs:
        try:
            json.dump(config, file, indent=4)  # ذخیره به صورت JSON معتبر
            file.write("\n\n")
        except ValueError as e:
            print(f"Error writing config to file: {e}")

print("5 V2Ray configurations generated and saved successfully!")
