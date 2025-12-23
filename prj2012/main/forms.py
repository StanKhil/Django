from django import forms


def validate_age(age):
    if age % 2 != 0:
        raise forms.ValidationError("Age invalid")
    
def feedback_validator(feedback):
    if "virus" in feedback:
        raise forms.ValidationError("Feedback contains 'virus'")

class ContactForm(forms.Form):
    name  = forms.CharField(max_length=20, label="Name: ")
    age = forms.IntegerField(max_value=100, min_value=18, label="Age: ", validators=[validate_age])
    email = forms.EmailField(label="Email: ")
    bio = forms.CharField(widget=forms.Textarea, label="Bio: ", required=False)
    agree = forms.BooleanField(label="Agree")

class FeedbackForm(forms.Form):
    nickname = forms.CharField(max_length=20, label="Your nickname: ")
    rate = forms.IntegerField(max_value=100, min_value=0, label="Your rate: ")
    feedback = forms.CharField(label="Your feedback: ", widget=forms.Textarea, validators=[feedback_validator])
    spoilers = forms.BooleanField(label="No spoilers: ")

class AddFilmForm(forms.Form):
    title = forms.CharField(label="Film title")
    director = forms.CharField(label="Director")
    release_year = forms.IntegerField(min_value=1900, max_value=2026, label="Release_year")
    rating = forms.DecimalField(max_digits=3, decimal_places=1, max_value=10.0, min_value=0.0, label="Rating")
    poster = forms.FileField(label="Film poster: ", required=False)