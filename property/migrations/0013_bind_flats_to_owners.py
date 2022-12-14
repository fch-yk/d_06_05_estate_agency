# Generated by Django 2.2.24 on 2022-10-25 18:52

from django.db import migrations

# pylint: disable=unused-argument


def bind_flats_to_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')  # noqa: N806
    owner_model = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    if not flats.exists():
        return
    for flat in flats.iterator():
        owner, _ = owner_model.objects.get_or_create(
            name=flat.owner,
            pure_phone=flat.owner_pure_phone,
            defaults={
                'name': flat.owner,
                'phonenumber': flat.owners_phonenumber,
                'pure_phone': flat.owner_pure_phone}
        )
        flat.owners.set([owner])


def unbind_flats_from_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')  # noqa: N806
    flats = Flat.objects.all()
    if flats.exists():
        for flat in flats.iterator():
            flat.owners.clear()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_owner_indexes'),
    ]

    operations = [
        migrations.RunPython(bind_flats_to_owners, unbind_flats_from_owners)
    ]
