## Django Template

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/GB6Eki?referralCode=U5zXSw)


##### Generate secret key
python3 manage.py shell
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())