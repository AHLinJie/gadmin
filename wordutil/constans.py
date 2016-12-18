# coding=utf-8
from __future__ import unicode_literals, absolute_import
import logging

logger = logging.getLogger(__name__)

DEFAULT_DICT_LIB = 'default_dict_lib'  # 默认词库
GOV_PRO_DICT_LIB = 'gov_pro_dict_lib'  # 政府项目词库
URI_DICT_LIB = 'uri_dict_lib'  # 网址链接词库
PHONE_DICT_LIB = 'phone_dict_lib'  # 联系电话

# 词库命名
JIEBA_CUSTOM_LIBS = (
    (DEFAULT_DICT_LIB, '默认词库'),
    (GOV_PRO_DICT_LIB, '政府项目词库'),
    (URI_DICT_LIB, '网址链接词库'),
    (PHONE_DICT_LIB, '联系电话词库'),
)

# 词库路径

DICT_LIB_DIR = 'jiebadic'
