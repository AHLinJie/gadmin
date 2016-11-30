# coding=utf-8
from __future__ import print_function, absolute_import
from . import html_downloader
from . import html_outputer
from . import html_parser
from . import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, route_url):
        count = 1
        self.urls.add_new_url(route_url)

        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print("craw %d : %s" % (count, new_url))
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)
            count += 1
            if count == 30:
                break

        self.outputer.output_html()
