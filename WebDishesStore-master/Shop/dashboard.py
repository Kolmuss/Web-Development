# from django.utils.translation import ugettext_lazy as _
# from grappelli.dashboard import modules, Dashboard
#
#
# class CustomDashboard(Dashboard):
#     def __init__(self, **kwargs):
#         Dashboard.__init__(self, **kwargs)
#
#         # append an app list module for "Applications"
#         # self.children.append(modules.AppList(
#         #     title=_('Applications'),
#         #     column=1,
#         #     collapsible=True,
#         #     exclude=('django.contrib.*',),
#         # ))
#
#         # append an app list module for "Administration"
#         self.children.append(modules.AppList(
#             title=_('Administration'),
#             column=1,
#             collapsible=True,
#             models=('django.contrib.*',),
#         ))
#
#         # append a recent actions module
#         self.children.append(modules.RecentActions(
#             title=_('Recent actions'),
#             column=2,
#             collapsible=False,
#             limit=5,
#         ))
#         # self.children.append(modules.ModelList(
#         #     title='Several Models',
#         #     column=1,
#         #     models=('django.contrib.*',)
#         # ))
#
#         self.children.append(modules.ModelList(
#             title='Shop',
#             column=1,
#             models=('Shop.models.Product', 'Shop.models.Article')
#         ))
#         self.children.append(modules.Feed(
#             title=_('Latest Django News'),
#             feed_url='http://www.djangoproject.com/rss/weblog/',
#             column=3,
#             limit=5,
#         ))

from django.utils.translation import ugettext_lazy as _
from admin_tools.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):

    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)
        self.children.append(modules.AppList(
            title=_('Applications'),
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.AppList(
            title=_('Administration'),
            models=('django.contrib.*',),
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            title=_('Recent Actions'),
            limit=5
        ))
        self.children.append(modules.RecentActions(
            title='Django CMS recent actions',
            include_list=('cms.page', 'cms.cmsplugin',)
        ))
        self.children.append(modules.Feed(
            title=_('Latest Django News'),
            feed_url='http://www.djangoproject.com/rss/weblog/',
            limit=5
        ))
