import pandas as pd
from dotenv import load_dotenv
from aocd import get_data
import os

load_dotenv()

if __name__ == "__main__":
    AOCD_SESSION = os.getenv('AOCD_SESSION')

    get_data(session=AOCD_SESSION, 
             day=1,
             year=2025)