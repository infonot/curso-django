from django import forms

from reviews.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

        help_texts = {
            'rating': '1 es pésimo, 5 es extraordinario.'
        }

        widgets = {
            'review': forms.Textarea(attrs={'rows': 5}),
        }