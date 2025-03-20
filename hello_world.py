from datetime import datetime
import sys

now = datetime.now()
h = now.strftime("%H")
m = now.strftime("%M")
s = now.strftime("%S")

projectPath = sys.path[0]

with open(projectPath + "/output.txt", "w+") as file:
    file.write(f"{h}h {m}m {s}s HelloWorld\n")