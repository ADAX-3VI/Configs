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
    return json.dumps(config, indent=4)

configs = []
for _ in range(5):
    # هر پیکربندی را به صورت جداگانه بررسی کنید
    try:
        config = generate_v2ray_config()
        configs.append(config)
    except ValueError as e:
        print(f"Error generating config: {e}")
        continue

# ذخیره در فایل
with open("v2ray_configs.txt", "w") as file:
    for config in configs:
        file.write(config + "\n\n")

print("5 V2Ray configurations generated and saved!")
