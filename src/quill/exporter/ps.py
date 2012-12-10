"""
Export to Postscript (PS)

EXAMPLES::

    >>> from quill.exporter.ps import Postscript
    >>> from tempfile import TemporaryFile
    >>> tmp = TemporaryFile(suffix='ps')
    >>> Postscript(tmp).book(sample_book)
    Title is set to Example Notebook
    UUID is set to 1fd6a485-33ed-4a45-a5a1-e06e55fdca57
    Creation time set to 2012-12-09 14:57:25
    Last modification time set to 2012-12-09 14:57:25
"""

import cairo

from quill.exporter.cairo_surface_paginated import CairoSurfacePaginated


class Postscript(CairoSurfacePaginated):
    """
    Exporter to PS
    
    :param fileobj: a filename or a file-like object
    """
    
    def __init__(self, fileobj):
        """
        The Python constructor
        """
        surface = cairo.PSSurface(fileobj, 1, 1)
        super(Postscript, self).__init__(surface)

