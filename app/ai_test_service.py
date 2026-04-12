import json
import os
from openai import OpenAI


def get_client():
    """
    Initializes and returns an OpenAI-compatible client using Groq API.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")

    return OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")


def get_time_limit(num_questions: int, test_type: str):
    if test_type == "full":
        return 180
    mapping = {10: 20, 15: 30, 20: 40}
    return mapping.get(num_questions, 30)


def validate_questions(questions_list):
    """Filter out malformed questions."""
    valid = []
    for q in questions_list:
        if "question" not in q or "question_type" not in q:
            continue
        q["question_type"] = q["question_type"].lower()
        if q["question_type"] in ["mcq", "msq"]:
            if "options" not in q or "answer" not in q:
                continue
            if not q.get("options") or len(q["options"]) != 4:
                continue
        if q["question_type"] == "nat":
            if "answer" not in q:
                continue
        valid.append(q)
    return valid


def call_llm(client, prompt):
    """Single LLM call — returns validated question list."""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a specialized GATE exam generator that only outputs valid JSON.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
        response_format={"type": "json_object"},
    )
    content = response.choices[0].message.content.strip()
    try:
        raw_data = json.loads(content)
        questions_list = raw_data.get("questions", []) if isinstance(raw_data, dict) else []
    except json.JSONDecodeError:
        return []
    return validate_questions(questions_list)


def generate_mcqs(
    subject_name: str = None,
    branch_name: str = None,
    test_type: str = "subject",
    num_questions: int = 10,
):
    client = get_client()

    # --- 1. PROMPT CONSTRUCTION ---
    if test_type == "subject":
        if not subject_name:
            raise ValueError("subject_name required for subject test")

        prompt = f"""
        Generate {num_questions} HIGH-QUALITY GATE-level questions for the subject: {subject_name}.

        DIFFICULTY:
        - Questions must be MODERATE to HARD level.
        - Focus on conceptual understanding, numerical solving, and tricky logic.
        - Avoid basic or definition-based questions.
        - Prefer multi-step reasoning and problem-solving questions.

        DISTRIBUTION:
        - 50% MCQ (single correct)
        - Remaining 50% split between MSQ and NAT
        - Ensure MCQs are slightly more than others

        QUESTION DESIGN:
        - Inspired by previous year GATE questions (PYQs), but DO NOT copy them exactly
        - Modify values, context, or framing to create new questions
        - Maintain GATE exam style and depth

        OUTPUT FORMAT (STRICT JSON ONLY):
        {{
        "questions": [
            {{
            "question": "...",
            "question_type": "mcq/msq/nat",
            "marks": 1 or 2,

            "options": {{
                "A": "...",
                "B": "...",
                "C": "...",
                "D": "..."
            }},  # ONLY for mcq/msq (must be null for nat)

            "answer": "A" OR ["A","C"] OR 12.5
            }}
        ]
        }}

        -STRICT RULES:
            - MCQ/MSQ must have EXACTLY 4 options
            - Each question must include "marks": 1 or 2
            - Maintain approximately equal number of 1-mark and 2-mark questions
            - STRICT: Every MCQ/MSQ MUST have exactly 4 options
            - Output must be valid JSON (no expressions)
            - All numerical answers must be decimal numbers
            - Do NOT use fractions like 1/2 or -1/6
            - Convert all answers to float (e.g., 0.5, -0.1667

        - MCQ:
            - Exactly 4 options
            - Only ONE correct answer (string)

        - MSQ:
            - Exactly 4 options
            - One or more correct answers (list)

        - NAT:
            - No options (options must be null or omitted)
            - Answer must be a number (int or float)
        
        - No explanations
        - No markdown
        - No extra text
        - Return ONLY valid JSON
        """

        # --- 2. API CALL (subject) ---
        valid_questions = call_llm(client, prompt)

    elif test_type == "full":
        if not branch_name:
            raise ValueError("branch_name required for full test")

        ga_prompt = f"""
        Generate a FULL-LENGTH, HIGH-QUALITY GATE mock test for the branch: {branch_name}.

        TOTAL QUESTIONS:
        - 10 General Aptitude (GA) questions ONLY. NO Core Engineering questions.

        DIFFICULTY:
        - Overall paper should match actual GATE level (MODERATE to HARD)
        - Include a balanced mix:
            - Conceptual questions
            - Numerical/problem-solving questions
            - Multi-step reasoning
            - Tricky and application-based questions
        - Avoid basic theory/definition-only questions

        SECTION DISTRIBUTION:
        - General Aptitude (10 Questions):
            - Mix of verbal ability, logical reasoning, and numerical aptitude

        QUESTION TYPE DISTRIBUTION (OVERALL):
        - 50% MCQ (single correct)
        - Remaining 50% split between MSQ and NAT
        - MCQs should be slightly more than MSQ and NAT individually

        MARKS DISTRIBUTION:
        - Follow GATE pattern:
            - Mix of 1-mark and 2-mark questions
            - Approximately equal distribution

        QUESTION DESIGN:
        - Inspired by previous year GATE questions (PYQs), but DO NOT copy
        - Modify values, logic, or context to create original questions
        - Maintain authentic GATE exam style and depth

        OUTPUT FORMAT (STRICT JSON ONLY):
        {{
        "questions": [
            {{
            "section": "aptitude",
            "question": "...",
            "question_type": "mcq/msq/nat",
            "marks": 1 or 2,

            "options": {{
                "A": "...",
                "B": "...",
                "C": "...",
                "D": "..."
            }},  # ONLY for mcq/msq (must be null for nat)

            "answer": "A" OR ["A","C"] OR 12.5
            }}
        ]
        }}

        STRICT RULES:
        - Each question MUST include "section": "aptitude"
        - MCQ/MSQ must have EXACTLY 4 options
        - NAT must have options = null or omitted
        - Each question must include "marks": 1 or 2
        - Maintain near equal number of 1-mark and 2-mark questions
        - Output must be valid JSON ONLY (no extra text, no markdown)
        - All numerical answers must be in decimal format
            - Convert fractions (e.g., 1/2 → 0.5, -1/6 → -0.1667)
        - NO explanations
        - NO duplicate questions

        MCQ:
        - Exactly 4 options
        - Only ONE correct answer (string)

        MSQ:
        - Exactly 4 options
        - One or more correct answers (list)

        NAT:
        - No options
        - Answer must be a number (int or float)

        FINAL INSTRUCTION:
        - Return ONLY valid JSON
        """

        core_prompt = f"""
        Generate a FULL-LENGTH, HIGH-QUALITY GATE mock test for the branch: {branch_name}.

        TOTAL QUESTIONS:
        - 55 Core Engineering questions ONLY. NO General Aptitude questions.
        - Cover the FULL syllabus with proper topic distribution
        - Avoid over-concentration on a single topic

        DIFFICULTY:
        - Overall paper should match actual GATE level (MODERATE to HARD)
        - Include a balanced mix:
            - Conceptual questions
            - Numerical/problem-solving questions
            - Multi-step reasoning
            - Tricky and application-based questions
        - Avoid basic theory/definition-only questions

        QUESTION TYPE DISTRIBUTION (OVERALL):
        - 50% MCQ (single correct)
        - Remaining 50% split between MSQ and NAT
        - MCQs should be slightly more than MSQ and NAT individually

        MARKS DISTRIBUTION:
        - Follow GATE pattern:
            - Mix of 1-mark and 2-mark questions
            - Approximately equal distribution
            - Total marks ≈ 90

        QUESTION DESIGN:
        - Inspired by previous year GATE questions (PYQs), but DO NOT copy
        - Modify values, logic, or context to create original questions
        - Maintain authentic GATE exam style and depth

        OUTPUT FORMAT (STRICT JSON ONLY):
        {{
        "questions": [
            {{
            "section": "core",
            "question": "...",
            "question_type": "mcq/msq/nat",
            "marks": 1 or 2,

            "options": {{
                "A": "...",
                "B": "...",
                "C": "...",
                "D": "..."
            }},  # ONLY for mcq/msq (must be null for nat)

            "answer": "A" OR ["A","C"] OR 12.5
            }}
        ]
        }}

        STRICT RULES:
        - Each question MUST include "section": "core"
        - MCQ/MSQ must have EXACTLY 4 options
        - NAT must have options = null or omitted
        - Each question must include "marks": 1 or 2
        - Maintain near equal number of 1-mark and 2-mark questions
        - Output must be valid JSON ONLY (no extra text, no markdown)
        - All numerical answers must be in decimal format
            - Convert fractions (e.g., 1/2 → 0.5, -1/6 → -0.1667)
        - NO explanations
        - NO duplicate questions
        - Ensure variety and coverage across topics

        MCQ:
        - Exactly 4 options
        - Only ONE correct answer (string)

        MSQ:
        - Exactly 4 options
        - One or more correct answers (list)

        NAT:
        - No options
        - Answer must be a number (int or float)

        FINAL INSTRUCTION:
        - Return ONLY valid JSON
        """

        # --- 2. API CALL (full — two separate calls, then merge) ---
        ga_questions = call_llm(client, ga_prompt)
        core_questions = call_llm(client, core_prompt)
        valid_questions = ga_questions + core_questions

    else:
        raise ValueError("Invalid test_type")

    # --- 3. FINAL CHECK ---
    min_required = 10 if test_type == "subject" else 30
    if len(valid_questions) < min_required:
        raise ValueError(
            f"AI returned too few valid questions ({len(valid_questions)}). "
            f"Expected at least {min_required}. Please try again."
        )

    # --- 4. FINAL ASSEMBLY ---
    return {
        "questions": valid_questions,
        "time_limit": get_time_limit(num_questions, test_type),
        "test_type": test_type,
        "total_count": len(valid_questions),
    }