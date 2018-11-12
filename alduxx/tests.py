
from django.test import TestCase

from alduxx.views import main_panel

class MainPanelTest(TestCase):
    def test_main_panel_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'alduxx/main_panel.html')
