from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=155)
    content = models.TextField()
    slug = models.SlugField(max_length=255) # A unique name ,we utilize access in the individual a post
    image = models.ImageField(upload_to = "images/" , default = "images/default.png")


#To construct the URL for us
#To make A link (with the help of slug)to our pages :to counstruct a URL based upon the information that  we provide
    def get_absolute_url(self):
        return reverse("blog:electric", args=[self.slug]) #indide the blog we have electric url
    #Every time we run this , we get our url for a very specific post , besic  on slug ,
    # thats matching the slug in  the post in the DataBase!



    def __str__(self):
         return self.title


