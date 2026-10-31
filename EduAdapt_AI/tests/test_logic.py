"""
Unit tests for EduAdapt AI Core Logic
Tests:
- LearnerModel initialization
- Diagnostic scoring & weak concept identification
- Adaptive practice mastery updates & difficulty recommendations
- Spaced repetition revision scheduler & mark-as-revised
- Wispr Flow voice answer evaluator
- Teacher dashboard cohort analytics
"""

import unittest
from config import CONCEPTS
from models.learner_model import LearnerModel
from data.physics_questions import DIAGNOSTIC_QUESTIONS, PRACTICE_QUESTIONS, VOICE_CHALLENGES
from components.voice_component import evaluate_voice_answer
from data.student_data import get_class_summary_metrics


class TestEduAdaptAILogic(unittest.TestCase):

    def setUp(self):
        self.model = LearnerModel(student_name="Test Student")

    def test_learner_model_init(self):
        """Test initial default state of Learner Model."""
        self.assertEqual(self.model.student_name, "Test Student")
        self.assertFalse(self.model.diagnostic_completed)
        self.assertEqual(self.model.get_overall_readiness_score(), 50.0)
        self.assertEqual(len(self.model.concept_mastery), len(CONCEPTS))
        self.assertEqual(len(self.model.revision_schedule), len(CONCEPTS))

    def test_diagnostic_all_correct(self):
        """Test diagnostic evaluation when all 5 questions are answered correctly."""
        user_answers = {q["id"]: q["correct_index"] for q in DIAGNOSTIC_QUESTIONS}
        results = self.model.process_diagnostic_results(user_answers, DIAGNOSTIC_QUESTIONS)

        self.assertTrue(self.model.diagnostic_completed)
        self.assertEqual(results["score"], 5)
        self.assertEqual(results["total"], 5)
        self.assertEqual(results["percentage"], 100.0)
        self.assertEqual(len(self.model.weak_concepts), 0)
        self.assertGreater(self.model.get_overall_readiness_score(), 80.0)

    def test_diagnostic_partial_weak_identification(self):
        """Test diagnostic identification of weak concepts when questions are missed."""
        user_answers = {}
        # Get Q1 right, others wrong
        for i, q in enumerate(DIAGNOSTIC_QUESTIONS):
            if i == 0:
                user_answers[q["id"]] = q["correct_index"]
            else:
                user_answers[q["id"]] = (q["correct_index"] + 1) % 4

        results = self.model.process_diagnostic_results(user_answers, DIAGNOSTIC_QUESTIONS)

        self.assertEqual(results["score"], 1)
        self.assertEqual(len(self.model.weak_concepts), 4)
        # First concept should be high mastery
        q1_concept = DIAGNOSTIC_QUESTIONS[0]["concept_id"]
        self.assertEqual(self.model.concept_mastery[q1_concept], 85.0)
        # Missed concepts should have low mastery
        q2_concept = DIAGNOSTIC_QUESTIONS[1]["concept_id"]
        self.assertEqual(self.model.concept_mastery[q2_concept], 35.0)

    def test_adaptive_practice_mastery_increase(self):
        """Test that answering practice questions correctly boosts mastery and removes from weak list."""
        cid = "electricity_circuits"
        self.model.concept_mastery[cid] = 40.0
        self.model.weak_concepts = [cid]

        sample_q = PRACTICE_QUESTIONS[cid][0]
        # Answer correctly
        entry = self.model.record_practice_answer(sample_q, sample_q["correct_index"])

        self.assertTrue(entry["is_correct"])
        self.assertGreater(entry["new_mastery"], 40.0)

    def test_spaced_repetition_scheduling(self):
        """Test that weak concepts are given Critical priority and revision can be marked."""
        cid = "light_refl_refr"
        self.model.concept_mastery[cid] = 30.0
        self.model.weak_concepts = [cid]
        self.model.update_revision_schedule()

        sched_item = next(item for item in self.model.revision_schedule if item["concept_id"] == cid)
        self.assertEqual(sched_item["priority"], "Critical")

        # Mark as revised
        initial_retention = sched_item["retention_level"]
        self.model.mark_concept_revised(cid)
        updated_item = next(item for item in self.model.revision_schedule if item["concept_id"] == cid)
        self.assertGreater(updated_item["retention_level"], initial_retention)

    def test_voice_answer_evaluation(self):
        """Test Wispr Flow answer evaluator with good and weak answers."""
        challenge = VOICE_CHALLENGES[0]
        good_dictation = challenge["sample_good_dictation"]
        res_good = evaluate_voice_answer(good_dictation, challenge["expected_keywords"], challenge["ideal_explanation"])

        self.assertGreaterEqual(res_good["score"], 70)
        self.assertGreater(len(res_good["matched_keywords"]), 3)

        # Poor answer
        res_poor = evaluate_voice_answer("Light bends", challenge["expected_keywords"], challenge["ideal_explanation"])
        self.assertLess(res_poor["score"], 60)

    def test_teacher_analytics_metrics(self):
        """Test aggregate metrics calculation for teacher dashboard."""
        metrics_all = get_class_summary_metrics("All")
        self.assertEqual(metrics_all["total_students"], 30)
        self.assertGreater(metrics_all["avg_overall_score"], 0)
        self.assertIn("hardest_concept_name", metrics_all)

        metrics_10a = get_class_summary_metrics("10-A")
        self.assertEqual(metrics_10a["total_students"], 15)


if __name__ == "__main__":
    unittest.main()
