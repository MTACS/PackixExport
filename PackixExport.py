#!/usr/bin/python

import sys
import json

if len(sys.argv) < 2:
    sys.exit("You need to specify an input file containing the API output");

inputfile = sys.argv[1]

with open(inputfile) as file_contents:
    data = json.load(file_contents)
    exported = 0
    uncompleted = 0
    anonymous = 0

    stripe = 0
    paypal = 0

    for index, transaction in enumerate(data):
        if transaction["status"] != "Completed":
            uncompleted += 1
            continue

        if transaction["stripe"]:
            payment = transaction["stripe"]
            stripe += 1
        elif transaction["paypal"]:
            payment = transaction["paypal"]
            paypal += 1
        else:
            print("Found no payment for index {}".format(index))
            continue

        email = payment["payer"]["email"]
        if email == "Unknown":
            anonymous += 1
            print("Found an anonymous checkout at index {}".format(index))
            continue

        exported += 1
        print("email: {}, date: {}".format(email, transaction["createdOn"]))
    print("\n\nTotal entries: {}\nExported: {}\nUncompleted: {}\nAnonymous: {}".format(len(data), exported, uncompleted, anonymous))
