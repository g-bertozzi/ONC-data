import onc
import json

def connect_to_onc():
    with open('config/config.json', 'r') as f:
        config = json.load(f)
    token = config['api_token']
    return onc.ONC(token=token)
