from django.db import models

# Create your models here.
class  Categoria(models.Model):
    
    nome = models.CharField(max_length=100)
    dt_criaçao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
class Transação(models.Model):
    data = models.DateTimeField()
    descrição = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observação = models.TextField(null=True, blank=True) 
    
    class Meta:
        verbose_name_plural='Transação'
     
    def __str__(self):
        return self.descrição     
