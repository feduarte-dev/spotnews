from django import forms


class CreateCategoryForm(forms.Form):
    name = forms.CharField(
        label="Nome",
        max_length=200,
        required=True,
    )


# Dúvida sobre tag Span
# Dúvida sobre o CSS
# Dúvida sobre a classe Meta para form
