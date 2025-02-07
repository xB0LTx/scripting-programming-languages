import typing
import re
address = "Al. prof. S. Kaliskiego 7 85-796 Bydgoszcz"
street_pattern = re.compile(r"(?P<street_name>\D+)\s")
street_name = street_pattern.search(address).group('street_name')

print(street_name)
