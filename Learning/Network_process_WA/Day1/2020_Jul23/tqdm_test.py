from tqdm import tqdm
from time import sleep

progress = tqdm(total=100)
for i in range(100):
    progress.update(i)
    sleep(0.1)

