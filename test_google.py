import requests

try:
    r = requests.get(
        "https://www.google.com",
        timeout=5
    )

    print("Connected:", r.status_code)

except Exception as e:
    print(e)