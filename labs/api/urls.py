from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="InSchoolTech API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    path("labs/", views.LabListCreateView.as_view(), name="lab-list"),
    path("labs/<uuid:pk>/", views.LabDetailView.as_view(), name="lab-detail"),
    path("tests/", views.TestListCreateView.as_view(), name="test-list"),
    path("tests/<uuid:pk>/", views.TestDetailView.as_view(), name="test-detail"),
    path("indicators/", views.IndicatorListCreateView.as_view(), name="indicator-list"),
    path(
        "indicators/<uuid:pkd>/",
        views.IndicatorDetailView.as_view(),
        name="indicator-detail",
    ),
    path("metrics/", views.MetricListCreateView.as_view(), name="metric-list"),
    path(
        "metrics/<uuid:pk>/",
        views.MetricDetailView.as_view(),
        name="metric-detail",
    ),
    path("scores/", views.ScoreListCreateView.as_view(), name="score-list"),
    path("scores/<uuid:pk>/", views.ScoreDetailView.as_view(), name="score-detail"),
    path("references/", views.ReferenceListCreateView.as_view(), name="reference-list"),
    path(
        "references/<uuid:pk>/",
        views.ReferenceDetailView.as_view(),
        name="reference-detail",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
