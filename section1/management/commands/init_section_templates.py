import os
from django.core.management.base import BaseCommand
from section1.models import PageTemplate


class Command(BaseCommand):
    help = "Insert section2..section8 and result page HTML into the database (PageTemplate model)."

    def handle(self, *args, **options):
        # Templates live here in this project:
        # section1/templates/section1/<template>.html
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
        template_dir = os.path.join(base_dir, "section1", "templates", "section1")
        # If base_dir resolution is wrong, fall back to this known absolute layout
        if not os.path.exists(template_dir):
            template_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")), "section1", "templates", "section1")



        mapping = {
            "section2": "section2.html",
            "section3": "section3.html",
            "section4": "section4.html",
            "section5": "section5.html",
            "section6-7": "section6-7.html",
            "section8": "section8.html",
            "result": "result.html",
            "candidate_detail": "candidate_detail.html",
            "company_questionnaire": "company_questionnaire.html",
            "contact_candidate": "contact_candidate.html",
            "saved_candidates": "saved_candidates.html",
        }





        created = 0
        updated = 0
        missing = []

        for key, filename in mapping.items():
            file_path = os.path.join(template_dir, filename)
            if not os.path.exists(file_path):
                missing.append(file_path)
                continue

            with open(file_path, "r", encoding="utf-8") as f:
                html = f.read()

            obj, is_created = PageTemplate.objects.get_or_create(key=key, defaults={"html_content": html})
            if is_created:
                created += 1
            else:
                if obj.html_content != html:
                    obj.html_content = html
                    obj.save(update_fields=["html_content"])
                    updated += 1

        if missing:
            self.stdout.write(self.style.WARNING(f"Missing templates ({len(missing)}):"))
            for p in missing:
                self.stdout.write(f" - {p}")

        self.stdout.write(self.style.SUCCESS(f"Page templates inserted. created={created}, updated={updated}."))

