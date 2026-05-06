# TODO

- [x] Inspect DB and existing seed commands for questionnaire.
- [x] Run migrations and initialize questionnaire with `init_full_questionnaire`.
- [x] Initialize page templates into `section1.models.PageTemplate` via `init_section_templates`.
- [ ] Fix incomplete Section 1 questions.
  - [ ] Update `core/management/commands/init_full_questionnaire.py` to add missing Section 1 questions (ordres 3, 4, 6, 7) based on `section1/templates/section1/section1.html`.
  - [ ] Re-run migrations if needed.
  - [ ] Re-run seed command.
  - [ ] Verify in DB that Section 1 has all 7 questions.

