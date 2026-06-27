def calculate_grade(score):
    """Return the letter grade for a numeric score.

    Grade rules:
      - 80 or higher: A
      - 70 to 79: B
      - 60 to 69: C
      - 50 to 59: D
      - below 50: F
    """
    try:
        score = float(score)
    except (TypeError, ValueError):
        raise ValueError("score must be a number")

    if score >= 80:
        return "A"
    if score >= 70:
        return "B"
    if score >= 60:
        return "C"
    if score >= 50:
        return "D"
    return "F"


if __name__ == "__main__":
    sample_scores = [60]
    for s in sample_scores:
        print(f"คะแนน {s} => เกรด {calculate_grade(s)}")
