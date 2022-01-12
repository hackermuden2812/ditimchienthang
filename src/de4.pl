pack([], []).
pack(L, Pack) :-pack(L, [], Pack).

pack([X], FrontPack, [[X|FrontPack]]).
pack([X,X|T], FrontPack, Pack) :-
    pack([X|T], [X|FrontPack], Pack).
pack([X,Y|T], FrontPack, [[X|FrontPack]|Pack]) :-
    X \= Y,
    pack([Y|T], [], Pack).

%tim sublist co do dai lon nhat
longest([],[]):-!.
longest([H|T],Dlist):- length(H,X),length(Dlist,M), X>M,longest(T,List).
get_longest([],L):- !
get_longest(L,N):- pack(L,DList), longest(DList,List), length(List,Len), N is Len.

