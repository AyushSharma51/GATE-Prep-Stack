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
        Generate {num_questions} GATE-level MCQs for the subject: {subject_name}.
        
        OUTPUT FORMAT:
        You must return a JSON object with a single key "questions" containing an array of objects.
        
        Example Structure:
        {{
          "questions": [
            {{
              "question": "The text of the question?",
              "options": {{ "A": "opt1", "B": "opt2", "C": "opt3", "D": "opt4" }},
              "answer": "A"
            }}
          ]
        }}

        STRICT RULES:
        - Exactly 4 options (A, B, C, D).
        - No markdown formatting (no ```json).
        - High technical accuracy for Graduate Aptitude Test in Engineering (GATE).
        """

    elif test_type == "full":
        if not branch_name:
            raise ValueError("branch_name required for full test")

        # NOTE: Generating 65 questions in one API call may hit token limits.
        # If this fails, consider reducing the count or batching.
        prompt = f"""
        Generate a full-length GATE mock test for {branch_name}.
        Include 10 General Aptitude and 55 Core Engineering questions.
        
        OUTPUT FORMAT:
        Return a JSON object: {{"questions": [...]}}
        Each question must include a "section" key (either "aptitude" or "core").
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
        if not all(k in q for k in ["question", "options", "answer"]):
            raise ValueError(
                "A question is missing required fields (question/options/answer)."
            )

        # Check for 4 options
        if len(q.get("options", {})) != 4:
            raise ValueError(
                f"Question '{q['question'][:30]}...' does not have exactly 4 options."
            )

    # --- 4. FINAL ASSEMBLY ---
    return {
        "questions": questions_list,
        "time_limit": get_time_limit(num_questions, test_type),
        "test_type": test_type,
        "total_count": len(questions_list),
    }
