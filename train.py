import tensorflow as tf
import torch
import sklearn

def train_models():
  """Trains the AI models."""
  tf.keras.models.Sequential()
  torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)
  sklearn.linear_model.LogisticRegression()

if __name__ == '__main__':
  train_models()