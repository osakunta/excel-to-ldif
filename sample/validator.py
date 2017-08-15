#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# Contains all the excel and mail list data
from data.data import *
from sample.cleaner import clean
from sample.slack import *

def valid_email(email, can_be_blank):
    regex = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")

    if can_be_blank and email == '':
        return True

    if not regex.match(email):
        return False

    try:
        email.encode('ascii')
    except UnicodeEncodeError:
        return False

    return True

def validate_emails(excel_sheet, mail_col, can_be_blank):
    for row in range(1, excel_sheet.nrows):
        emails = clean(excel_sheet.cell(row, mail_col).value).split('/')

        for email in emails:
            if not valid_email(email.strip(), can_be_blank):
                print(slack_message(
                    'Virheellinen sähköpostiosoite', 'Osoite "' + email + '" on virheellinen.',
                    excel_sheet.name,
                    str(row + 1)
                ))
