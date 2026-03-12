from openai import AsyncOpenAI
from database.orm import HealthProfile
from pydantic import BaseModel
from config import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)


class RiskPRedictionResult(BaseModel):
    diabetes_probability: float
    hypertension_probability: float
async def predict_health_risk(profile: HealthProfile, model_version: str) -> RiskPRedictionResult:
    prompt = f"""
    다음 건강 정보를 기반으로 당뇨와 고혈압 위험도를 0과 1 사이로 계산하세요.

    age: {profile.age}
    height_cm: {profile.height_cm}
    weight_kg: {profile.weight_kg}
    smoking: {profile.smoking}
    exercise_per_week: {profile.exercise_per_week}
    """

    await client.responses.parse(
        model=model_version,
        input=prompt,
        text_format=RiskPRedictionResult,
    )
    return response.output_parsed