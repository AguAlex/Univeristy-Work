% Varianta 1 Agusoaei Alexandru Gabriel grupa 133
%1
%cazurile de baza in functie de numarul de elemente din lista
removeOdd([X], [X]).  %pentru nr de elemente impar
removeOdd([], []).	  %pentru nr de elemnente par

%adaugam la rezultat fiecare element de pe prima pozitie, luate elementele 2 cate 2
removeOdd([X, _ | T], [X | Rez]) :- removeOdd(T, Rez).

%Teste: 
%
%?- removeOdd([a, b, c, d, e], R).
%R = [a, c, e].
%?- removeOdd([a, b, c, d], R).
%R = [a, c]


%2
%cazurile de baza cand mai ramane un singur punct doar in una din cele 2 liste
mergePts([p(X1, Y1)], [], [p(X1, Y1)]).
mergePts([], [p(X2, Y2)], [p(X2, Y2)]).

%adaugam la rezultat punctul cu prima coordonata mai mica
mergePts([p(X1, Y1) | T1], [p(X2, Y2) | T2], [p(X1, Y1) | Rez]) :- X1 =< X2,
    mergePts(T1, [p(X2, Y2) | T2], Rez).
mergePts([p(X1, Y1) | T1], [p(X2, Y2) | T2], [p(X2, Y2) | Rez]) :- X1 > X2,
    mergePts([p(X1, Y1) | T1], T2, Rez).

%Teste:
%?- mergePts([p(2, 4), p(3, 2), p(6, 3)], [p(1, 3), p(4, 1), p(7, 7)], R).
%R = [p(1, 3), p(2, 4), p(3, 2), p(4, 1), p(6, 3), p(7, 7)].
%?- mergePts([p(2, 4), p(4, 1), p(4, 1)], [p(1, 3), p(6, 2)], R).
%R = [p(1, 3), p(2, 4), p(4, 1), p(4, 1), p(6, 2)].
%?- mergePts([p(2, 4), p(4, 1)], [p(1, 2), p(4, 1)], R).
%R = [p(1, 2), p(2, 4), p(4, 1), p(4, 1)].

%3
%folosim predicat auxiliar 
noDuplicateVar(X) :- vars(X, []).

vars(V, [V | T]) :- atom(V), not(member(V, T)).
vars(non(X), R) :- vars(X, R).
vars(si(X, Y), R) :- vars(X, T), vars(Y, U), union(T, U, R).
vars(sau(X, Y), R) :- vars(X, T), vars(Y, U), union(T, U, R).
vars(imp(X, Y), R) :- vars(X, T), vars(Y, U), union(T, U, R).

%Teste:
%?- noDuplicateVar(imp(a, si(b, c))).
%true.
%?- noDuplicateVar(imp(a, si(b, a))).
%false



