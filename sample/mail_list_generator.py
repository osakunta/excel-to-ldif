#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Contains all the excel and mail list data
from data.data import divider
from sample.cleaner import clean
from sample.validator import valid_email
import json


class MailListGenerator:
    def __init__(self, excel_sheets, mail_list_names):
        self.list_divider = divider

        self.mail_lists = [
            {'name': mail_list_names[0], 'emails': []},
            {'name': mail_list_names[1], 'emails': []}
        ]

        self.excel_sheets_with_emails = [
            {'sheet': excel_sheets[0], 'email_col': 9},
            {'sheet': excel_sheets[1], 'email_col': 3}
        ]

    def parse_all(self):
        for sheet in self.excel_sheets_with_emails:
            self.__parse_emails(sheet['sheet'], sheet['email_col'])

        #print(json.dumps(residents, indent=4, sort_keys=True))
        return self.mail_lists

    def __parse_emails(self, excel_sheet, mail_col):
        current_list_index = 0

        for row in range(1, excel_sheet.nrows):
            apartment_cell = clean(excel_sheet.cell(row, 0).value)
            emails_in_one_cell = clean(excel_sheet.cell(row, mail_col).value).split('/')
            emails = list(filter(lambda email: valid_email(email), emails_in_one_cell))

            self.__extend_mail_list(current_list_index, emails)

            if self.__reached_divider_row(apartment_cell):
                current_list_index = 1

    def __extend_mail_list(self, email_list_index, emails):
        self.mail_lists[email_list_index]['emails'].extend(emails)

    def __reached_divider_row(self, apartment):
        return apartment == self.list_divider
