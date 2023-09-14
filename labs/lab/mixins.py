from django.db import models


class SoftDeletionModel(models.Model):
    is_active = models.BooleanField(default=True)

    def delete(self):
        self.is_active = False
        self.save()

    class Meta:
        abstract = True
