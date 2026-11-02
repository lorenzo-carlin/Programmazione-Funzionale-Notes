
---

>[!esercizio] Esercizio 3.1
>Scrivere una funzione `fact` che calcola il fattoriale di `n` ( > 1).

```sml
> fun fact (n) =
    if n = 0 then 1
    else fact(n-1)*n;
(* val fact = fn: int -> int *)
> fact(1);
(* val it = 1: int *)
> fact(10);
(* val it = 3628800: int *)
```

>[!esercizio] Esercizio 3.2
>Scrivere una funzione `cyclei` che, dato un intero `i` e una lista `L = [a1, ..., an]`, cicla la lista `L` per `i` volte, ossia produce `[a_i+1, a_i+2, ..., a_n, a_1, ... a_i]`.

```sml
> fun cyclei (i, L) =
    if i = 0 then L
    else cycle(i-1, tl(L)@[hd(L)]);
(* val cyclei = fn: int * 'a list -> 'a list *)
> cyclei(2,[1,2,3,4]);
(* val it = [3, 4, 1, 2]: int list *)
> cyclei(4,["a","b","c","d","e"]);
(* val it = ["e", "a", "b", "c", "d"]: string list *)
```

>[!esercizio] Esercizio 3.3
>Scrivere una funzione `duplicate` che duplica ogni elemento di una lista. Quindi, data la lista `L = [a_1, ..., a_n], restituisce [a_1, a_1, a_2, a_2, ..., a_n, a_n]`.

```sml
> fun duplicate (L) =
    if L = nil then nil
    else [hd(L)] @ [hd(L)] @ duplicate(tl(L));
(* val duplicate = fn: ''a list -> ''a list *)
> duplicate([1,2,3,4]);
(* val it = [1, 1, 2, 2, 3, 3, 4, 4]: int list *)
> duplicate(["a","b","c"]);
(* val it = ["a", "a", "b", "b", "c", "c"]: string list *)
```

>[!esercizio] Esercizio 3.4
>Scrivere una funzione `len` che calcola la lunghezza di una lista.

```sml
> fun len (L) =
    if L = nil then 0
    else len(tl(L))+1;
(* val len = fn: ''a list -> int *)
> len([1,2,3,4]);
(* val it = 4: int *)
> len(["a","b","c"]);
(* val it = 3: int *)
```

>[!esercizio] Esercizio 3.5
>Scrivere una funzione `pow` che calcola $x^i$, dove `x` è un numero reale e `i` un intero non negativo.

```sml
> fun pow(x:real, i:int) =
    if i = 0 then 1.0
    else x*pow(x, i-1);
(* val pow = fn: real * int -> real *)
> pow(2.1, 3);
(* val it = 9.261: real *)
> pow(2.0, 3);
(* val it = 8.0: real *)
```

>[!esercizio] Esercizio 3.6
>Scrivere una funzione `maxList` che calcola l'elemento maggiore di una lista di stringhe (in ordine lessicografico). La lista è non vuota.

```sml
> fun max(a: string, b: string) =
    if a > b then a
    else b;

> fun maxList(L: string list) =
    if L = nil then "a"
    else max(hd(L), maxList(tl(L)));
  
(* val max = fn: string * string -> string
val maxList = fn: string list -> string *)
> maxList(["a","abc","ab"]);
(* val it = "abc": string *)
```

> La teoria del pattern matching è nella pagina [07. Pattern matching](../teoria/07-pattern-matching.md).

>[!esercizio] Esercizio 3.7
>Scrivere la funzione `fact` che calcola il fattoriale, usando i pattern.

```sml
> fun fact (0) = 1
    | fact (n) = n*fact(n-1);
(* val fact = fn: int -> int *)
> fact(1);
(* val it = 1: int *)
> fact(10);
(* val it = 3628800: int *)
```

>[!esercizio] Esercizio 3.8
>Scrivere la funzione `cycle1` che cicla una lista di una posizione usando i pattern. Se la lista è vuota, ritornare la lista vuota.

```sml
> fun cycle1 (nil) = nil
    | cycle1 (L) = tl(L) @ [hd(L)];
(* val cycle1 = fn: 'a list -> 'a list *)
> cycle1([1,2,3,4,5]);
(* val it = [2, 3, 4, 5, 1]: int list *)
> cycle1([1]);
(* val it = [1]: int list *)
> cycle1(nil);
(* poly: : warning: The type of (it) contains a free type variable. // Setting it to a unique monotype.
val it = []: _a list *)
```

>[!esercizio] Esercizio 3.9
>Scrivere una funzione `cycleip` che, dato un intero `i` e una lista `L` = $[a_1, ..., a_n]$, cicla la lista per `i` volte, ossia produce $[a_i+1, a_i+2, ..., a_n, a_1, ..., a_i]$.

```sml
> fun cycleip (0, L) = L
    | cycleip (n, L) = cycleip(n-1, tl(L) @ [hd(L)]);
(* val cycleip = fn: int * 'a list -> 'a list *)
> cycleip(2,[1,2,3,4]);
(* val it = [3, 4, 1, 2]: int list *)
> cycleip(4,["a","b","c","d","e"]);
(* val it = ["e", "a", "b", "c", "d"]: string list *)
```

>[!esercizio] Esercizio 3.10
>Scrivere una funzione `duplicatep` che duplica ogni elemento di una lista, usando i pattern.

```sml
> fun duplicatep (nil) = nil
    | duplicatep (L) = [hd(L)] @ [hd(L)] @ duplicatep(tl(L));
(* val duplicatep = fn: 'a list -> 'a list *)
> duplicatep([1,2,3,4]);
(* val it = [1, 1, 2, 2, 3, 3, 4, 4]: int list *)
> duplicatep([2.0]);
(* val it = [2.0, 2.0]: real list *)
```

>[!esercizio] Esercizio 3.11
>Scrivere una funzione `power` che calcola $x^i$ , dove `x` è un reale e `i` è un intero non negativo.

```sml
> fun power (n, 0) = 1.0
    | power (n, i) = n*power(n, i-1);
(* val power = fn: real * int -> real *)
> power(2.1,3);
(* val it = 9.261: real *)
> power(2.0,3);
(* val it = 8.0: real *)
```

>[!esercizio] Esercizio 3.12
>Scrivere una funzione `maxList` che calcola il massimo di una lista di reali, assumendo che la lista sia non vuota.

```sml
> fun max (a: real, b: real) =
    if a > b then a
    else b;

> fun maxList (nil) = 0.0
    | maxList (L: real list) = max(hd(L), maxList(tl(L)));

(* val max = fn: real * real -> real
val maxList = fn: real list -> real *)
> maxList([2.0]);
(* val it = 2.0: real *)
> maxList([2.0,5.1,4.2]);
(* val it = 5.1: real *)
```