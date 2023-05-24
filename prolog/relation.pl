parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).
parent(bob, peter).
parent(peter, jim).


female(pam).
female(liz).
female(pat).
female(ann).

male(tom).
male(bob).
male(jim).
male(peter).


mother(X,Y):- parent(X,Y),female(X).
father(X,Y):- parent(X,Y),male(X).
haschild(X):- parent(X,_).
sister(X,Y):- parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.
grandFather(X,Y) :- parent(X,Z),parent(Z,Y),male(X).
grandMother(X,Y) :- parent(X,Z),parent(Z,Y),female(X).
grandparent(X,Y) :- parent(X,Z), parent(Z,Y).
husband(X,Y) :- parent(X,Z),parent(Y,Z), female(X),male(Y).
wife(X,Y) :- parent(X,Z),parent(Y,Z), female(X),male(Y).
uncle(X,Z) :- brother(X,Y), parent(Y,Z).




