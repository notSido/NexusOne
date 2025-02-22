import requests

def get_wireguard_tunnel(api_url, **kwargs):
    """Retrieve an existing WireGuard Tunnel."""
    tunnel_id = kwargs.get('id')
    endpoint = f"{api_url}/api/v2/vpn/wireguard/tunnel"
    params = {'id': tunnel_id}
    headers = kwargs.get('headers')
    response = requests.get(endpoint, params=params, auth=kwargs.get('auth'), headers=headers, verify=False)
    return response.json()

def get_wireguard_tunnels(api_url, **kwargs):
    """Retrieve a list of all existing wireguard tunnels"""
    endpoint = f"{api_url}/api/v2/vpn/wireguard/tunnels"
    headers = kwargs.get('headers')
    response = requests.get(endpoint, auth=kwargs.get('auth'), headers=headers, verify=False)
    return response.json()

def create_wireguard_tunnel(api_url, **kwargs):
    """Create a new WireGuard Tunnel."""
    tunnel_data = kwargs.get('data')
    endpoint = f"{api_url}/api/v2/vpn/wireguard/tunnel"
    headers = kwargs.get('headers')
    response = requests.post(endpoint, json=tunnel_data, auth=kwargs.get('auth'), headers=headers, verify=False)
    return response.json()

def update_wireguard_tunnel(api_url, **kwargs):
    """Update an existing WireGuard Tunnel."""
    tunnel_data = kwargs.get('data')
    endpoint = f"{api_url}/api/v2/vpn/wireguard/tunnel"
    headers = kwargs.get('headers')
    response = requests.patch(endpoint, json=tunnel_data, auth=kwargs.get('auth'), headers=headers, verify=False)
    return response.json()

def delete_wireguard_tunnel(api_url, **kwargs):
    """Delete an existing WireGuard Tunnel."""
    tunnel_id = kwargs.get('id')
    apply_flag = kwargs.get('apply', False)
    endpoint = f"{api_url}/api/v2/vpn/wireguard/tunnel"
    params = {'id': tunnel_id, 'apply': apply_flag}
    headers = kwargs.get('headers')
    response = requests.delete(endpoint, params=params, auth=kwargs.get('auth'), headers=headers, verify=False)
    return response.json()

def apply_pending_wireguard_changes(api_url, **kwargs):
    """Apply pending WireGuard changes"""
    endpoint = f"{api_url}/api/v2/vpn/wireguard/apply"
    headers = kwargs.get('headers')
    response = requests.post(endpoint, auth=kwargs.get('auth'), headers=headers, verify=False)
    return response.json()
