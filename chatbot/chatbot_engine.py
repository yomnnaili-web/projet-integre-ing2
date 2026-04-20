# chatbot_engine.py

def reset_session():
    return {
        "step": 0,
        "software": 0,
        "data": 0,
        "cyber": 0
    }


# ---------- UNDERSTANDING FUNCTIONS ----------

def understood_work_style(msg):
    msg = msg.lower()
    if any(word in msg for word in ["team", "people", "together", "friends"]):
        return "people"
    if any(word in msg for word in ["alone", "solo", "quiet", "myself"]):
        return "alone"
    return None


def understood_interest(msg):
    msg = msg.lower()
    if any(word in msg for word in ["build", "app", "website", "program", "code", "coding", "develop"]):
        return "software"
    if any(word in msg for word in ["hack", "security", "attack", "ctf", "exploit"]):
        return "cyber"
    if any(word in msg for word in ["data", "ai", "analysis", "math", "statistics", "model"]):
        return "data"
    return None


def understood_reaction(msg):
    msg = msg.lower()

    software_words = ["fix", "debug", "repair", "solve"]
    cyber_words = ["investigate", "trace", "attack", "who", "why", "cause"]
    data_words = ["logs", "analyze", "analysis", "patterns", "check"]

    software_score = sum(word in msg for word in software_words)
    cyber_score = sum(word in msg for word in cyber_words)
    data_score = sum(word in msg for word in data_words)

    # nothing detected
    if software_score == 0 and cyber_score == 0 and data_score == 0:
        return None

    # choose dominant intention
    if software_score >= cyber_score and software_score >= data_score:
        return "software"

    if cyber_score >= data_score:
        return "cyber"

    return "data"

    return None


# ---------- MAIN CHATBOT ----------

def get_bot_reply(user_message, session):
    if user_message == "__start__":
        session["step"] = 0

    step = session["step"]

    # STEP 0
    

    if step == 0:
        session["step"] = 1
        return "Hello I will help you find your ideal tech field.", session


    # STEP 1
    elif step == 1:
        choice = understood_work_style(user_message)

        if choice == "people":
            session["software"] += 1
        elif choice == "alone":
            session["data"] += 1
            session["cyber"] += 1
        else:
            return "Do you prefer working with people or alone?", session

        session["step"] = 2
        return "Nice What excites you most in tech?", session


    # STEP 2
    elif step == 2:
        choice = understood_interest(user_message)

        if choice == "software":
            session["software"] += 2
        elif choice == "cyber":
            session["cyber"] += 2
        elif choice == "data":
            session["data"] += 2
        else:
            return "Tell me what you enjoy: coding, hacking, or analyzing data?", session

        session["step"] = 3
        return "When a system crashes, what do you do first?", session


    # STEP 3
    elif step == 3:
        choice = understood_reaction(user_message)

        if choice == "software":
            session["software"] += 2
        elif choice == "cyber":
            session["cyber"] += 2
        elif choice == "data":
            session["data"] += 2
        else:
            return "If a program crashes, do you fix it, investigate the cause, or analyze logs?", session


        # FINAL RESULT
        software = session["software"]
        data = session["data"]
        cyber = session["cyber"]

        if software >= data and software >= cyber:
            result = " You match SOFTWARE ENGINEERING"
        elif data >= cyber:
            result = " You match DATA SCIENCE / AI"
        else:
            result = " You match CYBERSECURITY"

        return result, reset_session()
