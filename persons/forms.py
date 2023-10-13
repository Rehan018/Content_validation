from django import forms

from persons.models import Person, subdomain


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subdomain'].queryset = subdomain.objects.all()

        if 'domain' in self.data:
            try:
                domain_id = int(self.data.get('domain'))
                self.fields['subdomain'].queryset = subdomain.objects.filter(domain_id=domain_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty subdomain queryset
        elif self.instance.pk:
            self.fields['subdomain'].queryset = self.instance.domain.subdomain_set.order_by('name')

