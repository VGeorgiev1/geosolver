eqs = {Abs[A - B] + Abs[B - C] + Abs[C - A] == 5, Abs[A - B] == 2, 
  Abs[B - C] == 1, answer == Abs[A - C]}
variables = {A, B, C, answer}

listToPoints = N /@ ReIm /@ # &
substitute = variables /. # &

complexinstances = 
 FindInstance[
  Join[eqs, {variables[[1]] == 0, 
    Re[variables[[2]]] == 0}], variables, 2]
instances = listToPoints /@ substitute /@ complexinstances

Print[instances[[1]]]