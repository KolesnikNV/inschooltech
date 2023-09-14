from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from lab.models import (Indicator, IndicatorMetric, Lab, Metric, Reference,
                        Score, Test)


class LabListCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_create_lab(self):
        url = reverse("lab-list")
        data = {"name": "New Lab", "is_active": True}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lab.objects.count(), 1)
        self.assertEqual(Lab.objects.get().name, "New Lab")

    def test_get_lab_list(self):
        Lab.objects.create(name="Lab 1", is_active=True)
        Lab.objects.create(name="Lab 2", is_active=True)

        url = reverse("lab-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class TestListCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_get_test_list(self):
        lab = Lab.objects.create(name="Lab 1", is_active=True)
        Test.objects.create(
            lab=lab,
            started_at="2023-09-14T12:00:00Z",
            completed_at="2023-09-14T12:30:00Z",
            comment="Test 1",
            is_active=True,
        )
        Test.objects.create(
            lab=lab,
            started_at="2023-09-14T13:00:00Z",
            completed_at="2023-09-14T13:30:00Z",
            comment="Test 2",
            is_active=True,
        )

        url = reverse("test-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class IndicatorListCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_create_indicator(self):
        url = reverse("indicator-list")
        data = {"name": "New Indicator", "is_active": True}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Indicator.objects.count(), 1)
        self.assertEqual(Indicator.objects.get().name, "New Indicator")

    def test_get_indicator_list(self):
        Indicator.objects.create(name="Indicator 1", is_active=True)
        Indicator.objects.create(name="Indicator 2", is_active=True)

        url = reverse("indicator-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class MetricListCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_create_metric(self):
        url = reverse("metric-list")
        data = {"name": "Test Metric", "unit": "Test Unit"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_metric_list(self):
        url = reverse("metric-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MetricDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.metric = Metric.objects.create(name="Test Metric", unit="Test Unit")

    def test_get_metric_detail(self):
        url = reverse("metric-detail", kwargs={"pk": self.metric.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ScoreListCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_create_score(self):
        lab = Lab.objects.create(name="Lab 1", is_active=True)
        test = Test.objects.create(
            lab=lab,
            started_at="2023-09-14T12:00:00Z",
            completed_at="2023-09-14T12:30:00Z",
            comment="Test 1",
            is_active=True,
        )
        indicator = Indicator.objects.create(name="New Indicator", is_active=True)
        metric = Metric.objects.create(name="Test Metric", unit="Test Unit")
        indicator_metric = IndicatorMetric.objects.create(
            indicator=indicator,
            metric=metric,
        )
        url = reverse("score-list")
        data = {
            "test": test.id,
            "indicator_metric": indicator_metric.id,
            "score": 5.0,
            "indicator_name": "New Indicator",
            "metric_name": "Test Metric",
            "metric_unit": "Test Unit",
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Score.objects.count(), 1)
        self.assertEqual(Score.objects.get().score, 5.0)

    def test_get_score_list(self):
        lab = Lab.objects.create(name="Lab 1", is_active=True)
        test = Test.objects.create(
            lab=lab,
            started_at="2023-09-14T12:00:00Z",
            completed_at="2023-09-14T12:30:00Z",
            comment="Test 1",
            is_active=True,
        )
        indicator_metric = IndicatorMetric.objects.create(
            indicator=Indicator.objects.create(name="New Indicator", is_active=True),
            metric=Metric.objects.create(name="Test Metric", unit="Test Unit"),
        )
        Score.objects.create(test=test, indicator_metric=indicator_metric, score=5.0)
        Score.objects.create(test=test, indicator_metric=indicator_metric, score=4.0)

        url = reverse("score-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class ScoreDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        lab = Lab.objects.create(name="Lab 1", is_active=True)
        test = Test.objects.create(
            lab=lab,
            started_at="2023-09-14T12:00:00Z",
            completed_at="2023-09-14T12:30:00Z",
            comment="Test 1",
            is_active=True,
        )
        indicator_metric = IndicatorMetric.objects.create(
            indicator=Indicator.objects.create(name="New Indicator", is_active=True),
            metric=Metric.objects.create(name="Test Metric", unit="Test Unit"),
        )
        self.score = Score.objects.create(
            test=test, indicator_metric=indicator_metric, score=5.0
        )

    def test_get_score_detail(self):
        url = reverse("score-detail", kwargs={"pk": self.score.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReferenceCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_create_reference(self):
        lab = Lab.objects.create(name="Lab 1", is_active=True)
        test = Test.objects.create(
            lab=lab,
            started_at="2023-09-14T12:00:00Z",
            completed_at="2023-09-14T12:30:00Z",
            comment="Test 1",
            is_active=True,
        )
        indicator_metric = IndicatorMetric.objects.create(
            indicator=Indicator.objects.create(name="New Indicator", is_active=True),
            metric=Metric.objects.create(name="Test Metric", unit="Test Unit"),
        )
        url = reverse("reference-list")
        data = {
            "test": test.id,
            "indicator_metric": indicator_metric.id,
            "value": 10.0,
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reference.objects.count(), 1)
        self.assertEqual(Reference.objects.get().value, 10.0)

    def test_get_reference_list(self):
        indicator_metric = IndicatorMetric.objects.create(
            indicator=Indicator.objects.create(name="New Indicator", is_active=True),
            metric=Metric.objects.create(name="Test Metric", unit="Test Unit"),
        )
        Reference.objects.create(
            indicator_metric=indicator_metric, min_score=0.0, max_score=5.0
        )
        Reference.objects.create(
            indicator_metric=indicator_metric, min_score=5.1, max_score=10.0
        )

        url = reverse("reference-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class ReferenceDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        indicator_metric = IndicatorMetric.objects.create(
            indicator=Indicator.objects.create(name="New Indicator", is_active=True),
            metric=Metric.objects.create(name="Test Metric", unit="Test Unit"),
        )
        self.reference = Reference.objects.create(
            indicator_metric=indicator_metric, min_score=0.0, max_score=10.0
        )

    def test_get_reference_detail(self):
        url = reverse("reference-detail", kwargs={"pk": self.reference.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
