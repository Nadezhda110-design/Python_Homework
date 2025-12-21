from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Гагарина", "25", "15")
from_address = Address("654321", "Тюмень", "Центральная", "20", "10")


mailing = Mailing(
    to_address = to_address,
    from_address = from_address,
    track = "TR234567U",
    cost = 550
)

print(f"Отправление {mailing.track} из "
      f"{from_address.index}, {from_address.city}, "
      f"{from_address.street}, {from_address.house} - "
      f"{from_address.apartment} "
      f"в {to_address.index}, {to_address.city}, "
      f"{to_address.street}, {to_address.house} - "
      f"{to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")