from django import forms
from . import models
class BodyCheckForm(forms.Form):
    hight = forms.DecimalField(max_digits=3,required=True,error_messages={"required":"身高不能为空",'max_digits':"身高最多为3位数"})
    height = forms.DecimalField(max_digits=3,required=True, error_messages={'required': "体重不能为空",'max_digits':"体重最多为3位数"})
    chest = forms.DecimalField(max_digits=3,required=True, error_messages={'required': "胸围不能为空",'max_digits':"胸围最多为3位数"})
    waist = forms.DecimalField(max_digits=3,required=True, error_messages={'required': "腰围不能为空",'max_digits':"腰围最多为3位数"})
    hip = forms.DecimalField(max_digits=3,required=True, error_messages={'required': "臀围不能为空",'max_digits':"臀围最多为3位数"})
    queith = forms.DecimalField(max_digits=3,required=True, error_messages={'required': "静息心率不能为空",'max_digits':"静息心率最多为3位数"})
    maxh = forms.DecimalField(max_digits=3,required=True, error_messages={'required': "最大心率不能为空",'max_digits':"最大心率最多为3位数"})

    def __init__(self, *args, **kwargs):
        super(BodyCheckForm, self).__init__(*args, **kwargs)