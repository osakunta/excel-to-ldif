#!/bin/bash

cd /app/monitoring-scripts/excel-to-ldif/

python3 run.py

cd /app/vagrant/ldap

vagrant ssh -- -t './update-ldap.sh'
