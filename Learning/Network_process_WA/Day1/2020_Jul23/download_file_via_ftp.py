from ftplib import FTP
from tqdm import tqdm

def getsizeof_file(filename):
    return int([f[1] for f in ftp.mlsd(".") if f[0] == filename][0]["size"])

filename = input("Enter filename to download: ")
ftp = FTP("ftp.chandrashekar.info", "testuser", "w3lc0me")
ftp.debug(2)

ftp.cwd("/www/files")
progress = tqdm(total=getsizeof_file(filename))
with open(filename, "wb") as outfile:
    curr = 0
    def store(data):
        global curr
        progress.update(curr)
        outfile.write(data)
        curr += len(data)

    ftp.retrbinary(f"RETR {filename}", store)
