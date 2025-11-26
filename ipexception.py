import subprocess

mylist = ["8.8.8.8", "192.168.0.5"]

def testip(mylist):
    for i in mylist:
        try:

            result = subprocess.run(["ping", "-n", "1", i], capture_output=True, text=True)

            if result.returncode == 0:

                # Check ping time if "time=" exists
                if "time=" in result.stdout:
                    # Extract something like: time=23ms
                    part = result.stdout.split("time=")[1].split()[0]
                    ms = float(part.replace("ms", ""))

                    # Condition for slow ping
                    if ms > 20:
                        raise Exception("Slow Ping")

                print(f"{i} reachable")

            else:
                print(f"{i} not reachable")

        except Exception as e:
            print(f"{i} - Exception: {e}")

testip(mylist)


