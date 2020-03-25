from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def register(request):
    """view for registration"""
    if request.method != 'POST':
        # make a new form
        form = UserCreationForm()
    else:
        # validation and save the form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blog:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)


@login_required
def profile(request):
    """view for profile page"""
    context = {'user': request.user}
    return render(request, 'registration/profile.html', context)
