from django.db import models


class Shapes(models.Model):
    name = models.CharField(max_length=50, null=False)
    info_shapes = models.CharField(max_length=500)
    picture_shapes = models.ImageField(upload_to='burmax/Pictures/shapes/', blank=True)


class CutsTypes(models.Model):
    shapes = models.ForeignKey(Shapes, on_delete=models.CASCADE)
    types_name = models.CharField(max_length=50, null=False)
    info_types = models.CharField(max_length=500)
    picture_cuts =  models.ImageField(upload_to='burmax/Pictures/cuts', blank=True)


class ShankSize(models.Model):
    #shapes = models.ForeignKey(Shapes, on_delete=models.CASCADE)
    cutsTypes = models.ForeignKey(CutsTypes, on_delete=models.CASCADE)
    shank_size_name = models.CharField(max_length=50, null=False)


class HeadSize(models.Model):
    #shapes = models.ForeignKey(Shapes, on_delete=models.CASCADE)
    #cutsTypes = models.ForeignKey(CutsTypes, on_delete=models.CASCADE)
    shankSize = models.ForeignKey(ShankSize, on_delete=models.CASCADE)
    head_size_name = models.CharField(max_length=50, null=False)
