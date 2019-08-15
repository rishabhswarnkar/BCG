import requests
import json
import ast


URI = "BASE_URI"

def get_api_key():
  get_endpoint = "/api/v1/key"
  r = requests.get(url = URI + get_endpoint)
  data = ast.literal_eval(json.dumps(r.json()))
  print(data)
  return(data['key'])


def submit_request(name, email):
  post_endpoint = "/api/v1/submit?apiKey=" + get_api_key()
  p = {'name': name,
  'email': email}
  r = requests.post(url = URI + post_endpoint, data = p)
  
  print(r.status_code, r.reason)

submit_request("Rishabh Swarnkar", "rswarn2@illinois.edu")
