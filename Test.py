import requests
import base64

def main():
#API Authentication Parameters.
portal_name = "company"
portal_id = "8888"
client_id ="XYyUSH6PbDRDJpk3xEOfrNxHeifAhgfK35Yi3DLS"
client_secret ="2aZ5aDJ1vu1cgWNxWU0jvIEPTJLmHphgNP8g1dnNKveoj6LTLYKuuzOB8DTdVZ568oe53HqbHZIqmPX6FiuK8PmM4RUX581Ki4kbtHzYmB01RfqAB2Aw10DJ4LsjuWf8"

# base64 HTTP Header
auth_token = 'Basic ' + base64.b64encode("{}:{}".format(client_id,
client_secret).encode()).decode('ascii')
# Https GET Call
header = {'Authorization': auth_token}
url = 'https://' + portal_name + '.udemy.com/api-2.0/organizations/' + portal_id +
'/courses/list/'
querystring = {"fields[courses]": "@all", "page": "1", "page_size": "1"}
r = requests.request("GET", url, headers=header, params=querystring)
print(r.status_code)
# JSON Payload
results = r.json()
print(results)