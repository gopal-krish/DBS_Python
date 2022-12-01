
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 

class createorderform(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
        exclude=['status']

class createproductform(ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class createcustomerform(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']
