from django.db import models


class CandidateProfile(models.Model):
    full_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    recommended_field = models.CharField(max_length=100)
    personality_title = models.CharField(max_length=100)
    confidence_level = models.CharField(max_length=50, blank=True, null=True)

    engineering_score = models.IntegerField(default=0)
    business_score = models.IntegerField(default=0)
    creative_score = models.IntegerField(default=0)
    social_score = models.IntegerField(default=0)

    study_type = models.CharField(max_length=100, blank=True, null=True)
    professional_languages = models.JSONField(default=list, blank=True)
    skills = models.JSONField(default=list, blank=True)
    experience = models.JSONField(default=list, blank=True)
    work_preferences = models.JSONField(default=list, blank=True)
    personality_traits = models.JSONField(default=list, blank=True)

    cv_name = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name or f"Candidate #{self.id}"


class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=200)
    industry = models.JSONField(default=list, blank=True)
    company_size = models.CharField(max_length=50)
    location_pref = models.CharField(max_length=50)
    hire_interns = models.CharField(max_length=10)

    company_culture = models.JSONField(default=list, blank=True)
    work_pace = models.CharField(max_length=100, blank=True, null=True)
    management_style = models.CharField(max_length=100, blank=True, null=True)
    core_values = models.JSONField(default=list, blank=True)
    work_life_balance = models.CharField(max_length=100, blank=True, null=True)

    skills_required = models.JSONField(default=list, blank=True)
    experience_level_required = models.CharField(max_length=100, blank=True, null=True)
    languages_required = models.JSONField(default=list, blank=True)
    risk_tolerance = models.CharField(max_length=150, blank=True, null=True)
    personality_required = models.JSONField(default=list, blank=True)

    salary_range = models.CharField(max_length=100, blank=True, null=True)
    benefits_offered = models.JSONField(default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name


class CompanyCandidateMatch(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name="matches")
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name="matches")
    match_score = models.IntegerField(default=0)
    match_reason = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-match_score"]

    def __str__(self):
        return f"{self.company.company_name} - {self.candidate} ({self.match_score})"


class SavedCandidate(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)


class PageTemplate(models.Model):
    """Stores HTML templates for the multi-step questionnaire pages."""

    key = models.CharField(max_length=50, unique=True)
    html_content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key

