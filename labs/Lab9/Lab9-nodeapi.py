import requests

# Listens to existing localhost where node server is running
response = requests.get("http://localhost:3000/")
data = response.json()

# Logic to output Widget colors 
for widget in data:
    name = widget["name"]
    color = widget["color"]
    print(f"{name} is {color}.")
