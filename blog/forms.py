from django import forms

from .models import Post
from .models import Tag
from .models import Comment

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class TagForm(forms.Form):
    tag = forms.CharField(label='Your post tag', max_length=100)
    

class AddTagForm(forms.Form):
    tag = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=Tag.objects.all().values_list("id", "tag"),
    )

class FilterForm(forms.Form):
    fil = forms.CharField(label='your tags', max_length=100)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('rating','text')

