import pxssh
try:                                                            
    s = pxssh.pxssh()
    
    hostname = "192.168.56.101" 
    username = "root"
    password = "welcome"

   
    s.login(hostname, username, password)
    s.sendline('uptime')  # run a command

    s.prompt()             # match the prompt
    print(s.before)         # print everything before the prompt.

    s.sendline('ls -l')
    s.prompt()
    print(s.before)

    s.sendline ('df')
    s.prompt()
    print(s.before)

    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(str(e))
except:
    import sys
    sys.exc_info()
