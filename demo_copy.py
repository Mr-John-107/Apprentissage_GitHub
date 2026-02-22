import requests
from pyfiglet import print_figlet

print_figlet("PHOENIX")

r = requests.get('http://www.example.com')

print(r.status_code)