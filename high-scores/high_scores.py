def latest(scores):
    return scores[len(scores) - 1]


def personal_best(scores):
    sorted_scores = scores.copy()
    sorted_scores.sort(reverse=True)
    return sorted_scores[0]


def personal_top_three(scores):
    sorted_scores = scores.copy()
    sorted_scores.sort(reverse=True)
    return sorted_scores[0:3]
