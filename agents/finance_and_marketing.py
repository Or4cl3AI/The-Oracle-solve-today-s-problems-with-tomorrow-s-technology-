import torch

def generate_solution(problem):

  """Generates a solution to a finance and marketing problem."""

  if problem == 'optimize a marketing campaign':

    return torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)

  elif problem == 'forecast sales':

    return torch.hub.load('pytorch/ignite:v0.4.5', 'transformers', 'bert-base-uncased')

  else:

    return torch.hub.load('pytorch/hub:master', 'autoencoder', 'resnet18')