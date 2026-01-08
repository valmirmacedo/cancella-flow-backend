from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("access", "0006_alter_user_unidade"),
    ]

    operations = [
        # Esta migration atualiza apenas o estado do Django: `id` passa a ser UUIDField.
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.AlterField(
                    model_name="user",
                    name="id",
                    field=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False),
                ),
            ],
        )
    ]
