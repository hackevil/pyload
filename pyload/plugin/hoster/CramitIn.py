# -*- coding: utf-8 -*-

from pyload.plugin.internal.XFSHoster import XFSHoster


class CramitIn(XFSHoster):
    __name__    = "CramitIn"
    __type__    = "hoster"
    __version__ = "0.07"

    __pattern__ = r'http://(?:www\.)?cramit\.in/\w{12}'

    __description__ = """Cramit.in hoster plugin"""
    __license__     = "GPLv3"
    __authors__     = [("zoidberg", "zoidberg@mujmail.cz")]


    INFO_PATTERN = r'<span class=t2>\s*(?P<N>.*?)</span>.*?<small>\s*\((?P<S>.*?)\)'

    LINK_PATTERN = r'href="(http://cramit\.in/file_download/.*?)"'