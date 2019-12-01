from django import forms

class BodyCheckForm(forms.Form):
    hight = forms.DecimalField(error_messages={"required":"身高不能为空"})
    height = forms.DecimalField(required=True, error_messages={'required': "体重不能为空"})
    chest = forms.DecimalField(required=True, error_messages={'required': "胸围不能为空"})
    waist = forms.DecimalField(required=True, error_messages={'required': "腰围不能为空"})
    hip = forms.DecimalField(required=True, error_messages={'required': "臀围不能为空"})
    queith = forms.DecimalField(required=True, error_messages={'required': "静息心率不能为空"})
    maxh = forms.DecimalField(required=True, error_messages={'required': "最大心率不能为空"})