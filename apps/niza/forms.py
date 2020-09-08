from apps.utils.forms import BaseUserCreationForm
from .models import Customer


class CustomerForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = Customer
