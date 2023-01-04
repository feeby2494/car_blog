from django.contrib import admin

from .models import Universal_Word, Korean_Word, Japanese_Word, Mandarin_Word, English_Word

admin.site.register([Universal_Word, Korean_Word, Japanese_Word, Mandarin_Word, English_Word])


