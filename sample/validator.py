#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from sample.cleaner import clean
from sample.slack import slack_message, send_slack_notification


def valid_email(email):
    regex = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")

    if email == '':
        return True

    if not regex.match(email):
        return False

    try:
        email.encode('ascii')
    except UnicodeEncodeError:
        return False

    return True


def validate_emails(excel_sheet, mail_col):
    for row in range(1, excel_sheet.nrows):
        emails = clean(excel_sheet.cell(row, mail_col).value).split('/')

        for email in emails:
            if not valid_email(email.strip()):
                send_slack_notification(
                    slack_message(
                        'Virheellinen sähköpostiosoite', 'Osoite "' + email + '" on virheellinen.',
                        excel_sheet.name,
                        str(row + 1)
                    )
                )
