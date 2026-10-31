"""
Sample Student and Class Performance Data for EduAdapt AI
Target: Class 10 Physics (Sections 10-A and 10-B, 30 students)
Used by Teacher Dashboard and Class Analytics
"""

import random
from config import CONCEPTS

# 30 Realistic Class 10 Students
STUDENT_ROSTER = [
    {
        "id": "STU101",
        "name": "Aarav Sharma",
        "section": "10-A",
        "roll_no": 1,
        "diagnostic_score": 4,
        "overall_score": 82,
        "concept_mastery": {
            "light_refl_refr": 88,
            "electricity_circuits": 78,
            "heating_power": 85,
            "magnetic_effects": 70,
            "human_eye": 92
        },
        "weak_concepts": ["magnetic_effects"],
        "risk_category": "High Achiever",
        "attendance_pct": 96,
        "questions_attempted": 34,
        "practice_accuracy_pct": 84,
        "last_active": "Today, 10:15 AM",
        "teacher_notes": "Strong in optics; needs slight revision on Fleming's left hand rule."
    },
    {
        "id": "STU102",
        "name": "Diya Patel",
        "section": "10-A",
        "roll_no": 2,
        "diagnostic_score": 5,
        "overall_score": 94,
        "concept_mastery": {
            "light_refl_refr": 96,
            "electricity_circuits": 92,
            "heating_power": 95,
            "magnetic_effects": 90,
            "human_eye": 98
        },
        "weak_concepts": [],
        "risk_category": "High Achiever",
        "attendance_pct": 98,
        "questions_attempted": 48,
        "practice_accuracy_pct": 95,
        "last_active": "Today, 02:45 PM",
        "teacher_notes": "Exemplary student. Ready for advanced Olympiad / exemplar problems."
    },
    {
        "id": "STU103",
        "name": "Rohan Verma",
        "section": "10-A",
        "roll_no": 3,
        "diagnostic_score": 1,
        "overall_score": 38,
        "concept_mastery": {
            "light_refl_refr": 42,
            "electricity_circuits": 30,
            "heating_power": 35,
            "magnetic_effects": 40,
            "human_eye": 45
        },
        "weak_concepts": ["electricity_circuits", "heating_power", "magnetic_effects", "light_refl_refr", "human_eye"],
        "risk_category": "High Risk",
        "attendance_pct": 74,
        "questions_attempted": 12,
        "practice_accuracy_pct": 33,
        "last_active": "3 days ago",
        "teacher_notes": "Critical: Severe misconceptions in basic Ohm's law and parallel resistance. Remedial session recommended."
    },
    {
        "id": "STU104",
        "name": "Ananya Iyer",
        "section": "10-A",
        "roll_no": 4,
        "diagnostic_score": 3,
        "overall_score": 68,
        "concept_mastery": {
            "light_refl_refr": 75,
            "electricity_circuits": 52,
            "heating_power": 60,
            "magnetic_effects": 65,
            "human_eye": 88
        },
        "weak_concepts": ["electricity_circuits"],
        "risk_category": "Moderate",
        "attendance_pct": 91,
        "questions_attempted": 26,
        "practice_accuracy_pct": 69,
        "last_active": "Yesterday",
        "teacher_notes": "Good grasp of qualitative concepts; struggles with numerical circuit calculations."
    },
    {
        "id": "STU105",
        "name": "Kabir Khan",
        "section": "10-A",
        "roll_no": 5,
        "diagnostic_score": 2,
        "overall_score": 46,
        "concept_mastery": {
            "light_refl_refr": 48,
            "electricity_circuits": 40,
            "heating_power": 45,
            "magnetic_effects": 52,
            "human_eye": 45
        },
        "weak_concepts": ["electricity_circuits", "heating_power", "light_refl_refr", "human_eye"],
        "risk_category": "High Risk",
        "attendance_pct": 79,
        "questions_attempted": 18,
        "practice_accuracy_pct": 44,
        "last_active": "2 days ago",
        "teacher_notes": "Needs extra practice on ray diagrams and sign convention in mirror formula."
    },
    {
        "id": "STU106",
        "name": "Sanya Malhotra",
        "section": "10-A",
        "roll_no": 6,
        "diagnostic_score": 4,
        "overall_score": 79,
        "concept_mastery": {
            "light_refl_refr": 82,
            "electricity_circuits": 72,
            "heating_power": 75,
            "magnetic_effects": 80,
            "human_eye": 86
        },
        "weak_concepts": [],
        "risk_category": "High Achiever",
        "attendance_pct": 94,
        "questions_attempted": 30,
        "practice_accuracy_pct": 80,
        "last_active": "Today, 11:20 AM",
        "teacher_notes": "Consistent performer across all sections. Encouraged to take timed mocks."
    },
    {
        "id": "STU107",
        "name": "Vikramaditya Rao",
        "section": "10-A",
        "roll_no": 7,
        "diagnostic_score": 2,
        "overall_score": 52,
        "concept_mastery": {
            "light_refl_refr": 50,
            "electricity_circuits": 48,
            "heating_power": 55,
            "magnetic_effects": 52,
            "human_eye": 55
        },
        "weak_concepts": ["electricity_circuits", "light_refl_refr"],
        "risk_category": "Moderate",
        "attendance_pct": 85,
        "questions_attempted": 22,
        "practice_accuracy_pct": 50,
        "last_active": "Yesterday",
        "teacher_notes": "Frequently mixes up series and parallel formulas. Provide visual circuit simulation."
    },
    {
        "id": "STU108",
        "name": "Meera Nambiar",
        "section": "10-A",
        "roll_no": 8,
        "diagnostic_score": 5,
        "overall_score": 91,
        "concept_mastery": {
            "light_refl_refr": 94,
            "electricity_circuits": 88,
            "heating_power": 92,
            "magnetic_effects": 86,
            "human_eye": 95
        },
        "weak_concepts": [],
        "risk_category": "High Achiever",
        "attendance_pct": 99,
        "questions_attempted": 42,
        "practice_accuracy_pct": 90,
        "last_active": "Today, 04:10 PM",
        "teacher_notes": "Outstanding analytical skills. Active participant in voice dictation modules."
    },
    {
        "id": "STU109",
        "name": "Ishaan Gupta",
        "section": "10-A",
        "roll_no": 9,
        "diagnostic_score": 3,
        "overall_score": 64,
        "concept_mastery": {
            "light_refl_refr": 65,
            "electricity_circuits": 58,
            "heating_power": 62,
            "magnetic_effects": 60,
            "human_eye": 75
        },
        "weak_concepts": [],
        "risk_category": "Moderate",
        "attendance_pct": 88,
        "questions_attempted": 24,
        "practice_accuracy_pct": 65,
        "last_active": "Yesterday",
        "teacher_notes": "Steady progress. Responding well to adaptive micro-quizzes."
    },
    {
        "id": "STU110",
        "name": "Tanvi Deshmukh",
        "section": "10-A",
        "roll_no": 10,
        "diagnostic_score": 2,
        "overall_score": 49,
        "concept_mastery": {
            "light_refl_refr": 45,
            "electricity_circuits": 50,
            "heating_power": 46,
            "magnetic_effects": 54,
            "human_eye": 51
        },
        "weak_concepts": ["light_refl_refr", "heating_power"],
        "risk_category": "High Risk",
        "attendance_pct": 82,
        "questions_attempted": 19,
        "practice_accuracy_pct": 47,
        "last_active": "2 days ago",
        "teacher_notes": "Confused about power dissipated formula P = V^2 / R versus P = I^2 * R."
    },
    {
        "id": "STU111",
        "name": "Arjun Sen",
        "section": "10-A",
        "roll_no": 11,
        "diagnostic_score": 4,
        "overall_score": 85,
        "concept_mastery": {
            "light_refl_refr": 85,
            "electricity_circuits": 84,
            "heating_power": 88,
            "magnetic_effects": 82,
            "human_eye": 86
        },
        "weak_concepts": [],
        "risk_category": "High Achiever",
        "attendance_pct": 95,
        "questions_attempted": 36,
        "practice_accuracy_pct": 86,
        "last_active": "Today, 09:30 AM",
        "teacher_notes": "Very sound concepts; handwriting and presentation in subjective answers to be polished."
    },
    {
        "id": "STU112",
        "name": "Pooja Hegde",
        "section": "10-A",
        "roll_no": 12,
        "diagnostic_score": 3,
        "overall_score": 71,
        "concept_mastery": {
            "light_refl_refr": 78,
            "electricity_circuits": 62,
            "heating_power": 70,
            "magnetic_effects": 68,
            "human_eye": 77
        },
        "weak_concepts": [],
        "risk_category": "Moderate",
        "attendance_pct": 92,
        "questions_attempted": 28,
        "practice_accuracy_pct": 72,
        "last_active": "Yesterday",
        "teacher_notes": "Shows solid conceptual understanding; needs practice on speed."
    },
    {
        "id": "STU113",
        "name": "Devansh Singhal",
        "section": "10-A",
        "roll_no": 13,
        "diagnostic_score": 1,
        "overall_score": 41,
        "concept_mastery": {
            "light_refl_refr": 38,
            "electricity_circuits": 35,
            "heating_power": 42,
            "magnetic_effects": 45,
            "human_eye": 45
        },
        "weak_concepts": ["light_refl_refr", "electricity_circuits", "heating_power", "magnetic_effects", "human_eye"],
        "risk_category": "High Risk",
        "attendance_pct": 76,
        "questions_attempted": 14,
        "practice_accuracy_pct": 36,
        "last_active": "4 days ago",
        "teacher_notes": "Needs urgent intervention. Parent-teacher meeting suggested."
    },
    {
        "id": "STU114",
        "name": "Kavya Reddy",
        "section": "10-A",
        "roll_no": 14,
        "diagnostic_score": 4,
        "overall_score": 88,
        "concept_mastery": {
            "light_refl_refr": 90,
            "electricity_circuits": 86,
            "heating_power": 88,
            "magnetic_effects": 84,
            "human_eye": 92
        },
        "weak_concepts": [],
        "risk_category": "High Achiever",
        "attendance_pct": 97,
        "questions_attempted": 40,
        "practice_accuracy_pct": 89,
        "last_active": "Today, 01:15 PM",
        "teacher_notes": "Excellent conceptual clarity. Peer tutor candidate for Class 10 study circle."
    },
    {
        "id": "STU115",
        "name": "Nikhil Joshi",
        "section": "10-A",
        "roll_no": 15,
        "diagnostic_score": 3,
        "overall_score": 62,
        "concept_mastery": {
            "light_refl_refr": 64,
            "electricity_circuits": 55,
            "heating_power": 58,
            "magnetic_effects": 60,
            "human_eye": 73
        },
        "weak_concepts": [],
        "risk_category": "Moderate",
        "attendance_pct": 89,
        "questions_attempted": 25,
        "practice_accuracy_pct": 63,
        "last_active": "Yesterday",
        "teacher_notes": "Needs reinforcement on domestic electric circuits and earthing concepts."
    },

    # Section 10-B
    {
        "id": "STU116",
        "name": "Riya Chawla",
        "section": "10-B",
        "roll_no": 1,
        "diagnostic_score": 5,
        "overall_score": 96,
        "concept_mastery": {
            "light_refl_refr": 98,
            "electricity_circuits": 94,
            "heating_power": 96,
            "magnetic_effects": 92,
            "human_eye": 100
        },
        "weak_concepts": [],
        "risk_category": "High Achiever",
        "attendance_pct": 100,
        "questions_attempted": 52,
        "practice_accuracy_pct": 97,
        "last_active": "Today, 05:00 PM",
        "teacher_notes": "Class topper potential. Flawless grasp of Ray Optics and Electromagnetic induction."
    },
    {
        "id": "STU117",
        "name": "Pranav Nair",
        "section": "10-B",
        "roll_no": 2,
        "diagnostic_score": 2,
        "overall_score": 48,
        "concept_mastery": {
            "light_refl_refr": 46,
            "electricity_circuits": 42,
            "heating_power": 48,
            "magnetic_effects": 50,
            "human_eye": 54
        },
        "weak_concepts": ["light_refl_refr", "electricity_circuits", "heating_power"],
        "risk_category": "High Risk",
        "attendance_pct": 80,
        "questions_attempted": 16,
        "practice_accuracy_pct": 42,
        "last_active": "3 days ago",
        "teacher_notes": "Struggles with calculating equivalent resistance and refraction index problems."
    },
    {
        "id": "STU118",
        "name": "Sneha Mukherjee",
        "section": "10-B",
        "roll_no": 3,
        "diagnostic_score": 4,
        "overall_score": 83,
        "concept_mastery": {
            "light_refl_refr": 86,
            "electricity_circuits": 80,
            "heating_power": 84,
            "magnetic_effects": 78,
            "human_eye": 87
        },
        "weak_concepts": [],
        "risk_category": "High Achiever",
        "attendance_pct": 96,
        "questions_attempted": 35,
        "practice_accuracy_pct": 85,
        "last_active": "Today, 12:45 PM",
        "teacher_notes": "Very diligent. Strong performance in both diagnostic and adaptive modules."
    },
    {
        "id": "STU119",
        "name": "Aditya Kapoor",
        "section": "10-B",
        "roll_no": 4,
        "diagnostic_score": 3,
        "overall_score": 67,
        "concept_mastery": {
            "light_refl_refr": 70,
            "electricity_circuits": 60,
            "heating_power": 64,
            "magnetic_effects": 62,
            "human_eye": 79
        },
        "weak_concepts": [],
        "risk_category": "Moderate",
        "attendance_pct": 90,
        "questions_attempted": 27,
        "practice_accuracy_pct": 68,
        "last_active": "Yesterday",
        "teacher_notes": "Capable student. Encouraged to spend 15 min daily on formula revisions."
    },
    {
        "id": "STU120",
        "name": "Ananya Bhatt",
        "section": "10-B",
        "roll_no": 5,
        "diagnostic_score": 1,
        "overall_score": 39,
        "concept_mastery": {
            "light_refl_refr": 35,
            "electricity_circuits": 38,
            "heating_power": 40,
            "magnetic_effects": 42,
            "human_eye": 40
        },
        "weak_concepts": ["light_refl_refr", "electricity_circuits", "heating_power", "magnetic_effects", "human_eye"],
        "risk_category": "High Risk",
        "attendance_pct": 72,
        "questions_attempted": 11,
        "practice_accuracy_pct": 32,
        "last_active": "5 days ago",
        "teacher_notes": "Irregular attendance impacting learning continuity. Requires 1-on-1 tutoring."
    },
    {
        "id": "STU121",
        "name": "Karan Singhania",
        "section": "10-B",
        "roll_no": 6,
        "diagnostic_score": 4,
        "overall_score": 76,
        "concept_mastery": {
            "light_refl_refr": 80,
            "electricity_circuits": 72,
            "heating_power": 74,
            "magnetic_effects": 75,
            "human_eye": 79
        },
        "weak_concepts": [],
        "risk_category": "High Achiever",
        "attendance_pct": 93,
        "questions_attempted": 29,
        "practice_accuracy_pct": 78,
        "last_active": "Today, 08:50 AM",
        "teacher_notes": "Steady grasp across chapters. Focus on avoiding calculation errors."
    },
    {
        "id": "STU122",
        "name": "Bhavya Trivedi",
        "section": "10-B",
        "roll_no": 7,
        "diagnostic_score": 2,
        "overall_score": 53,
        "concept_mastery": {
            "light_refl_refr": 52,
            "electricity_circuits": 48,
            "heating_power": 54,
            "magnetic_effects": 50,
            "human_eye": 61
        },
        "weak_concepts": ["electricity_circuits"],
        "risk_category": "Moderate",
        "attendance_pct": 86,
        "questions_attempted": 20,
        "practice_accuracy_pct": 52,
        "last_active": "Yesterday",
        "teacher_notes": "Needs clarity on right-hand thumb rule vs Fleming's left hand rule."
    },
    {
        "id": "STU123",
        "name": "Manish Pandey",
        "section": "10-B",
        "roll_no": 8,
        "diagnostic_score": 3,
        "overall_score": 70,
        "concept_mastery": {
            "light_refl_refr": 74,
            "electricity_circuits": 66,
            "heating_power": 68,
            "magnetic_effects": 65,
            "human_eye": 77
        },
        "weak_concepts": [],
        "risk_category": "Moderate",
        "attendance_pct": 91,
        "questions_attempted": 27,
        "practice_accuracy_pct": 71,
        "last_active": "Today, 11:00 AM",
        "teacher_notes": "Participates enthusiastically in voice answers."
    },
    {
        "id": "STU124",
        "name": "Gauri Sundaram",
        "section": "10-B",
        "roll_no": 9,
        "diagnostic_score": 5,
        "overall_score": 93,
        "concept_mastery": {
            "light_refl_refr": 95,
            "electricity_circuits": 91,
            "heating_power": 94,
            "magnetic_effects": 90,
            "human_eye": 95
        },
        "weak_concepts": [],
        "risk_category": "High Achiever",
        "attendance_pct": 98,
        "questions_attempted": 45,
        "practice_accuracy_pct": 94,
        "last_active": "Today, 03:20 PM",
        "teacher_notes": "Excellent performance. Can help create concept flashcards for peers."
    },
    {
        "id": "STU125",
        "name": "Harsh Vardhan",
        "section": "10-B",
        "roll_no": 10,
        "diagnostic_score": 2,
        "overall_score": 55,
        "concept_mastery": {
            "light_refl_refr": 58,
            "electricity_circuits": 51,
            "heating_power": 52,
            "magnetic_effects": 54,
            "human_eye": 60
        },
        "weak_concepts": ["electricity_circuits", "heating_power"],
        "risk_category": "Moderate",
        "attendance_pct": 84,
        "questions_attempted": 21,
        "practice_accuracy_pct": 53,
        "last_active": "2 days ago",
        "teacher_notes": "Improving. Needs reinforcement on electric energy consumption calculation (kWh)."
    },
    {
        "id": "STU126",
        "name": "Ishita Saxena",
        "section": "10-B",
        "roll_no": 11,
        "diagnostic_score": 4,
        "overall_score": 81,
        "concept_mastery": {
            "light_refl_refr": 84,
            "electricity_circuits": 79,
            "heating_power": 82,
            "magnetic_effects": 76,
            "human_eye": 85
        },
        "weak_concepts": [],
        "risk_category": "High Achiever",
        "attendance_pct": 95,
        "questions_attempted": 33,
        "practice_accuracy_pct": 82,
        "last_active": "Today, 01:40 PM",
        "teacher_notes": "Strong grasp of theory. Practice more numericals on lens power."
    },
    {
        "id": "STU127",
        "name": "Varun Chopra",
        "section": "10-B",
        "roll_no": 12,
        "diagnostic_score": 3,
        "overall_score": 65,
        "concept_mastery": {
            "light_refl_refr": 68,
            "electricity_circuits": 61,
            "heating_power": 60,
            "magnetic_effects": 63,
            "human_eye": 73
        },
        "weak_concepts": [],
        "risk_category": "Moderate",
        "attendance_pct": 89,
        "questions_attempted": 24,
        "practice_accuracy_pct": 66,
        "last_active": "Yesterday",
        "teacher_notes": "Good effort. Keep up daily revision schedule."
    },
    {
        "id": "STU128",
        "name": "Simran Gill",
        "section": "10-B",
        "roll_no": 13,
        "diagnostic_score": 1,
        "overall_score": 44,
        "concept_mastery": {
            "light_refl_refr": 42,
            "electricity_circuits": 40,
            "heating_power": 45,
            "magnetic_effects": 44,
            "human_eye": 49
        },
        "weak_concepts": ["light_refl_refr", "electricity_circuits", "heating_power", "magnetic_effects", "human_eye"],
        "risk_category": "High Risk",
        "attendance_pct": 77,
        "questions_attempted": 15,
        "practice_accuracy_pct": 41,
        "last_active": "3 days ago",
        "teacher_notes": "Struggles with question comprehension. Assign foundation level practice questions."
    },
    {
        "id": "STU129",
        "name": "Yash Mehra",
        "section": "10-B",
        "roll_no": 14,
        "diagnostic_score": 4,
        "overall_score": 87,
        "concept_mastery": {
            "light_refl_refr": 88,
            "electricity_circuits": 85,
            "heating_power": 89,
            "magnetic_effects": 82,
            "human_eye": 91
        },
        "weak_concepts": [],
        "risk_category": "High Achiever",
        "attendance_pct": 96,
        "questions_attempted": 38,
        "practice_accuracy_pct": 88,
        "last_active": "Today, 10:40 AM",
        "teacher_notes": "Very sharp problem solving. Rapid responses in voice challenges."
    },
    {
        "id": "STU130",
        "name": "Tanya Bose",
        "section": "10-B",
        "roll_no": 15,
        "diagnostic_score": 3,
        "overall_score": 73,
        "concept_mastery": {
            "light_refl_refr": 76,
            "electricity_circuits": 68,
            "heating_power": 72,
            "magnetic_effects": 70,
            "human_eye": 79
        },
        "weak_concepts": [],
        "risk_category": "Moderate",
        "attendance_pct": 93,
        "questions_attempted": 31,
        "practice_accuracy_pct": 74,
        "last_active": "Today, 02:00 PM",
        "teacher_notes": "Well balanced in theory and formulas. Ready to advance to hard tier."
    }
]

