#
# Copyright (C) 2011 by Hartmut Goebel
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA

__all__ = ('HOMEPATH', 'CONFIGDIR', 'DEFAULT_CONFIGFILE',
           'is_py23', 'is_py24', 'is_py25', 'is_py26', 'is_py27',
           'is_win', 'is_cygwin', 'is_darwin', 'hashlib')

import os
import sys

is_py23 = sys.version_info >= (2,3)
is_py24 = sys.version_info >= (2,4)
is_py25 = sys.version_info >= (2,5)
is_py26 = sys.version_info >= (2,6)
is_py27 = sys.version_info >= (2,7)

is_win = sys.platform.startswith('win')
is_cygwin = sys.platform == 'cygwin'
is_darwin = sys.platform == 'darwin'

HOMEPATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

if is_win:
    CONFIGDIR = os.environ['APPDATA']
    if not CONFIGDIR:
        CONFIGDIR = os.path.expanduser('~\\Application Data')
elif is_darwin:
    CONFIGDIR = os.path.expanduser('~/Library/Application Support')
else:
    # According to XDG specification
    # http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
    CONFIGDIR = os.environ.get('XDG_DATA_HOME', None)
    if CONFIGDIR is None:
        CONFIGDIR = os.path.expanduser('~/.local/share')
CONFIGDIR = os.path.join(CONFIGDIR, 'pyinstaller')

DEFAULT_CONFIGFILE = os.path.join(CONFIGDIR, 'config.dat')


# For Python compatibility
try:
    # Python 2.5+
    import hashlib
except ImportError:
    import md5
    import sha
    class _Hash(object):
        def __init__(self):
            self.md5 = md5.new
            self.sha = sha.new
    hashlib = _Hash()
