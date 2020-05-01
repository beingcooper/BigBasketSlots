from twilio.rest import Client


account_sid = 'paste it from your Twilio account'
auth_token = 'paste it from your Twilio account'


your_number = "whatsapp:+91xxxxxxxxxx"

def send_whatsapp(msg):

    client = Client(account_sid, auth_token)    
    
    message = client.messages.create(body=msg,
                       from_='whatsapp:+14155238886', to=your_number)
    
    print(message.sid)
    

send_whatsapp("Hello World!")
    
    
