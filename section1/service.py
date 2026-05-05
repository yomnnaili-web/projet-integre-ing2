def calculate_score(data):

    scores = {
        "tech": 0,
        "business": 0,
        "health": 0,
        "creative": 0,
        "law": 0
    }

    # Get values with default fallback
    bac_section = data.get("bac_section", "")
    study_type = data.get("study_type", "")

    # Bac section scoring
    if bac_section == "info":
        scores["tech"] += 2
    if bac_section == "math":
        scores["tech"] += 1
    if bac_section == "eco":
        scores["business"] += 2
    if bac_section == "exp":
        scores["health"] += 2
    if bac_section == "lettres":
        scores["law"] += 1
        scores["creative"] += 1

    # Study type scoring
    if study_type == "engineering":
        scores["tech"] += 2
    if study_type == "medical":
        scores["health"] += 2
    if study_type == "business":
        scores["business"] += 2
    if study_type == "arts":
        scores["creative"] += 2
    if study_type == "law":
        scores["law"] += 2
    if study_type == "it":
        scores["tech"] += 2

    #--------------- scoring section2------------------



    # Q8
    if data.get("q8") == "logical":
        scores["tech"] += 2
    if data.get("q8") == "creative":
        scores["creative"] += 2
    if data.get("q8") == "collaborative":
        scores["business"] += 1
        scores["health"] += 1
    if data.get("q8") == "action":
        scores["business"] += 2

    # Q9
    if data.get("q9") == "leader":
        scores["business"] += 2
    if data.get("q9") == "organizer":
        scores["law"] += 2
    if data.get("q9") == "focused":
        scores["tech"] += 1
    if data.get("q9") == "motivator":
        scores["health"] += 2

    # Q10
    if data.get("q10") == "calm":
        scores["tech"] += 1
    if data.get("q10") == "energized":
        scores["business"] += 1

    # Q11
    if data.get("q11") == "freedom":
        scores["creative"] += 2
    if data.get("q11") == "purpose":
        scores["health"] += 2
    if data.get("q11") == "growth":
        scores["business"] += 2

    # Q12
    if data.get("q12") == "deep":
        scores["law"] += 1
    if data.get("q12") == "influence":
        scores["business"] += 2

    # Q13
    if data.get("q13") == "routine":
        scores["creative"] += 1
    if data.get("q13") == "chaos":
        scores["law"] += 1
    if data.get("q13") == "isolation":
        scores["business"] += 1
    if data.get("q13") == "slow":
        scores["tech"] += 1
    #----------scoring section3----------------    
    
    # Q14
    if data.get("q14") == "structured":
        scores["law"] += 2
    if data.get("q14") == "dynamic":
        scores["business"] += 2
    if data.get("q14") == "stable":
        scores["health"] += 2
    if data.get("q14") == "creative_env":
        scores["creative"] += 2

    # Q15
    if data.get("q15") == "motivated":
        scores["business"] += 1
    if data.get("q15") == "empowered":
        scores["tech"] += 1

    # Q16
    if data.get("q16") == "big_company":
        scores["business"] += 1
    if data.get("q16") == "startup":
        scores["tech"] += 2
    if data.get("q16") == "remote_company":
        scores["tech"] += 1
    if data.get("q16") == "public":
        scores["health"] += 2

    # Q17
    if data.get("q17") == "fixed":
        scores["law"] += 1
    if data.get("q17") == "flexible":
        scores["creative"] += 1
    if data.get("q17") == "project":
        scores["tech"] += 1

    # Q18
    if data.get("q18") == "abroad":
        scores["business"] += 1
    if data.get("q18") == "remote":
        scores["tech"] += 1

    # Q19
    if data.get("q19") == "high_risk":
        scores["business"] += 2
    if data.get("q19") == "low_risk":
        scores["health"] += 1

    # Q20
    if data.get("q20") == "career_first":
        scores["business"] += 1
    if data.get("q20") == "very_important":
        scores["health"] += 1

    

    best_field = max(scores, key=scores.get)

    return best_field, scores[best_field]


def calculate_full_score(data):
    """Same as calculate_score - for section2"""
    return calculate_score(data)


def calculate_complete_score(data):
    """Same as calculate_score - for section3"""
    return calculate_score(data)
