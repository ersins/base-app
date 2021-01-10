import os


class DatabaseEnv:
    """Sistem değişkenlerine eklenen verilerden veri alır."""
    NAME = os.getenv('POSTGRES_DB')
    USER = os.getenv('POSTGRES_USER')
    PASSWORD = os.getenv('POSTGRES_PASSWORD')
    HOST = os.getenv('DATABASE_HOST')
    PORT = os.getenv('DATABASE_PORT')


class SecretsEnv:
    """Sistem değişkenlerine eklenen SECRET_KEY verisini alır."""
    SECRET_KEY = os.getenv('SECRET_KEY')


class DebugEnv:
    DEDUG = int(os.getenv('DEBUG', 0))


class AllowedHostEnv:
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')


class Internationalization:
    LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'tr')
    TIME_ZONE = os.getenv('TIME_ZONE', 'Europe/Istanbul')


class FolderRoots:
    """FolderRoots."""

    def get_template_dirs(base_dir):
        return [os.path.join(base_dir, 'templates'),]

    def get_media_root(base_dir):
        return os.path.join(os.path.dirname(base_dir), "static_cdn", "media_root")

    def get_static_root(base_dir):
        return os.path.join(os.path.dirname(base_dir), "static_cdn", "static_root")

    def get_protected_root(base_dir):
        return os.path.join(os.path.dirname(base_dir), "static_cdn", "protected_media")

    def get_staticfiles_root(base_dir):
        return os.path.join(base_dir, "static_webapp")
