import argparse
import yaml
from endpoints import wireguard

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
    username = inventory.get('username')
    password = inventory.get('password')

    if not (api_url and username and password):
        print("Error: Inventory file must include api_url, username, and password.")
        return

    auth = (username, password)

    # Create a dispatch dictionary mapping method names to functions.
    # You can expand this dictionary as you add more endpoints.
    dispatch = dict(get_wireguard_tunnel=wireguard.get_wireguard_tunnel,
                    create_wireguard_tunnel=wireguard.create_wireguard_tunnel,
                    update_wireguard_tunnel=wireguard.update_wireguard_tunnel,
                    delete_wireguard_tunnel=wireguard.delete_wireguard_tunnel,
                    apply_pending_wireguard_changes=wireguard.apply_pending_wireguard_changes)

    # Process each task defined in the tasks YAML file
    for task in tasks:
        method_name = task.get('method')
        func = dispatch.get(method_name)
        if func:
            # Merge authentication and any other required parameters into kwargs.
            # This approach allows each function to extract what it needs from kwargs.
            task['auth'] = auth
            result = func(api_url, **task)
        else:
            result = {"error": f"Unknown method: {method_name}"}
        print(f"Result for task '{method_name}':")
        print(result)

if __name__ == '__main__':
    main()
