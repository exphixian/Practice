### To verify if an API exists ###
import requests

print("What is the API URL of the site?")
URL = str(input())
print()

API_response =requests.get(URL)
if API_response.status_code == 200:
    print("This site is available.")
    print()
elif API_response == 401:
    print("You do not have the proper credentials to verify this site.")
else:
    print(API_response.status_code)
