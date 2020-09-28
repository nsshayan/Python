
def head(command, lines=5):
   from subprocess import Popen, PIPE
   from shlex import split
   p = Popen(split(command), stdout=PIPE)
   return [ p.stdout.readline() for i in range(lines) ]

def extract_lines(command, start=0, stop=5):
   from subprocess import Popen, PIPE
   from shlex import split
   p = Popen(split(command), stdout=PIPE)
   data = []
   for i in range(0, stop):
       line = p.stdout.readline()
       if i >= start:
           data.append(line)
   return data

#print(head("ps ax", 3))
print(extract_lines("ls /usr", 3, 8))
#print(head("ifconfig"))

