import random
import json
import torch
import os

from redNeuronal.ChatBot_Algorithm.model import NeuralNet
from redNeuronal.ChatBot_Algorithm.nltk_utils import bag_of_words, tokenize


def main():
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    module_dir = os.path.dirname(__file__)  # get current directory
    with open(os.path.join(module_dir,'intents.json'), 'r') as json_data:
        intents = json.load(json_data)

    FILE = os.path.join(module_dir,"data.pth")
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    bot_name = "Samantha"
    print("Hablemos! (Si deseas salir escribe 'quit')")
    responses = list()
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        responses.append(sentence)
        if sentence == "quit":
            break

        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
        else:
            print(f"{bot_name}: No entiendo, podrias repetirlo por favor...")

    print("\nRespuestas dadas por el usuario\n")
    print(responses)

if __name__ == "__main__":
    main()