from django import forms
from .models import Message

# class for sending messages


class FormMessage(forms.ModelForm):
    user_name = forms.CharField(max_length=40,
                                widget=forms.TextInput(attrs={"tabindex": "1", "size": "18", "id": "name", "name": "name", "type": "text", "value": "",
                                                              "class": "input-xlarge", "placeholder": "Name"}))
    user_email = forms.EmailField(
                                widget=forms.EmailInput(attrs={"tabindex": "2", "size": "25", "id": "email", "name": "email", "type": "text",
                                                               "value": "", "class": "input-xlarge", "placeholder": "Email Address"}))
    user_message = forms.CharField(max_length=400,
                                widget=forms.Textarea(attrs={"tabindex": "3", "class": "input-xlarge", "id": "message", "name": "body",
                                                             "rows": "7", "placeholder": "Message"}))

    class Meta:
        model = Message
        fields = ('user_name', 'user_email', 'user_message')