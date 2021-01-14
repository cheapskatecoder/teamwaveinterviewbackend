from django.db import models

class Query(models.Model):
    query = models.TextField()
    results = models.JSONField()
    date_created = models.DateTimeField()

    def __str__(self):
        return "Query - {}".format(self.query)

    class Meta:
        verbose_name = 'Query'
        verbose_name_plural = 'Queries'
