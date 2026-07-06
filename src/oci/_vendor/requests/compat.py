# coding: utf-8
# Modified Work: Copyright (c) 2018, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# Copyright 2018 Kenneth Reitz

# -*- coding: utf-8 -*-

"""
requests.compat
~~~~~~~~~~~~~~~

This module handles import compatibility issues between Python 2 and
Python 3.
"""

from oci._vendor import chardet

import sys

# -------
# Pythons
# -------

# Syntax sugar.
_ver = sys.version_info

#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)

has_simplejson = False
try:
    import simplejson as json
    has_simplejson = True
except ImportError:
    import json

# ---------
# Specifics
# ---------

if is_py2:
    from urllib import (
        quote, unquote, quote_plus, unquote_plus, urlencode, getproxies,
        proxy_bypass, proxy_bypass_environment, getproxies_environment)
    from urlparse import urlparse, urlunparse, urljoin, urlsplit, urldefrag
    from urllib2 import parse_http_list
    import cookielib
    from Cookie import Morsel
    from StringIO import StringIO
    # Keep OrderedDict for backwards compatibility.
    from collections import Callable, Mapping, MutableMapping, OrderedDict

    builtin_str = str
    bytes = str
    str = unicode
    basestring = basestring
    numeric_types = (int, long, float)
    integer_types = (int, long)
    JSONDecodeError = ValueError

elif is_py3:
    from urllib.parse import urlparse, urlunparse, urljoin, urlsplit, urlencode, quote, unquote, quote_plus, unquote_plus, urldefrag  # noqa: F401
    from urllib.request import parse_http_list, getproxies, proxy_bypass, proxy_bypass_environment, getproxies_environment  # noqa: F401
    from http import cookiejar as cookielib  # noqa: F401
    from http.cookies import Morsel  # noqa: F401
    from io import StringIO  # noqa: F401
    # Keep OrderedDict for backwards compatibility.
    from collections import OrderedDict  # noqa: F401
    from collections.abc import Callable, Mapping, MutableMapping  # noqa: F401
    if has_simplejson:
        from simplejson import JSONDecodeError  # noqa: F401
    else:
        from json import JSONDecodeError  # noqa: F401

    builtin_str = str
    str = str
    bytes = bytes
    basestring = (str, bytes)
    numeric_types = (int, float)
    integer_types = (int,)
