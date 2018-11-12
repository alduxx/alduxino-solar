from django.test import TestCase
from solar.models import TemperatureMeasurement
import datetime
import pytz

class TemperatureMeasurementModelTest(TestCase):
    def test_saving_and_retrieving_temperature_reading(self):
        utc=pytz.UTC

        time_before = utc.localize(datetime.datetime.now())

        first_item = TemperatureMeasurement()
        first_item.collectorsTemperature = 50
        first_item.boilerTemperature = 47
        first_item.save()

        second_item = TemperatureMeasurement()
        second_item.collectorsTemperature = 70
        second_item.boilerTemperature = 60
        second_item.save()

        saved_items = TemperatureMeasurement.objects.all()
        self.assertEqual(saved_items.count(), 2)

        time_after = utc.localize(datetime.datetime.now())

        self.assertTrue(time_after > time_before)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.collectorsTemperature, 50)
        self.assertEqual(first_saved_item.boilerTemperature, 47)
        self.assertEqual(second_saved_item.collectorsTemperature, 70)
        self.assertEqual(second_saved_item.boilerTemperature, 60)
        self.assertTrue(first_saved_item.measured_at >= time_before)
        self.assertTrue(second_saved_item.measured_at >= time_before)

        # The tests bellow assume a settings.TEMP_DIFF_TRIGGER == 5
        self.assertEqual(first_saved_item.pump_supposed_to_be_running(), False)
        self.assertEqual(second_saved_item.pump_supposed_to_be_running(), True)

    def test_can_save_a_POST_request(self):
        response = self.client.post('/solar/api/temperature-measurement/',
            content_type="application/json",
            data={
                'collectorsTemperature': 35,
                'boilerTemperature': 25,
            })

        self.assertEqual(TemperatureMeasurement.objects.count(), 1)
        temperatureMeasurement = TemperatureMeasurement.objects.first()
        self.assertEqual(temperatureMeasurement.collectorsTemperature, 35)
        self.assertEqual(temperatureMeasurement.boilerTemperature, 25)
