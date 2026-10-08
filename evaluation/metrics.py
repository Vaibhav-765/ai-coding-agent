def evaluate_file_selection(expected, predicted):

    expected = set(expected)
    predicted = set(predicted)

    tp = len(expected & predicted)

    precision = tp / len(predicted) if predicted else 0

    recall = tp / len(expected) if expected else 0

    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall > 0
        else 0
    )

    return {
        "precision": round(precision, 2),
        "recall": round(recall, 2),
        "f1": round(f1, 2)
    }