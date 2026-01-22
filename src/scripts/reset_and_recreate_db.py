import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

import django
django.setup()

from django.conf import settings
from django.db import connection

def reset_sqlite(db_name):
    db_path = BASE_DIR / db_name
    if db_path.exists():
        print('Removing sqlite db:', db_path)
        db_path.unlink()
    else:
        print('SQLite DB not found at', db_path)

def reset_postgres():
    print('Resetting Postgres schema public (DROP SCHEMA CASCADE)')
    with connection.cursor() as cur:
        cur.execute('DROP SCHEMA public CASCADE;')
        cur.execute('CREATE SCHEMA public;')
        # Recreate extension for uuid-ossp if needed
        try:
            cur.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")
        except Exception:
            pass

def remove_migration_files():
    apps = ['access', 'cadastros']
    for app in apps:
        migrations_dir = BASE_DIR / app / 'migrations'
        if migrations_dir.exists():
            for f in migrations_dir.iterdir():
                if f.name == '__init__.py':
                    continue
                if f.is_file():
                    print('Removing migration file', f)
                    f.unlink()

def main():
    engine = settings.DATABASES['default'].get('ENGINE', '')
    name = settings.DATABASES['default'].get('NAME')
    print('Detected DB engine:', engine, 'name:', name)
    if 'sqlite' in engine:
        reset_sqlite(name)
    else:
        reset_postgres()

    print('Removing migration files')
    remove_migration_files()

    print('Done. Now run makemigrations and migrate.')

if __name__ == '__main__':
    main()
