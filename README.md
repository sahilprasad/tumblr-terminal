# Tumblr_Terminal

Creative name, huh? Tumblr_Terminal lets you blog your frustrations from the comfort of your terminal. Check out the examples below.

## Installation

I developed this with Python 2.7.6. If you are having trouble running it on your machine with Python 3.4+ or another version of Python, hit me up and we'll try to debug.

First, make sure you have a Tumblr account. This may or may not be a wise choice, depending on your levels of self-control.

Once you have one, you need to get login credentials. Namely, your Consumer API Key, and Consumer Secret Key.

Go to https://www.tumblr.com/oauth/apps to register an application. The only information that you absolutely need to provide are the 'Application name' and 'Administrative contact email'. These values can be whatever you want them to be, as the main purpose is just to retrieve the keys. A 'default callback URL' is needed to register, though. If you have plans for developing a web application that utilizes the API to integrate Tumblr into, for example, your personal website so that people can post about how cool you are, then you can set this to your domain name. But if you do not care, you can either set it to '/' (without the apostrophes, of course), or 'http:127.0.0.1', where the latter option allows you to develop on your local machine.

Now that you have your Consumer and Consumer Secret keys, install Tumblr_Terminal by running:
`pip install tumblr_terminal`
If everything went smoothly, when you start up your terminal and type `tumblr`, you should be prompted to enter your Consumer and Secret Keys, after which you will be told to follow a link.

Go through the link, and you will be asked to allow the application to access your information. Allow it, then copy the redirect URL and paste it into the terminal as instructed.

After following the instructions, restart your terminal and type `tumblr` again. If all went well, you should see a Batman logo that I may or may not get into legal trouble for. Congrats!

## Features

As of version 0.1, one can only make text posts. More features, including but not limited to posting pictures, quotes, audio and aspects such as draft and queue management are coming soon-ish.

## Examples

To make a text post without a title:
`$ tumblr -t "My post"`
For a text post with a title:
`$ tumblr -tt "My post"

## Credit

The `interactive_console.py` module is a modified version of the file in Tumblr's official Python client, found here: https://github.com/tumblr/pytumblr. Please read their LICENSE for more information regarding distribution and usage.

## Contact

sahil_prasad@brown.edu
