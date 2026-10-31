"""
EduAdapt AI - Learner Model & Knowledge Tracing Engine
Tracks concept mastery, diagnoses misconceptions, adapts question difficulty,
and schedules spaced-repetition revisions.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Any
from config import CONCEPTS, CONCEPT_MAP, MASTERY_THRESHOLDS


class LearnerModel:
    """Manages the student's cognitive state, concept mastery, and revision plan."""

    def __init__(self, student_name: str = "Aarav Sharma"):
        self.student_name = student_name
        self.student_class = "Class 10"
        self.subject = "Physics"
        
        # Diagnostic status
        self.diagnostic_completed = False
        self.diagnostic_score = 0
        self.diagnostic_total = 5
        self.diagnostic_timestamp = None
        self.diagnostic_details = []  # List of dicts for each question

        # Concept Mastery (0 - 100)
        # Default baseline prior to diagnostic is 50% for all concepts
        self.concept_mastery: Dict[str, float] = {
            c["id"]: 50.0 for c in CONCEPTS
        }

        # Concept history: list of {timestamp, delta, new_value, reason}
        self.mastery_history: Dict[str, List[Dict[str, Any]]] = {
            c["id"]: [] for c in CONCEPTS
        }

        # Weak concepts identified (< 60% mastery or failed in diagnostic)
        self.weak_concepts: List[str] = []

        # Misconception log: {concept_id: [misconceptions]}
        self.identified_misconceptions: Dict[str, List[str]] = {
            c["id"]: [] for c in CONCEPTS
        }

        # Practice history
        self.practice_history: List[Dict[str, Any]] = []

        # Voice challenge history
        self.voice_history: List[Dict[str, Any]] = []

        # Revision schedule
        self.revision_schedule: List[Dict[str, Any]] = []

        # General stats
        self.study_streak_days = 4
        self.total_questions_solved = 0
        self.total_correct_count = 0

        # Initialize default baseline revision schedule
        self._generate_initial_schedule()

    def process_diagnostic_results(self, user_answers: Dict[str, int], questions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Evaluate diagnostic test answers, set concept mastery, identify weak concepts,
        and generate a targeted spaced revision schedule.
        """
        score = 0
        details = []
        new_weak_concepts = []

        for q in questions:
            qid = q["id"]
            cid = q["concept_id"]
            selected_idx = user_answers.get(qid, -1)
            is_correct = (selected_idx == q["correct_index"])
            
            if is_correct:
                score += 1
                # Mastery set high for correct diagnostic answer
                self.concept_mastery[cid] = 85.0
            else:
                # Mark as weak concept, set lower mastery
                self.concept_mastery[cid] = 35.0
                if cid not in new_weak_concepts:
                    new_weak_concepts.append(cid)
                
                # Log misconception
                selected_letter = chr(65 + selected_idx) if 0 <= selected_idx < 4 else "None"
                reason = q["why_wrong"].get(selected_letter, "Selected incorrect option.")
                self.identified_misconceptions[cid].append(reason)

            # Record question audit
            details.append({
                "question_id": qid,
                "concept_id": cid,
                "concept_name": q["concept_name"],
                "subtopic": q.get("subtopic", ""),
                "question_text": q["question"],
                "selected_index": selected_idx,
                "correct_index": q["correct_index"],
                "is_correct": is_correct,
                "formula": q["formula"],
                "explanation": q["explanation"],
                "board_tip": q["board_tip"]
            })

        self.diagnostic_completed = True
        self.diagnostic_score = score
        self.diagnostic_total = len(questions)
        self.diagnostic_timestamp = datetime.now()
        self.diagnostic_details = details
        self.weak_concepts = new_weak_concepts
        self.total_questions_solved += len(questions)
        self.total_correct_count += score

        # Generate updated adaptive spaced revision schedule
        self.update_revision_schedule()

        return {
            "score": score,
            "total": len(questions),
            "percentage": round((score / len(questions)) * 100, 1),
            "weak_concepts": self.weak_concepts,
            "details": details
        }

    def record_practice_answer(self, question: Dict[str, Any], selected_index: int) -> Dict[str, Any]:
        """
        Update learner model when student answers an adaptive practice question.
        Dynamically adjusts concept mastery using difficulty-weighted deltas.
        """
        cid = question["concept_id"]
        is_correct = (selected_index == question["correct_index"])
        difficulty = question.get("difficulty", "Medium")

        old_mastery = self.concept_mastery.get(cid, 50.0)

        # Difficulty weighting
        delta_map = {
            "Easy": {"correct": 8.0, "incorrect": -12.0},
            "Medium": {"correct": 12.0, "incorrect": -9.0},
            "Hard": {"correct": 16.0, "incorrect": -6.0}
        }
        deltas = delta_map.get(difficulty, {"correct": 10.0, "incorrect": -8.0})
        delta = deltas["correct"] if is_correct else deltas["incorrect"]

        new_mastery = max(10.0, min(100.0, old_mastery + delta))
        self.concept_mastery[cid] = round(new_mastery, 1)

        # Update weak concepts list
        if new_mastery < 60.0 and cid not in self.weak_concepts:
            self.weak_concepts.append(cid)
        elif new_mastery >= 70.0 and cid in self.weak_concepts:
            self.weak_concepts.remove(cid)

        # Log practice entry
        entry = {
            "timestamp": datetime.now(),
            "question_id": question["id"],
            "concept_id": cid,
            "concept_name": question["concept_name"],
            "difficulty": difficulty,
            "selected_index": selected_index,
            "correct_index": question["correct_index"],
            "is_correct": is_correct,
            "old_mastery": old_mastery,
            "new_mastery": round(new_mastery, 1),
            "formula": question.get("formula", ""),
            "explanation": question.get("explanation", ""),
            "board_tip": question.get("board_tip", "")
        }
        self.practice_history.append(entry)
        self.total_questions_solved += 1
        if is_correct:
            self.total_correct_count += 1

        # Re-sync revision schedule
        self.update_revision_schedule()

        return entry

    def record_voice_attempt(self, challenge: Dict[str, Any], transcript: str, evaluation: Dict[str, Any]):
        """Store voice dictation attempt in learner history."""
        cid = challenge["concept_id"]
        entry = {
            "timestamp": datetime.now(),
            "challenge_id": challenge["id"],
            "title": challenge["title"],
            "concept_id": cid,
            "transcript": transcript,
            "score": evaluation["score"],
            "matched_keywords": evaluation["matched_keywords"],
            "missing_keywords": evaluation["missing_keywords"],
            "feedback": evaluation["feedback"]
        }
        self.voice_history.append(entry)
        
        # Slight mastery boost for good voice explanation
        if evaluation["score"] >= 70:
            current = self.concept_mastery.get(cid, 50.0)
            self.concept_mastery[cid] = min(100.0, current + 6.0)
            if self.concept_mastery[cid] >= 70.0 and cid in self.weak_concepts:
                self.weak_concepts.remove(cid)
            self.update_revision_schedule()

    def get_overall_readiness_score(self) -> float:
        """Weighted average readiness score across all Physics concepts."""
        total_weight = sum(c["weight"] for c in CONCEPTS)
        weighted_sum = sum(self.concept_mastery.get(c["id"], 50.0) * c["weight"] for c in CONCEPTS)
        return round(weighted_sum / total_weight, 1)

    def get_concept_status(self, concept_id: str) -> str:
        """Return status string for a concept."""
        m = self.concept_mastery.get(concept_id, 0)
        if m >= MASTERY_THRESHOLDS["mastered"]:
            return "Mastered"
        elif m >= MASTERY_THRESHOLDS["developing"]:
            return "Developing"
        else:
            return "Needs Focus"

    def get_recommended_difficulty(self, concept_id: str) -> str:
        """Adapt question difficulty based on student's current concept mastery."""
        m = self.concept_mastery.get(concept_id, 50.0)
        if m < 50:
            return "Easy"
        elif m < 75:
            return "Medium"
        else:
            return "Hard"

    def _generate_initial_schedule(self):
        """Build initial baseline revision schedule."""
        today = datetime.now()
        schedule = []
        for i, c in enumerate(CONCEPTS):
            cid = c["id"]
            # Spread across upcoming days
            due_date = today + timedelta(days=(i % 4) + 1)
            schedule.append({
                "concept_id": cid,
                "concept_name": c["name"],
                "icon": c["icon"],
                "due_date": due_date.strftime("%Y-%m-%d"),
                "due_display": "Today" if (i == 0) else due_date.strftime("%b %d, %Y"),
                "priority": "High" if i < 2 else "Medium",
                "recommended_mode": "Flashcards & Numericals",
                "retention_level": 70,
                "status": "Due Today" if (i == 0) else "Upcoming",
                "revision_interval_days": 3
            })
        self.revision_schedule = schedule

    def update_revision_schedule(self):
        """
        Recalculate Spaced Repetition (Ebbinghaus forgetting curve intervals)
        based on current concept mastery.
        """
        today = datetime.now()
        updated_schedule = []

        for c in CONCEPTS:
            cid = c["id"]
            mastery = self.concept_mastery.get(cid, 50.0)
            status = self.get_concept_status(cid)

            # Spaced repetition interval determination
            if status == "Needs Focus" or cid in self.weak_concepts:
                interval_days = 1  # Review immediately (today or tomorrow)
                priority = "Critical"
                retention_level = int(mastery * 0.8)
                rec_mode = "Step-by-step formula derivation & Easy tier"
            elif status == "Developing":
                interval_days = 4  # Review in 4 days
                priority = "Moderate"
                retention_level = int(mastery * 0.9)
                rec_mode = "Board-standard medium numericals & Voice Dictation"
            else:  # Mastered
                interval_days = 10  # Review in 10 days
                priority = "Low"
                retention_level = int(mastery * 0.95)
                rec_mode = "Speed mock & Exemplar conceptual questions"

            due_date = today + timedelta(days=interval_days if priority != "Critical" else 0)
            is_today = (due_date.date() == today.date())

            updated_schedule.append({
                "concept_id": cid,
                "concept_name": c["name"],
                "icon": c["icon"],
                "due_date": due_date.strftime("%Y-%m-%d"),
                "due_display": "Today (High Priority)" if is_today else due_date.strftime("%b %d, %Y"),
                "priority": priority,
                "recommended_mode": rec_mode,
                "retention_level": min(100, max(20, retention_level)),
                "status": "Due Today" if is_today else f"In {interval_days} days",
                "revision_interval_days": interval_days
            })

        # Sort schedule: Critical first, then by retention ascending
        priority_order = {"Critical": 0, "Moderate": 1, "Low": 2}
        updated_schedule.sort(key=lambda x: (priority_order.get(x["priority"], 3), x["retention_level"]))
        self.revision_schedule = updated_schedule

    def mark_concept_revised(self, concept_id: str):
        """User clicks 'Mark as Revised' - boosts retention and bumps review interval."""
        today = datetime.now()
        for item in self.revision_schedule:
            if item["concept_id"] == concept_id:
                # Boost retention
                item["retention_level"] = min(100, item["retention_level"] + 15)
                # Next interval is doubled (Spaced Repetition)
                new_interval = max(3, item["revision_interval_days"] * 2)
                item["revision_interval_days"] = new_interval
                next_date = today + timedelta(days=new_interval)
                item["due_date"] = next_date.strftime("%Y-%m-%d")
                item["due_display"] = next_date.strftime("%b %d, %Y")
                item["status"] = f"In {new_interval} days"
                if item["priority"] == "Critical":
                    item["priority"] = "Moderate"
                break
        
        # Slight boost to mastery
        cur = self.concept_mastery.get(concept_id, 50.0)
        self.concept_mastery[concept_id] = min(100.0, cur + 5.0)

    def reset_model(self):
        """Reset the learner model to fresh baseline."""
        self.__init__(self.student_name)
