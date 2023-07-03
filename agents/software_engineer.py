import tensorflow as tf

def generate_solution(problem):
  """Generates a solution to a software engineering problem."""

  if problem == 'design a new algorithm':
    return tf.keras.models.Sequential([
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

  elif problem == 'fix a bug in a code':
    return tf.keras.models.Sequential([
        tf.keras.layers.LSTM(128),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

  else:
    return tf.keras.models.Sequential([
        tf.keras.layers.Embedding(10000, 128),
        tf.keras.layers.LSTM(128),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])