def get_class_summary_metrics(section_filter="All"):
    """Calculate aggregate analytics for the class/section."""
    students = STUDENT_ROSTER
    if section_filter in ["10-A", "10-B"]:
        students = [s for s in students if s["section"] == section_filter]

    total_students = len(students)
    if total_students == 0:
        return {}

    avg_overall = sum(s["overall_score"] for s in students) / total_students
    avg_diag = sum(s["diagnostic_score"] for s in students) / total_students
    avg_attendance = sum(s["attendance_pct"] for s in students) / total_students

    # Risk breakdown
    high_risk = sum(1 for s in students if s["risk_category"] == "High Risk")
    moderate = sum(1 for s in students if s["risk_category"] == "Moderate")
    high_achiever = sum(1 for s in students if s["risk_category"] == "High Achiever")

    # Concept-wise class average
    concept_averages = {}
    for c in CONCEPTS:
        cid = c["id"]
        c_avg = sum(s["concept_mastery"].get(cid, 0) for s in students) / total_students
        concept_averages[cid] = round(c_avg, 1)

    # Hardest concept
    hardest_cid = min(concept_averages, key=concept_averages.get)
    hardest_cname = next(c["name"] for c in CONCEPTS if c["id"] == hardest_cid)

    return {
        "total_students": total_students,
        "avg_overall_score": round(avg_overall, 1),
        "avg_diagnostic_score": round(avg_diag, 2),
        "avg_attendance": round(avg_attendance, 1),
        "high_risk_count": high_risk,
        "moderate_count": moderate,
        "high_achiever_count": high_achiever,
        "concept_averages": concept_averages,
        "hardest_concept_id": hardest_cid,
        "hardest_concept_name": hardest_cname,
        "hardest_concept_avg": concept_averages[hardest_cid]
    }
