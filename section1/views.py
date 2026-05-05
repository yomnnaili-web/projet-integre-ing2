from django.shortcuts import render, redirect, get_object_or_404
from .models import CandidateProfile, CompanyProfile, CompanyCandidateMatch, SavedCandidate
from core.models import Question


def question_view(request):
    questions = Question.objects.all().order_by('ordre')
    return render(request, 'questionnaire.html', {'questions': questions})

def section1(request):
    if request.method == "POST":
        request.session["section1"] = {
            "bac": request.POST.get("bac"),
            "bac_section": request.POST.get("bac_section"),
            "average": request.POST.get("average"),
            "status": request.POST.get("status"),
            "study_type": request.POST.get("study_type"),
            "future_choice": request.POST.getlist("future_choice"),
            "change_reason": request.POST.getlist("change_reason"),
        }
        return redirect("section2")

    return render(request, "section1.html")


def section2(request):
    if request.method == "POST":
        request.session["section2"] = {
            "q8": request.POST.getlist("q8"),
            "q9": request.POST.getlist("q9"),
            "q10": request.POST.getlist("q10"),
            "q11": request.POST.getlist("q11"),
            "q12": request.POST.getlist("q12"),
            "q13": request.POST.getlist("q13"),
        }
        return redirect("section3")

    return render(request, "section2.html")


def section3(request):
    if request.method == "POST":
        request.session["section3"] = {
            "q14": request.POST.getlist("q14"),
            "q15": request.POST.getlist("q15"),
            "q16": request.POST.getlist("q16"),
            "q17": request.POST.getlist("q17"),
            "q18": request.POST.getlist("q18"),
            "q19": request.POST.getlist("q19"),
            "q20": request.POST.getlist("q20"),
        }
        return redirect("section4")

    return render(request, "section3.html")


def section4(request):
    if request.method == "POST":
        request.session["section4"] = {
            "q21": request.POST.getlist("q21"),
            "q22": request.POST.getlist("q22"),
            "q23": request.POST.getlist("q23"),
            "q24": request.POST.getlist("q24"),
        }
        return redirect("section5")

    return render(request, "section4.html")


def section5(request):
    if request.method == "POST":
        request.session["section5"] = {
            "q25": request.POST.getlist("q25"),
            "q26": request.POST.getlist("q26"),
            "q27": request.POST.getlist("q27"),
        }
        return redirect("section6-7")

    return render(request, "section5.html")


def section6(request):
    if request.method == "POST":
        request.session["section6"] = {
            "q28": request.POST.get("q28"),
            "q29": request.POST.getlist("q29"),
            "q30": request.POST.getlist("q30"),
        }
        return redirect("result")

    return render(request, "section6-7.html")


