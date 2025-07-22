from django.db import models

class APILog(models.Model):
    api_type = models.CharField(max_length=100)
    device_ip = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.api_type} | {self.device_ip} | {self.result} | {self.timestamp}"
