Angle = Abs[Arg[(#1 - #2)/(#3 - #2)]]*180/Pi &
Belongs = Im[((#1-#2) / ({#3 - #2}))] == 0 & 
eqs = ToExpression[$ScriptCommandLine[[2]]]
vars = ToExpression[$ScriptCommandLine[[3]]]


(* eqs = {
        Abs[A - B] + Abs[A - C] + Abs[B - C] == 5, 
        Abs[A - B] == 2, 
        Abs[A - C] == 1, 
        Abs[B - C] == answer}
vars = {A, B, C, answer} *)
Write[Streams["stderr"], vars]
fixing = If[Length[vars] < 3, {}, {vars[[1]] == 0, Re[vars[[2]]] == 0}]
full = Join[eqs, fixing]
Write[Streams["stderr"], full]
instance = FullSimplify[FindInstance[full, vars, Reals, 1]]
instance = If[Length[instance]==0, FullSimplify[FindInstance[full, vars, 1]], instance]
extract = N[(answer /. # /. ConditionalExpression[e_, _] :> ConditionalExpression[e, True])[[1]]] &

(* solved = FullSimplify[Solve[eqs, answer, 
        MaxExtraConditions -> All]] *)
        
Print[extract[instance]]