import yaml

def convert_yaml_to_tfvars(yaml_content):
    tfvars_content = ""
    yaml_data = yaml.safe_load(yaml_content)
    for key, value in yaml_data.items():
        if isinstance(value, list) or isinstance(value, tuple):
            value = '", "'.join(map(str, value))
            value = f'["{value}"]'
        elif isinstance(value, dict):
            value = '", "'.join([f'{k}={v}' for k, v in value.items()])
            value = f'{{{value}}}'
        else:
            value = f'"{value}"'
        tfvars_content += f"{key} = {value}\n"
    return tfvars_content

def yaml_to_tfvars(input_yaml_file, output_tfvars_file):
    with open(input_yaml_file, 'r') as f:
        yaml_content = f.read()
    tfvars_content = convert_yaml_to_tfvars(yaml_content)
    with open(output_tfvars_file, 'w') as f:
        f.write(tfvars_content)

# Input YAML file
input_yaml_file = "var.yml"

# Output tfvars file
output_tfvars_file = "var.tfvars"

# Convert YAML to tfvars
yaml_to_tfvars(input_yaml_file, output_tfvars_file)
