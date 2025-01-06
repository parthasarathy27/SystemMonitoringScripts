import requests

# Function to check application health
def check_app_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Application is UP. Status Code: {response.status_code}")
        else:
            print(f"Application is DOWN. Status Code: {response.status_code}")
    except requests.ConnectionError:
        print("Application is DOWN. Unable to connect.")

if __name__ == "__main__":
    # Get the application URL from the user
    url = input("Enter the application URL: ")
    check_app_health(url)
