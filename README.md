# BigBasketSlots
Automatic whatsapp alerts for free slots in Big Basket! 

## Requirements
* Python
* Windows Machine (Running on Linux may need some minor tweaks)

## Step 1 - Setup

We will use Twilio for sending whatsapp messages.

1. Create your free account [here](https://www.twilio.com/try-twilio). Login to your account and note down the auth_token and account_sid.
3. Activate Twilio-Whatsapp sandbox using the instructions [here](https://www.twilio.com/console/sms/whatsapp/sandbox). Save the bot number in your contacts. You will be receiving alerts from the same.

## Step 2 - Install the required libraries:
Run the folowing command in command prompt

> pip install -r requirements.txt


## Step 3 - Running the Code

1. Replace auth_token and account_sid in whatsapp.py from Step 1.
2. Replace your mobile number in whatsapp.py.
3. Run the folowing command in command prompt
> python whatsapp.py
4. If all goes well, you should receive a "Hello World" message on your whatsapp from the number you saved in Step 1.
5. Run the folowing command in command prompt
> python bigBasketSlots.py

## Flow
* Once you run the main command, a test controlled browser will open asking you to login to your BigBasket website using mobile OTP.
* Make sure you have some items added to your basket.
* Once you login it, it will starts monitoring the slots. You may minimize the window now but keep the program running.
* You will reveive a whatsapp message if a free slot if found.






