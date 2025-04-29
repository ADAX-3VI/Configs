import uuid
import json
import base64

def generate_v2ray_link():
    config = {
        "v": "2",
        "ps": "Auto Generated",
        "add": "v2rayserver.com",
        "port": "443",
        "id": str(uuid.uuid4()),
        "aid": "64",
        "net": "tcp",
        "type": "none",
        "host": "",
        "path": "/v2ray",
        "tls": "tls"
    }
    json_str = json.dumps(config, separators=(',', ':'))
    base64_str = base64.b64encode(json_str.encode()).decode()
    return f"vmess://{base64_str}"

links = []
for _ in range(5):
    links.append(generate_v2ray_link())

with open("v2ray_links.txt", "w") as file:
    file.write("\n".join(links))

print("5 V2Ray links generated and saved.")
