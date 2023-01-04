from django.db import models

class Universal_Word(models.Model):
    slug = models.SlugField()
    

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Korean_Word(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField()
    universal_word = models.ForeignKey(
        Universal_Word,
        related_name='korean_words',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Japanese_Word(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField()
    universal_word = models.ForeignKey(
        Universal_Word,
        related_name='japanese_words',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Mandarin_Word(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField()
    universal_word = models.ForeignKey(
        Universal_Word,
        related_name='mandarin_words',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class English_Word(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField()
    universal_word = models.ForeignKey(
        Universal_Word,
        related_name='english_words',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
