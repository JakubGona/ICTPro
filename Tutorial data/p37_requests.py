import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response)
if response.status_code == 200:  # OK
    data = response.json()
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")
    #print(data)

print("="*80)

response = requests.get("https://svatky.adresa.info/json")
print(response)
if response.status_code == 200:
    data = response.json()
    #print(data)
    print(f"Dnes má svátek:")
    for row in data:
        print(f"{row['name']}")

response = requests.get("https://svatky.adresa.info/txt")
print(response)
if response.status_code == 200:
    data = response.text
    print(data)