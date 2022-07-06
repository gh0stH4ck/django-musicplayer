def audio_validator(value) -> None:
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1] # return path + filename
    valid_exceptions = [".mp3", ".ogg", ".wav"]
    if not ext.lower() in valid_exceptions:
        raise ValidationError("Unsupported file exception")