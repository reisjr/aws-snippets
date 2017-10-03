from __future__ import print_function

import json

'''
Customizing User Pools messages using a custom attribute country
''' 

print('Loading function')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    if event["triggerSource"] == "CustomMessage_SignUp":
        country = event["request"]["userAttributes"]["custom:country"]
        
        if country == "BR":
            event["response"] = {
                "smsMessage": "BR: Seu codigo e " + event["request"]["codeParameter"],
                "emailMessage": "BR: Seu codigo e " + event["request"]["codeParameter"],
                "emailSubject": "Bem-vindo ao App Demo!"
            }
        elif country == "CO" or country == "AR" or country == "CL":
            event["response"] = {
                "smsMessage": "CO: Su clave es " + event["request"]["codeParameter"],
                "emailMessage": "CO: Su clave es " + event["request"]["codeParameter"],
                "emailSubject": "Bienvenido al App Demo!"
            }
        else:
            event["response"] = {
                "smsMessage": "EN: Your code is " + event["request"]["codeParameter"],
                "emailMessage": "EN: Your code is " + event["request"]["codeParameter"],
                "emailSubject": "Welcome to App Demo!"
            }
    
    return event
