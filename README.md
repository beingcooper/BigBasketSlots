# BigBasketSlots
Automatic alerts for free slots in Big Basket! 


We will use Twilio for sending whatsapp messages.
1. Create your free account [here](https://www.twilio.com/try-twilio)
2. Activate Twilio-Whatsapp sandbox using the instructions [here](https://www.twilio.com/console/sms/whatsapp/sandbox).

Install all the requirements:
> pip install -r requirements.txt

Edits required
1. Login to your Twilio account and get the auth_token and account_sid. Replace them in whatsapp.py file.
2. Replace your mobile number.
3. Run python whatsapp.py . If all goes well, you should receive a "Hello World" message on your whatsapp from the number you saved in Step 2.
4.



