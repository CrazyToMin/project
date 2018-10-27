from django import forms


# 返回到模板上的表单类
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=1, required=True,
                               error_messages={'required': '用户账户不能为空', 'invalid': '格式错误'},
                               widget=forms.TextInput(attrs={'class': 'c'}))
    password = forms.CharField(max_length=16, min_length=1, widget=forms.PasswordInput)
