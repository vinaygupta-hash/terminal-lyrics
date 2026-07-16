import sys
import time
lyrics = [
    (0.0, 0.6, "♪ Let's the music play"),
    (0.6, 4.2, "♪ Kya fitoor, dur raha kyu jaaye na?"),
    (4.2, 10.0, "♪ Yeh kasoor, noor ka tere hai sara."),
    (10.0,15.0, "♪ Kya hasii hai, usi ki wajah se to fasi main!!"),
    (15.2, 20.5, "♪ Ho uljhi, mil jaaye bas teri hi, teri hein, teri.. bahein..")
]

start = time.time()

for start_time, end_time, line in lyrics:
    while time.time() - start < start_time:
        time.sleep(0.01)
    duration = end_time - start_time
    delay = duration / len(line)
    for ch in line:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()