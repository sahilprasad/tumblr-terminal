import tumblr_terminal as t 
from colorama import init, Fore, deinit
import sys 

init() 

def usage():
	print('')
	print(Fore.BLUE + 'TEXT POSTS' + Fore.RESET)
	print('	To make a regular text post: ')
	print('		$ tumblr -t "[post body]"')
	print('	To make a text post with a title: ')
	print('		$ tumblr -tt "[post body]"')
	print('	To add tags to a text post: ')
	print('		$ tumblr [text post] --tags "tag1, tag2, tag3..."')
	print('	So, to make a text post with a title and tags: ')
	print('		$ tumblr -tt "This is my post" --tags "these, are, my, tags"')

def main():
	args = sys.argv[1:]

	if args == []:
		print('TUMBLR_TERMINAL developed by Sahil Prasad.')
		print("""
MMMMMMMMMMMMMMMMMMMMM.                             MMMMMMMMMMMMMMMMMMMMM
 `MMMMMMMMMMMMMMMMMMMM           M\  /M           MMMMMMMMMMMMMMMMMMMM'
   `MMMMMMMMMMMMMMMMMMM          MMMMMM          MMMMMMMMMMMMMMMMMMM'  
     MMMMMMMMMMMMMMMMMMM-_______MMMMMMMM_______-MMMMMMMMMMMMMMMMMMM    
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    
     .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.    
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  
                   `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'                
                          `MMMMMMMMMMMMMMMMMM'                    
                              `MMMMMMMMMM'                              
                                 MMMMMM                          
                                  MMMM                                  
                                   MM     
			""")
	else:
		try:

			if len(args) == 1:
				if args[0] == '--usage' or args[0] == '-usage':
					usage() 
				else:
					raise ValueError

			if (args[0] == '-t' or args[0] == '-pt' or args[0] == '-dt' or args[0] == '-qt' or 
				args[0] == '-tt' or args[0] == '-ptt' or args[0] == '-dtt' or args[0] == '-qtt'):
				body = args[1]
				tags = []
				state = None
				title = None
				if len(args) == 4 and (args[2] == '--tags' or args[2] == '-tags'):
					tags = args[3]
					tags = tags.split(",")

				if args[0] == '-dt' or args[0] == '-dtt':
					state = "draft"
				if args[0] == '-qt' or args[0] == '-qtt':
					state = "queue"

				if args[0] == '-tt' or args[0] == '-ptt' or args[0] == '-qtt' or args[0] == '-dtt':
					title = raw_input('Title: ')
					if title == '':
						title = None

				t.make_text_post(state=state, title=title, body=body, tags=tags)


		except ValueError:
			print(Fore.RED + 'ERROR' + Fore.RESET + ' : Invalid input detected.')
			print('Type '+ Fore.BLUE + 'tumblr' + Fore.RESET + 'or' + Fore.BLUE +
			 ' tumblr --usage' + Fore.RESET + ' for help.')
	

deinit()