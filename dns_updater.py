import config
import requests
import sys
import time

current_ip = sys.argv[1]

data = {
        "type" : "AAAA",
        "name" : f"{config.CLOUDFLARE_DNS}",
        "content" : current_ip,
        "ttl" : 1,
        "proxied" : False
        }

url = f"https://api.cloudflare.com/client/v4/zones/{config.CLOUDFLARE_ZONES_ID}/dns_records/{config.CLOUDFLARE_RECORD_ID}"

# headers
headers = {
        'Content-Type' : 'application/json',
        'Authorization' : f"Bearer {config.CLOUDFLARE_TOKEN}"
           }

print(f"url: {url} - data: {data}")
print(f"headers: {headers}")

while True:
    response = requests.put(url, json=data, headers=headers)
    print("Trying to update url...")
    if response.status_code == 200:
        print("Update ok")
        break

    s = 60
    from IPython import embed; embed()
    print(f"Updating failed. Status: {response.status_code}. Waiting for {s} seconds")
    print(response.content)
    time.sleep(s)


