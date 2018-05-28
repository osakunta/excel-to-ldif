from sample.mail_list_generator import MailListGenerator
from sample.ldif_parser import LdifParser
from data.data import ldif_file, residents, renters, again_renters

MailListGenerator([renters, again_renters]).parse_all()
LdifParser(ldif_file, residents).write_ldif()
