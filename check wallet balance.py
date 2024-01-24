import requests

def get_eth_balance(address, api_key):
    base_url = "https://api.etherscan.io"
    endpoint = "/api"  # Corrected the endpoint

    # Set the parameters for the API request
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": api_key,
    }

    try:
        response = requests.get(base_url + endpoint, params=params)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        data = response.json()

        # Check if the request was successful
        if data["status"] == "1":
            # Convert the balance from Wei to Ether
            balance_wei = int(data["result"])
            balance_ether = balance_wei / 10**18
            return balance_ether
        else:
            print(f"API Error: {data.get('message', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except ValueError as e:
        print(f"JSON Parsing Error: {e}")
        return None

# Replace 'your_etherscan_api_key' with your actual API key
api_key = "J1Z5DPIB2NHUUEMJ9TP39DW76IBWCXTP37"
address = "0x1f9090aaE28b8a3dCeaDf281B0F12828e676c326"  # Replace with the Ethereum address you want to check

balance = get_eth_balance(address, api_key)
if balance is not None:
    print(f"Balance of {address}: {balance} Ether")
