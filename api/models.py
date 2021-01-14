from django.db import models
from django.contrib.auth.models import User

class Query(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    query = models.TextField()
    results = models.JSONField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Query - {}".format(self.query)

    class Meta:
        verbose_name = 'Query'
        verbose_name_plural = 'Queries'
