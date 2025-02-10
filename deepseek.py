import requests

def test_completion():
    url = "http://localhost:8000/v1/completions"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "prompt": "Hello, how are you?",
        "max_tokens": 100
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Please ensure that:")
        print("1. The server is running at localhost:8000")
        print("2. The correct port number is being used")
        print("3. No firewall is blocking the connection")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    result = test_completion()
    if result:
        print(result) 