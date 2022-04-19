import json
import requests

#url = "http://numbersapi.com/5/math?json"
#response = requests.get(url)  # so we made a HTTP GET request here just like a browser would
# # so you want to be careful how often you make requests
# # some/many sites will rate limit you or even block you if you make too many requests (100 a second would not be cool)
categories={1:'math',2:'trivia',3:'date',4:'year'}
print('Available categories: ' )
for key, value in categories.items():
    print(key,value)
your_category=int(input("Choose one of categories (input 1-4): "))
your_number=input("enter any number: ")
#print(categories[your_category])
url="http://numbersapi.com/"+your_number+"/"+categories[your_category]+"?json"
#print(url)
response = requests.get(url)
if response.status_code==200:
    data_from_json = response.json()
    print(data_from_json)
    with open("my_data_from_url.json",mode="a") as file_stream_out:
        json.dump(data_from_json,file_stream_out, indent=4)
else:
    print("Error, cant read link. Error:", response.status_code)

# Response Code 200 is good! 404 not good :)
#http://en.wikipedia.org/wiki/List_if_HTTP_status_codes
#print(response.text)

#print(data_from_json['/ws/2/')
#print(data_from_json[0])