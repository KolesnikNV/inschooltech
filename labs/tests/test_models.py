import pytest

from lab.models import (Indicator, IndicatorMetric, Lab, Metric, Reference,
                        Score, Test)


@pytest.mark.django_db
def test_create_lab():
    lab = Lab.objects.create(name="New Lab", is_active=True)
    assert Lab.objects.count() == 1
    assert lab.name == "New Lab"


@pytest.mark.django_db
def test_create_test():
    lab = Lab.objects.create(name="Lab 1", is_active=True)
    test = Test.objects.create(
        lab=lab,
        started_at="2023-09-14T12:00:00Z",
        completed_at="2023-09-14T12:30:00Z",
        comment="Test 1",
        is_active=True,
    )
    assert Test.objects.count() == 1
    assert test.comment == "Test 1"


@pytest.mark.django_db
def test_create_indicator():
    indicator = Indicator.objects.create(name="New Indicator", is_active=True)
    assert Indicator.objects.count() == 1
    assert indicator.name == "New Indicator"


@pytest.mark.django_db
def test_create_metric():
    metric = Metric.objects.create(name="Test Metric", unit="Test Unit")
    assert Metric.objects.count() == 1
    assert metric.name == "Test Metric"


@pytest.mark.django_db
def test_create_score():
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
    score = Score.objects.create(
        test=test,
        indicator_metric=IndicatorMetric.objects.create(
            indicator=indicator, metric=metric
        ),
        score=5.0,
    )
    assert Score.objects.count() == 1
    assert score.score == 5.0


@pytest.mark.django_db
def test_create_reference():
    indicator = Indicator.objects.create(name="New Indicator", is_active=True)
    metric = Metric.objects.create(name="Test Metric", unit="Test Unit")
    indicator_metric = IndicatorMetric.objects.create(
        indicator=indicator, metric=metric
    )
    reference = Reference.objects.create(
        indicator_metric=indicator_metric, min_score=0.0, max_score=10.0
    )
    assert Reference.objects.count() == 1
    assert reference.min_score == 0.0
    assert reference.max_score == 10.0
