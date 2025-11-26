import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

Example = [20, 35, 50, 10, 60, 45]

def calculate_average(data):
    return sum(data) / len(data)

def get_summary(data):
    return {
        "min": min(data),
        "max": max(data),
        "average": calculate_average(data)
    }


result = get_summary(Example)
print(result)