def result(request):
    section1_data = request.session.get("section1", {})
    section2_data = request.session.get("section2", {})
    section3_data = request.session.get("section3", {})
    section4_data = request.session.get("section4", {})
    section5_data = request.session.get("section5", {})
    section6_data = request.session.get("section6", {})

    scores = {
        "Engineering / IT": 0,
        "Business / Management": 0,
        "Creative / Design": 0,
        "Social / Communication": 0,
    }

    # -----------------------------
    # SCORING LOGIC
    # -----------------------------
    study_type = section1_data.get("study_type")
    if study_type in ["engineering", "it"]:
        scores["Engineering / IT"] += 3
    elif study_type == "business":
        scores["Business / Management"] += 3
    elif study_type == "arts":
        scores["Creative / Design"] += 3
    elif study_type in ["medical", "law"]:
        scores["Social / Communication"] += 3

    for value in section4_data.get("q21", []):
        if value == "technical":
            scores["Engineering / IT"] += 2
        elif value == "business":
            scores["Business / Management"] += 2
        elif value == "creative":
            scores["Creative / Design"] += 2
        elif value == "social":
            scores["Social / Communication"] += 2

    for value in section4_data.get("q22", []):
        if value == "technical":
            scores["Engineering / IT"] += 2
        elif value == "business":
            scores["Business / Management"] += 2
        elif value == "creative":
            scores["Creative / Design"] += 2
        elif value == "social":
            scores["Social / Communication"] += 2

    for value in section4_data.get("q23", []):
        if value == "technical":
            scores["Engineering / IT"] += 2
        elif value == "business":
            scores["Business / Management"] += 2
        elif value == "creative":
            scores["Creative / Design"] += 2
        elif value == "social":
            scores["Social / Communication"] += 2

    for value in section4_data.get("q24", []):
        if value == "technical":
            scores["Engineering / IT"] += 2
        elif value == "business":
            scores["Business / Management"] += 2
        elif value == "creative":
            scores["Creative / Design"] += 2
        elif value == "social":
            scores["Social / Communication"] += 2

    skills = section5_data.get("q25", [])
    if "programming" in skills or "data" in skills:
        scores["Engineering / IT"] += 3
    if "sales" in skills or "leadership" in skills:
        scores["Business / Management"] += 3
    if "graphic" in skills or "video" in skills or "writing" in skills:
        scores["Creative / Design"] += 3
    if "speaking" in skills or "social" in skills:
        scores["Social / Communication"] += 3

    professional_languages = section6_data.get("q30", [])
    if "english" in professional_languages:
        scores["Engineering / IT"] += 1
        scores["Business / Management"] += 1

    # -----------------------------
    # SINGLE PROFILE DATA
    # -----------------------------
    profiles = {
        "Engineering / IT": {
            "personality_title": "The Analytical Builder",
            "personality_description": (
                "You seem to enjoy logic, structure, and solving practical problems. "
                "You are likely comfortable with technical learning, systems, and building useful solutions."
            ),
            "why_this_fits": (
                "Your answers suggest a strong attraction to technical reasoning, skill-based growth, "
                "and intellectually challenging work."
            ),
            "strengths": [
                "Logical thinking",
                "Problem-solving ability",
                "Comfort with structured learning",
                "Potential to grow in technical environments"
            ],
            "challenges": [
                "May overthink before acting",
                "May dislike vague or chaotic environments",
                "May need to strengthen communication in team settings"
            ],
            "how_we_help": [
                "Help you choose the right technical specialization",
                "Suggest certifications, projects, and internships",
                "Guide you in building a stronger technical profile"
            ],
            "career_examples": [
                "Software Developer",
                "Data Analyst",
                "Cybersecurity Analyst",
                "QA Engineer",
                "Web Developer"
            ]
        },
        "Business / Management": {
            "personality_title": "The Strategic Leader",
            "personality_description": (
                "You seem motivated by growth, results, responsibility, and impact. "
                "You may enjoy organizing people, making decisions, and pushing projects forward."
            ),
            "why_this_fits": (
                "Your profile suggests leadership potential, initiative, and an interest in strategy, "
                "performance, and achievement."
            ),
            "strengths": [
                "Leadership potential",
                "Decision-making mindset",
                "Motivation for achievement",
                "Good initiative and ambition"
            ],
            "challenges": [
                "May become impatient with slow progress",
                "May lose energy in repetitive roles",
                "May need more technical depth in some fields"
            ],
            "how_we_help": [
                "Help you identify the right business path",
                "Suggest internships and leadership-building experiences",
                "Guide you in presenting yourself professionally"
            ],
            "career_examples": [
                "Project Manager",
                "Marketing Specialist",
                "Business Analyst",
                "Sales Executive",
                "HR Coordinator"
            ]
        },
        "Creative / Design": {
            "personality_title": "The Creative Explorer",
            "personality_description": (
                "You seem imaginative, expressive, and driven by originality. "
                "You likely enjoy creating, designing, and turning ideas into meaningful work."
            ),
            "why_this_fits": (
                "Your answers show a strong need for creativity, freedom of expression, "
                "and visually or conceptually engaging work."
            ),
            "strengths": [
                "Creative thinking",
                "Originality",
                "Strong expressive potential",
                "Good fit for innovative projects"
            ],
            "challenges": [
                "May struggle in very rigid environments",
                "May lose motivation in repetitive tasks",
                "May need more structure to build a stable path"
            ],
            "how_we_help": [
                "Help you choose the right creative direction",
                "Guide you in building a portfolio",
                "Show you how to turn creativity into real opportunities"
            ],
            "career_examples": [
                "Graphic Designer",
                "UI/UX Designer",
                "Content Creator",
                "Video Editor",
                "Brand Designer"
            ]
        },
        "Social / Communication": {
            "personality_title": "The Human Connector",
            "personality_description": (
                "You seem people-oriented, empathetic, and motivated by meaning and connection. "
                "You may do your best work in roles that involve communication, support, or collaboration."
            ),
            "why_this_fits": (
                "Your profile points toward human-centered work, communication strengths, "
                "and a preference for meaningful interaction."
            ),
            "strengths": [
                "Communication potential",
                "Empathy and people awareness",
                "Teamwork orientation",
                "Motivation through impact and purpose"
            ],
            "challenges": [
                "May absorb stress from others",
                "May struggle in isolated roles",
                "May need stronger boundaries in demanding environments"
            ],
            "how_we_help": [
                "Help you identify people-focused career paths",
                "Guide you toward suitable practical experiences",
                "Help you communicate your strengths with confidence"
            ],
            "career_examples": [
                "Recruiter",
                "Teacher",
                "Customer Success Specialist",
                "Community Manager",
                "Career Advisor"
            ]
        }
    }

    # -----------------------------
    # SORT SCORES
    # -----------------------------
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    top_field, top_score = sorted_scores[0]
    second_field, second_score = sorted_scores[1]

    score_gap = top_score - second_score

    # -----------------------------
    # CONFIDENCE LEVEL
    # -----------------------------
    if top_score >= 14:
        confidence_level = "Very strong match"
    elif top_score >= 10:
        confidence_level = "Strong match"
    elif top_score >= 6:
        confidence_level = "Moderate match"
    else:
        confidence_level = "Exploratory match"

    # -----------------------------
    # HYBRID LOGIC
    # -----------------------------
    is_hybrid = score_gap <= 2 and second_score > 0

    hybrid_profiles = {
        ("Engineering / IT", "Creative / Design"): {
            "personality_title": "The Innovative Maker",
            "personality_description": (
                "You combine analytical thinking with creativity. You are likely someone who enjoys solving problems, "
                "but also cares about originality, design, and user experience."
            ),
            "why_this_fits": (
                "Your answers suggest a hybrid profile: technical enough to build, and creative enough to imagine better ways of doing things."
            ),
            "strengths": [
                "Mix of logic and creativity",
                "Ability to build and improve ideas",
                "Strong fit for digital product work",
                "Good potential in innovation-driven roles"
            ],
            "challenges": [
                "May feel split between technical and creative choices",
                "May need help choosing a focused direction",
                "May dislike roles that are too rigid or too vague"
            ],
            "how_we_help": [
                "Help you identify careers that combine tech and creativity",
                "Guide you toward a balanced learning path",
                "Suggest projects that strengthen both sides of your profile"
            ],
            "career_examples": [
                "UI/UX Designer",
                "Front-End Developer",
                "Product Designer",
                "Creative Technologist",
                "Digital Product Creator"
            ]
        },
        ("Creative / Design", "Engineering / IT"): {
            "personality_title": "The Innovative Maker",
            "personality_description": (
                "You combine analytical thinking with creativity. You are likely someone who enjoys solving problems, "
                "but also cares about originality, design, and user experience."
            ),
            "why_this_fits": (
                "Your answers suggest a hybrid profile: technical enough to build, and creative enough to imagine better ways of doing things."
            ),
            "strengths": [
                "Mix of logic and creativity",
                "Ability to build and improve ideas",
                "Strong fit for digital product work",
                "Good potential in innovation-driven roles"
            ],
            "challenges": [
                "May feel split between technical and creative choices",
                "May need help choosing a focused direction",
                "May dislike roles that are too rigid or too vague"
            ],
            "how_we_help": [
                "Help you identify careers that combine tech and creativity",
                "Guide you toward a balanced learning path",
                "Suggest projects that strengthen both sides of your profile"
            ],
            "career_examples": [
                "UI/UX Designer",
                "Front-End Developer",
                "Product Designer",
                "Creative Technologist",
                "Digital Product Creator"
            ]
        },

        ("Business / Management", "Social / Communication"): {
            "personality_title": "The Influential Coordinator",
            "personality_description": (
                "You combine leadership with people skills. You may be good at organizing, communicating, and motivating others toward shared goals."
            ),
            "why_this_fits": (
                "Your profile suggests that you are not only results-oriented, but also aware of people, relationships, and communication."
            ),
            "strengths": [
                "Leadership and people awareness",
                "Communication strength",
                "Good fit for team-based roles",
                "Ability to influence and coordinate"
            ],
            "challenges": [
                "May take on too much responsibility for others",
                "May struggle between performance and emotional pressure",
                "May need stronger boundaries"
            ],
            "how_we_help": [
                "Help you explore careers combining leadership and communication",
                "Guide you toward internships with team responsibility",
                "Help you present yourself as a future coordinator or manager"
            ],
            "career_examples": [
                "HR Manager",
                "Recruitment Specialist",
                "Customer Success Manager",
                "Project Coordinator",
                "Training Officer"
            ]
        },
        ("Social / Communication", "Business / Management"): {
            "personality_title": "The Influential Coordinator",
            "personality_description": (
                "You combine leadership with people skills. You may be good at organizing, communicating, and motivating others toward shared goals."
            ),
            "why_this_fits": (
                "Your profile suggests that you are not only results-oriented, but also aware of people, relationships, and communication."
            ),
            "strengths": [
                "Leadership and people awareness",
                "Communication strength",
                "Good fit for team-based roles",
                "Ability to influence and coordinate"
            ],
            "challenges": [
                "May take on too much responsibility for others",
                "May struggle between performance and emotional pressure",
                "May need stronger boundaries"
            ],
            "how_we_help": [
                "Help you explore careers combining leadership and communication",
                "Guide you toward internships with team responsibility",
                "Help you present yourself as a future coordinator or manager"
            ],
            "career_examples": [
                "HR Manager",
                "Recruitment Specialist",
                "Customer Success Manager",
                "Project Coordinator",
                "Training Officer"
            ]
        },

        ("Business / Management", "Creative / Design"): {
            "personality_title": "The Brand Strategist",
            "personality_description": (
                "You combine business thinking with creativity. You may be naturally drawn to building ideas, promoting value, and shaping how people see products or services."
            ),
            "why_this_fits": (
                "Your answers suggest a profile that enjoys both strategic thinking and creative expression."
            ),
            "strengths": [
                "Strategic and creative balance",
                "Good fit for market-facing roles",
                "Ability to think about value and presentation",
                "Strong potential in modern digital careers"
            ],
            "challenges": [
                "May hesitate between artistic freedom and business logic",
                "May need structure to choose the right direction",
                "May need stronger technical tools depending on the path"
            ],
            "how_we_help": [
                "Help you identify business-creative paths",
                "Guide you toward portfolio and project development",
                "Suggest practical paths like marketing, branding, and product communication"
            ],
            "career_examples": [
                "Digital Marketer",
                "Brand Strategist",
                "Content Strategist",
                "Product Marketing Assistant",
                "Social Media Manager"
            ]
        },
        ("Creative / Design", "Business / Management"): {
            "personality_title": "The Brand Strategist",
            "personality_description": (
                "You combine business thinking with creativity. You may be naturally drawn to building ideas, promoting value, and shaping how people see products or services."
            ),
            "why_this_fits": (
                "Your answers suggest a profile that enjoys both strategic thinking and creative expression."
            ),
            "strengths": [
                "Strategic and creative balance",
                "Good fit for market-facing roles",
                "Ability to think about value and presentation",
                "Strong potential in modern digital careers"
            ],
            "challenges": [
                "May hesitate between artistic freedom and business logic",
                "May need structure to choose the right direction",
                "May need stronger technical tools depending on the path"
            ],
            "how_we_help": [
                "Help you identify business-creative paths",
                "Guide you toward portfolio and project development",
                "Suggest practical paths like marketing, branding, and product communication"
            ],
            "career_examples": [
                "Digital Marketer",
                "Brand Strategist",
                "Content Strategist",
                "Product Marketing Assistant",
                "Social Media Manager"
            ]
        }
    }

    if is_hybrid and (top_field, second_field) in hybrid_profiles:
        selected_profile = hybrid_profiles[(top_field, second_field)]
        result_type = "hybrid"
        recommended_field = f"{top_field} + {second_field}"
        secondary_match = sorted_scores[2][0]
    else:
        selected_profile = profiles[top_field]
        result_type = "single"
        recommended_field = top_field
        secondary_match = second_field

    context = {
    "field": recommended_field,
    "score": top_score,
    "top_score": top_score,
    "second_score": second_score,
    "all_scores": scores,

    "personality_title": selected_profile["personality_title"],
    "personality_description": selected_profile["personality_description"],
    "why_this_fits": selected_profile["why_this_fits"],
    "strengths": selected_profile["strengths"],
    "challenges": selected_profile["challenges"],
    "how_we_help": selected_profile["how_we_help"],
    "career_examples": selected_profile["career_examples"],

    "confidence_level": confidence_level,
    "result_type": result_type,
    "primary_match": top_field,
    "secondary_match": secondary_match,
    "score_gap": score_gap,

    # 🔥 NEW ADDITIONS
    "personal_message": "Based on your answers, your profile shows a strong alignment with this direction.",
    
    "next_steps": [
        "Explore beginner resources in this field",
        "Build a small practical project",
        "Look for internships or real-world experience",
        "Develop your communication and professional skills"
    ],

    "ai_insight": "Your profile shows a valuable combination of skills and preferences that are highly relevant in today’s job market."
}
    request.session["result_data"] = {
    "field": recommended_field,
    "personality_title": selected_profile["personality_title"],
    "confidence_level": confidence_level,
    "all_scores": scores,
}

    return render(request, "result.html", context)


