from django import forms
from .models import BookStoreModel

class BookStoreForm(forms.ModelForm):
    class Meta:
        model=BookStoreModel
        fields=['id','book_name','author','category'] 