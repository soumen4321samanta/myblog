from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    #Category te post gulo group hobe(Technology, sports,etc)
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)

    class Meta:
        verbose_name_plural='categories'  #admin e "Catagory" na hoya catagoris dekha be
    
    def __str__(self):
        return self.name # admin e name dekhabe "Category object(1)" na


class Tag(models.Model):
    #Post e multiple tag lagano jabe (ManyToMany)
    
    name=models.CharField(max_length=50,unique=True)


    def __str__(self):
        return self.name
    

class Posted(models.Model):
    STATUS_CHOICES=[
        ('draft','Draft'),
        ('published','Published'),
    ]


    #Basic Fields
    title=models.CharField(max_length=200)
    body=models.TextField()
    status=models.CharField(max_length=9,choices=STATUS_CHOICES, default='draft')


    #Dates - auto set hobe
    created_at=models.DateTimeField(auto_now_add=True) #sudhu create hobe time
    updated_at=models.DateTimeField(auto_now=True)     # save holei update

    
    # Relationships
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name='posts')
    
    tag=models.ManyToManyField(Tag,blank=True,related_name='posts')


    class Meta:
        ordering=['-created_at']   #newest first
    
    def __str__(self):
        return self.title


