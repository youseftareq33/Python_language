import requests

# get(to make access to the page and get data from it)
response = requests.get('https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_Q6tnchBAP524PKyxWxTPxPKeMKTk6NAByG1W00r9')
print(response) # return status code
print(response.text) # print source code of the page
print(response.status_code) # print status code of page
response.raise_for_status()  # Raises an exception for HTTP errors

data=response.json() # to get data of json format
print(data.keys()) # to print keys
print(data.get("data").keys())# to print keys that inside data key
print("USD: ",data.get("data",{}).get("USD",-1)) # to print value of specific key that inside data key
print("USD: ",data["data"]["USD"]) # or u can use this to print value of specific key that inside data key

print("-----------------------------------------------"+"\n")
# post
data = {'JOD': '12.25'}
response = requests.post('https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_Q6tnchBAP524PKyxWxTPxPKeMKTk6NAByG1W00r9', data=data)
print(response)

print("-----------------------------------------------"+"\n")
# adding header
# let the client and the server pass additional information with an HTTP request or response. 
headers = {'User-Agent': 'My App'}
response = requests.get('https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_Q6tnchBAP524PKyxWxTPxPKeMKTk6NAByG1W00r9', headers=headers)

print("-----------------------------------------------"+"\n")


'''
 {'data': {'AUD': 1.5437902706, 'BGN': 1.7996702717, 'BRL': 4.8523705725, 'CAD': 1.3557501465,
   'CHF': 0.8790201474, 'CNY': 7.2789009738, 'CZK': 22.146733105, 'DKK': 6.8560211052, 
   'EUR': 0.9199701732, 'GBP': 0.7913601545, 'HKD': 7.8444012675, 'HRK': 7.0422210826,
   'HUF': 350.4519188084, 'IDR': 15237.649258667, 'ILS': 3.7962305226, 'INR': 82.5599229706,
   'ISK': 131.0128153791, 'JPY': 145.9846472174, 'KRW': 1319.4978875605, 'MXN': 16.7927618678,
   'MYR': 4.6434106014, 'NOK': 10.5812620621, 'NZD': 1.6752702774, 'PHP': 56.7455978551,
   'PLN': 4.1061506627, 'RON': 4.5455908007, 'RUB': 95.4156302859, 'SEK': 10.878731639,
   'SGD': 1.349670154, 'THB': 35.0057835253, 'TRY': 26.4908534806, 'USD': 1, 'ZAR': 18.4770230781}}
'''