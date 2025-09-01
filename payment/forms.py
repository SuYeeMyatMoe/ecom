from django import forms
from .models import DeliveryAddress

class DeliveryForm(forms.ModelForm):
    delivery_full_name= forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone'
        }),
        required=True
    )
    delivery_email= forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone'
        }),
        required=True
    )
    delivery_address= forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone'
        }),
        required=True
    )
    delivery_city= forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone'
        }),
        required=True
    )
    delivery_state= forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone'
        }),
        required=True
    )
    delivery_zipcode= forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone'
        }),
        required=True
    )



class PaymentForm(forms.Form):
    card_name = forms.CharField(
        label="Name on Card",
        required=True,  
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "John Doe"
        })
    )

    card_number = forms.CharField(
        label="Card Number",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "1234 5678 9012 3456",
            "maxlength": "19"
        })
    )

    card_exp_date = forms.CharField(
        label="Expiration Date",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "MM/YY"
        })
    )

    card_cvv_number = forms.CharField(
        label="CVV",
        required=True,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "123",
            "maxlength": "4"
        })
    )

    card_address1 = forms.CharField(
        label="Billing Address 1",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "123 Main St"
        })
    )

    card_address2 = forms.CharField(
        label="Billing Address 2",
        required=False,   # only optional field
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Apt, Suite, etc. (optional)"
        })
    )

    card_city = forms.CharField(
        label="City",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "New York"
        })
    )

    card_state = forms.CharField(
        label="State/Province",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "NY"
        })
    )

    card_zipcode = forms.CharField(
        label="Zip/Postal Code",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "10001"
        })
    )

    card_country = forms.CharField(
        label="Country",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "United States"
        })
    )


