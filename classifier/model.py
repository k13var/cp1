from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from transformers import pipeline


class Model:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("tblard/tf-allocine", use_fast=True)
        self.classifier = TFAutoModelForSequenceClassification.from_pretrained("tblard/tf-allocine")

        self.sentiment_analyzer = pipeline('sentiment-analysis', model=self.classifier, tokenizer=self.tokenizer)

    def predict(self, text):
        result = self.sentiment_analyzer(text)
        prediction = result[0]["label"]
        response = "Positif" if prediction == 'POSITIVE' else "Négatif"
        return text, response


model = Model()


def get_model():
    return model
