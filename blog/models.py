from django.db import models

class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=500, default="")
    titleContent = models.CharField(max_length=5000, default="")
    heading = models.CharField(max_length=500, default="")
    headingContent = models.CharField(max_length=5000)
    subHeading = models.CharField(max_length=500, default="")
    subHeadingContent = models.CharField(max_length=5000, default="")
    thumbnail = models.ImageField(upload_to="blog/images", default="")

    def __str__(self):
        return self.title
