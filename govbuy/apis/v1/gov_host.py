# coding=utf-8
from __future__ import unicode_literals, absolute_import
import os
import jieba
import re
import datetime
import logging
from ...models import GovHostInfo, CrawlPage
from wordutil.constans import JIEBA_CUSTOM_LIBS
from django.conf import settings

logger = logging.getLogger(__name__)


def get_govs_purchase_urls_list():
    # type: () -> Optional[List[GovHostInfo]]
    """获取采购页面地址列表
    """
    gs = GovHostInfo.objects.is_open_hosts()
    data = []
    for g in gs:
        data.append(g.purchase_url)
    return data


def get_host_id_by_host_url(host_url):
    return GovHostInfo.objects.get(host_url=host_url).id


def get_govs_purchase_urls_list_by_gov_name(name):
    # type: (text_type) -> Optional[List[text_type]]
    """通过网站名称获取主站链接
    """
    gs = GovHostInfo.objects.filter(name=name)
    data = []
    for g in gs:
        data.append(g.purchase_url)
    return data


def get_crawl_by_id(id):
    return CrawlPage.objects.get(id=id)


def get_crawl_page_by_host_and_project_page_url(host_id, project_page_url):
    # type:(int, text_type) -> Optional[CrawlPage]
    """获取列表页面记录(根据主站链接和内容页路径)
    """
    cp = CrawlPage.objects.filter(host_id=host_id, project_page_url__endswith=project_page_url).first()
    if cp:
        return cp
    return CrawlPage.objects.filter(project_page_url__endswith=project_page_url).first()


def get_uncrawled_purchase_urls():
    # type:() -> Optional[List[text_type]]
    """获取没有爬取过的项目内容也地址
    """
    gs = CrawlPage.objects.filter(is_crawled=False)
    data = []
    for g in gs:
        data.append(g.project_page_link())
    return data


def crawled_detail_page_content(crawl_url, project_name, project_content):
    # type: (text_type, text_type, text_type) -> None
    """保存爬虫 爬取的 项目 详情页面内容
    """
    host_url = crawl_url.split('/')[2]
    project_page_url = '/' + '/'.join(crawl_url.split('/')[3::])
    host_id = get_host_id_by_host_url('http://' + host_url.strip())
    crawlpage = get_crawl_page_by_host_and_project_page_url(host_id, project_page_url)
    now = datetime.datetime.now()
    if not crawlpage:
        print '从爬虫没有找到项目爬虫url:%s' % crawl_url
    if project_name and project_content:
        if len(project_name) < 64:
            crawlpage.logogram = project_name.strip()
        crawlpage.crawl_time = now
        crawlpage.html_source_code = project_content.strip()
        crawlpage.is_crawled = True
        crawlpage.save()


def jieba_fenci_for_crawl_doc(doc):
    """结巴分词
    """
    for lib in JIEBA_CUSTOM_LIBS:
        prodict = os.path.join(settings.STATICFILES_DIRS[0], 'jiebadic', lib[0])
        try:
            jieba.load_userdict(prodict)
        except IOError:
            continue

    rs = ['\xa0',
          '一、',
          '二、',
          '三、',
          '四、',
          '五、',
          '六、',
          '七、',
          '八、',
          '九、',
          '十、']
    for r in rs:
        doc = doc.replace(r, '')
    regex = re.compile(r'[\n\r\t,.:\-"；（）。、：，的<>》《()]')  # 去除换行 回车 制表符 中文标点符号
    t = regex.sub("", doc)
    fenci_data = jieba.tokenize(t)  # 结巴分词
    return fenci_data
