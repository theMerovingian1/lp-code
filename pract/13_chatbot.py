import streamlit as st
# from streamlit.server.server import Server

bot_name = "Tourist Guide"
knowledge_base = {
    "what is your name?": [
        f"My name is {bot_name}! \nI'm here to help you explore wonderful tourist destinations!"
    ],
    "hello": [
        f"Hello! I'm {bot_name}.\nReady to assist you in discovering amazing places to visit!"
    ],
    "what are the best tourist destinations in Italy?": [
        "1. Rome - The Eternal City",
        "2. Florence - Cradle of the Renaissance",
        "3. Venice - City of Canals",
        "4. Amalfi Coast - A Coastal Paradise",
        "5. Cinque Terre - Picturesque Villages",
    ],
    "what are the must-visit places in Paris?": [
        "1. Eiffel Tower - Iconic Landmark",
        "2. Louvre Museum - Home to Mona Lisa",
        "3. Notre-Dame Cathedral - Gothic Masterpiece",
        "4. Montmartre - Bohemian District",
        "5. Seine River Cruise - Romantic Experience",
    ],
    "what are the top attractions in New York City?": [
        "1. Statue of Liberty",
        "2. Central Park",
        "3. Empire State Building",
        "4. Times Square",
        "5. Broadway",
    ],
    "when is the best time to visit Bali?": [
        "The best time to visit Bali is during the dry season, from April to October, when the weather is sunny and the humidity is lower."
    ],
    "what are the top activities to do in Thailand?": [
        "1. Explore Bangkok's Grand Palace and Temples",
        "2. Relax on the beaches of Phuket",
        "3. Visit Chiang Mai and experience Thai culture",
        "4. Enjoy water sports in Krabi",
        "5. Explore the ancient ruins of Ayutthaya",
    ],
    "when do cherry blossoms bloom in Japan?": [
        "Cherry blossoms in Japan typically bloom in late March to early April, depending on the region and weather conditions."
    ],
}

st.header("Tourist Destination Enquiry Chatbot")

# Custom SessionState to maintain state across reruns


class SessionState:
    input_query = None


# Get SessionState for this session
session_state = SessionState()


def respond():
    input_query = session_state.input_query.lower()
    if input_query in knowledge_base:
        values = knowledge_base[input_query]
        for value in values:
            st.write(value)
    else:
        st.write("Question is not present in the knowledge base!\nCould you please enter the appropriate answer for the question below-")
        answer = st.text_input("Answer")
        add = st.button("Add answer")
        if add:
            knowledge_base[input_query] = [answer]


input_query = st.text_input("Enter your query here-")
ask_button = st.button("Ask")
quit_button = st.button("Quit")

if ask_button:
    session_state.input_query = input_query
    respond()
elif quit_button:
    st.write("Thank you for using the Tourist Guide Chatbot")
