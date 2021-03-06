from django.shortcuts import render
from .forms import ContactForm, SignUpForm
from django.core.mail import send_mail
from django.conf import settings
from .models import SignUp

# Create your views here.
def home(request):
    title = "Subscribe to our Newsletter"
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
    }
    if form.is_valid():
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get('full_name')
        if not full_name:
            full_name = 'New full name'
        instance.full_name = full_name

        # if not instance.full_name:
        #     instance.full_name = 'Adolfo'
        instance.save()
        context = {
            "title": "Thank you",
        }

    if request.user.is_authenticated() and request.user.is_staff:
        #print(SignUp.objects.all() )    ## output to stdout
        # for instance in SignUp.objects.all():
        #     print(instance)
        queryset = SignUp.objects.all().order_by('-timestamp') #.filter(full_name__icontains='Adolfo')
        # print(SignUp.objects.all().order_by('-timestamp').filter(full_name__icontains='Adolfo').count())
        context={
            "queryset": queryset
        }

    return render(request, "home.html", context)


def contact(request):
    title = "Contat Us"
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # Tutotrial uses iteritems. No longer supported
        # for key, value in form.cleaned_data.items():
        #     print( key, value )
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')
        # print(email, message,full_name)
        subject = 'Correo desde Django'
        email_message = """
        %s: %s via %s
        """ % (form_full_name, form_message, form_email)
        from_email = settings.EMAIL_HOST_USER
        to_email = [form_email]
        send_mail(subject, email_message, from_email,
                to_email, fail_silently=False)

    context = {
        'form': form,
        'title': title,
        'title_align_center': title_align_center,
    }
    return render(request, 'forms.html', context)
