import twitter

api = twitter.Api(consumer_key='XEC8SlepJBKZE8pAGc43YgZNH', 
	consumer_secret='Hy1IhAzzOY7RhFAQrNrCh9qwdNV6XuNlvxyASEWq9KiKcut7tb', 
	access_token_key='844344508556959744-6pn8HoyAneyoAOQMoitDBr0soBT2OTR',
	access_token_secret='pyruDOlONujI0KTksMG4UJaolFuDVSj8O6aW1gIcD2cGN')

# Post a status update
api.PostUpdate("Test status posted from python-twitter")

# Get each status on the bot's timeline and print them
timeline = api.GetUserTimeline(screen_name='ND_DS_SP17_Bot')
statuses = [s.text for s in timeline]
for s in statuses:
	print s
