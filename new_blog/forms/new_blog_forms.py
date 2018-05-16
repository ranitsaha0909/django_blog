from django.contrib.auth.models import User
from django import forms
from ..models.new_blog_models import Blog


class BlogForm(forms.ModelForm):
    # def clean_file(self):
    #     file = self.cleaned_data.get("picture", False)
    #     filetype = magic.from_buffer(file.read())
    #     extensions = ["JPEG", "JPG", "BMP", "PNG"]
    #     if not extensions in filetype:
    #         raise ValidationError("File is not an Image.")
    #     return picture
    class Meta:
        model = Blog
        fields = ('title', 'text', 'picture')
