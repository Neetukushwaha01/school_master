from django import forms

from .models import User,Gallery
class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=200,required=True)
    re_password = forms.CharField(max_length=200,required=True)

    email = forms.EmailField(max_length=200,required=True)
    class Meta:
        model =User
        fields =['name','email','phone','user_type']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("re_password")
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class LoginForm(forms.Form):
    email=forms.EmailField(max_length=200)
    password=forms.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class GalleryForm(forms.ModelForm):
    class Meta:
        model =Gallery
        fields =['image']