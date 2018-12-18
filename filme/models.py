from django.db import models

class Filme(models.Model):
    titulo = models.CharField('Título', max_length=80)
    the_movie_db_id = models.IntegerField('ID TMD')
    data_lancamento = models.DateField('Data lançamento')
    sinopse = models.TextField('Sinopse')
    imagem_poster = models.CharField('URL Poster', max_length=300)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'filme'
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        ordering = ['-data_lancamento']
