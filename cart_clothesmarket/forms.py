from django import forms


class QuantityForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={"type": "text", "class": "span1", "placeholder": "1"}))

    class Meta:

        fields = ('quantity',)
