from django.urls import path, include
from .views import ArticleView #SingleArticleView
from rest_framework.routers import DefaultRouter

"""
get_single = ArticleView.as_view({"get":"retrieve"})
cancel = ArticleView.as_view({"get":"cancel"})
get_list = ArticleView.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})


urlpatterns = [
    path("<title>",get_list),
    path("single/<title>",get_single),
    path("settings/cancel",cancel),
    #path("single/<int:pk>",SingleArticleView.as_view())
]
"""

router = DefaultRouter()
router.register(r"api",ArticleView)

urlpatterns = [
    path("",include(router.urls))
]