def section8(request):
    if request.method == "POST":
        request.session["section7"] = {
            "linkedin": request.POST.get("linkedin"),
            "portfolio": request.POST.get("portfolio"),
            "github": request.POST.get("github"),
            "notes": request.POST.get("notes"),
        }

        cv_file = request.FILES.get("cv")
        cv_name = cv_file.name if cv_file else ""

        section1_data = request.session.get("section1", {})
        section2_data = request.session.get("section2", {})
        section3_data = request.session.get("section3", {})
        section5_data = request.session.get("section5", {})
        section6_data = request.session.get("section6", {})
        result_data = request.session.get("result_data", {})

        CandidateProfile.objects.create(
            full_name=request.POST.get("full_name", ""),
            email=request.POST.get("email", ""),
            recommended_field=result_data.get("field", ""),
            personality_title=result_data.get("personality_title", ""),
            confidence_level=result_data.get("confidence_level", ""),
            engineering_score=result_data.get("all_scores", {}).get("Engineering / IT", 0),
            business_score=result_data.get("all_scores", {}).get("Business / Management", 0),
            creative_score=result_data.get("all_scores", {}).get("Creative / Design", 0),
            social_score=result_data.get("all_scores", {}).get("Social / Communication", 0),
            study_type=section1_data.get("study_type", ""),
            professional_languages=section6_data.get("q30", []),
            skills=section5_data.get("q25", []),
            experience=section5_data.get("q27", []),
            work_preferences=section3_data.get("q16", []) + section3_data.get("q17", []) + section3_data.get("q18", []),
            personality_traits=section2_data.get("q8", []) + section2_data.get("q9", []) + section2_data.get("q11", []),
            cv_name=cv_name,
            linkedin=request.POST.get("linkedin", ""),
            portfolio=request.POST.get("portfolio", ""),
            github=request.POST.get("github", ""),
        )

        return redirect("final")

    return render(request, "section8.html")
