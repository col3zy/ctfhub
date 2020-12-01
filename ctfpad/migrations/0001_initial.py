# Generated by Django 3.1.3 on 2020-12-01 18:22

import ctfpad.helpers
import ctfpad.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('points', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('note_id', models.CharField(blank=True, max_length=80)),
                ('flag', models.CharField(blank=True, max_length=128)),
                ('status', model_utils.fields.StatusField(choices=[('unsolved', 'unsolved'), ('solved', 'solved')], default='unsolved', max_length=100, no_check_for_status=True)),
                ('solved_time', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', when={'solved'})),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChallengeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Ctf',
            fields=[
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('url', models.URLField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('flag_prefix', models.CharField(blank=True, max_length=64)),
                ('team_login', models.CharField(blank=True, max_length=128)),
                ('team_password', models.CharField(blank=True, max_length=128)),
                ('ctftime_id', models.IntegerField(blank=True, default=0, null=True)),
                ('visibility', model_utils.fields.StatusField(choices=[('public', 'public'), ('private', 'private')], default='public', max_length=100, no_check_for_status=True)),
                ('weight', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=256, unique=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('github_url', models.URLField(blank=True)),
                ('youtube_url', models.URLField(blank=True)),
                ('blog_url', models.URLField(blank=True)),
                ('api_key', models.CharField(default=ctfpad.helpers.get_random_string_128, max_length=128)),
                ('avatar', models.ImageField(blank=True, upload_to='media/')),
                ('ctftime_id', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('avatar', models.ImageField(blank=True, upload_to='media/')),
                ('description', models.TextField(blank=True)),
                ('country', model_utils.fields.StatusField(choices=[('Andorra', 'Andorra'), ('United Arab Emirates', 'United Arab Emirates'), ('Afghanistan', 'Afghanistan'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Anguilla', 'Anguilla'), ('Albania', 'Albania'), ('Armenia', 'Armenia'), ('Angola', 'Angola'), ('Antarctica', 'Antarctica'), ('Argentina', 'Argentina'), ('American Samoa', 'American Samoa'), ('Austria', 'Austria'), ('Australia', 'Australia'), ('Aruba', 'Aruba'), ('Åland Islands', 'Åland Islands'), ('Azerbaijan', 'Azerbaijan'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Barbados', 'Barbados'), ('Bangladesh', 'Bangladesh'), ('Belgium', 'Belgium'), ('Burkina Faso', 'Burkina Faso'), ('Bulgaria', 'Bulgaria'), ('Bahrain', 'Bahrain'), ('Burundi', 'Burundi'), ('Benin', 'Benin'), ('Saint Barthélemy', 'Saint Barthélemy'), ('Bermuda', 'Bermuda'), ('Brunei', 'Brunei'), ('Bolivia', 'Bolivia'), ('Caribbean Netherlands', 'Caribbean Netherlands'), ('Brazil', 'Brazil'), ('Bahamas', 'Bahamas'), ('Bhutan', 'Bhutan'), ('Bouvet Island', 'Bouvet Island'), ('Botswana', 'Botswana'), ('Belarus', 'Belarus'), ('Belize', 'Belize'), ('Canada', 'Canada'), ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'), ('DR Congo', 'DR Congo'), ('Central African Republic', 'Central African Republic'), ('Republic of the Congo', 'Republic of the Congo'), ('Switzerland', 'Switzerland'), ("Côte d'Ivoire (Ivory Coast)", "Côte d'Ivoire (Ivory Coast)"), ('Cook Islands', 'Cook Islands'), ('Chile', 'Chile'), ('Cameroon', 'Cameroon'), ('China', 'China'), ('Colombia', 'Colombia'), ('Costa Rica', 'Costa Rica'), ('Cuba', 'Cuba'), ('Cape Verde', 'Cape Verde'), ('Curaçao', 'Curaçao'), ('Christmas Island', 'Christmas Island'), ('Cyprus', 'Cyprus'), ('Czechia', 'Czechia'), ('Germany', 'Germany'), ('Djibouti', 'Djibouti'), ('Denmark', 'Denmark'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('Algeria', 'Algeria'), ('Ecuador', 'Ecuador'), ('Estonia', 'Estonia'), ('Egypt', 'Egypt'), ('Western Sahara', 'Western Sahara'), ('Eritrea', 'Eritrea'), ('Spain', 'Spain'), ('Ethiopia', 'Ethiopia'), ('European Union', 'European Union'), ('Finland', 'Finland'), ('Fiji', 'Fiji'), ('Falkland Islands', 'Falkland Islands'), ('Micronesia', 'Micronesia'), ('Faroe Islands', 'Faroe Islands'), ('France', 'France'), ('Gabon', 'Gabon'), ('United Kingdom', 'United Kingdom'), ('England', 'England'), ('Northern Ireland', 'Northern Ireland'), ('Scotland', 'Scotland'), ('Wales', 'Wales'), ('Grenada', 'Grenada'), ('Georgia', 'Georgia'), ('French Guiana', 'French Guiana'), ('Guernsey', 'Guernsey'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Greenland', 'Greenland'), ('Gambia', 'Gambia'), ('Guinea', 'Guinea'), ('Guadeloupe', 'Guadeloupe'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Greece', 'Greece'), ('South Georgia', 'South Georgia'), ('Guatemala', 'Guatemala'), ('Guam', 'Guam'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Hong Kong', 'Hong Kong'), ('Heard Island and McDonald Islands', 'Heard Island and McDonald Islands'), ('Honduras', 'Honduras'), ('Croatia', 'Croatia'), ('Haiti', 'Haiti'), ('Hungary', 'Hungary'), ('Indonesia', 'Indonesia'), ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('Isle of Man', 'Isle of Man'), ('India', 'India'), ('British Indian Ocean Territory', 'British Indian Ocean Territory'), ('Iraq', 'Iraq'), ('Iran', 'Iran'), ('Iceland', 'Iceland'), ('Italy', 'Italy'), ('Jersey', 'Jersey'), ('Jamaica', 'Jamaica'), ('Jordan', 'Jordan'), ('Japan', 'Japan'), ('Kenya', 'Kenya'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Cambodia', 'Cambodia'), ('Kiribati', 'Kiribati'), ('Comoros', 'Comoros'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('North Korea', 'North Korea'), ('South Korea', 'South Korea'), ('Kuwait', 'Kuwait'), ('Cayman Islands', 'Cayman Islands'), ('Kazakhstan', 'Kazakhstan'), ('Laos', 'Laos'), ('Lebanon', 'Lebanon'), ('Saint Lucia', 'Saint Lucia'), ('Liechtenstein', 'Liechtenstein'), ('Sri Lanka', 'Sri Lanka'), ('Liberia', 'Liberia'), ('Lesotho', 'Lesotho'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Latvia', 'Latvia'), ('Libya', 'Libya'), ('Morocco', 'Morocco'), ('Monaco', 'Monaco'), ('Moldova', 'Moldova'), ('Montenegro', 'Montenegro'), ('Saint Martin', 'Saint Martin'), ('Madagascar', 'Madagascar'), ('Marshall Islands', 'Marshall Islands'), ('North Macedonia', 'North Macedonia'), ('Mali', 'Mali'), ('Myanmar', 'Myanmar'), ('Mongolia', 'Mongolia'), ('Macau', 'Macau'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Montserrat', 'Montserrat'), ('Malta', 'Malta'), ('Mauritius', 'Mauritius'), ('Maldives', 'Maldives'), ('Malawi', 'Malawi'), ('Mexico', 'Mexico'), ('Malaysia', 'Malaysia'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('New Caledonia', 'New Caledonia'), ('Niger', 'Niger'), ('Norfolk Island', 'Norfolk Island'), ('Nigeria', 'Nigeria'), ('Nicaragua', 'Nicaragua'), ('Netherlands', 'Netherlands'), ('Norway', 'Norway'), ('Nepal', 'Nepal'), ('Nauru', 'Nauru'), ('Niue', 'Niue'), ('New Zealand', 'New Zealand'), ('Oman', 'Oman'), ('Panama', 'Panama'), ('Peru', 'Peru'), ('French Polynesia', 'French Polynesia'), ('Papua New Guinea', 'Papua New Guinea'), ('Philippines', 'Philippines'), ('Pakistan', 'Pakistan'), ('Poland', 'Poland'), ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'), ('Pitcairn Islands', 'Pitcairn Islands'), ('Puerto Rico', 'Puerto Rico'), ('Palestine', 'Palestine'), ('Portugal', 'Portugal'), ('Palau', 'Palau'), ('Paraguay', 'Paraguay'), ('Qatar', 'Qatar'), ('Réunion', 'Réunion'), ('Romania', 'Romania'), ('Serbia', 'Serbia'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('Saudi Arabia', 'Saudi Arabia'), ('Solomon Islands', 'Solomon Islands'), ('Seychelles', 'Seychelles'), ('Sudan', 'Sudan'), ('Sweden', 'Sweden'), ('Singapore', 'Singapore'), ('Saint Helena, Ascension and Tristan da Cunha', 'Saint Helena, Ascension and Tristan da Cunha'), ('Slovenia', 'Slovenia'), ('Svalbard and Jan Mayen', 'Svalbard and Jan Mayen'), ('Slovakia', 'Slovakia'), ('Sierra Leone', 'Sierra Leone'), ('San Marino', 'San Marino'), ('Senegal', 'Senegal'), ('Somalia', 'Somalia'), ('Suriname', 'Suriname'), ('South Sudan', 'South Sudan'), ('São Tomé and Príncipe', 'São Tomé and Príncipe'), ('El Salvador', 'El Salvador'), ('Sint Maarten', 'Sint Maarten'), ('Syria', 'Syria'), ('Eswatini (Swaziland)', 'Eswatini (Swaziland)'), ('Turks and Caicos Islands', 'Turks and Caicos Islands'), ('Chad', 'Chad'), ('French Southern and Antarctic Lands', 'French Southern and Antarctic Lands'), ('Togo', 'Togo'), ('Thailand', 'Thailand'), ('Tajikistan', 'Tajikistan'), ('Tokelau', 'Tokelau'), ('Timor-Leste', 'Timor-Leste'), ('Turkmenistan', 'Turkmenistan'), ('Tunisia', 'Tunisia'), ('Tonga', 'Tonga'), ('Turkey', 'Turkey'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Tuvalu', 'Tuvalu'), ('Taiwan', 'Taiwan'), ('Tanzania', 'Tanzania'), ('Ukraine', 'Ukraine'), ('Uganda', 'Uganda'), ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'), ('United Nations', 'United Nations'), ('United States', 'United States'), ('Alaska', 'Alaska'), ('Alabama', 'Alabama'), ('Arkansas', 'Arkansas'), ('Arizona', 'Arizona'), ('California', 'California'), ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Iowa', 'Iowa'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Massachusetts', 'Massachusetts'), ('Maryland', 'Maryland'), ('Maine', 'Maine'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Missouri', 'Missouri'), ('Mississippi', 'Mississippi'), ('Montana', 'Montana'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Nebraska', 'Nebraska'), ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('Nevada', 'Nevada'), ('New York', 'New York'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Virginia', 'Virginia'), ('Vermont', 'Vermont'), ('Washington', 'Washington'), ('Wisconsin', 'Wisconsin'), ('West Virginia', 'West Virginia'), ('Wyoming', 'Wyoming'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vatican City (Holy See)', 'Vatican City (Holy See)'), ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'), ('Venezuela', 'Venezuela'), ('British Virgin Islands', 'British Virgin Islands'), ('United States Virgin Islands', 'United States Virgin Islands'), ('Vietnam', 'Vietnam'), ('Vanuatu', 'Vanuatu'), ('Wallis and Futuna', 'Wallis and Futuna'), ('Samoa', 'Samoa'), ('Kosovo', 'Kosovo'), ('Yemen', 'Yemen'), ('Mayotte', 'Mayotte'), ('South Africa', 'South Africa'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], default='Andorra', max_length=100, no_check_for_status=True)),
                ('timezone', model_utils.fields.StatusField(choices=[('UTC+0', 'UTC+0'), ('UTC-12', 'UTC-12'), ('UTC-11', 'UTC-11'), ('UTC-10', 'UTC-10'), ('UTC-9', 'UTC-9'), ('UTC-8', 'UTC-8'), ('UTC-7', 'UTC-7'), ('UTC-6', 'UTC-6'), ('UTC-5', 'UTC-5'), ('UTC-4', 'UTC-4'), ('UTC-3', 'UTC-3'), ('UTC-2', 'UTC-2'), ('UTC-1', 'UTC-1'), ('UTC+1', 'UTC+1'), ('UTC+2', 'UTC+2'), ('UTC+3', 'UTC+3'), ('UTC+4', 'UTC+4'), ('UTC+5', 'UTC+5'), ('UTC+6', 'UTC+6'), ('UTC+7', 'UTC+7'), ('UTC+8', 'UTC+8'), ('UTC+9', 'UTC+9'), ('UTC+10', 'UTC+10'), ('UTC+11', 'UTC+11'), ('UTC+12', 'UTC+12')], default='UTC+0', max_length=100, no_check_for_status=True)),
                ('last_scored', models.DateTimeField(null=True)),
                ('show_pending_notifications', models.BooleanField(default=False)),
                ('last_active_notification', models.DateTimeField(null=True)),
                ('joined_time', models.DateTimeField(null=True)),
                ('hedgedoc_password', models.CharField(max_length=64, null=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('github_url', models.URLField(blank=True)),
                ('blog_url', models.URLField(blank=True)),
                ('selected_ctf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ctfpad.ctf')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ctfpad.team')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ctf',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ctfpad.member'),
        ),
        migrations.CreateModel(
            name='ChallengeFile',
            fields=[
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(null=True, upload_to='files/', validators=[ctfpad.validators.challenge_file_max_size_validator])),
                ('mime', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=512)),
                ('hash', models.CharField(max_length=64)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctfpad.challenge')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='challenge',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ctfpad.challengecategory'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='ctf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctfpad.ctf'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='last_update_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='last_updater', to='ctfpad.member'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='solvers',
            field=models.ManyToManyField(blank=True, related_name='solved_challenges', to='ctfpad.Member'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='challenges', to='ctfpad.Tag'),
        ),
    ]
