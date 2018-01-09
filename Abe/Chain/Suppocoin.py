# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from .X11Chain import X11Chain

class Suppocoin(X11Chain):
    def __init__(chain, **kwargs):
        chain.name = 'Suppocoin'
        chain.code3 = 'SUPPO'
        chain.address_version = '\x3f'
        chain.script_addr_vers = '\x05'
        chain.magic = '\xbf\x0c\x6b\xbd'
        X11Chain.__init__(chain, **kwargs)

    datadir_conf_file_name = 'suppo.conf'
    datadir_rpcport = 7778
    datadir_p2pport = 7777