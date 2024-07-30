import string


def extract_birds(message: str) -> list[str]:
    if not isinstance(message, str):
        raise TypeError("Message must be str")
    for char in message:
        if char in string.punctuation:
            message = message.replace(char, " ")
    return message.split()


def fix_ingredients(ingredients: list) -> list[str]:
    if not isinstance(ingredients, list):
        raise TypeError("ingredients must be list")
    if not all(isinstance(item, str) for item in ingredients):
        raise TypeError("All elements must be str")
    for item in ingredients:
        if not item.casefold().startswith("z"):
            ingredients[ingredients.index(item)] = item[::-1]
    return ingredients


# if __name__ == "__main__":
#     print(extract_birds("Качка, Гуска; Курка. Півень: Індик"))
#     print(extract_birds("Голуб! Ластівка. Синиця; Сойка"))
#     print(extract_birds("Горобець Качка:Курка,Індик"))
#     print(fix_ingredients(["sugar", "zmilk", "retaW", "salt", "honey"]))
#     print(fix_ingredients(["zFlour", "liO", "hcaetS"]))
#     print(fix_ingredients(["zSalt", "retniW", "kcab"]))
