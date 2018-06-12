from django import forms

class CommentForm(forms.Form):
	name=forms.CharField(max_length=20,
		widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))#This is just used to make the Name and Commnet section beautiful
	comment=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Comment'}))