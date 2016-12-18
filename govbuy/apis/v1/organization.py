# coding=utf-8
from __future__ import unicode_literals, absolute_import
import logging

logger = logging.getLogger(__name__)


def add_organization(name, org_type):
    # type: (text_type, text_type) -> int, Organization
    """
    添加机构信息
    :param name:　机构名称
    :param org_type:　机构类型
    :return:　int, organization
    """
    from ...models import Organization
    if org_type not in [i[0] for i in Organization.ORG_TYPES]:
        raise Exception('机构类型错误!')
    if not name.strip():
        raise Exception('名称不能为空!')
    org, state = Organization.objects.get_or_create(
        org_type=org_type,
        name=name)
    code = 1 if state else 0
    return code, org


def get_org_by_name(name):
    # type: (text_type) -> Optional[Organization]
    """
    通过名称找组织机构
    :param name:
    :return:　组织或机构
    """
    from ...models import Organization
    return Organization.objects.filter(name=name.strip()).first()
