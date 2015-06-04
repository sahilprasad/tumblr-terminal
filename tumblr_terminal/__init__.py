import yaml
import os
import sys
import pytumblr
from interactive_console import new_oauth as auth

yaml_path = os.path.expanduser('~') + '/.tumblr'

if not os.path.exists(yaml_path):
	tokens = auth(yaml_path)
else:
	yaml_file = open(yaml_path, "r")
	tokens = yaml.safe_load(yaml_file)
	yaml_file.close()

# creating client to interact with
client = pytumblr.TumblrRestClient(
	tokens['consumer_key'],
	tokens['consumer_secret'],
	tokens['oauth_token'],
	tokens['oauth_token_secret']
)

blog_url = client.info()['user']['name']

def make_text_post(state=None, title=None, body=None):
	if body == None:
		print('Text post body missing, dawg.')
	else:
		if state == None:
			state = "published"
		if title != None:
			client.create_text(blog_url, state=state, title=title, body=body)
		else:
			client.create_text(blog_url, state=state, body=body)

		print('Text post %s to %s!' % (state, blog_url))
