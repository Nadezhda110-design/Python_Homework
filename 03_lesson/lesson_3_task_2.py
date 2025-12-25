from smartphone import Smartphone
catalog = [
    Smartphone("Nokia","2210", "+79161234567"),
    Smartphone("Samsung", "3210", "+79101234567"),
    Smartphone("Huawei", "1234", "+79101234568"),
    Smartphone("Xiaomi", "17", "+79101234569"),
    Smartphone("Honor", "12", "+79101234565")
]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}")