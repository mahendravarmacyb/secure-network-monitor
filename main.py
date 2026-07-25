from utils.logger import setup_logger
from utils.config import Config
from database_manager.database import Database


def main():
    # Initialize components
    logger = setup_logger()
    config = Config()
    db = Database()

    db.initialize()

    logger.info("Secure Network Monitor Started")

    while True:
        print("\n" + "=" * 40)
        print("   Secure Network Monitor")
        print("=" * 40)
        print("1. Host Discovery")
        print("2. Exit")
        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nHost Discovery Module (Coming Next Phase)")
            logger.info("Host Discovery selected")

        elif choice == "2":
            logger.info("Application Closed")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            logger.warning("Invalid menu option selected")


if __name__ == "__main__":
    main()
