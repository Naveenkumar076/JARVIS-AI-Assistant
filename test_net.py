import requests

try:
    r = requests.get("https://google.com")

    print("Internet working")

except Exception as e:
    print(e)