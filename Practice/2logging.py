import logging

logging.basicConfig(level=logging.INFO)
for i in range(1, 6):
    logging.info("Counting Start SuccessFully!....")
    print(i)
    logging.info("Counting End SuccessFully!....")

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')
