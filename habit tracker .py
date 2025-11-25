import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.0-flash")
st.title("Your Daily Habit Tracker")

name = st.text_input("Enter your name:")

# 1️⃣ Water
if st.checkbox("Did you drink at least 8 glasses of water today?", key="water_cb"):
    choice = st.radio("Pick one:", ["Yes", "No"], key="water_choice")
    if choice == "Yes":
        st.success("8 glasses of water keep your body hydrated, boost energy, support digestion, and improve skin health.")
    else:
        st.error("Try to drink more water!")

# 2️⃣ Study
if st.checkbox("Did you use any of your free time today to study or learn for one hour?", key="study_cb"):
    choice = st.radio("Pick one:", ["Yes", "No"], key="study_choice")
    if choice == "Yes":
        st.success("Awesome! Studying improves your knowledge and focus.")
    else:
        st.error("It’s okay — you can start something new tomorrow!")

# 3️⃣ Exercise
if st.checkbox("Did you exercise or walk for at least 20 minutes?", key="exercise_cb"):
    choice = st.radio("Pick one:", ["Yes", "No"], key="exercise_choice")
    if choice == "Yes":
        st.success("Exercise improves heart health, boosts energy, reduces stress, and strengthens muscles and mood.")
    else:
        st.error("Not exercising can lead to low energy and health risks.")

# 4️⃣ Healthy Meals
if st.checkbox("Did you eat healthy meals today?", key="meal_cb"):
    choice = st.radio("Pick one:", ["Yes", "No", "Somewhat"], key="meal_choice")
    if choice == "Yes":
        st.success("Great! Eating healthy keeps your body strong.")
    elif choice == "No":
        st.error("Try to reduce junk food tomorrow!")
    elif choice == "Somewhat":
        st.warning("Not bad! A little improvement will help a lot.")

# 5️⃣ Sleep
if st.checkbox("Did you sleep for at least 7 hours last night?", key="sleep_cb"):
    choice = st.radio("Pick one:", ["Yes", "No"], key="sleep_choice")
    if choice == "Yes":
        st.success("Sleeping 7 hours improves mood, boosts energy, and supports recovery.")
    else:
        st.error("Lack of sleep causes tiredness, poor focus, and more stress.")

# 6️⃣ Productivity
if st.checkbox("Did you do anything productive today, like work or studying?", key="prod_cb"):
    choice = st.radio("Pick one:", ["Yes", "No"], key="prod_choice")
    if choice == "Yes":
        st.success("Great! Staying productive builds discipline.")
    else:
        st.error("Try to do something productive tomorrow!")

# 7️⃣ Study Time
study_time = st.number_input("How many hours did you study today?", min_value=0.0, key="study_hours")
st.write(f"You studied for: {study_time} hours")

# 8️⃣ Mobile Usage
if st.checkbox("Did you limit mobile/social media usage today?", key="mobile_cb"):
    choice = st.radio("Pick one:", ["Yes", "No"], key="mobile_choice")
    if choice == "Yes":
        st.success("Great job keeping screen time low!")
    else:
        st.error("Try to reduce phone use tomorrow.")

# 9️⃣ Happiness
if st.checkbox("Did you do something today that made you happy or relaxed?", key="happy_cb"):
    choice = st.radio("Pick one:", ["Yes", "No"], key="happy_choice")
    if choice == "Yes":
        activity = st.text_input("What made you happy today?", key="happy_input")
        if activity:
            st.success(f"That's wonderful! Today you enjoyed: {activity}")
    else:
        st.warning("Try to do at least one thing that makes you happy tomorrow!")
