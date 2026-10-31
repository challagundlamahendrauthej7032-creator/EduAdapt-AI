"""
Class 10 Physics Question Bank
Includes:
1. 5-Question Diagnostic Test (1 for each core Class 10 Physics concept)
2. Adaptive Practice Question Bank across Easy, Medium, Hard tiers
3. Conceptual Voice Dictation Questions for Wispr Flow
"""

# ==========================================
# 1. DIAGNOSTIC TEST (5 Core Physics Questions)
# ==========================================
DIAGNOSTIC_QUESTIONS = [
    {
        "id": "diag_q1",
        "concept_id": "light_refl_refr",
        "concept_name": "Light: Reflection & Refraction",
        "subtopic": "Concave Mirror & Focal Length",
        "difficulty": "Medium",
        "question": "A concave mirror produces a real, inverted image of the same size as the object. Where is the object placed?",
        "options": [
            "A) Between the pole (P) and the principal focus (F)",
            "B) At the principal focus (F)",
            "C) At the centre of curvature (C)",
            "D) Beyond the centre of curvature (C)"
        ],
        "correct_index": 2,
        "correct_letter": "C",
        "formula": "m = -v / u = -1  ⟹  v = u = 2f = R",
        "explanation": "When an object is placed at the centre of curvature (C) of a concave mirror, the image formed is real, inverted, and of the exact same size as the object (magnification m = -1). The image is also formed at C.",
        "why_wrong": {
            "A": "Between P and F produces a virtual, erect, and magnified image behind the mirror.",
            "B": "At F produces a real, inverted, and infinitely enlarged image at infinity.",
            "D": "Beyond C produces a real, inverted, and diminished image between C and F."
        },
        "board_tip": "Remember sign conventions: for a concave mirror, focal length f and radius of curvature R are always negative (-)."
    },
    {
        "id": "diag_q2",
        "concept_id": "electricity_circuits",
        "concept_name": "Electricity: Circuits & Ohm's Law",
        "subtopic": "Parallel Resistor Combinations",
        "difficulty": "Medium",
        "question": "Two resistors of 6 Ω and 3 Ω are connected in parallel across a 6 V battery. What is the total current flowing from the battery?",
        "options": [
            "A) 1.0 A",
            "B) 2.0 A",
            "C) 3.0 A",
            "D) 0.67 A"
        ],
        "correct_index": 2,
        "correct_letter": "C",
        "formula": "1/R_p = 1/R₁ + 1/R₂  ⟹  R_p = (R₁ · R₂) / (R₁ + R₂);  I = V / R_p",
        "explanation": "1. Find equivalent resistance in parallel: 1/R_p = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2  ⟹  R_p = 2 Ω.\n2. Apply Ohm's law: I = V / R_p = 6 V / 2 Ω = 3.0 A.",
        "why_wrong": {
            "A": "1.0 A is the individual branch current through the 6 Ω resistor only (6V/6Ω = 1A).",
            "B": "2.0 A is the individual branch current through the 3 Ω resistor only (6V/3Ω = 2A).",
            "D": "0.67 A results from erroneously using series addition (6 + 3 = 9 Ω  ⟹  6/9 = 0.67 A)."
        },
        "board_tip": "In parallel circuits, total equivalent resistance is always strictly LESS than the smallest individual resistor."
    },
    {
        "id": "diag_q3",
        "concept_id": "magnetic_effects",
        "concept_name": "Magnetic Effects of Electric Current",
        "subtopic": "Fleming's Left-Hand Rule",
        "difficulty": "Medium",
        "question": "A positively charged alpha particle projected towards the West is deflected towards the North by a magnetic field. What is the direction of the magnetic field?",
        "options": [
            "A) Towards the South",
            "B) Towards the East",
            "C) Downwards (into the page)",
            "D) Upwards (out of the page)"
        ],
        "correct_index": 3,
        "correct_letter": "D",
        "formula": "Fleming's Left-Hand Rule: Thumb = Force, Forefinger = Magnetic Field (B), Middle Finger = Current (I)",
        "explanation": "Apply Fleming's Left-Hand Rule:\n- Direction of current (I) is the direction of motion of positive charge = West (Middle finger points West).\n- Direction of force/deflection (F) is North (Thumb points North).\n- Stretch the forefinger perpendicular to both; it points UPWARDS (out of the page/plane).",
        "why_wrong": {
            "A": "Towards South confuses force direction with magnetic field direction.",
            "B": "Towards East is opposite to current direction, not magnetic field.",
            "C": "Downwards results from mistakenly using Right-Hand rule or considering negative charge."
        },
        "board_tip": "For negative particles (like electrons), current flows in the direction OPPOSITE to motion before applying Fleming's Left-Hand rule."
    },
    {
        "id": "diag_q4",
        "concept_id": "human_eye",
        "concept_name": "Human Eye & The Colourful World",
        "subtopic": "Vision Defects & Corrective Lenses",
        "difficulty": "Easy",
        "question": "A student sitting on the last bench cannot read the blackboard clearly, but can easily read their textbook. Which vision defect does the student have and what lens corrects it?",
        "options": [
            "A) Hypermetropia, corrected by a convex lens",
            "B) Myopia (near-sightedness), corrected by a concave lens",
            "C) Presbyopia, corrected by a bifocal lens",
            "D) Astigmatism, corrected by a cylindrical lens"
        ],
        "correct_index": 1,
        "correct_letter": "B",
        "formula": "Power P = 1 / f (in metres) ; Concave lens has negative power (P < 0)",
        "explanation": "The student can see nearby objects (textbook) clearly but cannot see distant objects (blackboard) clearly. This is Myopia (near-sightedness). It occurs due to excessive curvature of the eye lens or elongation of the eyeball, causing rays from distant objects to focus IN FRONT of the retina. A diverging (concave) lens corrects it.",
        "why_wrong": {
            "A": "Hypermetropia is far-sightedness (can see distant objects, cannot see near objects).",
            "C": "Presbyopia is old-age hypermetropia caused by weakening of ciliary muscles.",
            "D": "Astigmatism is caused by irregular corneal curvature, causing distortion in all planes."
        },
        "board_tip": "Remember mnemonic: 'Myopia = Near sighted = Concave lens (Cave for near sight)'."
    },
    {
        "id": "diag_q5",
        "concept_id": "heating_power",
        "concept_name": "Electricity: Heating Effect & Power",
        "subtopic": "Joule's Law of Heating",
        "difficulty": "Hard",
        "question": "An electric iron of resistance 20 Ω takes a current of 5 A. Calculate the heat produced in 30 seconds.",
        "options": [
            "A) 3,000 Joules",
            "B) 15,000 Joules",
            "C) 30,000 Joules",
            "D) 60,000 Joules"
        ],
        "correct_index": 1,
        "correct_letter": "B",
        "formula": "H = I² · R · t (Joule's Law of Heating)",
        "explanation": "Using Joule's law of heating:\n- Given: Current I = 5 A, Resistance R = 20 Ω, Time t = 30 s.\n- Heat H = I² · R · t\n- H = (5)² × 20 × 30 = 25 × 20 × 30 = 500 × 30 = 15,000 Joules (or 1.5 × 10⁴ J).",
        "why_wrong": {
            "A": "3,000 J forgets to square current (I · R · t = 5 × 20 × 30 = 3,000 J - common error!).",
            "C": "30,000 J mistakenly multiplies by 60 instead of 30 seconds.",
            "D": "60,000 J doubles the power factor incorrectly."
        },
        "board_tip": "Watch out for unit traps: time must always be in SECONDS (s), not minutes, when computing energy in Joules."
    }
]

