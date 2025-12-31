from django import forms #폼기능가져옴
from .models import Movie #movie모델db가져오기

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "year","actor", "director","genre","runtime" ,"score", "review" ]
        widgets = {
            "score" : forms.NumberInput(attrs={"step": "0.1", "min": "0", "max": "5"}),
        }