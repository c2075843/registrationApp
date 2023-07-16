from courseapp.models import Group

def Courses(request):
    courses =Group.objects.all()
    return {"courses":courses}