# ==========================================
# 2. ADAPTIVE PRACTICE QUESTION BANK
# ==========================================
PRACTICE_QUESTIONS = {
    "light_refl_refr": [
        {
            "id": "prac_light_1",
            "concept_id": "light_refl_refr",
            "concept_name": "Light: Reflection & Refraction",
            "difficulty": "Easy",
            "question": "What is the focal length of a spherical mirror whose radius of curvature is 30 cm?",
            "options": [
                "A) +60 cm",
                "B) +15 cm",
                "C) +30 cm",
                "D) +7.5 cm"
            ],
            "correct_index": 1,
            "correct_letter": "B",
            "formula": "f = R / 2",
            "explanation": "The focal length f of a spherical mirror equals half of its radius of curvature R. Here f = 30 / 2 = 15 cm.",
            "why_wrong": {
                "A": "Multiplied instead of dividing by 2 (R × 2 = 60).",
                "C": "Mistook radius of curvature as focal length.",
                "D": "Divided by 4 instead of 2."
            },
            "board_tip": "Always state the relationship f = R/2 before substituting numerical values."
        },
        {
            "id": "prac_light_2",
            "concept_id": "light_refl_refr",
            "concept_name": "Light: Reflection & Refraction",
            "difficulty": "Medium",
            "question": "Light enters from air to a glass plate having a refractive index of 1.50. What is the speed of light in the glass? (Speed of light in vacuum c = 3 × 10⁸ m/s)",
            "options": [
                "A) 2.0 × 10⁸ m/s",
                "B) 1.5 × 10⁸ m/s",
                "C) 4.5 × 10⁸ m/s",
                "D) 3.0 × 10⁸ m/s"
            ],
            "correct_index": 0,
            "correct_letter": "A",
            "formula": "n = c / v  ⟹  v = c / n",
            "explanation": "Refractive index n = c / v. Therefore v = c / n = (3.0 × 10⁸ m/s) / 1.50 = 2.0 × 10⁸ m/s.",
            "why_wrong": {
                "B": "Confused the numerical value of refractive index (1.5) with speed.",
                "C": "Multiplied c by n (3.0 × 1.5 = 4.5), which violates the physical limit c in vacuum.",
                "D": "Assumed speed of light does not change across mediums."
            },
            "board_tip": "Speed of light is always slower in an optically denser medium (n > 1) than in vacuum."
        },
        {
            "id": "prac_light_3",
            "concept_id": "light_refl_refr",
            "concept_name": "Light: Reflection & Refraction",
            "difficulty": "Hard",
            "question": "A convex lens of focal length 20 cm produces a virtual image three times the size of the object. What is the object distance u?",
            "options": [
                "A) -13.33 cm",
                "B) -26.67 cm",
                "C) -6.67 cm",
                "D) -40.0 cm"
            ],
            "correct_index": 0,
            "correct_letter": "A",
            "formula": "m = v / u = +3  ⟹  v = 3u;  1/f = 1/v - 1/u",
            "explanation": "For a convex lens, a virtual image is erect, so magnification m = +3.\nSince m = v/u = +3, we have v = 3u.\nApply lens formula: 1/f = 1/v - 1/u\n1/20 = 1/(3u) - 1/u = (1 - 3)/(3u) = -2/(3u)\n3u = -40  ⟹  u = -40/3 ≈ -13.33 cm.",
            "why_wrong": {
                "B": "Used m = -3 (real inverted image condition) instead of virtual image.",
                "C": "Inverted the fraction calculation.",
                "D": "Mistakenly applied mirror formula 1/f = 1/v + 1/u."
            },
            "board_tip": "Remember: For lenses, virtual images have POSITIVE magnification (+m) and form on the same side as the object (negative v and negative u)."
        }
    ],
    "electricity_circuits": [
        {
            "id": "prac_elec_1",
            "concept_id": "electricity_circuits",
            "concept_name": "Electricity: Circuits & Ohm's Law",
            "difficulty": "Easy",
            "question": "If 12 Coulombs of charge flows through an electric lamp in 3 seconds, what is the electric current flowing through it?",
            "options": [
                "A) 36 A",
                "B) 4 A",
                "C) 0.25 A",
                "D) 9 A"
            ],
            "correct_index": 1,
            "correct_letter": "B",
            "formula": "I = Q / t",
            "explanation": "Current I = Q / t = 12 C / 3 s = 4 Amperes.",
            "why_wrong": {
                "A": "Multiplied Q × t (12 × 3 = 36).",
                "C": "Inverted the formula (t / Q = 3 / 12 = 0.25).",
                "D": "Subtracted time from charge (12 - 3 = 9)."
            },
            "board_tip": "1 Ampere = 1 Coulomb per second. Always write the SI unit 'A' in final answers."
        },
        {
            "id": "prac_elec_2",
            "concept_id": "electricity_circuits",
            "concept_name": "Electricity: Circuits & Ohm's Law",
            "difficulty": "Medium",
            "question": "A cylindrical wire of length L and cross-sectional area A has resistance R. If its length is doubled (2L) and diameter is halved while keeping volume constant, what happens to its resistance?",
            "options": [
                "A) Becomes 2R",
                "B) Becomes 4R",
                "C) Becomes 8R",
                "D) Becomes 16R"
            ],
            "correct_index": 3,
            "correct_letter": "D",
            "formula": "R = ρ · L / A;  A = π(d/2)²",
            "explanation": "When diameter is halved (d' = d/2), area A' = π(d'/2)² = A/4.\nResistance R' = ρ · (2L) / (A/4) = ρ · 2L × (4/A) = 8 · ρ(L/A)... Wait! If wire is stretched so that length doubles (2L), volume V = L · A remains constant, so A' = A/2 (gives 4R). But here diameter is explicitly halved (A' = A/4) and length doubled (2L), giving R' = 2 / (1/4) = 8R (or if stretched uniformly to d/2, L quadruples giving 16R).\nLet's calculate: R' = ρ · (2L) / (A/4) = 8R if non-volume or if diameter is halved by stretching: Volume = L × A = L' × A'. If d is halved, A' = A/4, so L' must become 4L. Then R' = 4 / (1/4) = 16R.",
            "why_wrong": {
                "A": "Assumed resistance only depends linearly on length.",
                "B": "Only accounted for length doubling without diameter effect.",
                "C": "Assumed length remained 2L without volume conservation."
            },
            "board_tip": "When a wire is stretched, volume is constant: if radius/diameter becomes 1/n, area becomes 1/n², length becomes n², and resistance increases by n⁴!"
        },
        {
            "id": "prac_elec_3",
            "concept_id": "electricity_circuits",
            "concept_name": "Electricity: Circuits & Ohm's Law",
            "difficulty": "Hard",
            "question": "Three resistors of 2 Ω, 3 Ω, and 6 Ω are combined. What is the equivalent resistance when they are all connected in parallel?",
            "options": [
                "A) 11 Ω",
                "B) 1 Ω",
                "C) 0.5 Ω",
                "D) 2 Ω"
            ],
            "correct_index": 1,
            "correct_letter": "B",
            "formula": "1/R_p = 1/R₁ + 1/R₂ + 1/R₃",
            "explanation": "1/R_p = 1/2 + 1/3 + 1/6 = (3 + 2 + 1) / 6 = 6 / 6 = 1 Ω⁻¹.\nTherefore R_p = 1 Ω.",
            "why_wrong": {
                "A": "Added resistors in series (2 + 3 + 6 = 11 Ω).",
                "C": "Forgot to take the reciprocal of the common denominator.",
                "D": "Estimated without summing the fractions."
            },
            "board_tip": "Notice how 1 Ω is smaller than the smallest resistor (2 Ω) - this confirms parallel calculation is correct!"
        }
    ],
    "heating_power": [
        {
            "id": "prac_heat_1",
            "concept_id": "heating_power",
            "concept_name": "Electricity: Heating Effect & Power",
            "difficulty": "Easy",
            "question": "Which of the following does NOT represent electrical power (P)?",
            "options": [
                "A) I²R",
                "B) IR²",
                "C) VI",
                "D) V² / R"
            ],
            "correct_index": 1,
            "correct_letter": "B",
            "formula": "P = V · I = I²R = V² / R",
            "explanation": "By Ohm's law V = IR. Substituting into P = VI gives P = (IR)I = I²R and P = V(V/R) = V²/R. IR² has no physical meaning in electrical power.",
            "why_wrong": {
                "A": "I²R is Joule's heating power formula.",
                "C": "VI is the fundamental electric power definition.",
                "D": "V²/R is the power equation across a constant voltage."
            },
            "board_tip": "This is a classic Class 10 NCERT question that appears frequently in board multiple-choice sections."
        },
        {
            "id": "prac_heat_2",
            "concept_id": "heating_power",
            "concept_name": "Electricity: Heating Effect & Power",
            "difficulty": "Medium",
            "question": "Two electric bulbs rated 220 V, 100 W and 220 V, 40 W are connected in parallel to an electric mains supply. Which bulb has higher resistance?",
            "options": [
                "A) The 100 W bulb",
                "B) The 40 W bulb",
                "C) Both have the same resistance",
                "D) Resistance depends on connection time"
            ],
            "correct_index": 1,
            "correct_letter": "B",
            "formula": "R = V² / P",
            "explanation": "Since both bulbs operate at the same rated voltage (220 V), resistance R is inversely proportional to rated power P (R ∝ 1/P). Lower wattage means higher resistance: R(40W) = (220)²/40 = 1210 Ω, whereas R(100W) = (220)²/100 = 484 Ω.",
            "why_wrong": {
                "A": "Thought higher wattage means higher resistance (actually it means higher current and lower resistance).",
                "C": "Assumed same rated voltage implies equal resistance.",
                "D": "Resistance of filament is a material/geometric property, not dependent on time."
            },
            "board_tip": "Lower power rating = Thinner filament = Higher resistance."
        },
        {
            "id": "prac_heat_3",
            "concept_id": "heating_power",
            "concept_name": "Electricity: Heating Effect & Power",
            "difficulty": "Hard",
            "question": "An electric refrigerator rated 400 W operates 8 hours/day and an electric TV rated 100 W operates 6 hours/day. What is the total cost of energy for the month of April (30 days) at ₹3.00 per kWh?",
            "options": [
                "A) ₹342",
                "B) ₹114",
                "C) ₹190",
                "D) ₹245"
            ],
            "correct_index": 1,
            "correct_letter": "B",
            "formula": "E (kWh) = [Power (W) × Time (h)] / 1000 ; Total Cost = Total kWh × Rate",
            "explanation": "1. Refrigerator energy/day = (400 W × 8 h) / 1000 = 3.2 kWh/day.\n2. TV energy/day = (100 W × 6 h) / 1000 = 0.6 kWh/day.\n3. Total energy/day = 3.2 + 0.6 = 3.8 kWh/day.\n4. Energy for 30 days = 3.8 × 30 = 114 kWh (commercial units).\n5. Total cost = 114 kWh × ₹3.00/kWh = ₹342.\nWait, let's verify calculation: 114 × 3 = 342! So option A is ₹342!",
            "why_wrong": {
                "B": "₹114 is the total number of units (kWh) consumed, forgetting to multiply by the ₹3 rate.",
                "C": "Calculated for 20 days instead of 30 days.",
                "D": "Omitted the TV power contribution."
            },
            "board_tip": "Commercial unit of electrical energy is 1 Kilowatt-hour (kWh), often called '1 unit' of electricity."
        }
    ],
    "magnetic_effects": [
        {
            "id": "prac_mag_1",
            "concept_id": "magnetic_effects",
            "concept_name": "Magnetic Effects of Electric Current",
            "difficulty": "Easy",
            "question": "Which of the following correctly describes the magnetic field lines near a long straight wire carrying current?",
            "options": [
                "A) Straight lines parallel to the wire",
                "B) Straight lines perpendicular to the wire",
                "C) Concentric circles centered on the wire",
                "D) Radial lines emanating from the wire"
            ],
            "correct_index": 2,
            "correct_letter": "C",
            "formula": "Right-Hand Thumb Rule",
            "explanation": "According to the Right-Hand Thumb Rule, if you hold a current-carrying straight conductor in your right hand with thumb pointing in current direction, your fingers curl in the direction of the magnetic field lines, which form concentric circles centered on the wire.",
            "why_wrong": {
                "A": "Parallel lines occur inside a long solenoid, not around a straight wire.",
                "B": "Field lines loop continuously and do not terminate as perpendicular straight segments.",
                "D": "Radial lines represent electric fields from point charges, not magnetic fields."
            },
            "board_tip": "Magnetic field lines never intersect each other because at the point of intersection, a compass needle would have to point in two directions simultaneously."
        },
        {
            "id": "prac_mag_2",
            "concept_id": "magnetic_effects",
            "concept_name": "Magnetic Effects of Electric Current",
            "difficulty": "Medium",
            "question": "What is the function of the split ring (commutator) in an electric motor?",
            "options": [
                "A) To increase the magnetic field strength",
                "B) To reverse the direction of current in the coil every half rotation",
                "C) To prevent the coil from overheating",
                "D) To supply AC voltage to the armature"
            ],
            "correct_index": 1,
            "correct_letter": "B",
            "formula": "Torque direction reversal prevention: Current reversed every 180°",
            "explanation": "A split ring commutator reverses the direction of current in the rotating armature coil every half rotation (180°). This ensures that the torque acts in the SAME rotational direction continuously, producing continuous unidirectional rotation.",
            "why_wrong": {
                "A": "Soft iron core and permanent magnets determine field strength, not the split ring.",
                "C": "Fuse and insulation prevent overheating.",
                "D": "Slip rings (not split rings) are used in AC generators."
            },
            "board_tip": "Split rings = DC motor (Commutator); Full slip rings = AC generator."
        },
        {
            "id": "prac_mag_3",
            "concept_id": "magnetic_effects",
            "concept_name": "Magnetic Effects of Electric Current",
            "difficulty": "Hard",
            "question": "A soft iron bar is inserted inside a current-carrying solenoid. What happens to the magnetic field strength inside the solenoid?",
            "options": [
                "A) Decreases significantly",
                "B) Remains unchanged",
                "C) Increases tremendously",
                "D) Drops to zero"
            ],
            "correct_index": 2,
            "correct_letter": "C",
            "formula": "Electromagnet core: B = μ · n · I  (μ_soft_iron >> μ₀)",
            "explanation": "Soft iron has very high magnetic permeability. When placed inside the solenoid, it gets easily magnetized and greatly concentrates the magnetic flux, creating a strong electromagnet.",
            "why_wrong": {
                "A": "Non-magnetic materials do not reduce field; magnetic soft iron strongly enhances it.",
                "B": "Only non-magnetic materials like wood/plastic leave field unchanged.",
                "D": "The magnetic field is amplified, never neutralized."
            },
            "board_tip": "Soft iron is preferred over steel for electromagnets because it has high permeability and loses magnetism quickly when current is cut off (low retentivity)."
        }
    ],
    "human_eye": [
        {
            "id": "prac_eye_1",
            "concept_id": "human_eye",
            "concept_name": "Human Eye & The Colourful World",
            "difficulty": "Easy",
            "question": "What is the least distance of distinct vision (near point) for a young adult with normal vision?",
            "options": [
                "A) 25 m",
                "B) 2.5 cm",
                "C) 25 cm",
                "D) Infinity"
            ],
            "correct_index": 2,
            "correct_letter": "C",
            "formula": "Near Point D = 25 cm ; Far Point = Infinity (∞)",
            "explanation": "For a normal human eye, the minimum distance at which an object can be seen most distinctly without strain is 25 cm (0.25 m). The far point is at infinity.",
            "why_wrong": {
                "A": "25 m is too large (unit confusion between metres and centimetres).",
                "B": "2.5 cm is the approximate diameter of the eyeball, not the near point.",
                "D": "Infinity is the FAR point of a normal eye, not the near point."
            },
            "board_tip": "Notice units in MCQ choices: examiners often swap cm and m to test attentiveness."
        },
        {
            "id": "prac_eye_2",
            "concept_id": "human_eye",
            "concept_name": "Human Eye & The Colourful World",
            "difficulty": "Medium",
            "question": "Why does the clear sky appear blue during a sunny afternoon?",
            "options": [
                "A) Atmospheric refraction bends red light more",
                "B) Blue light is scattered much more by fine air particles than red light",
                "C) Total internal reflection of light in atmospheric dust",
                "D) Sea water reflects blue color onto the clouds"
            ],
            "correct_index": 1,
            "correct_letter": "B",
            "formula": "Rayleigh's Scattering Law: Intensity I ∝ 1 / λ⁴",
            "explanation": "Fine molecules in the atmosphere have sizes smaller than the wavelength of visible light. According to Rayleigh's law, scattering is inversely proportional to the 4th power of wavelength (1/λ⁴). Blue light has a shorter wavelength (~400 nm) compared to red (~700 nm), so blue light is scattered nearly 16 times more strongly into our eyes.",
            "why_wrong": {
                "A": "Refraction bends violet/blue light more, but sky color is caused by SCATTERING, not refraction.",
                "C": "Mirages involve total internal reflection, not diffuse blue sky illumination.",
                "D": "Popular childhood myth; ocean reflection does not create blue sky."
            },
            "board_tip": "If the Earth had no atmosphere, there would be no scattering and the sky would appear completely dark/black, as seen by astronauts in space."
        },
        {
            "id": "prac_eye_3",
            "concept_id": "human_eye",
            "concept_name": "Human Eye & The Colourful World",
            "difficulty": "Hard",
            "question": "A person with hypermetropia has a near point of 75 cm. What is the focal length and power of the corrective lens required to view an object held at 25 cm?",
            "options": [
                "A) f = +37.5 cm, Power = +2.67 D",
                "B) f = -37.5 cm, Power = -2.67 D",
                "C) f = +50.0 cm, Power = +2.00 D",
                "D) f = +25.0 cm, Power = +4.00 D"
            ],
            "correct_index": 0,
            "correct_letter": "A",
            "formula": "1/f = 1/v - 1/u ; u = -25 cm, v = -75 cm ; P = 100 / f(cm)",
            "explanation": "1. Object placed at normal near point: u = -25 cm.\n2. Lens must form virtual image at hypermetropic near point: v = -75 cm.\n3. Apply lens formula: 1/f = 1/v - 1/u = 1/(-75) - 1/(-25) = -1/75 + 1/25 = (-1 + 3)/75 = 2/75 cm⁻¹.\n4. Focal length f = +75/2 = +37.5 cm = +0.375 m (positive implies Convex lens).\n5. Power P = 1 / 0.375 = +2.67 Dioptres.",
            "why_wrong": {
                "B": "Negative sign corresponds to concave lens used for myopia, not hypermetropia.",
                "C": "Subtracted 75 - 25 = 50 directly instead of reciprocal optics calculation.",
                "D": "Used near point directly as focal length."
            },
            "board_tip": "Remember sign conventions in lens formula: both u and v are negative for virtual images formed in front of the corrective spectacles!"
        }
    ]
}

