from django.db import models
from django.utils.text import slugify


class BlogPost(models.Model):
    CATEGORY_CHOICES = (
        ('planejamento', 'Planejamento Financeiro'),
        ('investimentos', 'Investimentos'),
        ('economia', 'Economia'),
        ('dicas', 'Dicas'),
        ('noticias', 'Notícias'),
        ('mercado', 'Mercado'),
    )

    title = models.CharField('Título', max_length=200)
    slug = models.SlugField('Slug', max_length=200, unique=True, blank=True)
    summary = models.CharField('Resumo', max_length=300)
    content = models.TextField('Conteúdo')
    image = models.ImageField('Imagem', upload_to='blog/', blank=True, null=True)
    category = models.CharField('Categoria', max_length=30, choices=CATEGORY_CHOICES, default='noticias')
    published = models.BooleanField('Publicado', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            # Ensure uniqueness
            original_slug = self.slug
            counter = 1
            while BlogPost.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f'{original_slug}-{counter}'
                counter += 1
        super().save(*args, **kwargs)
