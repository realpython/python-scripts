import requests

message = raw_input('Enter a Message: ')
number = raw_input('Enter the phone number: ')


payload = {'number': number, 'message': message}
r = requests.post("http://textbelt.com/text", data=payload)
if r.json()['success']:
    print('Success!')
else:
    print('Error!')