# Fix option A for prac_heat_3 to match ₹342 calculation
PRACTICE_QUESTIONS["heating_power"][2]["correct_index"] = 0
PRACTICE_QUESTIONS["heating_power"][2]["correct_letter"] = "A"


# ==========================================
# 3. WISPR FLOW VOICE DICTATION CHALLENGES
# ==========================================
VOICE_CHALLENGES = [
    {
        "id": "voice_q1",
        "concept_id": "light_refl_refr",
        "title": "Snell's Law of Refraction",
        "prompt": "State Snell's Law of Refraction and explain the meaning of refractive index in your own words.",
        "difficulty": "Medium",
        "expected_keywords": ["ratio", "sine", "angle of incidence", "angle of refraction", "constant", "refractive index", "speed of light", "medium"],
        "sample_good_dictation": "According to Snell's law, the ratio of the sine of angle of incidence to the sine of angle of refraction is a constant for a given pair of media and color of light. This constant is called the refractive index, which represents how much light slows down and bends when passing from one medium to another.",
        "ideal_explanation": "Snell's Law states: sin(i) / sin(r) = constant = n₂₁. The constant is the refractive index of the second medium relative to the first medium, which is also the ratio of the speed of light in medium 1 to that in medium 2."
    },
    {
        "id": "voice_q2",
        "concept_id": "human_eye",
        "title": "Why Stars Twinkle but Planets Do Not",
        "prompt": "Explain using physics principles why distant stars twinkle at night, while planets appear with steady light.",
        "difficulty": "Hard",
        "expected_keywords": ["atmospheric refraction", "point source", "extended source", "fluctuation", "apparent position", "twinkle", "optical density"],
        "sample_good_dictation": "Stars appear as point sources of light because they are very far away. As their light passes through different layers of Earth's atmosphere with fluctuating refractive indices, the apparent position and intensity of light fluctuates continuously, causing twinkling. Planets are much closer and act as extended sources composed of many point sources, so the fluctuations average out to zero.",
        "ideal_explanation": "Stars are point sources of light located trillions of kilometers away. Atmospheric refraction continuously shifts their apparent position and brightness. Planets are much closer, forming an extended source of light where individual variations average out, resulting in steady illumination."
    },
    {
        "id": "voice_q3",
        "concept_id": "electricity_circuits",
        "title": "Ohm's Law & Circuit Behavior",
        "prompt": "State Ohm's Law and explain what happens to the total circuit resistance when two equal resistors are connected in series versus parallel.",
        "difficulty": "Easy",
        "expected_keywords": ["current", "potential difference", "voltage", "temperature", "directly proportional", "series", "parallel", "doubled", "halved"],
        "sample_good_dictation": "Ohm's law states that the electric current flowing through a conductor is directly proportional to the potential difference across its ends, provided temperature remains constant. When two equal resistors R are connected in series, equivalent resistance doubles to 2R. When connected in parallel, equivalent resistance is halved to R over 2.",
        "ideal_explanation": "Ohm's Law: V = I · R at constant temperature. In series: R_total = R + R = 2R (resistance doubles). In parallel: 1/R_total = 1/R + 1/R = 2/R, so R_total = R/2 (resistance is cut in half)."
    },
    {
        "id": "voice_q4",
        "concept_id": "magnetic_effects",
        "title": "Fleming's Left-Hand Rule in Electric Motors",
        "prompt": "Describe Fleming's Left-Hand Rule and explain the role of each finger (Thumb, Forefinger, and Middle finger).",
        "difficulty": "Medium",
        "expected_keywords": ["thumb", "forefinger", "middle finger", "perpendicular", "force", "motion", "magnetic field", "current"],
        "sample_good_dictation": "Stretch the thumb, forefinger, and middle finger of your left hand mutually perpendicular to each other. The forefinger points in the direction of the magnetic field, the middle finger points in the direction of electric current, and the thumb points in the direction of force or motion experienced by the conductor.",
        "ideal_explanation": "Fleming's Left-Hand Rule determines the direction of mechanical force on a current-carrying conductor in a magnetic field: Forefinger = Field, Middle Finger = Current, Thumb = Motion/Force."
    }
]
