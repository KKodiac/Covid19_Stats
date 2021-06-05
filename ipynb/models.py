from model_setting import *
import tensorflow as tf
# MODLE INIT
class Model:
    def __init__(self):
        self.SIGHT = SIGHT
        self.Y_N = Y_N
        self.TEST_SIZE = TEST_SIZE
        self.EPOCHS = EPOCHS
        self.BATCH_SIZE = BATCH_SIZE
        self.LEARNING_RATE = L_R

        self.POS = POS
        self.DAYS = DAYS
        self.START_DATE = START_DATE

        
    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.Input(shape=(self.SIGHT, 1)),
            tf.keras.layers.LSTM(16, return_sequences=True, dropout=0.2),
            tf.keras.layers.LSTM(16, dropout=0.2),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(self.Y_N, activation=tf.keras.layers.LeakyReLU()),
        ])
        optim = tf.kears.optimizers.Adam(lr=self.LEARNING_RATE)
        model.compile(optimizer=optim, loss="huber")

        return model

class Predict(Model):
    self.model = Model.build_model().load_weights('weights.h5')
    pred_data = "../Data"