import json
import re
from app.services.llm_provider import generate_llm_response


def extract_json(response: str):
    cleaned = response.replace("```json", "").replace("```", "").strip()

    match = re.search(r"\{.*\}", cleaned, re.DOTALL)

    if not match:
        raise ValueError("No valid JSON found")

    return json.loads(match.group())


def generate_ui_structure(prompt: str):

    system_prompt = """
You are a senior UI/UX engineer.

Generate a modern, clean, visually appealing UI component schema.

Rules:
- Use good spacing and layout
- Use realistic UI patterns
- Avoid generic placeholder design
- Use inline styles (NO Tailwind)
- Make it visually balanced

Schema format:

{
  "componentName": "",
  "layout": "vertical | horizontal",
  "elements": [
    {
      "type": "image",
      "src": "",
      "style": {}
    },
    {
      "type": "text",
      "content": "",
      "style": {}
    },
    {
      "type": "button",
      "content": "",
      "style": {}
    }
  ],
  "styles": {}
}

Return ONLY JSON.
"""

    response = generate_llm_response(system_prompt, prompt)

    print("LLM RESPONSE:", response)

    return extract_json(response)