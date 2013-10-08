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
		message = client.messages.create(body="Just kidding " + x[0] + ", Clearly I am autistic and don't know how to space words properly. But again I'd like to remind you that you are definitely at the level of a " + x[2] + " rank League of Legends player!", to=x[1], from_="+13472526162")
		print "message sent to: " + x[0]
