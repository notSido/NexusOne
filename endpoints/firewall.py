import requests

def get_firewall_rule(api_url, **kwargs):
    """Retrieve an existing Firewall Rule"""
    rule_id = kwargs.get('id')
    endpoint = f"{api_url}/api/v2/firewall/rule"
    params = {'id': rule_id}
    headers = kwargs.get('headers')
    response = requests.get(endpoint, params=params, auth=kwargs.get('auth'), headers=headers, verify=False)
    return response.json()

def get_firewall_rules(api_url, **kwargs):
    """Retrieve a list of all firewall rules"""
    endpoint = f"{api_url}/api/v2/firewall/rules"
    headers = kwargs.get('headers')
    response = requests.get(endpoint, auth=kwargs.get('auth'), headers=headers, verify=False)
    return response.json()

def create_firewall_rule(api_url, **kwargs):
    """Create a new Firewall Rule"""
    rule_data = kwargs.get('data')
    endpoint = f"{api_url}/api/v2/firewall/rule"
    headers = kwargs.get('headers', {})
    response = requests.post(endpoint, json=rule_data, auth=kwargs.get('auth'), headers=headers, verify=False)
    return response.json()

def apply_pending_firewall_changed(api_url, **kwargs):
    """Apply pending Firewall Changes"""
    endpoint = f"{api_url}/api/v2/firewall/apply"
    headers = kwargs.get('headers', {})
    response = requests.post(endpoint, auth=kwargs.get('auth'), headers=headers, verify=False)