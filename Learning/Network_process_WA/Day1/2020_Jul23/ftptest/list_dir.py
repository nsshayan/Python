from ftplib import FTP

def process_data(data):
    print("...", data)

site = FTP("ftp.chandrashekar.info", "testuser", "w3lc0me")

site.cwd("/www/files")

site.retrlines("LIST", process_data)

site.quit()

