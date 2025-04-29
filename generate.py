import uuid
import json

# تولید UUID
def generate_uuid():
    return str(uuid.uuid4())

# تولید کانفیگ V2Ray
def generate_v2ray_config():
    config = {
        "v": "2",  # دقت کنید که مقدار به درستی به صورت رشته است
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
    return config  # بازگشت یک شیء JSON معتبر

configs = []

# ایجاد چندین کانفیگ
for _ in range(5):
    configs.append(generate_v2ray_config())

# ذخیره داده‌ها در فایل JSON
with open("v2ray_configs.txt", "w") as file:
    for config in configs:
        try:
            # استفاده از json.dump برای نوشتن به فایل
            json.dump(config, file, indent=4)
            file.write("\n\n")  # فاصله‌گذاری مناسب
        except ValueError as e:
            print(f"Error writing config: {e}")

print("5 V2Ray configurations generated and saved!")
