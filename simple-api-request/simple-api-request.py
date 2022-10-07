import requests

response = requests.get("https://api.exchangerate.host/convert?from=USD&to=TRY")
print(response.json())