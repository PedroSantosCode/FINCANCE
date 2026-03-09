from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'summary', 'content', 'image', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Título do post'}),
            'summary': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Resumo breve'}),
            'content': forms.Textarea(attrs={'class': 'form-input', 'rows': 10, 'placeholder': 'Conteúdo completo do post...'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
        }
