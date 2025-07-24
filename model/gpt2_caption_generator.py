import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class CaptionGenerator:
    def __init__(self, model_name="gpt2", max_length=50):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.max_length = max_length

    def generate_caption(self, prompt, style="default"):
        if style == "funny":
            prompt = f"Write a funny Instagram caption: {prompt}"
        elif style == "motivational":
            prompt = f"Write a motivational Instagram caption: {prompt}"
        elif style == "poetic":
            prompt = f"Write a poetic Instagram caption: {prompt}"
        elif style == "aesthetic":
            prompt = f"Write an aesthetic Instagram caption: {prompt}"
        else:
            prompt = f"Write an Instagram caption: {prompt}"

        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(
            inputs,
            max_length=self.max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            do_sample=True,
            temperature=0.8,
            top_k=50,
            top_p=0.95,
            pad_token_id=self.tokenizer.eos_token_id
        )

        caption = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return caption.replace(prompt, "").strip()

