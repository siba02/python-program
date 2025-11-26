import logging
import calculator


logging.basicConfig(filename='calculator.log',level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

def logged_calculator(x, y, op):
    logging.info(f"Calculator started with x={x}, y={y}, op='{op}'")

    try:
        result = calculator.calculator(x, y, op)
        logging.info(f"Calculator finished successfully. Result: {result}")
        return result
    
    except Exception as e:
        logging.error(f"Calculator encountered an error: {e}")
        return None



logged_calculator(10, 5,'*')