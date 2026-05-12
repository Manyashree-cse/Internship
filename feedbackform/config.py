import os                                # os → helps Python talk to your system (like environment variables)
from dotenv import load_dotenv           #load_dotenv → loads values from your .env file

load_dotenv()                            # Python reads your .env file

DB_HOST = os.getenv("DB_HOST")           #os.getenv-“Go to environment variables and get this value”
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

DEBUG = os.getenv("DEBUG") == "True"
                                         #It checks if the DEBUG value from the .env file is "True" and 
                                         # converts it into a boolean (True or False) for your Python program.