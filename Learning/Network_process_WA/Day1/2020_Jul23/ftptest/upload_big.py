from ftplib import FTP

site = FTP("ftp.chandrashekar.info", "testuser", "w3lc0me")

site.cwd("/www/files/python")

with open("testfile.zip", "rb") as f:
    class StoreFile:
        def read(self, size=0):
            print(size, end=' ', flush=True)
            return f.read(size)

    site.storbinary("STOR zzzzz_2018_oct_09.zip", StoreFile())

site.quit()
