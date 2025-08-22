import time

for h in range(0,24):
        for m in range(0,60):
            for s in range(0,60):
                  time.sleep(1)
                  print(f"{h}:{m}:{s}")
        
            