import json
import os
from openai import OpenAI


def get_client():
    """
    Initializes and returns an OpenAI-compatible client using Groq API.

    The Groq API uses the OpenAI SDK, making it easy to swap models.
    We point the base_url to Groq's endpoint.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")

    return OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")


def get_time_limit(num_questions: int, test_type: str):
    """
    Calculates the duration of the test in minutes.

    - Full Mock Tests are standard 180 minutes.
    - Subject tests use a heuristic of ~2 minutes per question.
    """
    if test_type == "full":
        return 180

    mapping = {10: 20, 15: 30, 20: 40}
    return mapping.get(num_questions, 30)


def generate_mcqs(
    subject_name: str = None,
    branch_name: str = None,
    test_type: str = "subject",
    num_questions: int = 10,
):
    """
    Generates GATE-level MCQs using the Groq Llama-3 model.

    FIX APPLIED:
    When using response_format={"type": "json_object"}, the LLM MUST return
    a dictionary (object) starting with '{'. We now instruct the AI to wrap
    the questions inside a "questions" key.
    """

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

    elif test_type == "full":
        if not branch_name:
            raise ValueError("branch_name required for full test")

        # NOTE: Generating 65 questions in one API call may hit token limits.
        # If this fails, consider reducing the count or batching.
        prompt = f"""
        Generate a FULL-LENGTH, HIGH-QUALITY GATE mock test for the branch: {branch_name}.

        TOTAL QUESTIONS:
        - 65 Questions in total:
            - 10 General Aptitude (GA)
            - 55 Core Engineering (from full syllabus)

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
        - Core Engineering (55 Questions):
            - Cover the FULL syllabus with proper topic distribution
            - Avoid over-concentration on a single topic

        QUESTION TYPE DISTRIBUTION (OVERALL):
        - 50% MCQ (single correct)
        - Remaining 50% split between MSQ and NAT
        - MCQs should be slightly more than MSQ and NAT individually

        MARKS DISTRIBUTION:
        - Follow GATE pattern:
            - Mix of 1-mark and 2-mark questions
            - Approximately equal distribution
            - Total marks ≈ 100

        QUESTION DESIGN:
        - Inspired by previous year GATE questions (PYQs), but DO NOT copy
        - Modify values, logic, or context to create original questions
        - Maintain authentic GATE exam style and depth

        OUTPUT FORMAT (STRICT JSON ONLY):
        {{
        "questions": [
            {{
            "section": "aptitude/core",
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
        - Each question MUST include "section" ("aptitude" or "core")
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
    else:
        raise ValueError("Invalid test_type")

    # --- 2. API CALL ---
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a specialized GATE exam generator that only outputs valid JSON.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,  # Lower temperature for more factual/structured output
        response_format={"type": "json_object"},
    )

    content = response.choices[0].message.content.strip()

    # --- 3. DATA PARSING & VALIDATION ---
    try:
        # Step A: Parse the raw string into a Python Dictionary
        raw_data = json.loads(content)

        # Step B: Extract the list from the "questions" wrapper
        if "questions" in raw_data:
            questions_list = raw_data["questions"]
        else:
            # Fallback if AI ignored the key and returned a list directly
            questions_list = raw_data if isinstance(raw_data, list) else []

    except json.JSONDecodeError:
        raise ValueError("AI failed to return valid JSON.")

    # Step C: Deep validation of question structure
    if not isinstance(questions_list, list) or len(questions_list) == 0:
        raise ValueError("AI returned an empty or invalid question list.")

    for q in questions_list:
        # Check for mandatory keys
        if "question" not in q or "question_type" not in q:
            raise ValueError("Missing required fields in question")

        if q["question_type"] in ["mcq", "msq"]:
            if "options" not in q or "answer" not in q:
                raise ValueError("MCQ/MSQ must have options and answer")

        if q["question_type"] == "nat":
            if "answer" not in q:
                raise ValueError("NAT must have numerical answer")

        # Check for 4 options
        if q["question_type"] in ["mcq", "msq"]:
            options = q.get("options")

            if not options or len(options) != 4:
                continue

    for q in questions_list:
        q["question_type"] = q["question_type"].lower()

    # --- 4. FINAL ASSEMBLY ---
    return {
        "questions": questions_list,
        "time_limit": get_time_limit(num_questions, test_type),
        "test_type": test_type,
        "total_count": len(questions_list),
    }
