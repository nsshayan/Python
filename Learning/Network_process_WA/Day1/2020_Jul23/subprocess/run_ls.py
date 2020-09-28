#import subprocess
from subprocess import Popen

#p = Popen("ls")

ret = Popen("ls").wait()
print("ls returned", ret)
