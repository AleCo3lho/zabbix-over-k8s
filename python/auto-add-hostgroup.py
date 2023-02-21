import apizabbix
import csv
from progressbar import ProgressBar, Percentage, ETA, ReverseBar, RotatingMarker, Timer

zapi = apizabbix.connect()


group = "meu-hostgroup"
hostcriado = zapi.hostgroup.create(name=group)
print(hostcriado)
zapi.user.logout()