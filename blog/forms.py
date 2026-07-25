from django import forms
from .models import Posted

class PostForm(forms.ModelForm):
    class Meta:
        model=Posted
        fields=['title','body','category','tag','status']
        # author field ei khane nai karon view e set korbo(logged in user)

        widgets={
            #Django te by default Textarea choto thake ----- boro koralam
            'body':forms.Textarea(attrs={'rows':8})
        }
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            #sob fields er label aro readable koro
            self.fields['title'].label='Post Title'
            self.fields['body'].label='Content'
            self.fields['category'].label='Category'
            self.fields['tag'].label='Tags'
            self.fields['status'].label='Status'
