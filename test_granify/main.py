from src.model.cat import Cat
from src.model.dog import Dog
from src.shop.pet_shop import PetShop
from src.db.data import Data



if __name__ == "__main__":
    cat = Cat()
    print(f"Name is currently: {cat.get_name()}")
    cat.set_name("Garfield")
    print(f"Name has been changed to: {cat.get_name()}")

    print(f"Cat age is: {cat.get_age()}")
    cat.speak()
    cat.speak()
    cat.speak()
    cat.speak()
    cat.speak("meooooooow")

    print(f"Cat age after speak five times: {cat.get_age()}")
    cat.set_name("Copo")
    cat.set_name("Gruñon")
    print(f"All Cat names: {cat.get_names()}")
    print(f"Average length of cat names: {cat.get_names()}")

    dog = Dog()
    cat.speak()

    data = Data()
    data.insert("Cat", cat)

    petshot = PetShop(data)
    petshot.save_test()
    petshot.save_pet_shop()
