from subprocess import Popen, PIPE

#p = Popen("ls | wc")
#p.wait()

ls_command = Popen("ls", stdout=PIPE)
wc_command = Popen("wc", stdin=ls_command.stdout)

ls_command.wait()
wc_command.wait()
print("done.")