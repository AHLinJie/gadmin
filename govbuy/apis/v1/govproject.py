# coding=utf-8
from __future__ import unicode_literals, absolute_import
import logging
from .gov_host import jieba_fenci_for_crawl_doc

logger = logging.getLogger(__name__)


def get_gov_project_model_fields():
    """
    获取 GovProject Model 的属性
    :return:
    """
    from ...models import GovProject
    fields = GovProject._meta.get_fields()
    return fields


def add_gov_project(name, issue_date, *args, **kwargs):
    # type: (text_type, text_type) -> bool, GovProject
    """
    添加项目信息
    :param name:　项目名称
    :param issue_date:　发布时间
    :param args:　
    :param kwargs:　其他数据
    :return:　bool, instance
    """
    from ...models import GovProject
    from .organization import get_org_by_name
    # 根据招标机构名称填写　招标机构id
    bid_person = kwargs.get('bid_person')  # 招标人
    org = get_org_by_name(bid_person)  # 通过招标人找招标机构
    p, state = GovProject.objects.get_or_create(
        bid_org_id=org.id,
        name=name,
        issue_date=issue_date
    )
    issue_org_name = kwargs.get('issue_org_name')  # 发布机构
    agency_org_name = kwargs.get('agency_org_name')  # 代理机构
    if issue_org_name:
        org = get_org_by_name(issue_org_name)
        if org:
            kwargs.update({'issue_org_id': org.id})  # 填写发布机构id
    if agency_org_name:
        org = get_org_by_name(agency_org_name)
        if org:
            kwargs.update({'agency_org_id': org.id})  # 填写代理机构id

    for k, v in kwargs.iteritems():
        if hasattr(p, k) and v and getattr(p, k) != v:
            setattr(p, k, v)
    p.save()
    return state, p


def get_gov_project_model_attr_list():
    fds = get_gov_project_model_fields()
    return [{'attname': fd.attname, 'verbose_name': fd.verbose_name} for fd in fds]


def update_project_by_crawl_doc(doc):
    """
    根据爬虫爬取内容 填写项目的数据
    :return:
    """
    from wordutil.apis.v1.govproattrsyn import get_gov_project_syn_att_list
    fenci = jieba_fenci_for_crawl_doc(doc=doc)
    atts = get_gov_project_syn_att_list()

    new_doc = ''
    for d in fenci:
        new_doc += d[0]
        for att in atts:
            if d[0] in att['att_set']:
                att['att_index_start'] = d[1]  # 2: 分词元组的最后一个元素,即最后一个index
                att['att_index_end'] = d[2]  # 2: 分词元组的最后一个元素,即最后一个index

    atts = sorted(atts, key=lambda k: k['att_index_start'])  # 排序 准备取值
    max_len = len(atts)
    for n, att in enumerate(atts):
        if att['att_index_start'] is None:
            continue
        if n + 1 > max_len:
            break
        if n + 1 == max_len:
            value = new_doc[att['att_index_end']::]
        else:
            value = new_doc[att['att_index_end'] + 1: atts[n + 1]['att_index_start']]
        print att['attname'], att['verbose_name'], '==>', value
