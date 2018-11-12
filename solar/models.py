from django.db import models
from django.conf import settings

class TemperatureMeasurement(models.Model):
    collectorsTemperature = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    boilerTemperature = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    measured_at = models.DateTimeField(auto_now_add=True)

    def pump_supposed_to_be_running(self):
        return (self.collectorsTemperature - self.boilerTemperature) >= settings.TEMP_DIFF_TRIGGER
