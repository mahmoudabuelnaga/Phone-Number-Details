# pip install phonenumbers
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number = '.....'

# C: Country
# H: History
ch_number = phonenumbers.parse(number)
print(ch_number)
print(geocoder.description_for_number(ch_number, 'en'))
print(carrier.name_for_number(ch_number, "en"))