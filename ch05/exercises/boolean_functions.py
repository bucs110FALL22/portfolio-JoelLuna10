
score = int(input("Typer your score: "))

def percentage_to_letter(score):

  if score >= 90:
    score = str(score, A)
  if score < 90 and score >= 80:
    score = str(score, B)
  if score < 80 and score >= 70:
    score = str(score, C)
  if score < 70 and score >= 60:
    score = str(score, D)
  if score < 60:
    score = str(score, F)

return


def is_passing(score):

  if score != "F":
    print("You are passing the course")

return
