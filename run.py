from sample.mail_list_generator import *
from sample.ldif_parser import LdifParser
from data.data import ldif_file, residents

parse_all()
LdifParser(ldif_file, residents).write_ldif()
