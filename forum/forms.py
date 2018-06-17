from django import forms
from .models import Forum_Thread, Post


class NewThreadForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5,
                   'placeholder': 'Type thread content here'
                   }
        ),
        max_length=5000,
        help_text='Max length of text is 5000'
    )

    class Meta:
        model = Forum_Thread
        fields = ['thread_name', 'message']


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5,
                   'placeholder': 'Type post content here'
                   }
        )
    )

    class Meta:
        model = Post
        fields = ['content', ]
