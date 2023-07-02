```python
import pandas as pd
import tensorflow as tf

def load_data():
    data = pd.read_csv('../data/train_data.csv')
    return data

def train(data):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(data, epochs=10)
    return model

def generate_solution(model, problem):
    solution = model.predict(problem)
    return solution

def main():
    data = load_data()
    model = train(data)
    problem = input("Please describe your problem: ")
    solution = generate_solution(model, problem)
    print("The solution to your problem is: ", solution)

if __name__ == "__main__":
    main()
```