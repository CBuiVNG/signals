from django.test import TestCase
from freezegun import freeze_time

from signals.apps.email_integrations.toezicht_or_nieuw_west import utils
from signals.apps.signals.factories import SignalFactory
from signals.apps.signals.models import STADSDEEL_NIEUWWEST, STADSDEEL_NOORD


class TestUtils(TestCase):
    signal = None
    signal_in_noord = None

    def setUp(self):
        self.signal = SignalFactory.create(
            category_assignment__category__parent__name='Overlast in de openbare ruimte',
            category_assignment__category__name='Fietswrak',
            location__stadsdeel=STADSDEEL_NIEUWWEST
        )

        self.signal_other_category = SignalFactory.create(
            category_assignment__category__parent__name='Some other main category',
            category_assignment__category__name='Some other category',
            location__stadsdeel=STADSDEEL_NIEUWWEST
        )

        self.signal_in_noord = SignalFactory.create(
            category_assignment__category__parent__name='Overlast in de openbare ruimte',
            category_assignment__category__name='Fietswrak',
            location__stadsdeel=STADSDEEL_NOORD
        )

    @freeze_time('2019-08-13T00:00:00+02:00')
    def test_is_signal_applicable_true(self):
        result = utils.is_signal_applicable(self.signal)
        self.assertEqual(result, True)

    @freeze_time('2019-08-13T12:00:00+02:00')
    def test_is_signal_applicable_is_business_hour(self):
        result = utils.is_signal_applicable(self.signal)
        self.assertEqual(result, False)

    @freeze_time('2019-08-13T00:00:00+02:00')
    def test_is_signal_applicable_outside_category_in_stadsdeel_nieuwwest(self):
        result = utils.is_signal_applicable(self.signal_other_category)
        self.assertEqual(result, False)

    @freeze_time('2019-08-13T00:00:00+02:00')
    def test_is_signal_applicable_in_category_outside_stadsdeel_nieuwwest(self):
        result = utils.is_signal_applicable(self.signal_in_noord)
        self.assertEqual(result, False)
