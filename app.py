import gradio as gr
import difflib

# Define all the responses for the chatbot
responses = {
    "menu": "Here's our menu: 🍕 Pizza, 🍔 Burgers, 🥗 Salads, 🧁 Desserts, 🍹 Beverages.",
    "timing": "We're open every day from 10 AM to 10 PM!",
    "reservation": "Sure! You can book a table by calling us at 123-456-7890, or visit our website to make a reservation.",
    "location": "We're located at 123 Food Street, Flavor Town. It's easy to find, right next to the central park!",
    "pizza": "Our pizzas include: \n1. Margherita 🍕 \n2. Pepperoni 🍕 \n3. Veggie Delight 🍕 \n4. BBQ Chicken 🍕",
    "pepperoni": "You have selected Pepperoni pizza! Would you like to confirm your order, add something else, or change your selection?",
    "margherita": "You have selected Margherita pizza! Would you like to confirm your order, add something else, or change your selection?",
    "veggie": "You have selected Veggie Delight pizza! Would you like to confirm your order, add something else, or change your selection?",
    "bbq": "You have selected BBQ Chicken pizza! Would you like to confirm your order, add something else, or change your selection?",
    "burger": "Our burgers include: \n1. Classic Cheeseburger 🍔 \n2. BBQ Bacon Burger 🍔 \n3. Veggie Burger 🍔",
    "cheeseburger": "You have selected Classic Cheeseburger! Would you like to confirm your order, add something else, or change your selection?",
    "bbq_burger": "You have selected BBQ Bacon Burger! Would you like to confirm your order, add something else, or change your selection?",
    "veggie_burger": "You have selected Veggie Burger! Would you like to confirm your order, add something else, or change your selection?",
    "salad": "Our salads include: \n1. Caesar Salad 🥗 \n2. Greek Salad 🥗 \n3. Garden Salad 🥗",
    "caesar": "You have selected Caesar Salad! Would you like to confirm your order, add something else, or change your selection?",
    "greek": "You have selected Greek Salad! Would you like to confirm your order, add something else, or change your selection?",
    "garden": "You have selected Garden Salad! Would you like to confirm your order, add something else, or change your selection?",
    "desserts": "Our desserts include: \n1. Chocolate Cake 🧁 \n2. Cheesecake 🧁 \n3. Apple Pie 🧁",
    "chocolate_cake": "You have selected Chocolate Cake! Would you like to confirm your order, add something else, or change your selection?",
    "cheesecake": "You have selected Cheesecake! Would you like to confirm your order, add something else, or change your selection?",
    "apple_pie": "You have selected Apple Pie! Would you like to confirm your order, add something else, or change your selection?",
    "beverages": "Our beverages include: \n1. Soft Drinks 🍹 \n2. Juices 🍹 \n3. Coffee 🍹 \n4. Iced Tea 🍹",
    "soft_drinks": "You have selected Soft Drinks! Would you like to confirm your order, add something else, or change your selection?",
    "juices": "You have selected Juices! Would you like to confirm your order, add something else, or change your selection?",
    "coffee": "You have selected Coffee! Would you like to confirm your order, add something else, or change your selection?",
    "iced_tea": "You have selected Iced Tea! Would you like to confirm your order, add something else, or change your selection?",
    "contact": "For any inquiries, you can reach us at 123-456-7890 or email us at support@restaurant.com.",
    "thank you": "You're welcome! 😊 If you need anything else, feel free to ask.",
    "address": "Please provide your delivery address.",
    "order_confirmation": "Your order has been confirmed! You will receive a confirmation email with the details. Thank you for choosing us!"
}

user_name = None
user_order = []
user_address = None

def chatbot_response(query):
    global user_name, user_order, user_address
    query = query.lower()

    # Ask for the name of the user if not already provided
    if user_name is None:
        user_name = query.strip()  # Accept anything as the name
        return f"Nice to meet you, {user_name}! 😊 How can I assist you today? Here are some options:\n" \
               f"1. View Menu\n" \
               f"2. View Location\n" \
               f"3. Make a Reservation\n" \
               f"4. Contact Support\n" \
               f"Please choose an option by typing the number."

    # Check for options selected (menu, location, reservation, etc.)
    if "1" in query or "menu" in query:
        return responses["menu"]
    elif "2" in query or "location" in query:
        return responses["location"]
    elif "3" in query or "reservation" in query:
        return responses["reservation"]
    elif "4" in query or "support" in query:
        return responses["contact"]

    # Handle food selection and show options for pizzas, burgers, etc.
    if "pizza" in query:
        return responses["pizza"]
    elif "pepperoni" in query:
        user_order.append("pepperoni")
        return responses["pepperoni"]
    elif "margherita" in query:
        user_order.append("margherita")
        return responses["margherita"]
    elif "veggie" in query:
        user_order.append("veggie")
        return responses["veggie"]
    elif "bbq" in query:
        user_order.append("bbq")
        return responses["bbq"]
    elif "burger" in query:
        return responses["burger"]
    elif "cheeseburger" in query:
        user_order.append("cheeseburger")
        return responses["cheeseburger"]
    elif "bbq_burger" in query:
        user_order.append("bbq_burger")
        return responses["bbq_burger"]
    elif "veggie_burger" in query:
        user_order.append("veggie_burger")
        return responses["veggie_burger"]
    elif "salad" in query:
        return responses["salad"]
    elif "caesar" in query:
        user_order.append("caesar")
        return responses["caesar"]
    elif "greek" in query:
        user_order.append("greek")
        return responses["greek"]
    elif "garden" in query:
        user_order.append("garden")
        return responses["garden"]
    elif "desserts" in query:
        return responses["desserts"]
    elif "chocolate_cake" in query:
        user_order.append("chocolate_cake")
        return responses["chocolate_cake"]
    elif "cheesecake" in query:
        user_order.append("cheesecake")
        return responses["cheesecake"]
    elif "apple_pie" in query:
        user_order.append("apple_pie")
        return responses["apple_pie"]
    elif "beverages" in query:
        return responses["beverages"]
    elif "soft_drinks" in query:
        user_order.append("soft_drinks")
        return responses["soft_drinks"]
    elif "juices" in query:
        user_order.append("juices")
        return responses["juices"]
    elif "coffee" in query:
        user_order.append("coffee")
        return responses["coffee"]
    elif "iced_tea" in query:
        user_order.append("iced_tea")
        return responses["iced_tea"]

    # Handle order confirmation and address collection
    if "confirm" in query or "yes" in query:
        if not user_address:
            return responses["address"]
        else:
            return responses["order_confirmation"]
    elif "address" in query:
        user_address = query.strip()
        return f"Thank you, {user_name}! We have received your address. Your order is being processed."
    else:
        return "I'm sorry, I didn't understand that. Could you please try again?"

# Creating Gradio Interface
iface = gr.Interface(fn=chatbot_response, inputs="text", outputs="text", title="Restaurant Chatbot")

if __name__ == "__main__":
    # Make sure this isn't in a while loop or any blocking code.
    iface.launch()
