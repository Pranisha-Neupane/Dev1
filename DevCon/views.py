from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from DevCon.models import CustomUser, Room, Message, Participents

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            request.session['userid'] = user.id
            request.session['email'] = email
            return redirect('dashboard')
        messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

# @login_required
def dashboard_view(request):
    rooms = Room.objects.all()
    return render(request, 'dashboard.html', {'rooms': rooms})
    

def logout_view(request):
    logout(request)
    return redirect('login')

# @login_required
def create_room(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user_id = request.session.get('userid')

        if not user_id:
            return redirect('login')  # or show an error message

        user = CustomUser.objects.get(id=user_id)

        room = Room.objects.create(title=title, description=description, created_by=user)
        Participents.objects.create(user=user, room=room)

        return redirect('dashboard')
    return render(request, 'create_room.html')

# @login_required
def join_room(request, room_id):
    room_instance = Room.objects.get(id=room_id)
    room_contents = Message.objects.filter(room=room_instance).order_by('time_stamp')
    rooms = Room.objects.filter(id=room_id)

    user = CustomUser.objects.get(id=request.session.get('userid'))

    try:
        Participents.objects.get(user=user, room_id=room_id)
    except Participents.DoesNotExist:
        Participents.objects.create(user=user, room_id=room_id)

    participents = Participents.objects.filter(room_id=room_id)


    return render(request, 'room.html', {
        'roomid': room_id,
        'roomcontent': room_contents,
        'rooms': rooms,
        'participents': participents,
        'auth': True
    })

# @login_required
def msg(request, room_id):
    if request.method == 'POST':
        body = request.POST.get('body')
        user = CustomUser.objects.get(id=request.session.get('userid'))
        room = Room.objects.get(id=room_id)
        Message.objects.create(user=user, room=room, body=body)
        return redirect('join_room', room_id=room_id)

# @login_required
def view_room(request, room_id):
    if request.method == 'POST':
        room = Room.objects.get(id=room_id)
        room_contents = Message.objects.filter(room=room).order_by('time_stamp')
        rooms = Room.objects.filter(id=room_id)
        participents = Participents.objects.filter(room_id=room_id)
        user = CustomUser.objects.get(id=request.session.get('userid'))
        try:
            Participents.objects.get(user=user, room_id=room_id)
            auth=True
        except Participents.DoesNotExist:
            auth=False

        return render(request, 'room.html', {
            'roomid': room_id,
            'roomcontent': room_contents,
            'rooms': rooms,
            'rooid':room_id,
            'participents':participents,
            'auth':auth
        })

from django.contrib.auth.decorators import login_required

# @login_required
def myrooms(request):
    user_id = request.session.get('userid')

    if not user_id:
        return redirect('login')  # or show error if not authenticated

    user = CustomUser.objects.get(id=user_id)
    participents = Participents.objects.filter(user=user)
    rooms = Room.objects.filter(id__in=participents.values_list('room_id', flat=True))

    return render(request, 'myrooms.html', {'rooms': rooms})
