// Simple client-side autofill for section1..section6-7 pages.
// It uses DOM name/value matches and checks/radios/selects accordingly.

function setCheckedByNameAndValue(name, value) {
  const inputs = document.querySelectorAll(`input[name="${name}"][value="${value}"]`);
  inputs.forEach(i => {
    i.checked = true;
  });
}

function setRadioByNameAndValue(name, value) {
  const inputs = document.querySelectorAll(`input[type="radio"][name="${name}"][value="${value}"]`);
  inputs.forEach(i => {
    i.checked = (i.value === value);
  });
}

function setSelectValue(name, value) {
  const sel = document.querySelector(`select[name="${name}"]`);
  if (!sel) return;
  sel.value = value;
}

function autofillAll() {
  // ===== Section 1 =====
  setRadioByNameAndValue('bac', 'yes');
  setSelectValue('bac_section', 'info');
  setSelectValue('average', 'excellent');
  setSelectValue('status', 'university');
  setSelectValue('study_type', 'it');

  // future_choice: multiple checkboxes
  setCheckedByNameAndValue('future_choice', 'same');

  // change_reason: can be anything; backend reads list
  setCheckedByNameAndValue('change_reason', 'better');

  // ===== Section 2 =====
  // q8..q13 are checkboxes
  setCheckedByNameAndValue('q8', 'logical');
  setCheckedByNameAndValue('q8', 'creative');

  setCheckedByNameAndValue('q9', 'leader');
  setCheckedByNameAndValue('q9', 'organizer');

  setCheckedByNameAndValue('q10', 'calm');
  setCheckedByNameAndValue('q10', 'energized');

  setCheckedByNameAndValue('q11', 'structure');
  setCheckedByNameAndValue('q11', 'growth');

  setCheckedByNameAndValue('q12', 'deep');
  setCheckedByNameAndValue('q12', 'listener');

  setCheckedByNameAndValue('q13', 'routine');
  setCheckedByNameAndValue('q13', 'slow');

  // ===== Section 3 =====
  setCheckedByNameAndValue('q14', 'dynamic');
  setCheckedByNameAndValue('q14', 'structured');

  setCheckedByNameAndValue('q15', 'empowered');
  setCheckedByNameAndValue('q15', 'motivated');

  setCheckedByNameAndValue('q16', 'startup');
  setCheckedByNameAndValue('q16', 'remote_company');

  setCheckedByNameAndValue('q17', 'flexible');
  setCheckedByNameAndValue('q17', 'project');

  setCheckedByNameAndValue('q18', 'tunisia');
  setCheckedByNameAndValue('q18', 'remote');

  setCheckedByNameAndValue('q19', 'moderate_risk');
  setCheckedByNameAndValue('q19', 'low_risk');

  setCheckedByNameAndValue('q20', 'important');
  setCheckedByNameAndValue('q20', 'career_first');

  // ===== Section 4 =====
  setCheckedByNameAndValue('q21', 'technical');
  setCheckedByNameAndValue('q21', 'business');

  setCheckedByNameAndValue('q22', 'technical');
  setCheckedByNameAndValue('q22', 'creative');

  setCheckedByNameAndValue('q23', 'technical');
  setCheckedByNameAndValue('q23', 'business');

  setCheckedByNameAndValue('q24', 'technical');
  setCheckedByNameAndValue('q24', 'business');

  // ===== Section 5 =====
  setCheckedByNameAndValue('q25', 'programming');
  setCheckedByNameAndValue('q25', 'data');
  setCheckedByNameAndValue('q25', 'writing');

  setCheckedByNameAndValue('q26', 'intermediate');

  setCheckedByNameAndValue('q27', 'internship');
  setCheckedByNameAndValue('q27', 'freelance');

  // ===== Section 6 =====
  // q28 is radio
  setRadioByNameAndValue('q28', 'limited');

  setCheckedByNameAndValue('q29', 'french');
  setCheckedByNameAndValue('q29', 'english');

  setCheckedByNameAndValue('q30', 'english');
  setCheckedByNameAndValue('q30', 'french');
}

document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('autofill-btn');
  if (!btn) return;
  btn.addEventListener('click', (e) => {
    e.preventDefault();
    autofillAll();
  });
});

