"""
    Two classes for media storage
"""

from storages.backends.s3boto import S3BotoStorage
from django.conf import settings

class StaticStorage(S3BotoStorage):
    """
    Storage for static files.
    The folder is defined in settings.STATIC_S3_PATH
    """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = settings.STATIC_S3_PATH
        super(StaticStorage, self).__init__(*args, **kwargs)

class MediaStorage(S3BotoStorage):
    """
    Storage for uploaded media files.
    The folder is defined in settings.MEDIA_S3_PATH
    """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = settings.MEDIA_S3_PATH
        super(DefaultStorage, self).__init__(*args, **kwargs)

class AudioRecordingStorage(S3BotoStorage):
    """
    Storage for uploaded audio recording files.
    The folder is defined in settings.AUDIO_RECORDING_S3_PATH
    """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = settings.AUDIO_RECORDING_S3_PATH
        super(DefaultStorage, self).__init__(*args, **kwargs)