from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TextIteratorStreamer,
)
from transformers.pipelines import pipeline

MODEL_ID = "argilla/notus-7b-v1"


def get_language_model():
    quantization_config = BitsAndBytesConfig(load_in_8bit=True)

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID, quantization_config=quantization_config, device_map="auto"
    )

    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

    streamer = TextIteratorStreamer(
        tokenizer, timeout=10, skip_prompt=True, skip_special_tokens=True
    )

    llm_pipe = pipeline(
        "text-generation",
        model=model,
        max_new_tokens=800,
        tokenizer=tokenizer,
        streamer=streamer,
    )

    return HuggingFacePipeline(pipeline=llm_pipe)
