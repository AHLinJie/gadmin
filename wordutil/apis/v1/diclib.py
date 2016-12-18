# coding=utf-8
from __future__ import unicode_literals, absolute_import
import os
from ...constans import *
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def word_dict_lib(word=None, dict_lib_name=DEFAULT_DICT_LIB, tail_num=30):
    # type: (Optional[text_type], text_type, int) -> List[text_type]
    """
    添加单词到词库文件
    :param word: 要添加的词 unicode 类型
    :param dict_lib_name: 词库名称
    :param tail_num: 要读取的文件尾行数
    :return: (code, 词库后30行)  code=0 表示没有追加，　code=1 表示追加了
    """
    dic_path = os.path.join(settings.STATICFILES_DIRS[0], DICT_LIB_DIR, dict_lib_name)
    # 没有文件则创建
    word = word.strip()

    def write_file(fp):
        if word is None:
            code = 0
        elif word in fp.readlines():  # 判断 word 是否在文件中(行级匹配) 不在 则添加到最后一行
            code = 0
        else:
            fp.write(word)  # 有则将 word 追加到最后一行
            fp.write(str('\n'))
            code = 1
        return code

    try:
        word = word.encode('utf-8')  # 将unicode编码的字符串转化为utf-8编码
    except UnicodeDecodeError:
        word = word.decode('utf-8')
    with open(dic_path, 'a+') as fp:
        try:
            code = write_file(fp)
        except UnicodeDecodeError:
            word = word.encode('utf-8')
            code = write_file(fp)
    tail_line_str = os.popen('tail -n %s %s' % (tail_num, dic_path)).read()  # 文件尾部
    tail_line_str = tail_line_str.decode('utf-8')  # 原始的tail_line_str utf-8编码的字符串转换为unicode编码
    return code, [i for i in tail_line_str.split('\n') if i]  # 读取最后 tails_num 行
