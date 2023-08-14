from django.urls import reverse
from rest_framework import serializers


from .models import Student, Group, User
from courseapp.models import Module, Registration


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]
        
        
        
class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ["name"]


class StudentSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(
        queryset=Group.objects.all(), slug_field="name"
    )
    email = serializers.ReadOnlyField(source="user.email")
    student_id = serializers.ReadOnlyField(source="user.username")
    
    class Meta:
        model = Student
        fields = [
            "student_id",
            "email",
            "address",
            "town",
            "country",
            "photo",
            "dob",
            "course",
        ]



class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = [
            "name",
            "code",
            "credit",
            "category",
            "description",
            "availability",
            "courses",        
        ]



class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ["id", "student", "module", "registration_date"]

