from .models import Department, Personnel

from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ("id", "name")


class PersonnelSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()
    department_id = serializers.IntegerField()
    created_by = serializers.StringRelatedField()
    created_by_id = serializers.IntegerField(required=False)

    class Meta:
        model = Personnel
        fields = ("id", "created_by", "created_by_id", "department", "department_id",
                  "first_name", "last_name", "salary", "participation_date")

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.created_by_id = self.context["request"].user.id
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.created_by_id = self.context["request"].user.id
        instance.save()
        return instance


class DepartmentPersonnelSerializer(serializers.ModelSerializer):
    personnel = PersonnelSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ("id", "name", "personnel")
