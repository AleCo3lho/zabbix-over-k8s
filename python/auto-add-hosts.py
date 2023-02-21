import apizabbix
import csv
from progressbar import ProgressBar, Percentage, ETA, ReverseBar, RotatingMarker, Timer

zapi = apizabbix.connect()

arq = csv.reader(open('../csv/hosts.csv'))

linhas = sum(1 for linha in arq)

f = csv.reader(open('../csv/hosts.csv'), delimiter=';')
bar = ProgressBar(maxval=linhas,widgets=[Percentage(), ReverseBar(), ETA(), RotatingMarker(), Timer()]).start()
i = 0

for [hostname] in f:
    hostcriado = zapi.host.create(
        host=hostname,
        status= 0,
        interfaces=[{
            "type": 1,
            "main": "1",
            "ip": "",
            "useip": 0,
            "dns": "zabbix-agent.zabbix.svc.cluster.local",
            "port": 10050
        }],
        groups=[{
            "groupid": 23
        }],
        templates=[
        {
            "templateid": 10413
        },
        {
            "templateid": 10564
        }
        ],
        macros=[
            {
                "macro": "{$CERT.WEBSITE.HOSTNAME}",
                "value": hostname
            },
            {
                "macro": "{$WEB.URL}",
                "value": hostname
            }
        ]
    )

    print(hostcriado)
    i += 1
    bar.update(i)

zapi.user.logout()
bar.finish