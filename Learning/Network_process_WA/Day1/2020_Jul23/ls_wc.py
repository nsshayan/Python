from subprocess import Popen, PIPE

ls_command = Popen(["ls", "-l"], stdout=PIPE)
wc_command = Popen("wc", stdin=ls_command.stdout)

ls_command.wait()
wc_command.wait()


