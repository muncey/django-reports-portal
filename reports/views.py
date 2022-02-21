from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Report

@login_required()
def index(request):
    report_list = Report.objects.order_by('-report_added_date')[:5]
    context = { 'report_list': report_list }
    return render(request, 'reports/index.html', context)

@login_required()
def detail(request, report_id):
  report = get_object_or_404(Report, pk=report_id)
  report_comment_list = report.reportcomment_set.all()
  return render(request, 'reports/detail.html', { 
    'report': report, 
    'comment_list': report_comment_list 
  })

@login_required()
def comment(request, report_id):
  report = get_object_or_404(Report, pk=report_id)
  comment_text = request.POST['comment_text']
  report.reportcomment_set.create(
    comment_text = comment_text,
    comment_added_date = timezone.now()
  )
  report_comment_list = report.reportcomment_set.all()
  return render(request, 'reports/detail.html', { 
    'report': report, 
    'comment_list': report_comment_list 
  })