from ftplib import FTP
from tqdm import tqdm
import os

site = FTP("ftp.chandrashekar.info", "testuser", "w3lc0me")

site.cwd("/files")

progress = tqdm(total=os.stat("testfile.zip").st_size)
with open("testfile.zip", "rb") as f:

    class StoreFile:
        def read(self, size=0):
            #print(size, end=' ', flush=True)
            progress.update(size)
            return f.read(size)

    site.storbinary("STOR zzzzz_2019_nov_26.zip", StoreFile())

site.quit()
progress.close()
