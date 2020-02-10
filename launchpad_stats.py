# this outputs the download count of a PPA
#
# See https://api.launchpad.net/+apidoc/devel.html#binary_package_publishing_history
# See https://help.launchpad.net/API/launchpadlib

from launchpadlib.launchpad import Launchpad
import os
import sys

USERNAME=sys.argv[1]
PPA=sys.argv[2]
PACKAGE=sys.argv[3]
VERSION=sys.argv[4]
cachedir = os.environ['HOME'] + '/.launchpadlib/cache/'
launchpad = Launchpad.login_anonymously('just testing', 'production', cachedir)

ppa = launchpad.people[USERNAME].getPPAByName(name=PPA)
bins = ppa.getPublishedBinaries(binary_name=PACKAGE, version=VERSION)
builds = []
total = 0
for bin in bins:
    count = bin.getDownloadCount()
    total += count
    if (count > 0):
        builds.append([count,'%s %s' % (bin.binary_package_name,bin.binary_package_version)])
builds_sorted = sorted(builds,key=lambda count: count[0],reverse=True)
for build in builds_sorted:
   print '%s:%s' % (build[0], build[1])
