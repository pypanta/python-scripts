#!/usr/bin/python2

from os import statvfs
from gi.repository import Notify


partitions = ('/', '/home', '/data')
limit = 2000
for partition in partitions:
    s = statvfs(partition)
    st = (s.f_bsize * s.f_bavail) / 1048576  #MiB
    if st < limit:
        Notify.init("Monitor Particija Hard Diska")
        n = Notify.Notification.new("UPOZORENJE!",
                                    "Particija %s je skoro puna. Dostupno %d MiB" % (partition, st), "dialog-warning")
        n.set_timeout(10000)
        n.show()
    else:
        pass
