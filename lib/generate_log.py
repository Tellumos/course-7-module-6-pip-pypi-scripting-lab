#! /usr/bin/env python3

from datetime import datetime
import requests

def generate_log(data):

    if type(data) != list:
        raise ValueError("Data is not a list")
    filename = f"log_{datetime.now().strftime("%Y%m%d")}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

fetch_data()