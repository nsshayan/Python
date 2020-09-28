from ftplib import FTP
from tqdm import tqdm

site = FTP("ftp.chandrashekar.info", "testuser", "w3lc0me")

site.cwd("/www/files")

def get_size_of(site, filename, path="."):
    return next((int(f[1]["size"]) \
                 for f in site.mlsd(path) \
                 if f[0] == filename))

try:
    fsize = get_size_of(site, "xml.zip")
    progress = tqdm(total=fsize)

    with open("testfile.zip", "wb") as f:
        def store(data):
            #print(".", len(data), end='', flush=True)
            f.write(data)
            progress.update(len(data))



        site.retrbinary("RETR xml.zip", store)
        #site.retrbinary("RETR june28.zip", f.write)

except Exception as e:
    print("Caught an error: ", e)
    from os import unlink
    unlink("testfile.zip")
finally:
    site.quit()
    progress.close()

# next( int(f[1]["size"]) for f in ftp.mlsd(".") if f[0] == "xml.zip")
