from rest_framework import serializers
from .models import CocktailProduct, OurUser

class CocktailProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CocktailProduct
        fields ='__all__'


class OurUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = OurUser
        fields = ['email','username','password','password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    #overwriting the save method
    def save(self):
        account  = OurUser(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password']

        if password != password2:
            raise serializers.ValidationError({'password':'Your passwords are not matching'})
        account.set_password(password)
        account.save()
        return account