def calculate_company_candidate_match(company, candidate):
    score = 0
    reasons = []

    industry_map = {
        "Technology / IT": "Engineering / IT",
        "Business / Finance": "Business / Management",
        "Creative / Media / Design": "Creative / Design",
        "Health / Medical": "Social / Communication",
        "Law / Consulting": "Social / Communication",
    }

    mapped_fields = [industry_map.get(item) for item in company.industry if industry_map.get(item)]
    if candidate.recommended_field in mapped_fields:
        score += 30
        reasons.append("Candidate's recommended field matches the company's industry.")

    skill_map = {
        "Technical / Programming": ["programming", "data"],
        "Creative / Design": ["graphic", "video", "writing"],
        "Communication / Soft skills": ["speaking", "social"],
        "Leadership / Management": ["leadership", "sales"],
        "Business / Analytical": ["sales", "leadership", "data"],
    }

    matched_skill_count = 0
    for required_skill in company.skills_required:
        mapped_candidate_skills = skill_map.get(required_skill, [])
        overlap = set(mapped_candidate_skills).intersection(set(candidate.skills))
        if overlap:
            matched_skill_count += 1
            reasons.append(f"Skill match found for {required_skill}.")
    score += matched_skill_count * 10

    company_langs = {lang.lower() for lang in company.languages_required}
    candidate_langs = {lang.lower() for lang in candidate.professional_languages}
    common_langs = company_langs.intersection(candidate_langs)
    if common_langs:
        score += 10
        reasons.append(f"Language match: {', '.join(common_langs)}.")

    exp_required = company.experience_level_required
    if exp_required == "Intern / Fresh graduate":
        score += 8
        reasons.append("Company accepts interns or fresh graduates.")
    elif exp_required == "1–3 years" and len(candidate.experience) >= 1:
        score += 10
        reasons.append("Candidate has early professional experience.")
    elif exp_required == "3–5 years" and len(candidate.experience) >= 2:
        score += 12
        reasons.append("Candidate has a stronger experience background.")
    elif exp_required == "Senior / Expert" and len(candidate.experience) >= 3:
        score += 15
        reasons.append("Candidate has advanced experience history.")

    personality_map = {
        "Logical / Analytical": ["logical", "structure", "technical"],
        "Creative / Visionary": ["creative", "freedom"],
        "Social / Team player": ["collaborative", "motivator", "social"],
        "Independent / Self-motivated": ["action", "focused", "independent"],
    }

    matched_personality_count = 0
    for trait in company.personality_required:
        mapped_traits = personality_map.get(trait, [])
        overlap = set(mapped_traits).intersection(set(candidate.personality_traits))
        if overlap:
            matched_personality_count += 1
            reasons.append(f"Personality match for {trait}.")
    score += matched_personality_count * 8

    # remote / location compatibility
    if "Remote work" in company.benefits_offered and (
        "remote_company" in candidate.work_preferences or "remote" in candidate.work_preferences
    ):
        score += 6
        reasons.append("Candidate prefers remote-friendly work.")

    if company.location_pref == "Remote-friendly" and (
        "remote_company" in candidate.work_preferences or "remote" in candidate.work_preferences
    ):
        score += 6
        reasons.append("Location preference is compatible with remote work.")

    if company.location_pref == "Local" and (
        "tunisia" in candidate.work_preferences or "local" in candidate.work_preferences
    ):
        score += 5
        reasons.append("Candidate has compatible local work preferences.")

    if company.hire_interns == "Yes" and "internship" in candidate.experience:
        score += 5
        reasons.append("Candidate already has internship-related exposure.")

    # bonus if company selected few criteria and candidate still aligns
    if not reasons and candidate.recommended_field:
        score += 5
        reasons.append("Candidate has a generally relevant profile.")

    explanation = "This candidate is a good match because: "
    if reasons:
        explanation += ", ".join(reasons[:3])
    else:
        explanation += "their profile aligns with your company needs."

    return score, reasons, explanation
