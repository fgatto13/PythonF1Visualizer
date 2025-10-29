import requests as rq

def fetch_driver(request, driver_number, speed=''):
    base_url = "https://api.openf1.org/v1"
    driver_name_url = f"{base_url}/{request}?driver_number={driver_number}&session_key=latest{speed}"
    try:
        response = rq.get(driver_name_url)
        response.raise_for_status()
        return response.json()
    except rq.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    number = input("Enter driver number: ")
    data = fetch_driver("drivers", number)
    print(data)
