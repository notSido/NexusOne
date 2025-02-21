import requests


def get_wireguard_tunnel(api_url, **kwargs):
    """Retrieve an existing WireGuard Tunnel."""
    tunnel_id = kwargs.get('id')
    endpoint = f"{api_url}/api/v2/vpn/wireguard/tunnel"
    params = {'id': tunnel_id}
    response = requests.get(endpoint, params=params, auth=kwargs.get('auth'), verify=False)
    return response.json()


def create_wireguard_tunnel(api_url, **kwargs):
    """Create a new WireGuard Tunnel."""
    tunnel_data = kwargs.get('data')
    endpoint = f"{api_url}/api/v2/vpn/wireguard/tunnel"
    response = requests.post(endpoint, json=tunnel_data, auth=kwargs.get('auth'), verify=False)
    return response.json()


def update_wireguard_tunnel(api_url, **kwargs):
    """Update an existing WireGuard Tunnel."""
    tunnel_data = kwargs.get('data')
    endpoint = f"{api_url}/api/v2/vpn/wireguard/tunnel"
    response = requests.patch(endpoint, json=tunnel_data, auth=kwargs.get('auth'), verify=False)
    return response.json()


def delete_wireguard_tunnel(api_url, **kwargs):
    """Delete an existing WireGuard Tunnel."""
    tunnel_id = kwargs.get('id')
    apply_flag = kwargs.get('apply', False)
    endpoint = f"{api_url}/api/v2/vpn/wireguard/tunnel"
    params = {'id': tunnel_id, 'apply': apply_flag}
    response = requests.delete(endpoint, params=params, auth=kwargs.get('auth'), verify=False)
    return response.json()

def apply_pending_wireguard_changes(api_url, **kwargs):
    """Apply pending WireGuard changes"""
    endpoint = f"{api_url}/api/v2/vpn/wireguard/apply"
    response = requests.post(endpoint, auth=kwargs.get('auth'), verify=False)
    return response.json()