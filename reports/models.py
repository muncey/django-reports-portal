from django.db import models

# Create your models here.
class Report(models.Model):
  report_name = models.CharField(max_length=100)
  report_comments = models.TextField()
  report_added_date = models.DateTimeField('date added')

class ReportComment(models.Model):
  report = models.ForeignKey(Report, on_delete=models.CASCADE)
  comment_text = models.TextField()
  comment_added_date = models.DateTimeField('date added')