def company_questionnaire(request):
    if request.method == "POST":
        company = CompanyProfile.objects.create(
            company_name=request.POST.get("company_name"),
            industry=request.POST.getlist("industry"),
            company_size=request.POST.get("company_size"),
            location_pref=request.POST.get("location_pref"),
            hire_interns=request.POST.get("hire_interns"),
            company_culture=request.POST.getlist("company_culture"),
            work_pace=request.POST.get("work_pace"),
            management_style=request.POST.get("management_style"),
            core_values=request.POST.getlist("core_values"),
            work_life_balance=request.POST.get("work_life_balance"),
            skills_required=request.POST.getlist("skills_required"),
            experience_level_required=request.POST.get("experience_level_required"),
            languages_required=request.POST.getlist("languages_required"),
            risk_tolerance=request.POST.get("risk_tolerance"),
            personality_required=request.POST.getlist("personality_required"),
            salary_range=request.POST.get("salary_range"),
            benefits_offered=request.POST.getlist("benefits_offered"),
        )

        candidates = CandidateProfile.objects.all()

        filter_field = request.POST.get("filter_field")
        filter_language = request.POST.get("filter_language")
        filter_experience = request.POST.get("filter_experience")

        if filter_field:
            candidates = candidates.filter(recommended_field=filter_field)

        if filter_language:
            candidates = [
                c for c in candidates
                if filter_language.lower() in [l.lower() for l in c.professional_languages]
            ]

        if filter_experience:
            candidates = [
                c for c in candidates
                if filter_experience in c.experience
            ]

        best_matches = []

        for candidate in candidates:
            match_score, match_reasons, explanation = calculate_company_candidate_match(company, candidate)

            if match_score >= 60:
                match_label = "Excellent Match"
            elif match_score >= 40:
                match_label = "Strong Match"
            elif match_score >= 20:
                match_label = "Moderate Match"
            else:
                match_label = "Low Match"

            CompanyCandidateMatch.objects.create(
                company=company,
                candidate=candidate,
                match_score=match_score,
                match_reason=" | ".join(match_reasons),
            )

            # نقصنا threshold من 40 إلى 20
            if match_score >= 20:
                best_matches.append({
                    "candidate": candidate,
                    "score": match_score,
                    "label": match_label,
                    "reasons": match_reasons,
                    "explanation": explanation,
                })

        best_matches = sorted(best_matches, key=lambda x: x["score"], reverse=True)[:5]

        company_summary = (
            f"This company is looking for profiles aligned with "
            f"{', '.join(company.skills_required)} and values "
            f"{', '.join(company.personality_required)}."
        )

        return render(request, "company_results.html", {
            "company": company,
            "best_matches": best_matches,
            "company_summary": company_summary,
        })

    return render(request, "company_questionnaire.html")
def candidate_detail(request, candidate_id):
    candidate = get_object_or_404(CandidateProfile, id=candidate_id)

    context = {
        "candidate": candidate,
    }
    return render(request, "candidate_detail.html", context)

def save_candidate(request, company_id, candidate_id):
    company = get_object_or_404(CompanyProfile, id=company_id)
    candidate = get_object_or_404(CandidateProfile, id=candidate_id)
    SavedCandidate.objects.get_or_create(
        company=company,
        candidate=candidate
    )

    return redirect( company_id=company.id)
def saved_candidates(request, company_id):
    company = get_object_or_404(CompanyProfile, id=company_id)
    saved = SavedCandidate.objects.filter(company=company)

    return render(request, "saved_candidates.html", {
        "company": company,
        "saved": saved
    })