import shutil
import duckdb
from datetime import datetime

def greeting():
    print(f"Hello from cron job! Current time: {datetime.now()}")
    print_hello()

def print_hello():
    print("Hello World greeting finished")

def duckdb_read():
    temp_db = "sample_temp.db"
    shutil.copy("sample.db", temp_db)
    con = duckdb.connect(temp_db)

    results = con.sql("SELECT count(*) FROM taxi;")
    print(results)

if __name__ == "__main__":
    greeting()
    duckdb_read()
