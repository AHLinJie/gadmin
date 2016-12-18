# coding=utf-8
from django.contrib import admin
from .models import GovHostInfo, ProContract, ProCarry, ChargePerson, GovProject, BidResult, Organization, CrawlPage


class GovProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'modified')
    list_filter = ('created', 'capital_source', 'project_progress')
    search_fields = ['=id', 'name', 'issue_org_name', 'bid_person', 'contacts_name']
    date_hierarchy = 'created'


admin.site.register(GovProject, GovProjectAdmin)


class GovHostInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'host_url', 'gov_level', 'is_open', 'created', 'modified')
    list_filter = ('created', 'gov_level', 'is_open')
    search_fields = ['=id', 'name']
    date_hierarchy = 'created'

    def reject_cash_out(self, request, queryset):
        # type: (HttpRequest, List[CashOut])
        """
        """
        return self.message_user(request, 'ok')

    reject_cash_out.short_description = '批量拒绝用户提现'
    actions = ['reject_cash_out']


admin.site.register(GovHostInfo, GovHostInfoAdmin)


class ProContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'contract_type', 'first_party', 'second_party', 'start_time', 'end_time',
                    'signed_time', 'signed_at', 'created', 'modified')
    list_filter = ('created', 'contract_type', 'is_print')
    search_fields = ['=id', 'first_party', 'second_party']
    date_hierarchy = 'created'


admin.site.register(ProContract, ProContractAdmin)


class ProCarryAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'name', 'cost', 'selling_price', 'label_price', 'created', 'modified')
    list_filter = ('created', 'carry_type')
    search_fields = ['=id', 'project_name', 'name', ]
    date_hierarchy = 'created'


admin.site.register(ProCarry, ProCarryAdmin)


class ChargePersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'charge_type', 'email', 'created', 'modified')
    list_filter = ('created', 'charge_type',)
    search_fields = ['=id', 'project_name', 'name', 'org_name']
    date_hierarchy = 'created'


admin.site.register(ChargePerson, ChargePersonAdmin)


class BidResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'org_name', 'bid_buy_type', 'bid_open_time', 'bid_win_time',
                    'created', 'modified')
    list_filter = ('created', 'bid_buy_type')
    search_fields = ['=id', 'project_name', 'org_name', ]
    date_hierarchy = 'created'


admin.site.register(BidResult, BidResultAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'created', 'modified')
    list_filter = ('created', 'org_type')
    search_fields = ['=id', 'name', 'address']
    # date_hierarchy = 'created'


admin.site.register(Organization, OrganizationAdmin)


class CrawlPageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'host_id',
        'host_url',
        'target_page',
        'is_crawled',
        'crawl_time',
        'created'
    )
    list_filter = ('is_crawled',)
    search_fields = ('host_id', 'html_source_code', 'logogram', 'project_page_url')
    date_hierarchy = 'crawl_time'

    def target_page(self, obj):
        x = '<a target="_blank" href="%s">%s</a>' % (obj.project_page_link(), obj.logogram)
        return x

    target_page.allow_tags = True
    target_page.short_description = u"目标页面"


admin.site.register(CrawlPage, CrawlPageAdmin)
