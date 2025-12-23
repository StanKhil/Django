from django import forms

class BookForm(forms.Form):
    id = forms.IntegerField()
    title = forms.CharField(max_length=255)
    author = forms.CharField(max_length=255)
    year = forms.IntegerField()
    genre = forms.CharField(max_length=100)
    publisher = forms.CharField(max_length=255)
    is_available = forms.BooleanField(required=False)
    cover = forms.FileField(
        required=False,
        label="Обкладинка книги"
    )


class ReaderForm(forms.Form):
    id = forms.IntegerField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=30)
    email = forms.EmailField()
    created_at = forms.DateTimeField()
    avatar = forms.ImageField(required=False)
    books = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    avatar = forms.FileField(
        required=False,
        label="Аватарка"
    )

