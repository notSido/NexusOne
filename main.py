import argparse
import yaml
import importlib

# List of module names containing your methods
ENDPOINT_MODULES = ["endpoints.wireguard", "endpoints.firewall"]  # Add more modules as needed

def load_yaml_file(file_path):
    """Generic function to load YAML from a file."""
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(
        description="CLI application to execute pfSense API tasks based on YAML configuration"
    )
    parser.add_argument('--inventory', required=True, help="Path to inventory YAML file with API credentials")
    parser.add_argument('--tasks', required=True, help="Path to tasks YAML file")
    args = parser.parse_args()

    # Load inventory and tasks from YAML files
    inventory = load_yaml_file(args.inventory)
    tasks_config = load_yaml_file(args.tasks)
    tasks = tasks_config.get('tasks', [])

    api_url = inventory.get('api_url')
    if not api_url:
        raise Exception('No API URL provided, quitting!')

    # Initialize headers
    headers = None

    # Determine authentication method
    if inventory.get('username') and inventory.get('password'):
        auth = (inventory.get('username'), inventory.get('password'))
    elif inventory.get('api_key'):
        auth = None
        headers = {'x-api-key': inventory.get('api_key')}
    else:
        raise Exception('No valid auth methods provided in the inventory file, quitting!')

    # Dynamically load all available methods from the modules
    methods = {}
    for module_name in ENDPOINT_MODULES:
        module = importlib.import_module(module_name)
        for method_name in dir(module):
            if not method_name.startswith("_"):  # Ignore private/internal methods
                methods[method_name] = getattr(module, method_name)

    # Process each task defined in the tasks YAML file
    for task in tasks:
        method_name = task.get('method')
        func = methods.get(method_name)
        if func:
            task['auth'] = auth
            task['headers'] = headers if headers else {}
            result = func(api_url, **task)
        else:
            result = {"error": f"Unknown method: {method_name}"}
        
        print(f"Result for task '{method_name}':")
        print(result)

if __name__ == '__main__':
    main()
