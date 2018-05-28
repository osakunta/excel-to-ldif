from sample.mail_list_generator import *
from sample.ldif_parser import LdifParser

parse_all()
LdifParser().write_ldif()
