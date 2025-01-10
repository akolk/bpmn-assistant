import os

from dotenv import load_dotenv

from bpmn_assistant.core import LLMFacade, MessageItem
from bpmn_assistant.core.enums import (
    AnthropicModels,
    FireworksAIModels,
    GoogleModels,
    OpenAIModels,
    OutputMode,
    Provider,
)


def get_llm_facade(model: str, output_mode: OutputMode = OutputMode.JSON) -> LLMFacade:
    """
    Get the LLM facade based on the model type
    Args:
        model: The model to use
        output_mode: The output mode for the LLM response (JSON or text)
    Returns:
        LLMFacade: The LLM facade
    """
    load_dotenv(override=True)

    if is_openai_model(model):
        api_key = os.getenv("OPENAI_API_KEY")
        provider = Provider.OPENAI
    elif is_anthropic_model(model):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        provider = Provider.ANTHROPIC
    elif is_google_model(model):
        api_key = os.getenv("GOOGLE_API_KEY")
        provider = Provider.GOOGLE
    elif is_fireworks_ai_model(model):
        api_key = os.getenv("FIREWORKS_AI_API_KEY")
        provider = Provider.FIREWORKS_AI
    else:
        raise Exception("Invalid model")

    return LLMFacade(
        provider,
        api_key,
        model,
        output_mode=output_mode,
    )


def get_available_providers() -> dict:
    load_dotenv(override=True)
    openai_api_key = os.getenv("OPENAI_API_KEY")
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
    google_api_key = os.getenv("GOOGLE_API_KEY")
    fireworks_api_key = os.getenv("FIREWORKS_AI_API_KEY")

    openai_present = openai_api_key is not None and len(openai_api_key) > 0
    anthropic_present = anthropic_api_key is not None and len(anthropic_api_key) > 0
    google_present = google_api_key is not None and len(google_api_key) > 0
    fireworks_ai_present = fireworks_api_key is not None and len(fireworks_api_key) > 0

    return {
        "openai": openai_present,
        "anthropic": anthropic_present,
        "google": google_present,
        "fireworks_ai": fireworks_ai_present,
    }


def replace_reasoning_model(model: str) -> str:
    """
    Returns GPT-4o if o1-preview is requested, or GPT-4o-mini if o1-mini is requested.
    Otherwise returns the original model.
    """
    if model == OpenAIModels.O1.value:
        return OpenAIModels.GPT_4O.value
    elif model == OpenAIModels.O1_MINI.value:
        return OpenAIModels.GPT_4O_MINI.value
    return model


def is_openai_model(model: str) -> bool:
    return model in [model.value for model in OpenAIModels]


def is_reasoning_model(model: str) -> bool:
    return model in [model.value for model in [OpenAIModels.O1, OpenAIModels.O1_MINI]]


def is_anthropic_model(model: str) -> bool:
    return model in [model.value for model in AnthropicModels]


def is_google_model(model: str) -> bool:
    return model in [model.value for model in GoogleModels]


def is_fireworks_ai_model(model: str) -> bool:
    return model in [model.value for model in FireworksAIModels]


def message_history_to_string(message_history: list[MessageItem]) -> str:
    """
    Convert a message history list into a formatted string.
    """
    return "\n".join(
        f"{message.role.capitalize()}: {message.content}" for message in message_history
    )
