import sys
import requests

def main(client_id, client_name):
    print(f"Client ID: {client_id}, Client Name: {client_name}")
    # Exemplo de chamada a uma API de teste
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    print(f"API Response: {response.json()}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: myscript.py <client_id> <client_name>")
        sys.exit(1)
    client_id = sys.argv[1]
    client_name = sys.argv[2]
    main(client_id, client_name)
