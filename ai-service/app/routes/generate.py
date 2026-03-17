from fastapi import APIRouter
from app.schemas.prompt_schema import PromptRequest
from app.services.ai_service import generate_ui_structure
from app.services.code_generator import generate_react_component

router = APIRouter()

@router.post("/generate")
def generate_component(data: PromptRequest):

    ui_schema = generate_ui_structure(data.prompt)

    code = generate_react_component(ui_schema)

    return {
        "schema": ui_schema,
        "code": code
    }