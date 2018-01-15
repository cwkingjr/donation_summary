#!/usr/bin/env python3

import csv

donations = {}

with open('raw_donations.csv', 'r') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        fundraiser_in_memory = row[0]
        amount = float(row[1])
        first_name = row[2]
        last_name = row[3]
        email = row[4]

        # we want to exclude these because they are duplicates
        if fundraiser_in_memory.strip() == 'FIM':
            continue

        if email not in donations:
            donations[email] = {'first_name': first_name,
                                'last_name' : last_name,
                                'amount' : amount,
                                'largest_donation' : amount,
                                'count' : 1
                               }
        else:
            donations[email]['count'] += 1
            donations[email]['amount'] += amount
            if amount > donations[email]['largest_donation']:
                donations[email]['largest_donation'] = amount

print('email, lastName, firstName, totalAmount, donationCount, averageDonation, largestDonation')
for email in donations:
    avg = donations[email]['amount'] / donations[email]['count']
    largest_donation = donations[email]['largest_donation']
    # some folks put commas in their last name field (e.g., "Lastname, MD")
    last_name = '"%s"' % donations[email]['last_name']
    first_name = '"%s"' % donations[email]['first_name']
    amount = donations[email]['amount']
    count = donations[email]['count']
    print("%s,%s,%s,%.2f,%d,%.2f,%.2f" % (email, last_name, first_name, amount, count, avg, largest_donation))
