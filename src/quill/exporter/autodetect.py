"""
Automatically Detect Exporter from File Extension
"""

from quill.exporter.base import QuillExporterError


def autodetect_exporter(filename):
    f = filename.lower()
    if f.endswith('.svg'):
        from quill.exporter.svg import Svg
        return Svg(filename)
    if f.endswith('.pdf'):
        from quill.exporter.pdf import Pdf
        return Pdf(filename)
    if f.endswith('.ps'):
        from quill.exporter.ps import Postscript
        return Postscript(filename)
    if f.endswith('.xoj'):
        from quill.exporter.xournal import Xournal
        return Xournal(filename)
    if f.endswith('.quill'):
        from quill.exporter.quill_exporter import QuillExporter
        return QuillExporter(filename)
    raise QuillExporterError('cannot export '+filename)

