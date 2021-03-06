#
# Copyright (c) 2013 Citrix Systems, Inc.
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

from bvtlib.mongodb import get_autotest

class UnableToFindLatestRelease(Exception):
    """Autotest database has no latest release"""

def latest_release():
    """Get latest release"""
    mdb = get_autotest()
    latest = mdb.releases.find_one({'_id':'latest'})
    if latest is None:
        raise UnableToFindLatestRelease()
    return latest
