# Generated by Django 2.2.4 on 2019-08-16 15:31

import apps.adjudication.fields
from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.fields.ranges
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
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
            name='Appearance',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(-30, 'Disqualified'), (-20, 'Scratched'), (-10, 'Completed'), (0, 'New'), (7, 'Built'), (10, 'Started'), (20, 'Finished'), (25, 'Variance'), (30, 'Verified'), (40, 'Advanced')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('num', models.IntegerField(help_text='The order of appearance for this round.')),
                ('draw', models.IntegerField(blank=True, help_text='The draw for the next round.', null=True)),
                ('is_private', models.BooleanField(default=False, help_text='Copied from entry.')),
                ('is_single', models.BooleanField(default=False, help_text='Single-round group')),
                ('participants', models.CharField(blank=True, default='', help_text='Director(s) or Members (listed TLBB)', max_length=255)),
                ('representing', models.CharField(blank=True, default='', help_text='Representing entity', max_length=255)),
                ('onstage', models.DateTimeField(blank=True, help_text='\n            The actual appearance datetime.', null=True)),
                ('actual_start', models.DateTimeField(blank=True, help_text='\n            The actual appearance datetime.', null=True)),
                ('actual_finish', models.DateTimeField(blank=True, help_text='\n            The actual appearance datetime.', null=True)),
                ('pos', models.IntegerField(blank=True, help_text='Actual Participants-on-Stage', null=True)),
                ('stats', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('base', models.FloatField(blank=True, help_text='\n            The incoming base score used to determine most-improved winners.', null=True)),
                ('variance_report', models.FileField(blank=True, default='', upload_to=apps.adjudication.fields.UploadPath('variance_report'))),
                ('csa_report', models.FileField(blank=True, default='', upload_to=apps.adjudication.fields.UploadPath('csa_report'))),
                ('group_id', models.UUIDField(blank=True, null=True)),
                ('name', models.CharField(blank=True, default='', help_text='\n            The name of the resource.\n        ', max_length=255)),
                ('kind', models.IntegerField(blank=True, choices=[(32, 'Chorus'), (41, 'Quartet'), (46, 'VLQ')], help_text='\n            The kind of group.\n        ', null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(10, 'Male'), (20, 'Female'), (30, 'Mixed')], help_text='\n            The gender of group.\n        ', null=True)),
                ('district', models.IntegerField(blank=True, choices=[(110, 'BHS'), (200, 'CAR'), (205, 'CSD'), (210, 'DIX'), (215, 'EVG'), (220, 'FWD'), (225, 'ILL'), (230, 'JAD'), (235, 'LOL'), (240, 'MAD'), (345, 'NED'), (350, 'NSC'), (355, 'ONT'), (360, 'PIO'), (365, 'RMD'), (370, 'SLD'), (375, 'SUN'), (380, 'SWD')], null=True)),
                ('division', models.IntegerField(blank=True, choices=[('EVG', [(10, 'EVG Division I'), (20, 'EVG Division II'), (30, 'EVG Division III'), (40, 'EVG Division IV'), (50, 'EVG Division V')]), ('FWD', [(60, 'FWD Arizona'), (70, 'FWD Northeast'), (80, 'FWD Northwest'), (90, 'FWD Southeast'), (100, 'FWD Southwest')]), ('LOL', [(110, 'LOL 10000 Lakes'), (120, 'LOL Division One'), (130, 'LOL Northern Plains'), (140, 'LOL Packerland'), (150, 'LOL Southwest')]), ('MAD', [(170, 'MAD Central'), (180, 'MAD Northern'), (190, 'MAD Southern')]), ('NED', [(210, 'NED Granite and Pine'), (220, 'NED Mountain'), (230, 'NED Patriot'), (240, 'NED Sunrise'), (250, 'NED Yankee')]), ('SWD', [(260, 'SWD Northeast'), (270, 'SWD Northwest'), (280, 'SWD Southeast'), (290, 'SWD Southwest')])], null=True)),
                ('bhs_id', models.IntegerField(blank=True, null=True)),
                ('code', models.CharField(blank=True, default='', help_text='\n            Short-form code.', max_length=255)),
            ],
            options={
                'ordering': ['num'],
            },
        ),
        migrations.CreateModel(
            name='Panelist',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(-10, 'Inactive'), (-5, 'Released'), (0, 'New'), (10, 'Active')], default=10, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('num', models.IntegerField(blank=True, null=True)),
                ('kind', models.IntegerField(choices=[(10, 'Official'), (20, 'Practice'), (30, 'Observer')])),
                ('category', models.IntegerField(blank=True, choices=[(5, 'DRCJ'), (10, 'CA'), (30, 'Music'), (40, 'Performance'), (50, 'Singing')], null=True)),
                ('psa_report', models.FileField(blank=True, default='', upload_to=apps.adjudication.fields.UploadPath('psa_report'))),
                ('person_id', models.UUIDField(blank=True, null=True)),
                ('name', models.CharField(blank=True, default='', help_text='\n            The prefix of the person.', max_length=255)),
                ('first_name', models.CharField(blank=True, default='', help_text='\n            The first name of the person.', max_length=255)),
                ('last_name', models.CharField(blank=True, default='', help_text='\n            The last name of the person.', max_length=255)),
                ('district', models.IntegerField(blank=True, choices=[(110, 'BHS'), (200, 'CAR'), (205, 'CSD'), (210, 'DIX'), (215, 'EVG'), (220, 'FWD'), (225, 'ILL'), (230, 'JAD'), (235, 'LOL'), (240, 'MAD'), (345, 'NED'), (350, 'NSC'), (355, 'ONT'), (360, 'PIO'), (365, 'RMD'), (370, 'SLD'), (375, 'SUN'), (380, 'SWD')], null=True)),
                ('representing', models.CharField(blank=True, default='', help_text='\n            District', max_length=10)),
                ('email', apps.adjudication.fields.LowerEmailField(blank=True, help_text='\n            The contact email of the resource.', max_length=254, null=True)),
                ('cell_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='\n            The cell phone number of the resource.  Include country code.', max_length=128, null=True, region=None)),
                ('airports', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=3), blank=True, default=list, null=True, size=None)),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.adjudication.fields.UploadPath('image'))),
                ('bhs_id', models.IntegerField(blank=True, null=True)),
                ('owners', models.ManyToManyField(related_name='panelists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(0, 'New')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('num', models.IntegerField()),
                ('asterisks', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None)),
                ('dixons', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None)),
                ('penalties', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(choices=[(10, 'Primarily Patriotic/Religious Intent'), (30, 'Instrumental Accompaniment'), (40, 'Chorus Exceeding 4-Part Texture'), (50, 'Sound Equipment or Electronic Enhancement')]), blank=True, default=list, size=None)),
                ('stats', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('chart_id', models.UUIDField(blank=True, null=True)),
                ('title', models.CharField(blank=True, default='', max_length=255)),
                ('arrangers', models.CharField(blank=True, default='', max_length=255)),
                ('appearance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='adjudication.Appearance')),
            ],
            options={
                'get_latest_by': ['num'],
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(0, 'New'), (10, 'Verified'), (25, 'Cleared'), (30, 'Flagged'), (35, 'Revised'), (40, 'Confirmed')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('points', models.IntegerField(blank=True, help_text='\n            The number of points (0-100)', null=True, validators=[django.core.validators.MaxValueValidator(100, message='Points must be between 0 - 100'), django.core.validators.MinValueValidator(0, message='Points must be between 0 - 100')])),
                ('panelist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='adjudication.Panelist')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='adjudication.Song')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(0, 'New'), (10, 'Built'), (20, 'Started'), (25, 'Completed'), (27, 'Verified'), (30, 'Published')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('kind', models.IntegerField(choices=[(1, 'Finals'), (2, 'Semi-Finals'), (3, 'Quarter-Finals')])),
                ('num', models.IntegerField(default=0)),
                ('spots', models.IntegerField(default=0)),
                ('date', models.DateField(blank=True, null=True)),
                ('footnotes', models.TextField(blank=True, help_text='\n            Freeform text field; will print on OSS.')),
                ('oss_report', models.FileField(blank=True, default='', upload_to=apps.adjudication.fields.UploadPath('oss_report'))),
                ('sa_report', models.FileField(blank=True, default='', upload_to=apps.adjudication.fields.UploadPath('sa_report'))),
                ('legacy_oss', models.FileField(blank=True, default='', upload_to=apps.adjudication.fields.UploadPath('legacy_oss'))),
                ('is_reviewed', models.BooleanField(default=False, help_text='Reviewed for history app')),
                ('convention_id', models.UUIDField(blank=True, null=True)),
                ('nomen', models.CharField(blank=True, default='', max_length=255)),
                ('timezone', timezone_field.fields.TimeZoneField(blank=True, help_text='\n            The local timezone of the convention.', null=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=apps.adjudication.fields.UploadPath('image'))),
                ('session_id', models.UUIDField(blank=True, null=True)),
                ('session_kind', models.IntegerField(blank=True, choices=[(32, 'Chorus'), (41, 'Quartet'), (42, 'Mixed'), (43, 'Senior'), (44, 'Youth'), (45, 'Unknown'), (46, 'VLQ')], help_text='\n            The kind of session.  Generally this will be either quartet or chorus.\n        ', null=True)),
                ('owners', models.ManyToManyField(related_name='rounds', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': ['num'],
            },
        ),
        migrations.AddField(
            model_name='panelist',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panelists', to='adjudication.Round'),
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(-10, 'Inactive'), (0, 'New'), (10, 'Active')], default=0)),
                ('num', models.IntegerField(blank=True, null=True)),
                ('winner', models.CharField(blank=True, max_length=1024, null=True)),
                ('award_id', models.UUIDField(blank=True, null=True)),
                ('name', models.CharField(blank=True, help_text='Award Name.', max_length=255, null=True)),
                ('kind', models.IntegerField(blank=True, choices=[(32, 'Chorus'), (41, 'Quartet')], null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(10, 'Male'), (20, 'Female'), (30, 'Mixed')], help_text='\n            The gender to which the award is restricted.  If unselected, this award is open to all combinations.\n        ', null=True)),
                ('level', models.IntegerField(blank=True, choices=[(10, 'Championship'), (30, 'Qualifier'), (45, 'Representative'), (50, 'Deferred'), (60, 'Manual'), (70, 'Improved - Raw'), (80, 'Improved - Standard')], null=True)),
                ('season', models.IntegerField(blank=True, choices=[(1, 'Summer'), (2, 'Midwinter'), (3, 'Fall'), (4, 'Spring')], null=True)),
                ('description', models.TextField(blank=True, help_text='\n            The Public description of the award.', max_length=1000, null=True)),
                ('district', models.CharField(blank=True, max_length=255, null=True)),
                ('division', models.IntegerField(blank=True, choices=[(10, 'EVG Division I'), (20, 'EVG Division II'), (30, 'EVG Division III'), (40, 'EVG Division IV'), (50, 'EVG Division V'), (60, 'FWD Arizona'), (70, 'FWD Northeast'), (80, 'FWD Northwest'), (90, 'FWD Southeast'), (100, 'FWD Southwest'), (110, 'LOL 10000 Lakes'), (120, 'LOL Division One'), (130, 'LOL Northern Plains'), (140, 'LOL Packerland'), (150, 'LOL Southwest'), (170, 'MAD Central'), (180, 'MAD Northern'), (190, 'MAD Southern'), (210, 'NED Granite and Pine'), (220, 'NED Mountain'), (230, 'NED Patriot'), (240, 'NED Sunrise'), (250, 'NED Yankee'), (260, 'SWD Northeast'), (270, 'SWD Northwest'), (280, 'SWD Southeast'), (290, 'SWD Southwest')], null=True)),
                ('age', models.IntegerField(blank=True, choices=[(10, 'Seniors'), (20, 'Novice'), (30, 'Youth')], null=True)),
                ('is_novice', models.BooleanField(blank=True, default=False, null=True)),
                ('size', models.IntegerField(blank=True, choices=[(100, 'Plateau 1'), (110, 'Plateau 2'), (120, 'Plateau 3'), (130, 'Plateau 4'), (140, 'Plateau A'), (150, 'Plateau AA'), (160, 'Plateau AAA'), (170, 'Plateau AAAA'), (180, 'Plateau B'), (190, 'Plateau I'), (200, 'Plateau II'), (210, 'Plateau III'), (220, 'Plateau IV'), (230, 'Small')], null=True)),
                ('size_range', django.contrib.postgres.fields.ranges.IntegerRangeField(blank=True, null=True)),
                ('scope', models.IntegerField(blank=True, choices=[(100, 'Plateau 1'), (110, 'Plateau 2'), (120, 'Plateau 3'), (130, 'Plateau 4'), (140, 'Plateau A'), (150, 'Plateau AA'), (160, 'Plateau AAA'), (170, 'Plateau AAAA'), (175, 'Plateau AAAAA')], null=True)),
                ('scope_range', django.contrib.postgres.fields.ranges.DecimalRangeField(blank=True, null=True)),
                ('tree_sort', models.IntegerField(blank=True, editable=False, null=True)),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outcomes', to='adjudication.Round')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='appearance',
            name='outcomes',
            field=models.ManyToManyField(blank=True, related_name='appearances', to='adjudication.Outcome'),
        ),
        migrations.AddField(
            model_name='appearance',
            name='owners',
            field=models.ManyToManyField(related_name='appearances', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appearance',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appearances', to='adjudication.Round'),
        ),
    ]
