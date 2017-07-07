from django import forms
from .models import Schilderij


class SchilderijForm(forms.ModelForm):

	class Meta:
		model = Schilderij
		fields = ('beschrijving','formaat','image','zichtbaar')
		labels = {
            'zichtbaar': ('Zichtbaar?'),
        }

	def __init__(self, *args, **kwargs):
		super(SchilderijForm, self).__init__(*args, **kwargs)
		self.fields['beschrijving'].widget.attrs['class'] = 'form-control'
		self.fields['formaat'].widget.attrs['class'] = 'form-control'
		# self.data = self.data.copy() 
		
		# print('Processing form \n')
		# print(self.data)
		# if not self.data.get('image'):
		# 	print ('no image')
		# 	pk = self.data.get('pk')
		# 	print (pk)
			# print('no image supplied')

		# self.fields['image'].widget.attrs['class'] = 'filestyle'
		# self.fields['image'].widget.attrs['data-classButton'] = 'btn btn-primary'
		# self.fields['image'].widget.attrs['data-classIcon'] = 'icon-plus'
		# self.fields['image'].widget.attrs['data-buttonText'] = 'Foto wijzigen'

	# def validate_image(self):
	# 	data = self.cleaned_data['image']
	# 	print(data)
	# 	print('HELLOOOOOOOOO')

	# 	return data

