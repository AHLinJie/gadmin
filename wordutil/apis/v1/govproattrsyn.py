# coding=utf-8
from __future__ import unicode_literals, absolute_import
import logging
import operator

logger = logging.getLogger(__name__)


def get_attr_synonym_by_word(word):
    # type: (text_type) -> List[Dict[str, text_type]]
    """找出 一个 词的 近义词
    """
    from ...models.govproattr import GovProAttrSyn
    return GovProAttrSyn.object.valid_syn().filter(main_word=word).values('attribute_field', 'synonym_word')


def _simple_deal(main_word, sample_words):
    """
    简单处理, 找出 sample_words 列表中 和 main_word 词义相近的词
    :param main_word:
    :param sample_words:
    :return:
    """
    res = []
    for s in sample_words:
        if abs(len(s) - len(main_word)) < 8:
            res.append(s)
    return res


def _cal_word_lib_point(main_word, lib_words):
    # type: (text_type, List[text_type]) -> int
    """
    计算 main_word 的 相似分值
    :param main_word: 被评分词
    :param lib_words: 近义词 词库
    :return:
    """
    main_word = main_word.replace(' ', '')
    total_point = 100  # 根据 遍历 次数(给分次数) 平分100数值 如果是 2次 循环给分 则 每个循环前
    for_1_total_point = 40
    for_2_total_point = 60

    lib_words = ''.join(lib_words)
    for_2_get_point = 0
    if len(main_word) > 2:  # 大于两个字的情况 比较
        data = []
        t = ''
        for k, v in enumerate(main_word):
            if k % 2 == 0:
                data.append(t)
                t = ''
            t = t + v
        for_2_s_point = for_2_total_point / len(data) - 1
        count_2 = 0
        for i in data[1::]:
            if i in lib_words:
                count_2 += 1
        for_2_get_point = for_2_s_point * count_2
    elif len(main_word) == 2:
        if main_word in lib_words:
            for_2_get_point = for_2_total_point  # 第二次满分
    else:
        for_1_total_point = total_point
    for_1_s_point = for_1_total_point / len(main_word)
    count = 0
    for one in main_word:
        if one in lib_words:
            count += 1
    for_1_get_point = for_1_s_point * count
    return for_1_get_point, for_2_get_point


def synonym_service(main_word, sample_words):
    # type: (text_type, List[text_type]) -> List[text_type]
    """
    相似词识别, 找出 sample_words 列表中 和 main_word 词义相近的词
    :param main_word: 对比词 (属性名称)
    :param sample_words: 样本词 (分词结果 或者是 分词处理后的结果)
    :return: 相似词
    """
    res = _simple_deal(main_word, sample_words)  # 简单词相似处理
    ws_lib = get_attr_synonym_by_word(main_word)
    if not ws_lib:  # 没有近义词  对应词库
        return res
    lib_words = [i['synonym_word'] for i in ws_lib]  # 近义词 词库列表
    r_points = {}
    for r in res:
        if r in lib_words:
            r_points[r] = 100  # 在同义词词库中则为100分
        else:
            point = _cal_word_lib_point(r, lib_words)  # 计算某个词 和对应词库的 得分
            r_points[r] = point
    return sorted(r_points.items(), key=operator.itemgetter(1))  # 按照 分值 排序的 元组列表返回


def add_synonym_word_2_db(word, attname):
    # type: (text_type, text_type) -> Tuple[text_type, text_type, text_type]
    """
    添加同义词到数据库
    :param word:
    :param attname:
    :return:
    """
    from govbuy.apis.v1.govproject import get_gov_project_model_fields
    from ...models import GovProAttrSyn
    fields = get_gov_project_model_fields()
    for f in fields:
        if f.attname == attname:
            syn, state = GovProAttrSyn.object.get_or_create(
                main_word=f.verbose_name,
                synonym_word=word)
            syn.attribute_field = f.attname
            syn.save()
            code = 1 if state else 0
            return code, syn.main_word, syn.synonym_word
    return 0, '', ''
