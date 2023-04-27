from rest_framework import serializers
from .models import Student
# Create your serializer here.
# class StudentSerializer(serializers.Serializer):
#     fname = serializers.CharField(max_length=30)
#     lname = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)
#     age = serializers.IntegerField()
    
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance

class StudentSerializer(serializers.ModelSerializer):
    # number = serializers.IntegerField(write_only=True)
    born_year = serializers.SerializerMethodField()# for add new method, read only
    path = serializers.StringRelatedField()
    path_id = serializers.IntegerField()
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ("fname","lname","number")
        # exclude = ("number",)
    def get_born_year(self, obj):# this func has to start "get" and variable name
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age