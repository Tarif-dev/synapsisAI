from groq import Groq
from app.config.settings import settings

client = Groq(api_key=settings.GROQ_API_KEY)


def generate_llm_response(system_prompt: str, user_prompt: str):

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        temperature=0.2,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.choices[0].message.content