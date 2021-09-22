import logging, os, platform

if platform.platform().startswith("Windows"):
    logging_file = os.path.join(os.getenv("HOMEDRIVE"), os.getenv("HOMEPATH"), "test.log")
else:
    logging_file = os.path.join(os.getenv("Home"), "test.log")

print("Save log in", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s : %(levelname)s : %(message)s",
    filename=logging_file,
    filemode="w",
)

logging.debug("Program beginning")
logging.info("Some actions")
logging.warning("Program ending")
