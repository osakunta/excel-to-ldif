#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# Contains all the excel and mail list data
from data.data import *
from sample.cleaner import clean
from sample.slack import *

def validate_email(email, can_be_blank, line):
    regex = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")

    #print(email)

    if can_be_blank and email == '':
        return

    try:
        if not regex.match(email):
            raise ValueError

        email.encode('ascii')

    except UnicodeEncodeError or ValueError:
        print('Invalid email address "' + email + '" on row ' + str(line))

def validate_emails(excel_sheet, mail_col):
    for row in range(1, excel_sheet.nrows):
        emails = clean(excel_sheet.cell(row, mail_col).value).split('/')

        for email in emails:
            validate_email(email, True, row + 1)
