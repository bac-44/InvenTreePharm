#!/usr/bin/env python3
from getpass import getpass

import pandas as pd
import requests
from requests.auth import HTTPBasicAuth


API_ROOT = "http://52.15.243.0/api"
MAX_RETRIES = 3


def run():
    username = input("Username: ")
    password = getpass("Password: ")

    df = pd.read_csv("./ingredient-list.csv", dtype=str, keep_default_na=False)
    for index, row in df.iterrows():
        description = row["Description"]
        code = row["Code"]
        print(f"Processing row {index} with Code {code}")

        if code == "":
            print(f"Skipping row {index}, invalid code")
            continue

        request_body = {
            "IPN": code,
            "name": description,
            "description": "Imported ingredient",
            "tags": ["csv_to_api_import"],
            # This is a generated property controlled by the PART_NAME_FORMAT setting:
            #"full_name": description,
        }

        retry_count = 0
        should_retry = True
        while retry_count < MAX_RETRIES and should_retry:
            retry_count += 1
            print(f"Sending creation request (attempt {retry_count}/{MAX_RETRIES})")

            response = requests.post(
                f"{API_ROOT}/part/",
                json=request_body,
                auth=HTTPBasicAuth(username, password),
            )

            if response.status_code == 400:
                errors = response.json()
                if errors["non_field_errors"] == ["Part with this Name, IPN and Revision already exists.", "Part with this Name, IPN and Revision already exists."]:
                    print(f"Skipping part {code}, already exists")
                    should_retry = False
                    continue

            if response.status_code == 502:
                print("Bad gateway, retrying")
                continue

            try:
                response.raise_for_status()
            except Exception as e:
                breakpoint()
                print(response.text)
                raise

            print(f"Part created: {response}")
            should_retry = False

    print("Script done")


if __name__ == "__main__":
    run()
