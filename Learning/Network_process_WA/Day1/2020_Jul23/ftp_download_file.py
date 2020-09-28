from ftplib import FTP

ftp = FTP("ftp.chandrashekar.info", "testuser", "w3lc0me")

ftp.cwd("/www/files")

with open("xml.zip", "wb") as outfile:

    def store(data):
        print("storing", len(data), "bytes")
        # print("#", end="", flush=True)
        outfile.write(data)

    ftp.retrbinary("RETR xml.zip", store)

ftp.close()
