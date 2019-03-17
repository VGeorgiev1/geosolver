Angle = Abs[Arg[(#1 - #2)/(#3 - #2)]]*180/Pi &
Belongs = Im[((#1-#2) / ({#3 - #2}))] == 0 && 0<=Re[((#1-#2) / ({#3 - #2}))]<=1&
AngularBisector = Abs[#1-#2] / Abs[#2-#3] == Abs[#1-#4]/Abs[#3-#4]&
(* eqs = ToExpression[$ScriptCommandLine[[2]]]
vars = ToExpression[$ScriptCommandLine[[3]]] *)

eqs = {        
 ((3) == (Abs[((A) - (B))])),
 ((4) == (Abs[((B) - (C))])),
 ((5) == (Abs[((A) - (C))])),
 (Belongs[(D),(A),(C)]),
 (AngularBisector[(A), (B), (C),(D)]),
 Angle[A,B,D] == answer
}
vars = {A, B,C,D, answer}
Write[Streams["stderr"], vars]
full = Join[eqs, fixing]
fixing = If[Length[vars] < 3, {}, {vars[[1]] == 0, Re[vars[[2]]] == 0}]
Write[Streams["stderr"], full]
instance = FullSimplify[FindInstance[full, vars, 2]]
Write[Streams["stderr"],instance]
extract = N[(answer /. # /. ConditionalExpression[e_, _] :> ConditionalExpression[e, True])[[1]]] &

(* solved = FullSimplify[Solve[eqs, answer, 
        MaxExtraConditions -> All]] *)

Print[extract[instance]]