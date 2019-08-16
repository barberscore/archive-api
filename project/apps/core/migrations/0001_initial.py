# Generated by Django 2.2.4 on 2019-08-16 15:26

import apps.core.fields
from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.utils.timezone
import django_fsm
import model_utils.fields
import phonenumber_field.modelfields
import timezone_field.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Award Name.', max_length=255)),
                ('status', django_fsm.FSMIntegerField(choices=[(-10, 'Inactive'), (0, 'New'), (10, 'Active')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('kind', models.IntegerField(choices=[(32, 'Chorus'), (41, 'Quartet')])),
                ('gender', models.IntegerField(blank=True, choices=[(10, 'Male'), (20, 'Female'), (30, 'Mixed')], help_text='\n            The gender to which the award is restricted.  If unselected, this award is open to all combinations.\n        ', null=True)),
                ('level', models.IntegerField(choices=[(10, 'Championship'), (30, 'Qualifier'), (45, 'Representative'), (50, 'Deferred'), (60, 'Manual'), (70, 'Improved - Raw'), (80, 'Improved - Standard')])),
                ('season', models.IntegerField(choices=[(1, 'Summer'), (2, 'Midwinter'), (3, 'Fall'), (4, 'Spring')])),
                ('district', models.IntegerField(blank=True, choices=[(110, 'BHS'), (200, 'CAR'), (205, 'CSD'), (210, 'DIX'), (215, 'EVG'), (220, 'FWD'), (225, 'ILL'), (230, 'JAD'), (235, 'LOL'), (240, 'MAD'), (345, 'NED'), (350, 'NSC'), (355, 'ONT'), (360, 'PIO'), (365, 'RMD'), (370, 'SLD'), (375, 'SUN'), (380, 'SWD')], null=True)),
                ('division', models.IntegerField(blank=True, choices=[(10, 'EVG Division I'), (20, 'EVG Division II'), (30, 'EVG Division III'), (40, 'EVG Division IV'), (50, 'EVG Division V'), (60, 'FWD Arizona'), (70, 'FWD Northeast'), (80, 'FWD Northwest'), (90, 'FWD Southeast'), (100, 'FWD Southwest'), (110, 'LOL 10000 Lakes'), (120, 'LOL Division One'), (130, 'LOL Northern Plains'), (140, 'LOL Packerland'), (150, 'LOL Southwest'), (170, 'MAD Central'), (180, 'MAD Northern'), (190, 'MAD Southern'), (210, 'NED Granite and Pine'), (220, 'NED Mountain'), (230, 'NED Patriot'), (240, 'NED Sunrise'), (250, 'NED Yankee'), (260, 'SWD Northeast'), (270, 'SWD Northwest'), (280, 'SWD Southeast'), (290, 'SWD Southwest')], null=True)),
                ('is_single', models.BooleanField(default=False, help_text='Single-round award')),
                ('threshold', models.FloatField(blank=True, help_text='\n            The score threshold for automatic qualification (if any.)\n        ', null=True)),
                ('minimum', models.FloatField(blank=True, help_text='\n            The minimum score required for qualification (if any.)\n        ', null=True)),
                ('advance', models.FloatField(blank=True, help_text='\n            The score threshold to advance to next round (if any) in\n            multi-round qualification.\n        ', null=True)),
                ('spots', models.IntegerField(blank=True, help_text='Number of top spots which qualify', null=True)),
                ('description', models.TextField(blank=True, help_text='\n            The Public description of the award.', max_length=1000)),
                ('notes', models.TextField(blank=True, help_text='\n            Private Notes (for internal use only).')),
                ('age', models.IntegerField(blank=True, choices=[(10, 'Seniors'), (20, 'Novice'), (30, 'Youth')], null=True)),
                ('is_novice', models.BooleanField(default=False)),
                ('size', models.IntegerField(blank=True, choices=[(100, 'Plateau 1'), (110, 'Plateau 2'), (120, 'Plateau 3'), (130, 'Plateau 4'), (140, 'Plateau A'), (150, 'Plateau AA'), (160, 'Plateau AAA'), (170, 'Plateau AAAA'), (180, 'Plateau B'), (190, 'Plateau I'), (200, 'Plateau II'), (210, 'Plateau III'), (220, 'Plateau IV'), (230, 'Small')], null=True)),
                ('size_range', django.contrib.postgres.fields.ranges.IntegerRangeField(blank=True, null=True)),
                ('scope', models.IntegerField(blank=True, choices=[(100, 'Plateau 1'), (110, 'Plateau 2'), (120, 'Plateau 3'), (130, 'Plateau 4'), (140, 'Plateau A'), (150, 'Plateau AA'), (160, 'Plateau AAA'), (170, 'Plateau AAAA'), (175, 'Plateau AAAAA')], null=True)),
                ('scope_range', django.contrib.postgres.fields.ranges.DecimalRangeField(blank=True, null=True)),
                ('tree_sort', models.IntegerField(blank=True, editable=False, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(-20, 'Protected'), (-10, 'Inactive'), (0, 'New'), (10, 'Active')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('title', models.CharField(max_length=255)),
                ('arrangers', models.CharField(max_length=255)),
                ('composers', models.CharField(blank=True, default='', max_length=255)),
                ('lyricists', models.CharField(blank=True, default='', max_length=255)),
                ('holders', models.TextField(blank=True, default='')),
                ('description', models.TextField(blank=True, default='', help_text="\n            Fun or interesting facts to share about the chart (ie, 'from Disney's Lion King, first sung by Elton John'.)", max_length=1000)),
                ('notes', models.TextField(blank=True, default='', help_text='\n            Private Notes (for internal use only).')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.core.fields.ImageUploadPath('image'))),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(-10, 'Inactive'), (0, 'New'), (10, 'Active')], default=10, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('name', models.CharField(help_text='\n            The common name of the person.', max_length=255)),
                ('first_name', models.CharField(help_text='\n            The first name of the person.', max_length=255)),
                ('last_name', models.CharField(help_text='\n            The last name of the person.', max_length=255)),
                ('part', models.IntegerField(blank=True, choices=[(1, 'Tenor'), (2, 'Lead'), (3, 'Baritone'), (4, 'Bass')], null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(10, 'Male'), (20, 'Female')], null=True)),
                ('district', models.IntegerField(blank=True, choices=[(110, 'BHS'), (200, 'CAR'), (205, 'CSD'), (210, 'DIX'), (215, 'EVG'), (220, 'FWD'), (225, 'ILL'), (230, 'JAD'), (235, 'LOL'), (240, 'MAD'), (345, 'NED'), (350, 'NSC'), (355, 'ONT'), (360, 'PIO'), (365, 'RMD'), (370, 'SLD'), (375, 'SUN'), (380, 'SWD')], null=True)),
                ('email', apps.core.fields.LowerEmailField(blank=True, help_text='\n            The contact email of the resource.', max_length=254, null=True)),
                ('address', models.TextField(blank=True, default='', help_text='\n            The complete address of the resource.', max_length=1000)),
                ('home_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='\n            The home phone number of the resource.  Include country code.', max_length=128, region=None)),
                ('work_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='\n            The work phone number of the resource.  Include country code.', max_length=128, region=None)),
                ('cell_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='\n            The cell phone number of the resource.  Include country code.', max_length=128, region=None)),
                ('airports', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=3), blank=True, default=list, null=True, size=None)),
                ('description', models.TextField(blank=True, default='', help_text='\n            A bio of the person.  Max 1000 characters.', max_length=1000)),
                ('notes', models.TextField(blank=True, default='', help_text='\n            Notes (for internal use only).')),
                ('bhs_id', models.IntegerField(blank=True, null=True)),
                ('source_id', models.CharField(blank=True, db_index=True, max_length=100, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.core.fields.ImageUploadPath('image'))),
                ('owners', models.ManyToManyField(blank=True, related_name='persons', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='The name of the quartet/chorus.', max_length=255)),
                ('status', django_fsm.FSMIntegerField(choices=[(-10, 'Inactive'), (-5, 'AIC'), (0, 'New'), (10, 'Active')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('kind', models.IntegerField(choices=[(32, 'Chorus'), (41, 'Quartet'), (46, 'VLQ')], help_text='\n            The kind of group.\n        ')),
                ('gender', models.IntegerField(choices=[(10, 'Male'), (20, 'Female'), (30, 'Mixed')], default=10, help_text='\n            The gender of group.\n        ')),
                ('district', models.IntegerField(blank=True, choices=[(110, 'BHS'), (200, 'CAR'), (205, 'CSD'), (210, 'DIX'), (215, 'EVG'), (220, 'FWD'), (225, 'ILL'), (230, 'JAD'), (235, 'LOL'), (240, 'MAD'), (345, 'NED'), (350, 'NSC'), (355, 'ONT'), (360, 'PIO'), (365, 'RMD'), (370, 'SLD'), (375, 'SUN'), (380, 'SWD')], null=True)),
                ('division', models.IntegerField(blank=True, choices=[('EVG', [(10, 'EVG Division I'), (20, 'EVG Division II'), (30, 'EVG Division III'), (40, 'EVG Division IV'), (50, 'EVG Division V')]), ('FWD', [(60, 'FWD Arizona'), (70, 'FWD Northeast'), (80, 'FWD Northwest'), (90, 'FWD Southeast'), (100, 'FWD Southwest')]), ('LOL', [(110, 'LOL 10000 Lakes'), (120, 'LOL Division One'), (130, 'LOL Northern Plains'), (140, 'LOL Packerland'), (150, 'LOL Southwest')]), ('MAD', [(170, 'MAD Central'), (180, 'MAD Northern'), (190, 'MAD Southern')]), ('NED', [(210, 'NED Granite and Pine'), (220, 'NED Mountain'), (230, 'NED Patriot'), (240, 'NED Sunrise'), (250, 'NED Yankee')]), ('SWD', [(260, 'SWD Northeast'), (270, 'SWD Northwest'), (280, 'SWD Southeast'), (290, 'SWD Southwest')])], null=True)),
                ('bhs_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('code', models.CharField(blank=True, help_text='\n            Legacy Short-form code (chapters only).', max_length=255)),
                ('website', models.URLField(blank=True, default='', help_text='\n            The website URL of the resource.')),
                ('location', models.CharField(blank=True, help_text='\n            The geographical location of the resource.', max_length=255)),
                ('participants', models.CharField(blank=True, default='', help_text='Director(s) or Members (listed TLBB)', max_length=255)),
                ('chapters', models.CharField(blank=True, help_text='\n            The denormalized chapter group.', max_length=255)),
                ('is_senior', models.BooleanField(default=False, help_text='Qualifies as a Senior Group.  Must be set manually.')),
                ('is_youth', models.BooleanField(default=False, help_text='Qualifies as a Youth Group.  Must be set manually.')),
                ('description', models.TextField(blank=True, help_text='\n            A description of the group.  Max 1000 characters.', max_length=1000)),
                ('notes', models.TextField(blank=True, help_text='\n            Notes (for internal use only).')),
                ('source_id', models.CharField(blank=True, db_index=True, max_length=100, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.core.fields.ImageUploadPath('image'))),
                ('charts', models.ManyToManyField(blank=True, related_name='groups', to='core.Chart')),
                ('owners', models.ManyToManyField(blank=True, related_name='groups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='Convention',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(-10, 'Inactive'), (0, 'New'), (5, 'Built'), (10, 'Active')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('name', models.CharField(default='Convention', max_length=255)),
                ('district', models.IntegerField(blank=True, choices=[(110, 'BHS'), (200, 'CAR'), (205, 'CSD'), (210, 'DIX'), (215, 'EVG'), (220, 'FWD'), (225, 'ILL'), (230, 'JAD'), (235, 'LOL'), (240, 'MAD'), (345, 'NED'), (350, 'NSC'), (355, 'ONT'), (360, 'PIO'), (365, 'RMD'), (370, 'SLD'), (375, 'SUN'), (380, 'SWD')], null=True)),
                ('season', models.IntegerField(choices=[(3, 'Fall'), (4, 'Spring')])),
                ('panel', models.IntegerField(blank=True, choices=[(1, 'Single'), (2, 'Double'), (3, 'Triple'), (4, 'Quadruple'), (5, 'Quintiple')], null=True)),
                ('year', models.IntegerField(choices=[(2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939)])),
                ('open_date', models.DateField(blank=True, null=True)),
                ('close_date', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('venue_name', models.CharField(default='(TBD)', help_text='\n            The venue name (when available).', max_length=255)),
                ('location', models.CharField(default='(TBD)', help_text='\n            The general location in the form "City, State".', max_length=255)),
                ('timezone', timezone_field.fields.TimeZoneField(blank=True, help_text='\n            The local timezone of the convention.', null=True)),
                ('description', models.TextField(blank=True, help_text='\n            A general description field; usually used for hotel and venue info.', max_length=1000)),
                ('divisions', apps.core.fields.DivisionsField(base_field=models.IntegerField(choices=[('EVG', [(10, 'EVG Division I'), (20, 'EVG Division II'), (30, 'EVG Division III'), (40, 'EVG Division IV'), (50, 'EVG Division V')]), ('FWD', [(60, 'FWD Arizona'), (70, 'FWD Northeast'), (80, 'FWD Northwest'), (90, 'FWD Southeast'), (100, 'FWD Southwest')]), ('LOL', [(110, 'LOL 10000 Lakes'), (120, 'LOL Division One'), (130, 'LOL Northern Plains'), (140, 'LOL Packerland'), (150, 'LOL Southwest')]), ('MAD', [(170, 'MAD Central'), (180, 'MAD Northern'), (190, 'MAD Southern')]), ('NED', [(210, 'NED Granite and Pine'), (220, 'NED Mountain'), (230, 'NED Patriot'), (240, 'NED Sunrise'), (250, 'NED Yankee')]), ('SWD', [(260, 'SWD Northeast'), (270, 'SWD Northwest'), (280, 'SWD Southeast'), (290, 'SWD Southwest')])]), blank=True, default=list, help_text='Only select divisions if required.  If it is a district-wide convention do not select any.', size=None)),
                ('kinds', apps.core.fields.DivisionsField(base_field=models.IntegerField(choices=[(32, 'Chorus'), (41, 'Quartet'), (42, 'Mixed'), (43, 'Senior'), (44, 'Youth'), (45, 'Unknown'), (46, 'VLQ')]), blank=True, default=list, help_text='The session kind(s) created at build time.', size=None)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=apps.core.fields.UploadPath('image'))),
                ('owners', models.ManyToManyField(related_name='conventions', to=settings.AUTH_USER_MODEL)),
                ('persons', models.ManyToManyField(blank=True, related_name='conventions', to='core.Person')),
            ],
        ),
        migrations.AddConstraint(
            model_name='chart',
            constraint=models.UniqueConstraint(fields=('title', 'arrangers'), name='unique_chart'),
        ),
        migrations.AddConstraint(
            model_name='convention',
            constraint=models.UniqueConstraint(fields=('year', 'season', 'name', 'district'), name='unique_convention'),
        ),
    ]
