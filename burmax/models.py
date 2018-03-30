from django.db import models


class Shapes(models.Model):
    name = models.CharField(max_length=50)
    info_shapes = models.CharField(max_length=500)
    picture_shapes = models.CharField(max_length=1000)


class CutsTypes(models.Model):
    shapes = models.ForeignKey(Shapes, on_delete=models.CASCADE)
    types_name = models.CharField(max_length=50)
    info_types = models.CharField(max_length=500)
    picture_cuts = models.CharField(max_length=1000)


class ShankSize(models.Model):
    cutsTypes = models.ForeignKey(CutsTypes, on_delete=models.CASCADE)
    shank_size_name = models.CharField(max_length=50)


class HeadSize(models.Model):
    shankSize = models.ForeignKey(ShankSize, on_delete=models.CASCADE)
    head_size_name = models.CharField(max_length=50)
