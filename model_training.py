import tensorflow as tf
from sklearn.model_selection import train_test_split

#Split into train and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state= 42)

#Train the model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(100, activation='relu', input_shape=(X.shape[1],)))
model.add(tf.keras.layers.Dense(100, activation='relu'))
model.add(tf.keras.layers.Dense(100, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='linear'))

#Compile model
model.compile(optimizer = 'Adam', loss = 'mean_squared_error')

#fit model
model.fit(X_train, y_train, epochs = 50)

