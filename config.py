"""
EduAdapt AI - Configuration & Constants
Target: Class 10 Physics (Adaptive Exam-Prep Tutor with Learner Model)
"""

APP_NAME = "EduAdapt AI"
APP_SUBTITLE = "Adaptive Exam-Prep Tutor with Learner Model • Class 10 Physics"
TARGET_GRADE = "Class 10"
SUBJECT = "Physics"
BOARD_EXAM_DATE = "2026-03-02"  # Target Board Exam date

# Core Class 10 Physics Concepts
CONCEPTS = [
    {
        "id": "light_refl_refr",
        "name": "Light: Reflection & Refraction",
        "short_name": "Light & Optics",
        "icon": "🔦",
        "weight": 25,
        "key_formulas": ["1/f = 1/v + 1/u (Mirror)", "1/f = 1/v - 1/u (Lens)", "n = c/v = sin(i)/sin(r)", "P = 1/f(m)"],
        "description": "Spherical mirrors, ray tracing, lens formula, magnification, and refractive index."
    },
    {
        "id": "electricity_circuits",
        "name": "Electricity: Circuits & Ohm's Law",
        "short_name": "Circuits & Resistance",
        "icon": "⚡",
        "weight": 25,
        "key_formulas": ["V = I · R", "R_series = R1 + R2 + ...", "1/R_parallel = 1/R1 + 1/R2", "R = ρ(L/A)"],
        "description": "Electric current, potential difference, Ohm's law, and series/parallel resistor combinations."
    },
    {
        "id": "heating_power",
        "name": "Electricity: Heating Effect & Power",
        "short_name": "Joule Heating & Power",
        "icon": "🔥",
        "weight": 15,
        "key_formulas": ["H = I² · R · t", "P = V · I = I²R = V²/R", "1 kWh = 3.6 × 10⁶ J"],
        "description": "Joule's law of heating, electric power, and commercial electric energy consumption."
    },
    {
        "id": "magnetic_effects",
        "name": "Magnetic Effects of Electric Current",
        "short_name": "Magnetism & Induction",
        "icon": "🧲",
        "weight": 20,
        "key_formulas": ["Fleming's Left-Hand Rule (Motor)", "Right-Hand Thumb Rule", "B ∝ n · I (Solenoid)"],
        "description": "Magnetic fields around conductors, solenoids, Fleming's rules, and electromagnetic induction."
    },
    {
        "id": "human_eye",
        "name": "Human Eye & The Colourful World",
        "short_name": "Human Eye & Optics",
        "icon": "👁️",
        "weight": 15,
        "key_formulas": ["Myopia: Concave Lens", "Hypermetropia: Convex Lens", "Rayleigh Scattering ∝ 1/λ⁴"],
        "description": "Vision defects (myopia, hypermetropia), prism dispersion, atmospheric refraction, and scattering."
    }
]

CONCEPT_MAP = {c["id"]: c for c in CONCEPTS}

# Mastery Thresholds
MASTERY_THRESHOLDS = {
    "mastered": 80,    # >= 80%
    "developing": 55,  # 55% - 79%
    "weak": 0          # < 55%
}

MASTERY_COLORS = {
    "Mastered": "#10b981",    # Emerald green
    "Developing": "#f59e0b",  # Amber
    "Needs Focus": "#ef4444"  # Red
}
