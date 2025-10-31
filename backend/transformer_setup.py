# transformer_setup.py
# Optional: small script to show how to use a HuggingFace transformer for inference.
# This does NOT include fine-tuning; it's an example for using a pretrained sequence classifier.

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

MODEL_NAME = 'microsoft/deberta-base-mnli'  # example; replace with a fake-news fine-tuned model if available

def get_pipeline():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    nlp = pipeline('text-classification', model=model, tokenizer=tokenizer, return_all_scores=True)
    return nlp

if __name__ == '__main__':
    nlp = get_pipeline()
    text = "This is a test news headline about something dramatic."
    print(nlp(text))
