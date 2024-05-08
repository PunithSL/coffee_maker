# coffee_maker
The Python program simulates a coffee machine with a menu and ingredient tracking. Users can select coffee options, pay with coins, and receive their order. It ensures ingredient availability, handles transactions, and provides reports. The program interacts through the console, offering a seamless coffee ordering experience.



1. Menu and Resources Setup:
   - The program begins by defining a menu of coffee options (`MENU`) and the initial quantities of ingredients available (`resources`). It also includes a placeholder for tracking the money collected from transactions.

2. Function Definitions:
   - `check_requirements(order_item)`: This function checks if there are sufficient ingredients to fulfill a coffee order. It compares the required ingredients for a specific coffee item with the available quantities in the resources dictionary.
   - `calculate_price(quarters, dimes, nickels, pennies)`: This function calculates the total price of a coffee order based on the number of quarters, dimes, nickels, and pennies inserted by the user.
   - `report()`: This function prints a report of the current quantities of ingredients and the amount of money collected.
   - `off()`: This function exits the program.

3. Transaction and Coffee Making:
   - `transaction_and_coffee_making(order_item, total_price)`: This function handles the transaction process after a user places an order. It checks if the user has inserted enough money, calculates change if applicable, updates the money collected, and deducts the required ingredients from the resources.
   - `coffee_making_process()`: This function orchestrates the entire coffee making process. It prompts the user for their coffee order, handles special commands like "report" and "off", checks ingredient availability, and facilitates the transaction.

4.  User Interaction :
   - The program interacts with the user through the console. It prompts the user to select a coffee option, insert coins for payment, and provides feedback on the transaction outcome.

5.  Error Handling :
   - The program handles various scenarios such as invalid user input, insufficient ingredients, and insufficient payment, providing appropriate messages to the user in each case.

Overall, this program provides a basic simulation of a coffee machine, allowing users to select from a menu of coffee options, pay for their order with coins, and receive their desired beverage. It also provides functionality for checking ingredient availability, reporting current resources, and gracefully exiting the program.
