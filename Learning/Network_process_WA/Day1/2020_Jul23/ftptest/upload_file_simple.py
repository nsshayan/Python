from ftplib import FTP

site = FTP("ftp.chandrashekar.info", "testuser", "w3lc0me")
site.set_debuglevel(7)

site.cwd("/www/files")

with open("nov29.zip", "rb") as f:
    class FileProxy:
        def __init__(self, fp):
            self.fp = fp

        def read(self, size=None):
            print(("Reading {} bytes...".format(size)))
            return self.fp.read(size)
    file_proxy = FileProxy(f)

    site.storbinary("STOR zzzzzzzzzzz_2018_mar22.zip", file_proxy)

site.quit()
