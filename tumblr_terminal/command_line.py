import tumblr_terminal as t 
from colorama import init, Fore, deinit
import sys 

init() 

def usage():
	print('To make a text post: ')
	print('$ tumblr -t "[post body]"')
	print('To make a text post with a title: ')
	print('$ tumblr -tt "[post body]"')

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

			if args[0] == '-t' or args[0] == '-qt' or args[0] == '-dt' or args[0] == '-pt':
				if len(args) == 1:
					raise ValueError
				body = args[1]
				t.make_text_post(body=body)
			elif args[0] == '-tt' or args[0] == '-qtt' or args[0] == '-dtt' or args[0] == '-ptt':
				if len(args) == 1:
					raise ValueError
				body = args[1] 
				title = raw_input('Title: ')
				if title == '':
					title = None
				t.make_text_post(title=title, body=body)
			else:
				raise ValueError 
		except ValueError:
			print(Fore.RED + 'ERROR' + Fore.RESET + ' : Invalid input detected.')
			usage()
	

deinit()