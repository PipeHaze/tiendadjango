from rest_framework import serializers
from tiendita.models import Producto, Categoria
from account.models import UserBase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields = ['id','categoria','creado_por','precio', 'titulo', 'autor', 'descripcion','imagen', 'slug', 'en_stock', 'activo','aprobado']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','nombre','slug']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = UserBase
        fields = ['id','email', 'user_name', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserBase.objects.create_user(password=password, **validated_data)
        return user
    
class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance
    
    def validate_username(self, data):
        users = UserBase.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError("Este usuarioya existe, ingresa otro")
        else:
            return data





    

