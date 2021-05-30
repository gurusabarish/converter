from django.shortcuts import render, HttpResponse
import docx2pdf


def docstopdf(request):
    if request.method == 'POST':
        docs = request.FILES['docs']
        pdf = docx2pdf.convert(docs)

        return HttpResponse(pdf, content_type='application/pdf')
    return render(request, 'docstopdf.html')
