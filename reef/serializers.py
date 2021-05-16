from rest_framework import serializers
from .models import Student, Advisor, Parent,  ActivityChange, ActivityDetail, UpdateRequest

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student 
        fields = '__all__'

class AdvisorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advisor
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields = '__all__'

class UpdateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdateRequest
        fields = '__all__'


class ActivityChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityChange
        fields = '__all__'

class ActivityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityDetail
        fields = '__all__'
