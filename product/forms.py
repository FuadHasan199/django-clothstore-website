from django.forms import ModelForm
from product.models import Review

class ReviewForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(ModelForm, self).__init__(*args,**kwargs)
        self.fields['comment'].widget.attrs.update({'class':'form-control'})
        

    class Meta:
        model = Review
        fields = ['comment','rating']