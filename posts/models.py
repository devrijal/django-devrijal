from django.db import models

STATUS_CHOICE = (
		(1, 'Active'),
		(0, 'Inactive'),
	)
# Create your models here.
class Posts(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=256, default='')
	content = models.TextField(max_length=3000)
	category_id = models.IntegerField(default=0)
	slug = models.SlugField(help_text="A short label, generally used in URLs.")
	is_active = models.IntegerField(default=0, choices=STATUS_CHOICE)
	created_date = models.DateTimeField(auto_now=True)
	updated_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title
