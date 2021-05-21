from django import forms
from django.contrib.auth import get_user_model, authenticate


# creation form of registration


User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(
                                widget=forms.TextInput(attrs={"type": "text", "placeholder": "Имя",
                                                              "class": "input-xlarge"}))
    password1 = forms.CharField(
                                widget=forms.PasswordInput(attrs={"type": "password", "placeholder": "Введите пароль",
                                                                  "class": "input-xlarge"}))
    password2 = forms.CharField(
                                widget=forms.PasswordInput(attrs={"type": "password", "placeholder": "Введите пароль еще раз",
                                                                  "class": "input-xlarge"}))

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self, *args, **kwargs):
        data = self.cleaned_data

        if data['password1'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password2']

# creation form of login


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if (not user) or (not user.check_password(password)):
                raise forms.ValidationError('Неверный пароль или логин')
        return super().clean(*args, **kwargs)