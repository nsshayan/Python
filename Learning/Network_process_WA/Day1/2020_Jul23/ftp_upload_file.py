from ftplib import FTP

ftp = FTP("ftp.chandrashekar.info", "testuser", "w3lc0me")
ftp.set_debuglevel(7)
ftp.cwd("/www/files")

with open("xml.zip", "rb") as infile:
    class FileProxy:
        def __init__(self, file):
            self.file = file

        def read(self, size):
            print("Reading", size, "bytes")
            # print("#", end="", flush=True)
            return self.file.read(size)

    file_proxy = FileProxy(infile)
    ftp.storbinary("STOR zz_new_file_may31.zip", file_proxy)

ftp.close()
