import streamlit as st
import re


cuisine_descriptions = {
    'italian': "Italian cuisine is known for its emphasis on fresh, high-quality ingredients. Pasta, pizza, olive oil, and wine are staples. Regional variations include Northern Italian dishes like risotto and hearty stews, while Southern Italy is famous for its seafood and citrus flavors.",
    'french': "French cuisine is characterized by its sophisticated techniques and emphasis on sauces. Classic dishes include coq au vin, ratatouille, and escargot. French culinary traditions vary by region, with distinct influences in Provence, Burgundy, and Normandy.",
    'japanese': "Japanese cuisine places great importance on seasonality and presentation. Sushi, sashimi, ramen, and tempura are popular dishes. Japanese food often features fresh fish, rice, and umami-rich ingredients like soy sauce and miso.",
    'indian': "Indian cuisine is renowned for its rich and diverse flavors. Spices such as cumin, coriander, and turmeric are key components. Popular dishes include curry, biryani, and tandoori preparations. Each region in India has its own unique culinary traditions.",
    'chinese': "Chinese cuisine is diverse, with regional variations like Cantonese, Sichuan, and Hunan. Stir-frying, steaming, and braising are common cooking techniques. Popular dishes include dim sum, Peking duck, and various noodle and rice dishes.",
    'mexican': "Mexican cuisine is known for its bold and spicy flavors. Tacos, enchiladas, guacamole, and salsa are staples. Corn, beans, and chili peppers are commonly used ingredients. Each region in Mexico contributes distinct flavors to the overall cuisine.",
    'mediterranean': "Mediterranean cuisine, prevalent in countries like Greece, Spain, and Lebanon, focuses on fresh produce, olive oil, and lean proteins. Dishes include Greek salad, paella, and falafel. The diet is associated with health benefits due to its emphasis on whole foods.",
    'thai': "Thai cuisine is a balance of sweet, sour, salty, and spicy flavors. Pad Thai, green curry, and tom yum soup are popular dishes. Thai cooking often incorporates aromatic herbs like lemongrass, basil, and cilantro.",
    'brazilian': "Brazilian cuisine is diverse, influenced by indigenous, African, and Portuguese flavors. Feijoada, a black bean stew with pork, is a traditional dish. Barbecue (churrasco) is a popular cooking method, and tropical fruits play a significant role in desserts.",
    'middle eastern': "Middle Eastern cuisine, found in countries like Lebanon, Iran, and Israel, features dishes like hummus, falafel, and kebabs. Ingredients such as chickpeas, olive oil, and spices like cumin and coriander are commonly used."
}

def rule_based_food_chatbot(user_input):
    greetings = ['hello', 'hi', 'hey', 'greetings']
    farewells = ['bye', 'goodbye', 'see you', 'farewell']
    inquiries = ['favorite food', 'recommendation', 'recipe', 'cuisine']
    gratitude = ['thank you', 'thanks', 'appreciate it']

    if re.search(r'\brecipe\b', user_input, re.IGNORECASE):
        return "I'm sorry, I don't have a specific recipe. But I can help with recommendations."

    elif re.search(r'\bcuisine\b', user_input, re.IGNORECASE):
       
        matched_cuisine = next((cuisine for cuisine in cuisine_descriptions.keys() if cuisine in user_input.lower()), None)
        if matched_cuisine:
            return cuisine_descriptions[matched_cuisine]
        else:
            return "It's wonderful that you're interested in cuisines! If you have a specific cuisine in mind, feel free to mention it, and I'll provide more information."

    # Check user input against predefined rules
    elif any(word in user_input.lower() for word in greetings):
        return "Hello! What can I help you with in the world of food today?"

    elif any(word in user_input.lower() for word in farewells):
        return "Goodbye! Enjoy your culinary adventures!"

    elif any(word in user_input.lower() for word in inquiries):
        if 'cuisine' in user_input.lower():
            return "Each cuisine has its own distinct characteristics and flavors. If you have a specific cuisine in mind, let me know, and I'll share more about it."
        else:
            return "I'm a food enthusiast! Ask me about your favorite food, a specific cuisine, and I'll do my best to help."

    elif any(word in user_input.lower() for word in gratitude):
        return "You're welcome! If you have more food-related questions or want information about a specific cuisine, feel free to ask."

    else:
        return "I'm sorry, I didn't catch that. Could you ask me something about food, mention a specific cuisine, or try rephrasing?"


def main():
    st.title("Food Chatbot")
    user_input = st.text_input("You:")
    
    if st.button("Submit"):
        response = rule_based_food_chatbot(user_input)
        st.text("Chatbot: " + response)

if __name__ == "__main__":
    main()
