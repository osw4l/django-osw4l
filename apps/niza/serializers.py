from rest_framework.serializers import ModelSerializer
from .models import CustomerReview


class CustomerReviewSerializer(ModelSerializer):
    class Meta:
        model = CustomerReview
        fields = (
            'title',
            'position',
            'customer',
            'comment',
            'score'
        )
