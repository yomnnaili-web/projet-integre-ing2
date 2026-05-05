from django.shortcuts import render, redirect, get_object_or_404
from .models import CandidateProfile, CompanyProfile, CompanyCandidateMatch, SavedCandidate
from section1.models import CandidateProfile


def question_view(request):
    return render(request, 'section1/questions.html')
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

    return render(request, "section1/section1.html")


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

    return render(request, "section1/section2.html")


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

    return render(request, "section1/section3.html")


def section4(request):
    if request.method == "POST":
        request.session["section4"] = {
            "q21": request.POST.getlist("q21"),
            "q22": request.POST.getlist("q22"),
            "q23": request.POST.getlist("q23"),
            "q24": request.POST.getlist("q24"),
        }
        return redirect("section5")

    return render(request, "section1/section4.html")


def section5(request):
    if request.method == "POST":
        request.session["section5"] = {
            "q25": request.POST.getlist("q25"),
            "q26": request.POST.getlist("q26"),
            "q27": request.POST.getlist("q27"),
        }
        return redirect("section6-7")

    return render(request, "section1/section5.html")


def section6(request):
    if request.method == "POST":
        request.session["section6"] = {
            "q28": request.POST.get("q28"),
            "q29": request.POST.getlist("q29"),
            "q30": request.POST.getlist("q30"),
        }
        return redirect("result")

    return render(request, "section1/section6-7.html")


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

    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    top_field, top_score = sorted_scores[0]
    second_field, second_score = sorted_scores[1]

    score_gap = top_score - second_score

    if top_score >= 14:
        confidence_level = "Very strong match"
    elif top_score >= 10:
        confidence_level = "Strong match"
    elif top_score >= 6:
        confidence_level = "Moderate match"
    else:
        confidence_level = "Exploratory match"

    is_hybrid = score_gap <= 2 and second_score > 0

    # Simplified profiles for brevity (expand as needed)
    profiles = {
        top_field: {
            "personality_title": f"The {top_field} Specialist",
            "personality_description": f"Your profile matches {top_field.lower()}.",
            "strengths": ["Key strength 1", "Key strength 2"],
            "career_examples": [f"Career in {top_field}"]
        }
    }

    recommended_field = top_field

    context = {
        "field": recommended_field,
        "score": top_score,
        "top_score": top_score,
        "confidence_level": confidence_level,
        "all_scores": scores,
    }
    request.session["result_data"] = context

    return render(request, "section1/result.html", context)


def section8(request):
    if request.method == "POST":
        # Create candidate profile from session
        section1_data = request.session.get("section1", {})
        result_data = request.session.get("result_data", {})

        CandidateProfile.objects.create(
            full_name=request.POST.get("full_name", ""),
            email=request.POST.get("email", ""),
            recommended_field=result_data.get("field", ""),
            # ... other fields
        )

        return redirect("result")

    return render(request, "section1/section8.html")


def company_questionnaire(request):
    if request.method == "POST":
        # ... company creation logic
        return render(request, "section1/company_results.html", {"company": company})

    return render(request, "section1/company_questionnaire.html")


def candidate_detail(request, candidate_id):
    candidate = get_object_or_404(CandidateProfile, id=candidate_id)
    return render(request, "section1/candidate_detail.html", {"candidate": candidate})


def save_candidate(request, company_id, candidate_id):
    company = get_object_or_404(CompanyProfile, id=company_id)
    candidate = get_object_or_404(CandidateProfile, id=candidate_id)
    SavedCandidate.objects.get_or_create(company=company, candidate=candidate)
    return redirect('saved_candidates', company_id=company.id)


def saved_candidates(request, company_id):
    company = get_object_or_404(CompanyProfile, id=company_id)
    saved = SavedCandidate.objects.filter(company=company)
    return render(request, "section1/saved_candidates.html", {"company": company, "saved": saved})
