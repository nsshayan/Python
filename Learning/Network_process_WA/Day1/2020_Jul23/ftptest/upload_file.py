from ftplib import FTP

site = FTP("ftp.chandrashekar.info", "testuser", "w3lc0me")

site.cwd("/www/files")

with open("testfile.zip", "rb") as f:
    site.storbinary("STOR zzzzzzzzzz_new_file_2018_aug20.zip", f)

site.quit()
