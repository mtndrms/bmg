import requests

# Make changes for tagging
# This is for the new branch

response = requests.get("https://api.exchangerate.host/convert?from=USD&to=TRY")
print(response.json())
