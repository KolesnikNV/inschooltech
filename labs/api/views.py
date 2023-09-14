from rest_framework import generics
from lab.models import Lab, Test, Indicator, Metric, Score, Reference
from .serializers import (
    LabSerializer,
    TestSerializer,
    IndicatorSerializer,
    MetricSerializer,
    ScoreSerializer,
    ReferenceSerializer,
)


class LabListCreateView(generics.ListCreateAPIView):
    queryset = Lab.objects.filter(is_active=True)
    serializer_class = LabSerializer


class LabDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lab.objects.filter(is_active=True)
    serializer_class = LabSerializer


class TestListCreateView(generics.ListCreateAPIView):
    queryset = Test.objects.filter(is_active=True)
    serializer_class = TestSerializer


class TestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.filter(is_active=True)
    serializer_class = TestSerializer


class IndicatorListCreateView(generics.ListCreateAPIView):
    queryset = Indicator.objects.filter(is_active=True)
    serializer_class = IndicatorSerializer


class IndicatorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Indicator.objects.filter(is_active=True)
    serializer_class = IndicatorSerializer


class MetricListCreateView(generics.ListCreateAPIView):
    queryset = Metric.objects.filter(is_active=True)
    serializer_class = MetricSerializer


class MetricDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Metric.objects.filter(is_active=True)
    serializer_class = MetricSerializer


class ScoreListCreateView(generics.ListCreateAPIView):
    queryset = Score.objects.filter(is_active=True)
    serializer_class = ScoreSerializer


class ScoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.filter(is_active=True)
    serializer_class = ScoreSerializer


class ReferenceListCreateView(generics.ListCreateAPIView):
    queryset = Reference.objects.filter(is_active=True)
    serializer_class = ReferenceSerializer


class ReferenceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reference.objects.filter(is_active=True)
    serializer_class = ReferenceSerializer
