from sample.mail_list_generator import MailListGenerator
from sample.ldif_parser import LdifParser
from data.data import ldif_file, renters, again_renters, mail_list_names, list_divider

mail_lists = MailListGenerator([renters, again_renters], mail_list_names, list_divider).parse_all()
LdifParser(ldif_file, mail_lists).write_ldif()
