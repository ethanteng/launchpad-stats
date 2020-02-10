# this outputs the download count of a PPA
#
# See https://api.launchpad.net/+apidoc/devel.html#binary_package_publishing_history
# See https://help.launchpad.net/API/launchpadlib

from launchpadlib.launchpad import Launchpad
import os

cachedir = os.environ['HOME'] + '/.launchpadlib/cache/'
launchpad = Launchpad.login_anonymously('just testing', 'production', cachedir)

ppa = launchpad.people['gridcoin'].getPPAByName(name='gridcoin-stable')
binaries = ppa.getPublishedBinaries(binary_name='gridcoinresearch', version='4.0.6.0-45~ubuntu16.04.1')
b1 = binaries[0]
print(b1.getDownloadCount())
#print(b1.getDailyDownloadTotals(start_date='2020-01-01', end_date='2020-01-31'))
