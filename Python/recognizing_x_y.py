import tensorflow as tf
import numpy as np

model = tf.keras.Sequential([
    tf.keras.Input(shape=[1,]),
    tf.keras.layers.Dense(units=1)
])
model.compile(optimizer='sgd', loss='mean_squared_error')

x = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0, 110.0], dtype=float)
y = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0, 199.0, 201.0, 203.0, 205.0, 207.0, 209.0, 211.0, 213.0, 215.0, 217.0, 219.0], dtype=float)

model.fit(x, y, epochs=500)

print(f"Model predicted: {model.predict(np.array([10.0]), verbose=0).item():.5f}")