import numpy
import torch

# Define model
class NeuralNetwork(torch.nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = torch.nn.Flatten()
        self.linear_relu_stack = torch.nn.Sequential(
            torch.nn.Linear(23, 128),
            torch.nn.ReLU(),
            torch.nn.Linear(128, 128),
            torch.nn.ReLU(),
            torch.nn.Linear(128, 128),
            torch.nn.ReLU(),
            torch.nn.Linear(128, 128),
            torch.nn.ReLU(),
            torch.nn.Linear(128, 128),
            torch.nn.ReLU(),
            torch.nn.Linear(128, 128),
            torch.nn.ReLU(),
            torch.nn.Linear(128, 128),
            torch.nn.ReLU(),
            torch.nn.Linear(128, 3),
            torch.nn.ReLU()
        )

    def forward(self, x):
        logits = self.linear_relu_stack(x)
        return logits


class Model:
    def __init__(self):
        self.device = "cpu"
        self.model = NeuralNetwork().to(self.device)
        self.loss_fn = torch.nn.CrossEntropyLoss()
        self.optimizer = torch.optim.SGD(self.model.parameters(), lr=1e-2)


    def train(self, dataloader):
        size = len(dataloader.dataset)
        for batch, (X, y) in enumerate(dataloader):
            X, y = X.to(self.device), y.to(self.device)

            # Compute prediction error
            pred = self.model(X)
            loss = self.loss_fn(pred, y)

            # Backpropagation
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

            if batch % 100 == 0:
                loss, current = loss.item(), batch * len(X)
                print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]", flush = True)

    def predict_bet(self, x):
        self.model.eval()
        x = torch.Tensor(numpy.asarray(x))
        with torch.no_grad():
            return ["HOME", "DRAW", "AWAY"][self.model(x).argmax(0)]

    def fit(self, training_set, training_label, epochs):
        print(self.model)
        tensor_x = torch.Tensor(training_set)
        tensor_y = torch.Tensor(training_label).to(torch.long)
        dataset = torch.utils.data.TensorDataset(tensor_x, tensor_y)
        dataloader = torch.utils.data.DataLoader(dataset, batch_size=64)
        for t in range(epochs):
            print(f"Epoch {t+1}\n-------------------------------", flush = True)
            self.train(dataloader)
        print("Done!")

    def evaluate(self, test_set, test_label):
        test_loss, test_acc = 1, 1
        print('\nTest loss:', test_loss)
        print('Test accuracy:', test_acc)
        print()

    def save(self, file):
        torch.save(self.model.state_dict(), file)

    def load(self, file):
        self.model = NeuralNetwork()
        self.model.load_state_dict(torch.load(file))

