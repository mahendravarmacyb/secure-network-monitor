import logging
import os

def setup_logger():
# ensure that if already exists don't throw error
    os.makedirs("logs",exist_ok = True)

    logger = logging.getLogger("Secure Network Monitor")
    logger.setLevel(logging.INFO)

# ensure to avoid duplicates

    if logger.hasHandlers():
        return logger

   # get record a log file
    file_handler = logging.FileHandler("logs/network_monitor.log")
 # Console output
    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == "__main__":
    logger = setup_logger()

    logger.info("Logger initialized successfully.")
    logger.warning("This is a warning.")
    logger.error("This is an error.")
