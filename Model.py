import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load your data into a DataFrame
df = pd.read_csv(r"C:\Users\Mikhael\Downloads\Satria-Data\Data\trainPrototype.csv")

# Replace NaN values with an empty string
df = df.fillna("")

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.1, random_state=42)

# Convert the text data into a matrix of token counts
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Train the Logistic Regression model
clf = LogisticRegression().fit(X_train_counts, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test_counts)

# Reset the index of y_test and convert y_pred to a Series with a matching index
y_test = y_test.reset_index(drop=True)
y_pred = pd.Series(y_pred, index=y_test.index)

# Create a DataFrame with the actual labels and predicted labels
results_df = pd.DataFrame({'actual_label': y_test, 'predicted_label': y_pred})

# Write the results to a new CSV file
results_df.to_csv(r"C:\Users\Mikhael\Downloads\Satria-Data\Data\resultsPrototype1.csv", index=False)

# Print the accuracy of the model
print("Accuracy: ", accuracy_score(y_test, y_pred))


# Write the results to a new CSV file
results_df.to_csv(r"C:\Users\Mikhael\Downloads\Satria-Data\Data\resultsPrototype1.csv", index=False)