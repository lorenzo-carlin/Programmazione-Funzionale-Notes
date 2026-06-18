
---

>[!esercizio] Esercizio 2.1
>Scrivere una funzione che calcola il cubo di un numero reale.

```sml
> val cube = fn n:real => n * n * n;
(* val cube = fn: real -> real *)
> fun Cube (n: real) = n * n * n;
(* val Cube = fn: real -> real *)
> cube(2.9);
(* val it = 24.389: real *)
> Cube(2.9);
(* val it = 24.389: real *)
```

>[!esercizio] Esercizio 2.2
>Scrivere una funzione `min3` che calcola il minore di una tupla di tre elementi del tipo `int*int*int`.

```sml
> fun min3 (a, b, c) =
    if a < b then
      if a < c then
        a
      else
        c
    else
      if c < b then
        c
      else
        b;      
(* val min3 = fn: int * int * int -> int *)
> min3(13, 14, 15);
(* val it = 13: int *)
```

>[!esercizio] Esercizio 2.3
>Scrivere una funzione `third` che calcola il terzo elemento di una lista (che ha almeno 3 elementi).

```sml
> fun third (l) = hd(tl(tl(l)));
(* val third = fn: 'a list -> 'a *)
> third [12, 13, 14, 15];
(* val it = 14: int *)
```
Il warning esce perché ML indica che la funzione potrebbe dare problemi con liste di meno di 3 elementi. Per il momento lo ignoriamo.

>[!esercizio] Esercizio 2.4
>Scrivere una funzione `reverse` che inverte una tupla di lunghezza 3.

```sml
> fun reverse (a, b, c) = (c, b, a);
(* val reverse = fn: 'a * 'b * 'c -> 'c * 'b * 'a *)
> reverse (12, 13, 14);
(* val it = (14, 13, 12): int * int * int *)
```

>[!esercizio] Esercizio 2.5
>Scrivere una funzione `thirdchar` che trova la stringa contenente il terzo carattere di una stringa data (la stringa ha almeno 3 caratteri).

```sml
> fun thirdchar (s:string) = str (hd(tl(tl(explode(s)))));
(* val thirdchar = fn: string -> string *)
> thirdchar ("ciao");
(* val it = "a": string *)
```

>[!esercizio] Esercizio 2.6
>Scrivere una funzione `cycle` che shifta una lista di un elemento (la lista ha almeno un elemento).

```sml
> fun cycle (l) = tl(l @ [hd(l)]);
(* val cycle = fn: 'a list -> 'a list *)
> cycle [1, 2, 3, 4, 5, 6, 7];
(* val it = [2, 3, 4, 5, 6, 7, 1]: int list *)
```

>[!esercizio] Esercizio 2.7
>Scrivere una funzione `min_max_pair` che, dati 3 interi (sotto forma di tupla), produca una coppia composta dall'elemento più piccolo e da quello più grande.

```sml
fun min3 (a, b, c) = 
  if a < b then
    if a < c then a
    else c
  else
    if c < b then c
    else b;

fun max3 (a, b, c) = 
  if a > b then
    if a > c then a
    else c
  else
    if c > b then c
    else b;

fun min_max_pair (a, b, c) = (min3(a, b, c), max3(a, b, c));

(* val min3 = fn: int * int * int -> int *)
(* val max3 = fn: int * int * int -> int *)
(* val min_max_pair = fn: int * int * int -> int * int *)

> min_max_pair (1, 2, 3);
(* val it = (1, 3): int * int *)
> min_max_pair (3, 4, 2);
(* val it = (2, 4): int * int *)
```

>[!esercizio] Esercizio 2.8
>Scrivere una funzione `sort` che, dati 3 interi (sotto forma di tupla), produca una lista ordinata dei 3.

```sml
fun sort (a, b, c) = 
  if a < b then
    if b < c then [a, b, c]
    else
      if a < c then [a, c, b]
      else [c, a, b]
  else
    if a < c then [b, a, c]
    else
      if b < c then [b, c, a]
      else [c, b, a];

(* val sort = fn: int * int * int -> int list *)

> sort (1, 2, 3);
(* val it = [1, 2, 3]: int list *)
> sort (1, 3, 2);
(* val it = [1, 2, 3]: int list *)
> sort (2, 1, 2);
```

>[!esercizio] Esercizio 2.9
>Scrivere una funzione `rnd` che arrotonda un numero reale al numero decimale più vicino.

```sml
fun rnd (x: real) = real(round(x * 10.0)) / 10.0;
(* val rnd = fn: real -> real *)
> rnd (2.56);
(* val it = 2.6: real *)
> rnd (5.678);
(* val it = 5.7: real *)
```

>[!esercizio] Esercizio 2.10
>Scrivere una funzione `rem` che, data una lista, rimuove il secondo elemento (la lista ha 2 o + elementi).

```sml
fun rem (l) = [hd(l)] @ tl(tl(l));
(* val rem = fn: 'a list -> 'a list *)
> rem [1,2,3,4];
(* val it = [1, 3, 4]: int list *)
> rem [1,2];
(* val it = [1]: int list *)
```