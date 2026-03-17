import json
import re
from app.services.llm_provider import generate_llm_response


def generate_ui_structure(prompt: str) -> dict:
    """
    Generates a UI schema JSON from a natural language prompt
    using an LLM.
    """

    system_prompt = """
You are an expert UI architect.

Convert the user prompt into a JSON UI schema.

Schema format:

{
  "componentName": "",
  "layout": "vertical | horizontal",
  "elements": [
    {"type": "image"},
    {"type": "text"},
    {"type": "button"}
  ],
  "styles": {
    "padding": "",
    "borderRadius": "",
    "shadow": true
  }
}

Return ONLY valid JSON. Do not include explanations.
"""

    # Call LLM
    response = generate_llm_response(system_prompt, prompt)

    print("RAW LLM RESPONSE:", response)

    try:
        # Remove markdown code blocks like ```json
        cleaned = response.replace("```json", "").replace("```", "").strip()

        # Extract JSON object safely
        match = re.search(r"\{.*\}", cleaned, re.DOTALL)

        if not match:
            raise ValueError("No valid JSON found in LLM response")

        json_str = match.group()

        # Convert JSON string → Python dictionary
        parsed_json = json.loads(json_str)

        return parsed_json

    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON returned by LLM: {e}")