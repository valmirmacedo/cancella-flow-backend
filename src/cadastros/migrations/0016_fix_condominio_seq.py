from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cadastros", "0015_condominio_logo_db_content_type_and_more"),
    ]

    operations = [
        migrations.RunSQL(
            "SELECT setval(pg_get_serial_sequence('cadastros_condominio','id'), COALESCE((SELECT MAX(id) FROM cadastros_condominio), 0));",
            reverse_sql="SELECT setval(pg_get_serial_sequence('cadastros_condominio','id'), COALESCE((SELECT MAX(id) FROM cadastros_condominio), 0));",
        )
    ]
