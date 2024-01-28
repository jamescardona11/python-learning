# Granify test

## run code & test
**dependency python**

1- Open terminal
2- Go to the root folder called "test granify"
3- run code ```python3 main.py```
4- run test ```python3 tests/main_test.py```


## Project overview
- src: All base files to complete the task
  1- **db/**: everything related with the database and sql file
  2- **helper/**: helper functions like random number
  3- **model/**: base models for app (Cat, Dog, Animal)
  4- **shop/**: PetShop interactor

- test: Some tests


## Why

The project is very simple; I made the modeling using some abstract classes to implement the functionality and delegate some responsibilities.
Starting with abstract modeling helped me to split behavior; for example, if I need to create more animals, the only thing I need to do is extends IAnimal, and everything is working as expected.

I created an abstract class for another reason when I made the testing easier, "controlling" the expected behavior. For example, creating a helper to get the random number generator is more valuable than creating something internal in the Cat, Is easier to test a random number generator because I control the behavior that tries to test something internal in the Cat. If the required change and the random generator need to change, the test helps me to prevent errors.

In the same way, I made "data" if the future, I want to integrate an ORM or DB provider I wish to decouple the "Data" functionality that is something in my domain, and I don't want to depend on the library, in this case creating an abstract class easily in the future I can implement an adapter pattern to keep decoupled the ORM.

## Disagree
The requirement, like "speak" in the Animal that print is not a good choice, I prefer to "speak" returns a string; depending on the complexity of the requirement, I can create a decorator pattern to save or print that information, separating the responsibilities.

In the same way with PetShop, the save_logs is not a good solution, In my case, I prefer to create a specific class to have the responsibilities to capture the database interaction, but this class interacts directly with the "Data" class no with a PetShop implementation.



