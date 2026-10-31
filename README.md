# ⚛️ EduAdapt AI — Adaptive Exam-Prep Tutor with a Learner Model

> **Target Audience:** Class 10 Physics (CBSE / ICSE / State Boards)  
> **Tech Stack:** Python 3.10+, Streamlit, Altair, Pandas, Web Speech API (Wispr Flow Voice Dictation)

---

## 📌 Problem Statement & Overview
Class 10 Physics is one of the most critical foundational subjects for secondary students, combining abstract theoretical concepts (electromagnetism, ray optics) with mathematical numericals (Ohm's law, lens formula, Joule heating). Traditional exam prep treats all learners identically, ignoring knowledge gaps and forgetting curves.

**EduAdapt AI** solves this with an **Adaptive Learner Model & Knowledge Tracing Engine** that continuously profiles a student's cognitive mastery across Class 10 Physics chapters, diagnoses underlying misconceptions from incorrect choices, generates targeted adaptive practice, schedules spaced repetitions, and allows **voice dictation through Wispr Flow** for verbal concept articulation.

---

## 🌟 Key Features Breakdown

### 1. 🏠 Beautiful Student Dashboard
- **Board Readiness Score**: Dynamic weighted readiness metric based on Class 10 Physics syllabus weightage.
- **CBSE Board Exam Countdown & Study Streak**: Tracks consecutive daily preparation days.
- **Concept Health Overview**: Visual cards for Light & Optics, Circuits, Joule Heating, Magnetism, and Human Eye.
- **Actionable Hub**: Direct navigation to Diagnostic Test, Weak Concept Practice, Revision Planner, and Voice Dictation.

### 2. 📝 Diagnostic Test (5 High-Yield Physics MCQs)
- Covers the 5 core Class 10 Physics chapters:
  1. *Light: Reflection & Refraction* (Concave mirror & focal length)
  2. *Electricity: Circuits & Ohm's Law* (Parallel resistor current calculation)
  3. *Magnetic Effects of Electric Current* (Fleming's Left-Hand Rule)
  4. *Human Eye & The Colourful World* (Myopia defect & concave lens correction)
  5. *Electricity: Heating Effect & Power* (Joule's law numerical calculation)

### 3. 🎯 Score Calculation & In-Depth Results
- Immediate score calculation (Score out of 5, accuracy percentage, proficiency badge).
- Celebratory visual feedback (`st.balloons()` for scores $\ge 80\%$).
- Comprehensive post-test breakdown with instant diagnosis of weak chapters.

### 4. 📊 Concept Mastery Tracking (Learner Model)
- Maintains continuous knowledge tracing ($0\%$ to $100\%$) for every physics topic.
- Dynamic color-coded tiers:
  - 🟢 **Mastered** ($\ge 80\%$)
  - 🟡 **Developing** ($55\% - 79\%$)
  - 🔴 **Needs Focus** ($< 55\%$)
- Visualized using interactive **Altair** charts with a benchmark $80\%$ Board Target Line.

### 5. 🔍 Weak Concept Identification & Misconception Analysis
- Flags any topic where incorrect answers occur or mastery drops below $60\%$.
- Logs specific misconceptions (e.g., *forgetting to square current in $H = I^2Rt$*, *confusing parallel vs series equivalent resistance*, *misinterpreting sign conventions*).

### 6. ⚡ Adaptive Practice Question Generator
- Dynamically generates and filters practice questions tailored to the student's identified weak areas.
- **Calibrated Difficulty Engine**:
  - Automatically recommends **Easy**, **Medium**, or **Hard** questions based on current mastery.
  - Updates concept mastery in real time upon every correct or incorrect submission.

### 7. 📅 Spaced Repetition Revision Schedule
- Based on the **Ebbinghaus Forgetting Curve**:
  - Weak concepts scheduled for **Day 1 (Today)** and **Day 3**.
  - Developing concepts scheduled for **Day 4 - 7**.
  - Mastered concepts scheduled for **Day 10 - 14**.
- Includes functional **"Mark as Revised"** buttons that dynamically boost memory retention and expand review intervals.
- Integrated quick-access **Board Formula Sheet**.

### 8. 👨‍🏫 Teacher Dashboard & Cohort Analytics
- Sample class performance data for **30 Class 10 students** across Sections 10-A and 10-B.
- Cohort average score, diagnostic completion rate, and attendance tracking.
- **Chapter Difficulty Heatmap**: Instantly identifies the bottleneck chapter for the entire class.
- **At-Risk Learner Monitor**: Highlights students requiring remedial intervention ($<50\%$ mastery).
- **Searchable Student Roster & Deep-Dive Profile Drawer**: Inspect any individual student's concept radar, practice accuracy, and personalized teacher notes.

### 9. 🎙️ Wispr Flow Voice Dictation
- **Voice-first answer input** powered by Wispr Flow styling and browser Web Speech API.
- Enables students to practice the **Feynman Technique** by verbally explaining physics concepts out loud.
- **Real-Time Live Dictation**: Transcribes speech directly in browser.
- **Semantic Answer Evaluator**: Analyzes dictated speech for scientific keywords, clarity, and conceptual completeness, returning a score ($0-100\%$) and model board exam answers.
- **Quick Voice Simulation Presets**: Allows 1-click testing of spoken answers even without an active microphone.

### 10. 💡 Useful Feedback After Every Answer
- Displayed immediately after every diagnostic and practice question:
  - Correct / Incorrect status banner.
  - Complete step-by-step mathematical derivation and physical reasoning.
  - **📐 Core Formula Callout**: Highlights the exact equation required.
  - **⚠️ Common Exam Misconceptions**: Explains why distractor choices were wrong.
  - **🎯 Class 10 Board Exam Tip**: High-yield exam advice for scoring full marks.

---

## 📂 Project Architecture

```
EduAdapt_AI/
├── app.py                      # Main Streamlit application entry point & router
├── config.py                   # Class 10 syllabus, concepts, weights & constants
├── requirements.txt            # Project dependencies
├── README.md                   # Complete documentation & run guide
├── .streamlit/
│   └── config.toml             # Streamlit theme & server configuration
├── data/
│   ├── physics_questions.py    # Diagnostic MCQs, practice question bank & voice challenges
│   └── student_data.py         # 30-student cohort dataset for Teacher Dashboard
├── models/
│   └── learner_model.py        # Knowledge tracing engine, mastery updater & scheduler
├── components/
│   ├── ui_helpers.py           # Custom CSS, hero banners, badges & feedback cards
│   ├── charts.py               # Altair interactive charts (bar breakdown, heatmaps, donuts)
│   └── voice_component.py      # Wispr Flow speech recorder & semantic answer evaluator
├── views/
│   ├── student_dashboard.py    # Student KPI overview & concept status
│   ├── diagnostic_test.py      # 5-MCQ diagnostic assessment & results
│   ├── adaptive_practice.py    # Weak concept practice generator & live updater
│   ├── revision_planner.py     # Spaced repetition revision calendar
│   ├── voice_dictation.py      # Wispr Flow voice studio & speech challenge
│   └── teacher_dashboard.py    # Teacher cohort analytics, roster & student deep-dive
└── tests/
    └── test_logic.py           # 7 comprehensive unit tests for core algorithms
```

---

## 🚀 Quickstart Instructions

### 1. Prerequisites
- Python 3.10 or higher installed.

### 2. Install Dependencies
Open a terminal in the project directory and run:
```bash
pip install -r requirements.txt
```

### 3. Run the Web Application
Launch EduAdapt AI using Streamlit:
```bash
streamlit run app.py
```
The application will open in your default browser at:  
👉 **`http://localhost:8501`**

### 4. Run the Unit Test Suite
Verify that all algorithms, scoring, and learner models pass unit tests:
```bash
python -m unittest tests/test_logic.py
```
*(All 7 unit tests pass in 0.001s)*

---

## 🧪 Interactive Walkthrough Guide

1. **Student Dashboard**: Explore current readiness, syllabus status, and study streak.
2. **Diagnostic Test**: Navigate to *Diagnostic Test (5 MCQs)*, solve the 5 Physics questions, and click *Submit Diagnostic Test*. Notice the immediate score calculation, weak concept tagging, and step-by-step feedback with Board tips.
3. **Adaptive Practice**: Navigate to *Adaptive Practice*. Notice that questions are dynamically filtered to your weak concepts with an AI-calibrated difficulty level. Check your answer to watch concept mastery update in real time!
4. **Revision Schedule**: View your Spaced Repetition timeline. Click *Mark as Revised* to boost retention level and watch the interval recalculate.
5. **Wispr Flow Voice Dictation**: Select *Wispr Flow Voice Dictation*. Click *Start Dictating* to speak using your microphone, or click *Simulate: Ideal Verbal Answer* to test the semantic evaluator. Click *Analyze Spoken Answer* to see captured scientific keywords and feedback!
6. **Teacher Dashboard**: Switch to *Teacher Dashboard* in the sidebar. Toggle between Section 10-A and 10-B, inspect the Class Difficulty Heatmap, filter the 30-student roster by risk tier, and select any student for a 1-on-1 performance deep dive.
7. **Reset Demo**: Click *🔄 Reset Demo / Re-baseline* in the sidebar at any point to restart fresh.
