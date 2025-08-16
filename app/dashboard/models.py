from django.db import models

# (Opcional) Para administrar accesos desde DB:
# class Link(models.Model):
#     name = models.CharField(max_length=100)
#     url = models.URLField()
#     btn = models.CharField(max_length=20, default='primary')  # primary, success, dark, info, etc.
#     def __str__(self):
#         return self.name
