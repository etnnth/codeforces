import tensorflow
import numpy


class Model:
    def __init__(self):
        self.model = tensorflow.keras.Sequential([
            tensorflow.keras.layers.Dense(10, activation='relu'),
            tensorflow.keras.layers.Dense(3)
            ])
        self.compile()
        self.probability_model = None
        self.create_probability_model()

    def create_probability_model(self):
        self.probability_model = tensorflow.keras.Sequential([self.model,
            tensorflow.keras.layers.Softmax()])

    def compile(self):
        self.model.compile(optimizer='adam',
            loss=tensorflow.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy'])
        self.create_probability_model()

    def predict(self, prediction_set):
        return self.probability_model.predict(prediction_set)

    def predict_bet(self, prediction_set):
        return ["HOME", "DRAW", "AWAY"][numpy.argmax(self.predict(prediction_set))]

    def fit(self, training_set, training_label, epoch):
        self.model.fit(training_set, training_label, epochs=epoch)

    def evaluate(self, test_set, test_label):
        test_loss, test_acc = self.model.evaluate(test_set, test_label, verbose=2)
        print('\nTest loss:', test_loss)
        print('Test accuracy:', test_acc)
        print()

    def save(self, file):
        self.model.save(file)

    def load(self, file):
        self.model = tensorflow.keras.models.load_model(file)
        self.compile()
        self.create_probability_model()

