from django.db import models

class Post(models.Model):
    titulo= models.CharField(max_length=100)
    contenido= models.TextField()

    def __str__(self) -> str:
        return self.titulo
    
class Autor(models.Model):
    nombre= models.CharField(max_length=50)
    edad= models.IntegerField()
    email= models.EmailField()

    def __str__(self) -> str:
        return self.nombre
    
class Comentario(models.Model):
    contenido=models.CharField(max_length=150)
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.contenido