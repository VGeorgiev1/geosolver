Angle = Abs[Arg[(#1 - #2)/(#3 - #2)]]*180/Pi &

eqs = ToExpression[$ScriptCommandLine[[2]]]
vars = ToExpression[$ScriptCommandLine[[3]]]


(* eqs = {
        Abs[A - B] + Abs[A - C] + Abs[B - C] == 5, 
        Abs[A - B] == 2, 
        Abs[A - C] == 1, 
        Abs[B - C] == answer}
vars = {A, B, C, answer} *)
full = Join[eqs, {vars[[1]] == 0, Re[vars[[2]]] == 0}]
Write[Streams["stderr"], full]
Write[Streams["stderr"], vars]
instance = FullSimplify[FindInstance[full, vars, 1]]

extract = N[(answer /. # /. ConditionalExpression[e_, _] :> ConditionalExpression[e, True])[[1]]] &

(* solved = FullSimplify[Solve[eqs, answer, 
        MaxExtraConditions -> All]] *)


Print[extract[instance]]