from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from useraccounts.forms import CustomSignupForm
from django.contrib.auth.views import LoginView
from django.template.loader import render_to_string
from django.core.mail import send_mail
# Create your views here.

class UserLoginView(LoginView):
    template_name='login.html'
    redirect_authenticated_user=True# for not to get login again after loin

    # def get_success_url(self):
    #     if self.request.user.is_superuser:
    #         return HttpResponseRedirect(redirect_to)
    #     else:
    #         return HttpResponseRedirect(redirect_to)

    
def signup_view(request):
    form=CustomSignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('user:login'))
    context={'form': form}
    return render(request, 'register.html', context)


def send_conform_email(request):
    subject="Test Subject"
    message='Test message'
    from_email='sauravjoc22@gmail.com'
    recipient_list=['nirajanjoc19@gmail.com',]
    html_message=render_to_string('email_test.html', {'name':'PYTHON'})
    result= send_mail(subject, message, from_email, recipient_list, html_message=html_message)
    return HttpResponse(result)