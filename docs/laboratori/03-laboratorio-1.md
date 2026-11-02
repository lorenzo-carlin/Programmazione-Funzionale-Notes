>[!esercizio] Esercizio 1.1
>Scrivere l'espressione per convertire:
>1. `123.45` nel numero intero inferiore più vicino
>2. `-123.45` nel numero intero inferiore più vicino
>3. `123.45` nel numero intero superiore più vicino
>4. `-123.45` nel numero intero superiore più vicino

```sml
> floor(123.45);
(* val it = 123: int *)

> floor(~123.45);
(* val it = ~124: int *)

> ceil(123.45);
(* val it = 124: int *)

> ceil(~123.45);
(* val it = ~123: int *)
```

>[!esercizio] Esercizio 1.2
>Scrivere l'espressione per convertire:
>1. `#"Y"` a un intero
>2. `120` a un carattere
>3. `97.0` a un carattere
>4. `#"N"` a un reale
>5. `#"Z"` a una stringa

```sml
> ord(#"Y");
(* val it = 89: int *)

> chr(120);
(* val it = #"x": char *)

> chr(floor(97.0));
(* val it = #"a": char *)

> real(ord(#"N"));
(* val it = 78.0: real *)

> str(#"Z");
(* val it = "Z": string *)
```

>[!esercizio] Esercizio 1.3
>Come possiamo correggere gli errori in queste espressioni?
>1. `ceil(4);`
>2. `if true then 5+6 else 7.0;`

```sml
> ceil(4.0);
(* val it = 4: int *)

> if true then 5+6 else 7;
(* val it = 11: int *)
```

>[!esercizio] Esercizio 1.4
>Come possiamo fixare gli errori in queste espressioni?
>1. `if 0 then 1 else 2;`
>2. `ord("a")`

```sml
> if false then 1 else 2;
(* val it = 2: int *)

> ord(#"a");
(* val it = 97: int *)
```

>[!esercizio] Esercizio 1.5
>Correggi le seguenti espressioni:
>1. `explode ["bar"];`
>2. `implode (#"a", #"b");`
>3. `["r"]::["a", "t"];`

```sml
> explode "bar";
(* val it = [#"b", #"a", #"r"]: char list *)

> implode [#"a", #"b"];
(* val it = "ab": string *)

> "r"::["a", "t"];
(* val it = ["r", "a", "t"]: string list *)
```

>[!esercizio] Esercizio 1.6
>Dai esempi di questi tipi di oggetti, senza usare liste vuote:
>1. `int list list list`
>2. `(int * char) list`
>3.  `string list * (int * (real * string)) * int`

```sml
> [[[1, 2], [3, 4]], [[5, 6], [7, 8]]];
(* val it = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]: int list list list *)

> [(1, #"a"), (2, #"b"), (3, #"c")];
(* val it = [(1, #"a"), (2, #"b"), (3, #"c")]: (int * char) list *)

> (["ciao", "amico"], (27, (13.10, "auguri")), 18);
(* val it = (["ciao", "amico"], (27, (13.1, "auguri")), 18): string list * (int * (real * string)) * int *)
```

>[!esercizio] Esercizio 1.7
>Dai esempi di questi tipi di oggetti, senza usare liste vuote:
>1. `((int * int) * (bool list) * real) * (real * string)`
>2. `(bool * int) * char`
>3. `real * int list list list list`

```sml
> (((1, 2), [true, true, false], 3.4), (5.6, "ciao"));
(* val it = (((1, 2), [true, true, false], 3.4), (5.6, "ciao")): ((int * int) * bool list * real) * (real * string) *)

> ((true, 1), #"a");
(* val it = ((true, 1), #"a"): (bool * int) * char *)

> (1.2, [[[[1, 2], [3, 4]], [[5, 6], [6, 7]]], [[[8, 9], [10, 11]], [[12, 13], [14, 15]]]]);
(* val it = (1.2, [[[[1, 2], [3, 4]], [[5, 6], [6, 7]]], [[[8, 9], [10, 11]], [[12, 13], [14, 15]]]]): real * int list list list list *)
```
