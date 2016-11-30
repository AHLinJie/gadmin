# coding=utf-8
from __future__ import unicode_literals, absolute_import
import logging
from ...models import GovHostInfo

logger = logging.getLogger(__name__)


def get_govs_purchase_urls_list():
    # type: () -> Optional[List[GovHostInfo]]
    """获取采购页面地址列表
    """
    gs = GovHostInfo.objects.all()
    data = []
    for g in gs:
        data.append(g.purchase_url)
    return data
