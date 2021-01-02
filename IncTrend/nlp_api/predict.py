import requests
import json
import torch
import numpy as np

from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader, SequentialSampler
from transformers import BertForSequenceClassification
from transformers import BertTokenizer

path = '../../fine_tune_bert/'
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
batch_size = 32
epochs = 4
seed_val = 42


class Predict:
    def __init__(self, company):
        self.company = company
        self.messages = []

    def _get_messages(self):
        api_url = f"https://api.stocktwits.com/api/2/streams/symbol/{self.company}.json"
        response = requests.get(api_url, verify=False)
        if response.status_code == 200:
            print(f'Successfully GET message from stocktwits for {self.company}')
            dict_data = json.loads(response.content)
            for e in dict_data['messages']:
                self.messages.append(e['body'])

        else:
            print(f'Failed to fetch messages from stocktwits for {self.company}')

    def get_predictions(self):
        self._get_messages()

        input_ids = []
        attention_masks = []
        new_labels = []

        for i in range(len(self.messages)):
            encoded = tokenizer.encode_plus(  # encoded the pre tokenized message
                text=tokenizer.tokenize(self.messages[i]),
                max_length=128,
                padding='max_length',
                truncation=True,
                add_special_tokens=True,
                is_split_into_words=True,
                return_attention_mask=True,
                return_tensors='pt'
            )

            input_ids.append(encoded['input_ids'])
            attention_masks.append(encoded['attention_mask'])
            new_labels.append(1)

        input_ids = torch.cat(input_ids, dim=0)
        attention_masks = torch.cat(attention_masks, dim=0)
        new_labels = torch.tensor(new_labels)

        test_dataset = TensorDataset(input_ids, attention_masks, new_labels)
        test_data = DataLoader(
            test_dataset,
            sampler=SequentialSampler(test_dataset),
            batch_size=batch_size
        )

        model = BertForSequenceClassification.from_pretrained(path)
        model.eval()

        predictions = []

        for batch in test_data:
            batch = tuple(t for t in batch)
            b_input_ids, b_input_mask, b_labels = batch

            with torch.no_grad():
                outputs = model(b_input_ids, token_type_ids=None, attention_mask=b_input_mask)

            logits = outputs[0]
            logits = logits.detach().cpu().numpy()
            predictions.append(logits)

        predictions = np.argmax(predictions[0], axis=1).flatten()
        res = []

        for i in range(len(self.messages)):
            res.append(('Bullish' if predictions[i] == 1 else 'Bearish', self.messages[i]))

        return res


# for testing purposes
def main():
    predictions = Predict('AAPL').get_predictions()
    for prediction, message in predictions:
        print(prediction)


if __name__ == "__main__":
    main()
