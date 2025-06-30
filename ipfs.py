import requests
import json

# PINATA_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI0MDFmZGY1Mi0wN2UwLTRkMTUtYmZjNi00NDMzMzY2NTZiNzMiLCJlbWFpbCI6ImZhbmd5aWxpQHNlYXMudXBlbm4uZWR1IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiRlJBMSJ9LHsiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiTllDMSJ9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6IjIzNjg2MjM5NjEzMzg0NGRjMzJmIiwic2NvcGVkS2V5U2VjcmV0IjoiZTgxYmRmYzkzYjQ5YjNjZjY5M2QzOWNiNmQzNmIxNWRlMWIxNGRjZGZlZGU2N2FjYTAzNWJhYWQzMTNiM2I3OCIsImV4cCI6MTc4Mjg1MDA3OX0.Mc4BoHW8fLtFv9dTjFol7sYHnQ4U5kQqFCJHBpJlWDc"

def pin_to_ipfs(data):
    assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
    #YOUR CODE HERE
    
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

    # headers = {
    #     "Authorization": f"Bearer {PINATA_JWT}",
    #     "Content-Type": "application/json"
    # }

    response = requests.post(url, headers=headers, json={"pinataContent": data})
    response.raise_for_status()
    cid = response.json()["IpfsHash"]

    return cid

def get_from_ipfs(cid,content_type="json"):
    assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
    #YOUR CODE HERE	
    gateway_url = f"https://gateway.pinata.cloud/ipfs/{cid}"
    response = requests.get(gateway_url)
    response.raise_for_status()

    data = response.json()
    assert isinstance(data,dict), f"get_from_ipfs should return a dict"
    return data

# if __name__ == "__main__":
#     test_data = {"hello": "world", "value": 42}
#     cid = pin_to_ipfs(test_data)
#     print("Uploaded CID:", cid)

#     retrieved = get_from_ipfs(cid)
#     print("Retrieved Data:", retrieved)
