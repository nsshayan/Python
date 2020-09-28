from ftplib import FTP
from glob import glob

site = FTP("ftp.chandrashekar.info", "testuser", "w3lc0me")

site.cwd("/www/files/python")
site.mkd("pyscripts")
site.cwd("pyscripts")


for py_file in glob("*.py"):
    print("Uploading", py_file)
    with open(py_file, "rb") as f:
        site.storbinary("STOR {}".format(py_file), f)

site.quit()

