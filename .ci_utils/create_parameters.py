import os
import json


def create_parameters():
    root_dir = os.getcwd()
    file_path = os.path.join(root_dir, ".deployment", "aws", "parameters.json")
    params_keys = ["EC2ImageId", "MyPublicIP", "SshPort", "InstanceType"]
    params_values = [f"{os.getenv('image_id')}", f"{os.getenv('my_public_ip')}",
                    f"{os.getenv('ssh_port')}", f"{os.getenv('instance_type')}"]
    final_dict = dict(zip(params_keys,params_values))
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(final_dict, file)


if __name__ == "__main__":
    print("creating parameters.json")
    create_parameters()
    print("parameters.json created")
