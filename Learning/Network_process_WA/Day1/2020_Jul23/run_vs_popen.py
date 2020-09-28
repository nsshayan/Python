from subprocess import run, Popen

#p = Popen("ls")
p = run(["ls", "/dffd"], check=True)
print(p)
print(p.returncode)
