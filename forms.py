from  django import forms

class BootstrapForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class RecordSearchForm(BootstrapForm):
    options = (('artist','Artist'), ('title','Title'), ('label','Label'), ('catalog_no','Catalog No'))
    search = forms.CharField(max_length=50, help_text='Search')
    search_by = forms.ChoiceField(widget=forms.Select,choices=options, help_text='Search By')

    class Meta:
        fields = ['search','search_by']

