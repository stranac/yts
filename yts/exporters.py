from scrapy.exporters import XmlItemExporter


class BitTorrentRSSExporter(XmlItemExporter):
    def __init__(self, file, **kwargs):
        kwargs["root_element"] = "rss"
        super().__init__(file, **kwargs, dont_fail=True)

    def start_exporting(self):
        self.xg.startDocument()
        self.xg.startElement(self.root_element, {"version": "2.0"})
        self._beautify_newline()

        self.xg.startElement("channel", {})
        self._beautify_newline()

        self._beautify_indent()
        self.xg.startElement("title", {})
        self.xg.characters(self._kwargs["feed_title"])
        self.xg.endElement("title")
        self._beautify_newline()

        self._beautify_indent()
        self.xg.startElement("description", {})
        self.xg.characters(self._kwargs["feed_description"])
        self.xg.endElement("description")
        self._beautify_newline()

    def _export_xml_field(self, name, serialized_value, depth):

        if name == "download_link":
            self._beautify_indent(depth=depth)
            self.xg.startElement("enclosure", {"url": serialized_value, "type": "application/x-bittorrent"})
            self.xg.endElement("enclosure")
            self._beautify_newline()
        else:
            super()._export_xml_field(name, serialized_value, depth)

    def finish_exporting(self):
        self.xg.endElement("channel")
        self._beautify_newline()
        super().finish_exporting()
