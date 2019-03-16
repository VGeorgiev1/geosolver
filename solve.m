Angle[_a, _b, _c] := N[Abs[Arg[(a - b)/(c - b)]]] * 180 / Pi



eqs = ToExpression[$ScriptCommandLine[[2]]]

solved = Solve[eqs, answer, MaxExtraConditions -> All]
(* Write[Streams["stderr"], solved] *)
simplified = FullSimplify[solved]

extracted = simplified /. ConditionalExpression[e_, _] :> ConditionalExpression[e, True]

extracted2 = answer /. extracted

final = extracted2[[1]]

Print[final]