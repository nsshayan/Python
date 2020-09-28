from ftplib import FTP

site = FTP("ftp.chandrashekar.info", "testuser", "w3lc0me")

site.cwd("/www/files")


try:
    with open("testfile.zip", "wb") as f:
        def store(data):
            print(".", end='', flush=True)
            f.write(data)

        site.retrbinary("RETR xml.zip", store)
        #site.retrbinary("RETR june28.zip", f.write)

except Exception as e:
    print("Caught an error: ", e)
    from os import unlink
    unlink("testfile.zip")
finally:
    site.quit()

# next( int(f[1]["size"]) for f in ftp.mlsd(".") if f[0] == "xml.zip")
