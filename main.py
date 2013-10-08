from twilio.rest import TwilioRestClient

account_sid = "ACd04a3d6d646809d8e2aafa609e03d38d"
auth_token = "dae02b5d7c0b54b3fae7aa05560c1d81"
client = TwilioRestClient(account_sid, auth_token)

recName = []
recNum = []
with open('contacts') as f:
	name = []
	for line in f:
		name.append([str(x) for x in line.split()])
	for x in name:		
		message = client.messages.create(body="Hello " + x[0] + " " + x[1] + "! This is an automated message to let you know that you have a care package waiting for you! Please come pick it up on the first floor of " + x[3] + " suite! Hope you have a great day!", to=x[2], from_="+13472526162")
		print "message sent to: " + x[0]
