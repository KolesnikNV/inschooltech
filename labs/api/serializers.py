from rest_framework import serializers
from lab.models import Lab, Test, Indicator, Metric, Score, Reference


class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = "__all__"


class ScoreSerializer(serializers.ModelSerializer):
    indicator_name = serializers.CharField(source="indicator_metric.indicator.name")
    metric_name = serializers.CharField(source="indicator_metric.metric.name")
    metric_unit = serializers.CharField(source="indicator_metric.metric.unit")
    is_within_normal_range = serializers.SerializerMethodField()

    class Meta:
        model = Score
        fields = (
            "id",
            "score",
            "indicator_name",
            "metric_name",
            "metric_unit",
            "is_within_normal_range",
        )

    def create(self, validated_data):
        indicator_metric = validated_data.pop("indicator_metric")
        score = Score.objects.create(**validated_data)
        score.indicator = indicator_metric.indicator
        score.save()
        return score

    def get_is_within_normal_range(self, obj):
        if reference := obj.indicator_metric.reference_set.first():
            return reference.min_score <= obj.score <= reference.max_score
        return False


class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = "__all__"


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = "__all__"


class IndicatorMetricSerializer(serializers.ModelSerializer):
    indicator_name = serializers.CharField(source="indicator.name")
    metric_name = serializers.CharField(source="metric.name")
    metric_unit = serializers.CharField(source="metric.unit")

    class Meta:
        model = Indicator
        fields = (
            "indicator_name",
            "metric_name",
            "metric_unit",
            "is_active",
            "created_at",
            "updated_at",
        )


class TestSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    lab_id = serializers.UUIDField(source="lab.id")
    results = ScoreSerializer(many=True, source="score_set", read_only=True)
    duration_seconds = serializers.SerializerMethodField()

    class Meta:
        model = Test
        fields = ("id", "lab_id", "duration_seconds", "results")

    def get_duration_seconds(self, obj):
        duration = (obj.completed_at - obj.started_at).total_seconds()
        return int(duration)


class ReferenceSerializer(serializers.ModelSerializer):
    indicator_metric_data = IndicatorMetricSerializer(
        source="indicator_metric", read_only=True
    )

    class Meta:
        model = Reference
        fields = (
            "id",
            "min_score",
            "max_score",
            "indicator_metric_data",
            "is_active",
            "created_at",
            "updated_at",
        )
