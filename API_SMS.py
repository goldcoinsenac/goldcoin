import requests

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {
    "authorization": "API_KEY_OF_YOURS",
    "message": "This is test Message sent from \
    Python Script using REST API.",
    "language": "english",
    "route": "q",
    "numbers": "87988177520, 87992043499"}

headers = {
    'cache-control': "no-cache"
}
try:
response = requests.request("GET", url, headers=headers, params=querystring)