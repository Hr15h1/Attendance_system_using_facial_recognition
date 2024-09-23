from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Load the data
with open("./data/faces_data.pkl", "rb") as f:
    faces = pickle.load(f)
with open("./data/names.pkl", "rb") as f:
    names = pickle.load(f)


# Split the data
X_train, X_test, y_train, y_test = train_test_split(faces, names, test_size=0.2, random_state=42)


# Create the model
knn = KNeighborsClassifier(n_neighbors=4)

# Train the model
knn.fit(faces, names)

# Save the model
with open("./data/knn.pkl", "wb") as f:
    pickle.dump(knn, f)
