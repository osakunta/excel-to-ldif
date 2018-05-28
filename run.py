from sample.mail_list_generator import MailListGenerator
from sample.ldif_parser import LdifParser
from data.data import ldif_file, residents

MailListGenerator().parse_all()
LdifParser(ldif_file, residents).write_ldif()
