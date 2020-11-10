import scrapy

from datetime import datetime
from email.utils import format_datetime


def _format_pubdate(datetime_string):
    """Change upload datetime from yts format to RSS format (rfc822)."""
    return format_datetime(datetime.fromisoformat(datetime_string))


def _torrent_sort_key(torrent):
    """Torrent priority.

    Always download BlueRay version if available, prefer 1080p over 720p.
    """
    return (torrent["type"] == "blueray", torrent["quality"] == "1080p", torrent["quality"] == "720p")


class YTSSpider(scrapy.Spider):
    """Scrape movie information from yts.mx."""

    def parse_api(self, response):
        """Extract movie data from yts API."""
        for movie in response.json()["data"].get("movies", []):
            best_fit = max(movie["torrents"], key=_torrent_sort_key)
            yield {
                "title": movie["title_long"],
                "description": movie["summary"],
                "link": movie["url"],
                "guid": f"{movie['url']}#{best_fit['quality']}",
                "pubDate": _format_pubdate(movie["date_uploaded"]),
                "download_link": best_fit["url"],
            }
