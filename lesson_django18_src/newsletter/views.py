from django.shortcuts import render
from .forms import ContactForm, SignUpForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    title = "Welcome"
    # if request.user.is_authenticated():
    #     title = "My Title %s" % (request.user)

    # add a form
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

    return render(request, "example_fluid.html", context)


def contact(request):
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
    }
    return render(request, 'forms.html', context)
