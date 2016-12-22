# coding=utf-8
from django.contrib import admin
from .models import DeployCil
from django.shortcuts import redirect
import subprocess
import commands

class DeployCilAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created')
    list_filter = ('created', 'is_valid')
    search_fields = ['=id', 'name', 'command']
    list_display_links = ['id', 'name']
    date_hierarchy = 'created'

    def deploy_sth(self, request, queryset):
        # type: (HttpRequest, List[CashOut])
        """批量 执行　部署任务
        """
        if queryset.count() > 1:
            return self.message_user(request, '拒絕執行多條命令')
        command = queryset.first().command
        code, outs = commands.getstatusoutput(command)
        self.message_user(request, u'執行命令: %s'%' '.join(command))
        for out in outs.split('\n'):
            self.message_user(request, u'%s' % out)
        origin_url = request.get_full_path()
        return redirect(origin_url)

    deploy_sth.short_description = '部署服务'
    actions = ['deploy_sth']


admin.site.register(DeployCil, DeployCilAdmin)
