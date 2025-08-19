import streamlit as st
from nltk.chat.util import Chat, reflections
import base64

# -------------------------------
# 🤖 Chatbot rules
# -------------------------------
pairs = [
    [r"(hi|hello|hey|hii|good morning|good evening)", 
     ["Hello! Welcome to Fresh & Clean Laundry Shop 🧺. How can I help you today?"]],
    [r"(.*)service(.*)", 
     ["Our services include washing, ironing, dry cleaning, stain removal, express service, and home delivery."]],
    [r"(.*)price(.*)", 
     ["Our pricing depends on the item. Shirts ₹30, Pants ₹40, Bedsheet ₹60, Dry Cleaning starts from ₹100."]],
    [r"(.*)delivery(.*)", 
     ["Regular delivery in 48 hours. Express delivery in 24 hours."]],
    [r"(.*)offer(.*)", 
     ["We currently have 10% off on orders above ₹500!"]],
    [r"(.*)payment(.*)", 
     ["We accept cash, UPI, debit/credit cards, and online wallets."]],
    [r"(.*)contact(.*)", 
     ["You can call us at +91-9876543210 or email us at support@laundryshop.com"]],
    [r"(bye|goodbye|see you|exit|quit|ok bye)", 
     ["Thank you for visiting Fresh & Clean Laundry Shop 🧺. Goodbye!"]],
    [r"(.*)", 
     ["Sorry, I can't answer that. Please call our customer care at +91-9876543210 or drop an email at support@laundryshop.com"]],
]

chat = Chat(pairs, reflections)

# -------------------------------
# 🎨 Background image
# -------------------------------
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("pexels-myatezhny39-2927523.jpg")  # replace with your file

# -------------------------------
# 📌 UI Title
# -------------------------------
st.markdown("<h1 style='text-align:center; color:white;'>🧺 Fresh & Clean Laundry Shop Chatbot</h1>", unsafe_allow_html=True)

# -------------------------------
# 📌 Input
# -------------------------------
user_input = st.text_input("💬 Ask me something:")

if user_input:
    response = chat.respond(user_input)
    
    # ❌ Instead of appending, overwrite old chat
    st.session_state.history = [("You", user_input), ("Bot", response)]

# -------------------------------
# 📌 Show only the latest Q&A
# -------------------------------
if "history" in st.session_state:
    for speaker, msg in st.session_state.history:
        if speaker == "You":
            st.markdown(
                f"""
                <div style='text-align:right; margin:10px;'>
                    <span style='background:#4CAF50; color:white; padding:10px 15px; border-radius:15px; display:inline-block;'>
                        {msg}
                    </span>
                </div>
                """, unsafe_allow_html=True
            )
        else:  # Bot
            st.markdown(
                f"""
                <div style='text-align:left; margin:10px;'>
                    <span style='background:rgba(255,255,255,0.9); color:black; padding:10px 15px; border-radius:15px; display:inline-block;'>
                        {msg}
                    </span>
                </div>
                """, unsafe_allow_html=True
            )
