
# Standard Library
import datetime
import logging
import requests
# Django
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.apps import apps
from django.conf import settings

from apps.core.tasks import update_person_from_membercenter
from apps.core.tasks import update_group_from_membercenter
from apps.core.tasks import update_group_owners_from_membercenter

# First-Party
User = get_user_model()
Person = apps.get_model('core.person')
Group = apps.get_model('core.group')

log = logging.getLogger('updater')


class Command(BaseCommand):
    help = "Command to sync with Member Center database."

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            dest='days',
            nargs='?',
            const=1,
            help='Number of days to update.',
        )

        parser.add_argument(
            '--hours',
            type=int,
            dest='hours',
            nargs='?',
            const=1,
            help='Number of hours to update.',
        )

        parser.add_argument(
            '--minutes',
            type=int,
            dest='minutes',
            nargs='?',
            const=1,
            help='Number of hours to update.',
        )

    def handle(self, *args, **options):
        # Set Cursor
        if options['days']:
            cursor = timezone.now() - datetime.timedelta(days=options['days'], hours=1)
        elif options['hours']:
            cursor = timezone.now() - datetime.timedelta(hours=options['hours'], minutes=5)
        elif options['minutes']:
            cursor = timezone.now() - datetime.timedelta(minutes=options['minutes'], seconds=5)
        else:
            cursor = None

        # Sync Persons
        self.stdout.write("Fetching Persons from Member Center...")
        endpoint, _, token = settings.MEMBERCENTER_URL.partition('@')
        url = "{0}/bhs/person".format(endpoint)
        headers = {
            'Authorization': 'Token {0}'.format(token)
        }
        page = 1
        params = {
            'modified__gt': cursor,
            'page': page,
        }
        response = requests.get(
            url,
            headers=headers,
            params=params,
        ).json()
        t = response['meta']['pagination']['count']
        if t:
            i = 0
            pages = response['meta']['pagination']['pages']
            while page <= pages:
                response = requests.get(
                    url,
                    headers=headers,
                    params=params,
                ).json()
                items = response['data']
                for item in items:
                    i += 1
                    self.stdout.flush()
                    self.stdout.write("Updating {0} of {1} Persons...".format(i, t), ending='\r')
                    update_person_from_membercenter.delay(item)
                page += 1
                params['page'] = page
            self.stdout.write("")
        self.stdout.write("Updated {0} Persons.".format(t))
        # if not cursor:
        #     humans = list(Human.objects.values_list('id', flat=True))
        #     self.stdout.write("Deleting Person orphans...")
        #     t = Person.objects.delete_orphans(humans)
        #     self.stdout.write("Deleted {0} Person orphans.".format(t))

        # Sync Groups
        self.stdout.write("Fetching Groups from Member Center...")
        endpoint, _, token = settings.MEMBERCENTER_URL.partition('@')
        url = "{0}/bhs/group".format(endpoint)
        headers = {
            'Authorization': 'Token {0}'.format(token)
        }
        page = 1
        params = {
            'modified__gt': cursor,
            'kind__gt': 30,
            'page': page,
        }
        response = requests.get(
            url,
            headers=headers,
            params=params,
        ).json()
        t = response['meta']['pagination']['count']
        if t:
            i = 0
            pages = response['meta']['pagination']['pages']
            while page <= pages:
                response = requests.get(
                    url,
                    headers=headers,
                    params=params,
                ).json()
                items = response['data']
                for item in items:
                    i += 1
                    self.stdout.flush()
                    self.stdout.write("Updating {0} of {1} Groups...".format(i, t), ending='\r')
                    update_group_from_membercenter.delay(item)
                page += 1
                params['page'] = page
            self.stdout.write("")
        self.stdout.write("Updated {0} Groups.".format(t))

        # Sync Roles
        self.stdout.write("Fetching Officers from Member Center...")
        endpoint, _, token = settings.MEMBERCENTER_URL.partition('@')
        url = "{0}/bhs/officer".format(endpoint)
        headers = {
            'Authorization': 'Token {0}'.format(token)
        }
        page = 1
        params = {
            'modified__gt': cursor,
            'group__kind__gt': 30,
            'page': page,
        }
        response = requests.get(
            url,
            headers=headers,
            params=params,
        ).json()
        t = response['meta']['pagination']['count']
        if t:
            i = 0
            pages = response['meta']['pagination']['pages']
            while page <= pages:
                response = requests.get(
                    url,
                    headers=headers,
                    params=params,
                ).json()
                items = response['data']
                for item in items:
                    i += 1
                    self.stdout.flush()
                    self.stdout.write("Updating {0} of {1} Roles...".format(i, t), ending='\r')
                    update_group_owners_from_membercenter.delay(item)
                page += 1
                params['page'] = page
            self.stdout.write("")
        self.stdout.write("Updated {0} Officers.".format(t))

        self.stdout.write("Complete.")
