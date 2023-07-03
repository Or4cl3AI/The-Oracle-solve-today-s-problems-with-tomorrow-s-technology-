import sklearn

def generate_solution(problem):

  """Generates a solution to a video game design problem."""

  if problem == 'create a new game mechanic':

    return sklearn.linear_model.LogisticRegression()

  elif problem == 'balance a game':

    return sklearn.ensemble.RandomForestClassifier()

  else:

    return sklearn.neighbors.KNeighborsClassifier()