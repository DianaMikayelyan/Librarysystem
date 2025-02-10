import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .models import Book, BorrowRecord, UserActivity
from .forms import LoginForm
from django.utils import timezone
from django.http import JsonResponse ,HttpResponse
from django.contrib import messages
from django.conf import settings
import logging



logger = logging.getLogger(__name__)

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if book.available:
        book.available = False
        book.save()

        BorrowRecord.objects.create(
            user=request.user,
            book=book,
            borrowed_at=timezone.now(),
            return_by=timezone.now() + timezone.timedelta(days=30)  # 30 days from now
        )

        UserActivity.objects.create(user=request.user, book=book, activity_type='borrow')

        #  PDF donwloadi
        file_path = os.path.join(settings.MEDIA_ROOT, book.digital_file.name)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{book.title}.pdf"'
                return response
        else:
            return JsonResponse({'success': False, 'error': 'File not found'})

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Book not available'})


@login_required
def download_book(request,book_id):
    book = get_object_or_404(Book,id=book_id)
    file_path = os.path.join(settings.MEDIA_ROOT, book.digital_file.name)

    if os.path.exists(file_path):
        with open(file_path,'rb') as file:
            response = HttpResponse(file.read(),content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename={book.title}.pdf"'
            return response
    else:
        return HttpResponse('file not found', status=404)


@login_required
def read_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    
    UserActivity.objects.create(user=request.user, book=book, activity_type='read')

    return redirect(book.read_link)

# glxavorej

def index(request):
    books = Book.objects.all()
    return render(request, 'library/library.html', {'books': books})
   
# usersignup
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'remember-me' in request.POST:
                request.session.set_expiry(60 * 60 * 24 * 30)  # 30 or
            else:
                request.session.set_expiry(0)  # Browser close

            messages.success(request, 'You are now logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'library/login.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session.set_expiry(60 * 60 * 24 * 30)  # 30 or
            messages.success(request, 'You have successfully signed up and are now logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below:')
    else:
        form = UserCreationForm()
    return render(request, 'library/signup.html', {'form': form})



def logout_view(request):
    logout(request)
    messages.success(request,'You have been logged out')
    return redirect('login')


def user_profile(request):
    return render(request, 'library/user.html')

