import subprocess

mylist = ["8.8.8.8", "192.168.0.5"]

def testip(mylist):
    for i in mylist:
        result = subprocess.run(["ping", "1", i], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"{i} is reachable.")
        else:
            print(f"{i} is not reachable.")
testip(mylist)
