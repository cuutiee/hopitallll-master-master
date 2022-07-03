from rest_framework import serializers

from .models import NewUser


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = NewUser
        fields = ['email', 'user_name', 'full_name','img',
                  'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self,image):
        
        account = NewUser(
            email=self.validated_data['email'],
            user_name=self.validated_data['user_name'],
            full_name=self.validated_data['full_name'],
            img=image,
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match'})
        account.set_password(password)
        account.save()
        return account