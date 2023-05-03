from rest_framework import serializers
from .models import *
from asyncore import read


class OrderForUser__Serializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnForUser
        fields = '__all__'


class WorkerReport__Serializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerReport
        fields = '__all__'


class User__Serializer(serializers.ModelSerializer):
    order_for_user = OrderForUser__Serializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "order_for_user", 'worker_id']


class Worker__Serializer(serializers.ModelSerializer):
    user_for_worker = User__Serializer(many=True, read_only=True)
    report_worker = WorkerReport__Serializer(many=True, read_only=True)

    class Meta:
        model = Worker
        fields = ["id", "fname", "tel_number", "password",
                  "worker_tip", "today_money", "user_for_worker", "report_worker"]