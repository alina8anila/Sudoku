
column([], _, []).
column([Rows|Rest], Colin, [Elem|Colrest]):- % Rows, in, Ans
    nth1(Colin, Rows, Elem), %Elem=Rows[Colin]
    column(Rest, Colin, Colrest).


block(Rows, Row, Col, Ans) :-
    Rstart is ((Row-1)//3)*3 +1,
    Cstart is ((Col-1)//3)*3 +1,
    Rend is Rstart+2,
    Cend is Cstart+2,
    findall(Cell,(
        between(Rstart, Rend, Ro),
        between(Cstart, Cend, Co),
        nth1(Ro, Rows, Rowlist),
        nth1(Co, Rowlist, Cell)), Ans).

can_place(Rows, Row, Col, Val) :-
    nth1(Row, Rows, Rowlist),     
    nth1(Col, Rowlist, Cell),     
    Cell = 0,                     

    \+member(Val, Rowlist),

    column(Rows, Col, Collist),
    \+member(Val, Collist),

    block(Rows, Row, Col, Blocklist),
    \+member(Val, Blocklist).