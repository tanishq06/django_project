# Generated by Django 3.1.7 on 2021-06-10 14:03

from __future__ import unicode_literals
from django.db import migrations


LANGUAGES  = [
    {
        'name': 'Plain Text',
        'lang_code': 'text',
        'slug': 'text',
        'mime': 'text/plain',
        'file_extension': '.txt',
    },
    {
        'name': 'Bash',
        'lang_code': 'bash',
        'slug': 'bash',
        'mime': 'application/x-sh',
        'file_extension': '.sh',
    },
    {
        'name': 'C',
        'lang_code': 'c',
        'slug': 'c',
        'mime': 'text/x-chdr',
        'file_extension': '.c',
    },
    {
        'name': 'C#',
        'lang_code': 'c#',
        'slug': 'c-sharp',
        'mime': 'text/plain',
        'file_extension': '.aspx,',
    },
    {
        'name': 'C++',
        'lang_code': 'c++',
        'slug': 'cpp',
        'mime': 'text/x-c++hdr',
        'file_extension': '.txt',
    },
    {
        'name': 'CSS',
        'lang_code': 'css',
        'slug': 'css',
        'mime': 'text/css',
        'file_extension': '.css,',
    },
    {
        'name': 'HTML',
        'lang_code': 'html',
        'slug': 'html',
        'mime': 'text/plain',
        'file_extension': '.html',
    },
    {
        'name': 'Java',
        'lang_code': 'java',
        'slug': 'java',
        'mime': 'text/x-java',
        'file_extension': '.java',
    },
    {
        'name': 'JavaScript',
        'lang_code': 'js',
        'slug': 'js',
        'mime': 'application/javascript',
        'file_extension': '.js',
    },
    {
        'name': 'JSON',
        'lang_code': 'json',
        'slug': 'json',
        'mime': 'application/json',
        'file_extension': '.json',
    },
    {
        'name': 'PHP',
        'lang_code': 'php',
        'slug': 'php',
        'mime': 'text/x-php',
        'file_extension': '.php',
    },
    {
        'name': 'Python',
        'lang_code': 'python',
        'slug': 'python',
        'mime': 'text/x-cython',
        'file_extension': '.py',
    },
    {
        'name': 'Perl',
        'lang_code': 'perl',
        'slug': 'perl',
        'mime': 'text/x-cython',
        'file_extension': '.py',
    },
    {
        'name': 'SQL',
        'lang_code': 'sql',
        'slug': 'sql',
        'mime': 'text/x-sql',
        'file_extension': '.sql',
    },
    {
        'name': 'Ruby',
        'lang_code': 'ruby',
        'slug': 'ruby',
        'mime': 'text/x-ruby',
        'file_extension': '.rb',
    },
    {
        'name': 'Swift',
        'lang_code': 'swift',
        'slug': 'swift',
        'mime': 'text/x-swift',
        'file_extension': '.swift',
    }

]




# forward function
def add_languages(apps, schema_editor):
    Language = apps.get_model('djangobin', 'Language')

    for lang in LANGUAGES:
        l = Language.objects.get_or_create(
            name = lang['name'],
            lang_code = lang['lang_code'],
            slug = lang['slug'],
            mime = lang['mime'],
            file_extension = lang['file_extension'],
        )

        print(l)


# backward function
def remove_languages(apps, schema_editor):
    Language = apps.get_model('djangobin', 'Language')

    for lang in LANGUAGES:
        l = Language.objects.get(
            lang_code=lang['lang_code'],
        )

        l.delete()



class Migration(migrations.Migration):

    dependencies = [
        ('djangobin', '0006_auto_20210610_1911'),
    ]

    operations = [
        migrations.RunPython(
            add_languages,
            remove_languages
        )
    ]