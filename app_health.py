import requests

# Application URL
URL = "https://www.google.co.in/" 

def check_app_health():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print(f"Application is UP. Status Code: {response.status_code}")
        else:
            print(f"Application is DOWN. Status Code: {response.status_code}")
    except requests.ConnectionError:
        print("Application is DOWN. Unable to connect.")

if __name__ == "__main__":
    check_app_health()