from django.shortcuts import render,redirect
from .models import Profile,User
from .forms import UserForm,AdditionalInfoForm
from django.http import HttpResponse

# CVB
from django.views.generic import TemplateView,DetailView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'user/index.html'
    extra_context = {'title': 'Home'}

def sign_up(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        additional_form = AdditionalInfoForm(request.POST)

        if user_form.is_valid() and additional_form.is_valid():
            user = user_form.save()

            additional = additional_form.save(commit=False)
            additional.user = user

            if 'profile_pic' in request.FILES:
                additional.profile_pic = request.FILES['profile_pic']
            additional.save()
            return redirect('login')
        else:
            print(user_form.errors,additional_form.errors)
    else:
        user_form = UserForm()
        additional_form = AdditionalInfoForm()
    return render(request,'user/user_form.html',{'user_form': user_form,
                                                'additional_form': additional_form,
                                                'title':'sign_up'})

class ProfileDetailView(DetailView):

    model = Profile
    