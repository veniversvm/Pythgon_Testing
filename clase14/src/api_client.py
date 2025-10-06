import requests

"""
    La idea es poder mockear el proceso que realiza esta funcion
"""
def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # import ipdb; ipdb.set_trace()

    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"],
    }


if __name__ == "__main__":
    result = get_location("8.8.8.8")
    print(result)