import requests

def prnt_resp(res):
    if 'application/json' in res.headers['Content-Type']:
        res.json()
    else:
        resp.text()

    #print(res.text)
    print(res.json())
    # print(res.status_code)
    # print(type(res.json()))
    # print(res.headers)
    # print(type(res.headers))

status = 'available'
headers = {'accept': 'application/json'}
data = {
  "id": 2132274020372,
  "category": {
    "id": 34637649823764,
    "name": "Dogs"
  },
  "name": "Max",
  "photoUrls": [
    ""
  ],
  "tags": [
    {
      "id": 17316487316487,
      "name": "www"
    }
  ],
  "status": "available"

}

data1 = {
  "id": 2132274020372,
  "category": {
    "id": 34637649823764,
    "name": "Cats"
  },
  "name": "Murzick",
  "photoUrls": [
    ""
  ],
  "tags": [
    {
      "id": 17316487316487,
      "name": "hhjhj"
    }
  ],
  "status": "available"
}

#resp = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers={'accept': 'application/json'})
resp = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'}, headers=headers)
prnt_resp(resp)

resp1 = requests.post("https://petstore.swagger.io/v2/pet", headers=headers, json=data)
prnt_resp(resp1)
pet_dict = dict(resp1.json())
pet_id = pet_dict["id"]

# resp2 = requests.post("https://petstore.swagger.io/v2/pet/"+str(pet_id), data={'status': 'sold'}, headers=headers)
# prnt_resp(resp2)

resp2 = requests.put("https://petstore.swagger.io/v2/pet/", headers=headers, json=data1)
prnt_resp(resp2)

resp3 = requests.delete("https://petstore.swagger.io/v2/pet/"+str(pet_id), headers={'accept': 'application/json', 'api_key': 'special-key'})
prnt_resp(resp3)




