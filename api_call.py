log=[]
attempts=0
max_retries=3
success=False

def mock_api():
    return "fail" if attempts<2 else "success"

while attempts < max_retries:
    attempts+=1
    result=mock_api()
    log.append(f"Attempt {attempts}: {result}")
    if result=="success":
        success=True
        break
    else:
        log.append("Retrying...")
if success:
    log.append("API call succeeded.")
else:
    log.append("API call failed after max retries.")        

print("\n".join(log))
