var JIEBA_DIC = '';
function addToDictInput(word) {
// 添加分词结果的单个词　到　加入词库的　输入框
    var dicLibInput = $('#input-dic-lib-word');
    var synonym = $('#input-synonym-word');
    JIEBA_DIC = JIEBA_DIC + word;
    dicLibInput.val(JIEBA_DIC);
    synonym.val('');
}
function addToSynonymInput(word) {
    var dicLibInput = $('#input-dic-lib-word');
    var synonym = $('#input-synonym-word');
    var oldv = synonym.val();
    synonym.val(oldv + word);
    dicLibInput.val('');
}
function clearDicInput() {
    // 清空　添加词库　输入框
    var dicLibInput = $('#input-dic-lib-word');
    dicLibInput.val('');
}

function clearSynonymDicInput() {
    // 清空　近义词　输入框
    var synonym = $('#input-synonym-word');
    synonym.val('');
}

var addSynonym = function (attname) {
    // type: (text_type) -> None
    //　添加同义词
    var url = '/govbuy/addsynonym/';
    var synonym = $('#input-synonym-word').val();
    var data = {'synonym_word': synonym, 'attname': attname};
    var actionDom = $('.add-word-2-synonym');
    layer.confirm('确定吗？', {
        btn: ['确定', '取消'] //按钮
    }, function () {
        if (actionDom.hasClass('loading')) {
            return
        }
        actionDom.addClass('loading');
        var func = function (res) {
            actionDom.removeClass('loading');
            layer.msg(res.info);
            $('#input-synonym-word').val('')
        };
        serverData(data, func, url, 'post');
    }, function () {
    });
};

var addJieBaDicLib = function (dictLibChoice) {
    // type: (text_type) -> None
    //　添加结巴词库
    var url = '/govbuy/addjiebadic/';
    var word = $('#input-dic-lib-word').val();
    var data = {'word': word, 'lib_choice': dictLibChoice};
    var actionDom = $('.add-word-2-jieba-dic');
    layer.confirm('确定吗？', {
        btn: ['确定', '取消'] //按钮
    }, function () {
        if (actionDom.hasClass('loading')) {
            return
        }
        actionDom.addClass('loading');
        var func = function (res) {
            actionDom.removeClass('loading');
            layer.msg(res.info);
            $('#input-dic-lib-word').val('');
            JIEBA_DIC = ''
        };
        serverData(data, func, url, 'post');
    }, function () {
    });
};

$(document).ready(function () {
    var dp = $('.date-picker');
    dp.datetimepicker({
        format: 'YYYY-MM-DD'
    });

    // 添加机构
    $("#org-add-form").on("submit", function (event) {
        // 添加　组织机构信息
        var formdata = $(this).serializeArray();
        var data = {};
        $(formdata).each(function (index, obj) {
            data[obj.name] = obj.value;
        });
        var url = '/govbuy/addorg/';
        var actionDom = $('#org-add-form');
        layer.confirm('确定吗？', {
            btn: ['确定', '取消'] //按钮
        }, function () {
            if (actionDom.hasClass('loading')) {
                return
            }
            actionDom.addClass('loading');
            var func = function (res) {
                actionDom.removeClass('loading');
                layer.msg(res.info);
                $('#org-name').val('')
            };
            serverData(data, func, url, 'post');
        }, function () {
        });
        return false
    });

    // 添加项目信息
    $("#project-info-add-form").on("submit", function (event) {
        // 添加　组织机构信息
        var formdata = $(this).serializeArray();
        var data = {};
        $(formdata).each(function (index, obj) {
            data[obj.name] = obj.value;
        });
        var url = '/govbuy/addproject/';
        var actionDom = $('#project-info-add-form');
        layer.confirm('确定吗？', {
            btn: ['确定', '取消'] //按钮
        }, function () {
            if (actionDom.hasClass('loading')) {
                return
            }
            actionDom.addClass('loading');
            var func = function (res) {
                actionDom.removeClass('loading');
                layer.msg(res.info);
                $('#project-info-add-form input').val('');// 清空表单
            };
            serverData(data, func, url, 'post');
        }, function () {
        });
        return false
    });

});

