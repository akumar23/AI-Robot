import torch
import torch.nn as nn

class Action_Conditioned_FF(nn.Module):
    def __init__(self, input_size=6, hidden_size=5, outptut_size=1):

        super(Action_Conditioned_FF, self).__init__()
        self.input_to_hidden = nn.Linear(input_size, hidden_size)
        self.nonlinear_activation = nn.Sigmoid()
        self.hidden_to_output = nn.Linear(hidden_size, outptut_size)

    def forward(self, input):
        hidden = self.input_to_hidden(input)
        hidden = self.nonlinear_activation(hidden)
        output = self.hidden_to_output(hidden)
        return output


    def evaluate(self, model, test_loader, loss_function):
        loss = 0
        for idx, sample in enumerate(test_loader):
            loss += loss_function(self.forward(sample['input']), sample['label'])
        result = loss / len(test_loader)
        return loss

def main():
    model = Action_Conditioned_FF()

if __name__ == '__main__':
    main()
