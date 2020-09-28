from ftplib import FTP

filename = input("Enter filename to download: ")
ftp = FTP("ftp.chandrashekar.info", "testuser", "w3lc0me")

ftp.cwd("/www/files")

with open(filename, "wb") as outfile:

    def store(data):
        outfile.write(data)
        print("#", end="", flush=True)

    ftp.retrbinary(f"RETR {filename}", store)