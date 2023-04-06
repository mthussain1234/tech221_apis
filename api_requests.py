import requests
import json

# post_codes_req = requests.get("https://api.postcodes.io/postcodes/e126aw")
pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/gengar")
print(pokemon_req.content)
# print(post_codes_req)

# print(post_codes_req.status_code)

# print(post_codes_req.headers)

# print(post_codes_req.content)
# print(post_codes_req.json())

# post - post requests are very api dependent

# json.dumps() -> method to turn a python object (collection, variable, boolean)
# into a JSON string
# json_body = json.dumps({"postcodes": ["PR8 0SG", "M45 6GN", "EX165BL"]})

# json.dump() -> writes to a JSON file

# headers = {"Content-Type": "application/json"}
#
# post_multi_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_body)
#
# print(post_multi_req.json())