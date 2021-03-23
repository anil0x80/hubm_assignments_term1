import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-0.005*x))


def sigmoid_derivative(x):
    return 0.005 * x * (1 - x)


def read_and_divide_into_train_and_test(csv_file):
    df_rawdata = pd.read_csv(csv_file)  # create dataframe from a csv file
    df_data = df_rawdata[df_rawdata["Bare_Nuclei"] != '?']  # filter out bad columns.
    del df_data['Code_number']
    training_inputs = df_data.sample(frac=0.8, random_state=200)
    test_inputs = df_data.drop(training_inputs.index)
    training_labels = training_inputs["Class"]
    test_labels = test_inputs["Class"]
    del training_inputs['Class']
    del test_inputs['Class']
    training_inputs = training_inputs.apply(pd.to_numeric, errors='coerce').fillna(training_inputs)
    test_inputs = test_inputs.apply(pd.to_numeric, errors='coerce').fillna(test_inputs)
    return training_inputs, training_labels, test_inputs, test_labels, df_data


def run_on_test_set(test_inputs, test_labels, weights):
    tp = 0
    test_predictions = sigmoid(test_inputs.dot(weights))
    test_predictions = (test_predictions > 0.5).astype(int)

    for predicted_val, label in zip(test_predictions, test_labels):
        if predicted_val == label:
            tp += 1

    return tp / len(test_labels)


def plot_heatmap(df):
    fig, ax = plt.subplots()
    corr = df.corr()
    plt.imshow(corr)
    plt.xticks(range(9), df.columns, fontsize=8, rotation=90)
    plt.yticks(range(9), df.columns, fontsize=8)
    color_bar = plt.colorbar()
    color_bar.ax.tick_params(labelsize=8)

    for i in range(9):
        for j in range(9):
            text = ax.text(j, i, corr.values[i, j].round(1),
                           ha="center", va="center", color="w")

    plt.show()


def plot_loss_accuracy(accuracy_array, loss_array):
    plt.plot(range(2500), accuracy_array)
    plt.xlabel('# Epochs')
    plt.ylabel('Accuracy')
    plt.show()

    plt.plot(range(2500), loss_array)
    plt.xlabel('# Epochs')
    plt.ylabel('Loss')
    plt.show()


def main():
    csv_file = './breast-cancer-wisconsin.csv'
    iteration_count = 2500
    np.random.seed(1)
    weights = 2 * np.random.random((9, 1)) - 1
    accuracy_array = []
    loss_array = []
    training_inputs, training_labels, test_inputs, test_labels, df = read_and_divide_into_train_and_test(csv_file)

    for iteration in range(iteration_count):
        outputs = training_inputs.dot(weights)
        outputs = sigmoid(outputs)
        loss = training_labels.sub(outputs.squeeze())
        tuning = loss.mul(sigmoid_derivative(outputs.squeeze()))
        train = training_inputs.transpose()
        dotted = train.dot(tuning)
        weights = dotted.add(weights.squeeze())
        loss_array.append(loss.mean())
        accuracy = run_on_test_set(test_inputs, test_labels, weights)
        accuracy_array.append(accuracy)

    plot_loss_accuracy(accuracy_array, loss_array)
    plot_heatmap(df)


if __name__ == '__main__':
    main()
