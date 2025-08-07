import tensorflow as tf
import numpy as np

model = tf.keras.Sequential([
    tf.keras.Input(shape=[1,]),
    tf.keras.layers.Dense(units=1)
])
model.compile(optimizer='sgd', loss='mean_squared_error')

x = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
y = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(x, y, epochs=500)

print(f"Model predicted: {model.predict(np.array([10.0]), verbose=0).item():.5f}")