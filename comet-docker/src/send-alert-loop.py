#!/usr/bin/env python
"""
 Run a VOEvent sending loop

    Arguments:
       1: host (e.g. 'comet-broker')
       2: interval (e.g. 1 = 1 second)
       3: max runtime (e.g. 60 = 60 seconds)

"""

import fourpiskytools
from fourpiskytools.identity import id_keys
import voeventparse
import time
from threading import Event, Thread
import logging
from subprocess import call
from time import sleep
import sys
from threading import Timer

logging.basicConfig(filename='/home/comet/logs/comet.log',level=logging.INFO)

identity = {
    id_keys.address : 'voevent.organization.tld',
    id_keys.stream : 'ProjectFooAlerts',
    id_keys.shortName : 'ProjectFoo',
    id_keys.contactName : "Jo Bloggs",
    id_keys.contactEmail : "jb@observatory.org",
    }



class RepeatedTimer(object):
    def __init__(self, interval, function, host, identity, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.host = host
        self.test_packet = fourpiskytools.voevent.create_test_packet(identity)
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def main():
    """
    Run a VOEvent sending loop

    Arguments:
       1: host (e.g. 'comet-broker')
       2: interval (e.g. 1 = 1 second)
       3: max runtime (e.g. 60 = 60 seconds)
    """

    logging.info("Starting VOEvent sending loop...")
    test_packet = fourpiskytools.voevent.create_test_packet(identity)
    rt = RepeatedTimer(float(sys.argv[2]), call, sys.argv[1], identity, "comet-sendvo --host=" + sys.argv[1] + " --port=8098 < test_packet.xml", shell=True)
    try:
        sleep(float(sys.argv[3]))
    finally:
        rt.stop()


if __name__ == "__main__":
    main()



