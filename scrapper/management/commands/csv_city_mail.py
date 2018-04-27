import logging

from django.core.management import BaseCommand
from django.utils.timezone import now

from app.settings import BASE_DIR
from scrapper.models import Profile
from scrapper.service.csv import dict_to_csv

log = logging.getLogger('console')


class Command(BaseCommand):
    help = "city / segment matrix"

    def handle(self, *args, **options):
        profiles = Profile.objects.filter(email_provider__isnull=False).all()

        # 2 dim dictionary from all records
        m = {}
        for profile in profiles:
            if profile.email_provider in m and profile.city in m[profile.email_provider]:
                m[profile.email_provider][profile.city] += 1
            else:
                if profile.email_provider not in m:
                    m[profile.email_provider] = dict()
                m[profile.email_provider].update({profile.city: 1})

        dict_to_csv(m,  '{}/files/csv/by_city_mail_{}.csv'.format(BASE_DIR, now()))
