from django import forms 
from .models import Post, Category
#cat = [('coding', 'coding'), ('sports', 'sports'), ('art', 'art')]
choices = Category.objects.all().values_list('name','name')

choice_list = [] 

for item in choices: 
    choice_list.append(item)

class PostForm(forms.ModelForm): 
    class Meta: 
        model = Post 
        fields = ('title', 'title_tag', 'author', 'category', 'body') 
        
        widgets = { 
                  
                  'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Title Here' }),
                  'title_tag': forms.TextInput(attrs={'class': 'form-control', }),
                'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'mark', 'type': 'hidden' }),

                 # 'author': forms.Select(attrs={'class': 'form-control', }),
                  'category': forms.Select(choices = choice_list, attrs={'class': 'form-control', }),
                  'body': forms.Textarea(attrs={'class': 'form-control', }),
                  
                  
                  }
class EditForm(forms.ModelForm): 
    class Meta: 
        model = Post 
        fields = ('title', 'body') 
        
        widgets = { 
                  
                  'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'This is Title Placeholder' }),
                  'title_tag': forms.TextInput(attrs={'class': 'form-control', }),
                  #'author': forms.Select(attrs={'class': 'form-control', }),
                  'body': forms.Textarea(attrs={'class': 'form-control', }),
                  
                  
                  }
