from tqdm import tqdm
from time import sleep

duration = 10
progress = tqdm(total=duration)
for i in range(duration):
    progress.update()
    sleep(1)
progress.close()
