import uuid
import json

def generate_uuid():
    """Generates a random UUID."""
    return str(uuid.uuid4())

def generate_v2ray_config():
    """Generates a single V2Ray config dictionary."""
    return {
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

def main():
    """Main function to generate multiple configs and save them to a file."""
    configs = [generate_v2ray_config() for _ in range(5)]
    
    with open("v2ray_configs.txt", "w") as file:
        for config in configs:
            json.dump(config, file, indent=4)
            file.write("\n\n")

    print("Successfully generated and saved 5 V2Ray configurations!")

if __name__ == "__main__":
    main()
