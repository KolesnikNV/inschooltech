import os
import django
import random
from faker import Faker
from lab.models import (
    Lab,
    Test,
    Indicator,
    Metric,
    IndicatorMetric,
    Score,
    Reference,
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "labs.settings")
django.setup()

fake = Faker()


def generate_lab_data(num_entries):
    for _ in range(num_entries):
        lab_name = fake.company()
        is_active = random.choice([True, False])
        Lab.objects.create(name=lab_name, is_active=is_active)


def generate_indicator_data(num_entries):
    for _ in range(num_entries):
        indicator_name = fake.word()
        description = fake.sentence()
        is_active = random.choice([True, False])
        Indicator.objects.create(
            name=indicator_name, description=description, is_active=is_active
        )


def generate_metric_data(num_entries):
    for _ in range(num_entries):
        metric_name = fake.word()
        description = fake.sentence()
        unit = fake.word()
        is_active = random.choice([True, False])
        Metric.objects.create(
            name=metric_name, description=description, unit=unit, is_active=is_active
        )


def generate_indicator_metric_data(num_entries):
    indicators = Indicator.objects.all()
    metrics = Metric.objects.all()
    for _ in range(num_entries):
        indicator = random.choice(indicators)
        metric = random.choice(metrics)
        is_active = random.choice([True, False])
        IndicatorMetric.objects.create(
            indicator=indicator, metric=metric, is_active=is_active
        )


def generate_score_data(num_entries):
    tests = Test.objects.all()
    indicator_metrics = IndicatorMetric.objects.all()
    for _ in range(num_entries):
        score = round(random.uniform(0, 100), 6)
        test = random.choice(tests)
        indicator_metric = random.choice(indicator_metrics)
        is_active = random.choice([True, False])
        Score.objects.create(
            score=score,
            test=test,
            indicator_metric=indicator_metric,
            is_active=is_active,
        )


def generate_reference_data(num_entries):
    indicator_metrics = IndicatorMetric.objects.all()
    for _ in range(num_entries):
        min_score = round(random.uniform(0, 100), 6)
        max_score = round(min_score + random.uniform(1, 10), 6)
        indicator_metric = random.choice(indicator_metrics)
        is_active = random.choice([True, False])
        Reference.objects.create(
            min_score=min_score,
            max_score=max_score,
            indicator_metric=indicator_metric,
            is_active=is_active,
        )


num_entries = 10
generate_lab_data(num_entries)
generate_indicator_data(num_entries)
generate_metric_data(num_entries)
generate_indicator_metric_data(num_entries)
generate_score_data(num_entries)
generate_reference_data(num_entries)
print(f"Созданы тестовые данные для всех моделей.")
