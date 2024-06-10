**Problem Description: Coffee Shop**
> The coffee shop wants to create a simple web application to manage orders and display the menu.

**Flask Application Design**

## HTML Files

- **menu.html:** Displays the menu of coffee, tea, and pastries.
- **order.html:** Includes a form for customers to place orders and select their drink and pastries.

## Routes

- **'/'**: Home page that displays a welcome message.
- **'/menu'**: Displays the menu page (**menu.html**) with the list of coffee, tea, and pastries, along with their prices.
- **'/order'**: Displays the order page (**order.html**) with a form for customers to enter their order details, including drink, pastries, and quantity.
- **'/submit-order'**: Receives the submitted order from the **'/order'** page, processes the order information, and displays a confirmation message with the order details.