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
            apartment = clean(excel_sheet.cell(row, 0).value).replace(' ', '_')
            emails = clean(excel_sheet.cell(row, mail_col).value).replace(' ', '')

            self.__set_value(current_list_index, emails)

            if self.__reached_divider_row(apartment):
                current_list_index = 1

    @staticmethod
    def __set_list_to(new_list):
        global mail_list
        mail_list = new_list

    def __set_value(self, email_list_index, values):
        if values:
            emails = values.split('/')

            for email in emails:
                if not valid_email(email):
                    emails.remove(email)

            self.mail_lists[email_list_index]['emails'].extend(emails)

    def __reached_divider_row(self, apartment):
        return apartment == self.list_divider
