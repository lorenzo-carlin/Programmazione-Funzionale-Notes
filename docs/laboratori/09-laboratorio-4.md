> **Esercizio 4.1**
>
> Scrivere una funzione `flip` che flippa gli elementi alternati, usando i pattern. Se la dimensione della lista è dispari, si lasci l'ultimo elemento invariato.
> Quindi la lista $[a_1,a_2,...,a_{n-1},a_n]$ diventa $[a_2,a_1,...,a_n,a_{n-1}]$.

```sml
> fun flip (nil) = (nil)
	| flip ([a]) = ([a])
	| flip (a::b::xs) = (b::a::flip(xs));
(* val flip = fn: 'a list -> 'a list *)
> flip [1,2,3,4,5];
(* val it = [2, 1, 4, 3, 5]: int list *)
> flip [1,2,3,4];
(* val it = [2, 1, 4, 3]: int list *)
```

> **Esercizio 4.2**
>
> Scrivere una funzione `remove` che, data una lista `L` e un intero `i`, ritorna `L` con l'`i`-esimo elemento eliminato. Se la lunghezza di `L` è minore di `i`, ritorna `L` invariata.

```sml
> fun remove (nil, i) = nil
    | remove (L, 1) = tl(L)
    | remove (L, i) = hd(L)::remove(tl(L), i-1);
(* val remove = fn: 'a list * int -> 'a list *)
> remove([1],1);
(* val it = []: int list *)
> remove([1,2,3],3);
(* val it = [1, 2]: int list *)
> remove([1,2],3);
(* val it = [1, 2]: int list *)
```

> **Esercizio 4.3**
>
> Scrivere una funzione `square` che prende in input un intero `n` e calcola il quadrato di `n` tramite la formula $n^2 = (n-1)^2 + 2n -1$, usando i pattern.

```sml
> fun square (0) = (0)
    | square (n) = square(n-1)+2*n-1;
(* val square = fn: int -> int *)
> square(2);
(* val it = 4: int *)
> square(5);
(* val it = 25: int *)
> square(0);
(* val it = 0: int *)
```

> **Esercizio 4.4**
>
> Scrivere una funzione `flip` che prende in input una lista di coppie di interi e ordina ogni coppia in modo che il primo numero della coppia sia il minore.

```sml
> fun flip (nil) = (nil)
    | flip ((a,b)::xs) =
      if a < b then (a,b)::flip(xs)
      else (b,a)::flip(xs);
(* val flip = fn: (int * int) list -> (int * int) list *)
> flip [(1,2),(4,3)];
(* val it = [(1, 2), (3, 4)]: (int * int) list *)
> flip [(5,2),(4,3),(6,5),(1,2)];
(* val it = [(2, 5), (3, 4), (5, 6), (1, 2)]: (int * int) list *)
> flip [(1,1),(1,2)];
(* val it = [(1, 1), (1, 2)]: (int * int) list *)
> flip nil;
(* val it = []: (int * int) list *)
```

> **Esercizio 4.5**
>
> Scrivere una funzione `vowel` che prende in input una lista di caratteri e ritorna `true` se il primo elemento della lista è una vocale, usando i pattern.

```sml
> fun vowel (nil) = false
    | vowel ((#"a")::xs) = true
    | vowel ((#"e")::xs) = true
    | vowel ((#"i")::xs) = true
    | vowel ((#"o")::xs) = true
    | vowel ((#"u")::xs) = true
    | vowel (L) = false;
(* val vowel = fn: char list -> bool *)
> vowel [#"a"];
(* val it = true: bool *)
> vowel [#"b", #"c"];
(* val it = false: bool *)
> vowel [#"a", #"b"];
(* val it = true: bool *)
> vowel nil;
(* val it = false: bool *)
```

> **Esercizio 4.6**
>
> Assumiamo, per il momento, di rappresentare i set tramite liste: gli elementi possono trovarsi in qualsiasi ordine, senza ripetizioni.
> Scrivere una funzione `member(x,S)` per testare se `x` è un membro del set `S`, usando i pattern.

```sml
> fun member (x, nil) = false
    | member (x, a::xs) =
      if(x = a) then true
      else member(x, xs);
(* val member = fn: ''a * ''a list -> bool *)
> member(1, [2,3]);
(* val it = false: bool *)
> member(2, [2,3,1]);
(* val it = true: bool *)
> member(5,nil);
(* val it = false: bool *)
> member("b",["aa","c"]);
(* val it = false: bool *)
```

> **Esercizio 4.7**
>
> Scrivere una funzione `delete` che elimina l'elemento `x` dal set `S`, usando i pattern. Se `x` non appartiene al set `S`, la funzione ritorna `S` invariato.

```sml
> fun delete (x, nil) = (nil)
    | delete (x, a::xs) =
      if(x = a) then xs
      else a::delete(x, xs);
(* val delete = fn: ''a * ''a list -> ''a list *)
> delete(1,[2,3,4]);
(* val it = [2, 3, 4]: int list *)
> delete(1,[2,1,3]);
(* val it = [2, 3]: int list *)
> delete(1,nil);
(* val it = []: int list *)
> delete(#"a",[#"c",#"b",#"a"]);
(* val it = [#"c", #"b"]: char list *)
```

> **Esercizio 4.8**
>
> Scrivere una funzione `insert` che inserisce un elemento `x` nel set `S` (in qualsiasi posizione), usando i pattern. `x` viene inserita solo se non è già presente.

```sml
> fun insert (x, nil) = ([x])
    | insert (x, a::xs) =
      if(x = a) then a::xs
      else a::insert(x, xs);
(* val insert = fn: ''a * ''a list -> ''a list *)
> insert(2,[3,4,5]);
(* val it = [3, 4, 5, 2]: int list *)
> insert(3,[3,4,5]);
(* val it = [3, 4, 5]: int list *)
> insert(2, nil);
(* val it = [2]: int list *)
> insert (#"a",[#"b",#"c"]);
(* val it = [#"b", #"c", #"a"]: char list *)
```

> **Esercizio 4.9**
>
> Scrivere una funzione `insertAll` che prende un elemento `a` e una lista `L` e inserisce `a` come primo elemento di ogni elemento di `L`.

```sml
> fun insertAll (a, nil) = (nil)
    | insertAll (a, x::xs) = ([a]@x)::insertAll(a,xs);
(* val insertAll = fn: 'a * 'a list list -> 'a list list *)
> insertAll(1,[[2,3],[],[3]]);
(* val it = [[1, 2, 3], [1], [1, 3]]: int list list *)
> insertAll(1,nil);
(* val it = []: int list list *)
> insertAll(#"c",[[#"a",#"t"],[#"a",#"r"],nil]);
(* val it = [[#"c", #"a", #"t"], [#"c", #"a", #"r"], [#"c"]]: char list list *)
```

> **Esercizio 4.10**
>
> Scrivere una funzione `powerSet` che prende una lista `L` e produce l'insieme delle parti di `L` (in qualsiasi ordine).

```sml
> fun insertAll (a, nil) = (nil)
    | insertAll (a, x::xs) = ([a]@x)::insertAll(a,xs);

> fun powerSet (nil) = ([[]])
    | powerSet (x::xs) = (powerSet(xs)@insertAll(x,powerSet(xs)));

(* val insertAll = fn: 'a * 'a list list -> 'a list list
val powerSet = fn: 'a list -> 'a list list *)
> powerSet([3]);
(* val it = [[], [3]]: int list list *)
> powerSet([1,2,3]);
(* val it = [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]: int list list *)
> powerSet nil;
(* poly: : warning: The type of (it) contains a free type variable. Setting it to a unique monotype.
val it = [[]]: _a list list *)
> powerSet[#"a",#"c"];
(* val it = [[], [#"c"], [#"a"], [#"a", #"c"]]: char list list *)
```

> **Esercizio 4.11**
>
> Scrivere una funzione `prodDiff` che, data una lista di reali $[a_1,...,a_n]$, calcoli $\displaystyle \prod_{i < j} (a_i - a_j)$.

```sml
> fun mulDif (x, nil) = 1.0
    | mulDif (x, a::xs) = (x-a)*mulDif(x,xs);

> fun prodDiff (nil) = 1.0
    | prodDiff ([x]: real list) = 1.0
    | prodDiff (x::xs) = mulDif(x, xs)*prodDiff(xs);

(* val mulDif = fn: real * real list -> real
val prodDiff = fn: real list -> real *)
> prodDiff([1.0,2.0,3.0]);
(* val it = ~2.0: real *)
> prodDiff(nil);
(* val it = 1.0: real *)
```

> **Esercizio 4.12**
>
> Scrivere una funzione `is_one` che ritorna `"one"` se il parametro passato è `1` e `"anything else"` altrimenti, usando il costrutto `case` e il pattern matching con `fun` e `fn`.

```sml
> fun is_one (1) = "one"
    | is_one (_) = "anything else";
(* val is_one = fn: int -> string *)

> fun is_one_case x = case x of
      1 => "one"
    | _ => "anything else";
(* val is_one_case = fn: int -> string *)

> val is_one_fn = fn 1 => "one" | _ => "anything else";
(* val is_one_fn = fn: int -> string *)

> is_one(1);
(* val it = "one": string *)
> is_one(3);
(* val it = "anything else": string *)
> is_one_case(1);
(* val it = "one": string *)
> is_one_fn(3);
(* val it = "anything else": string *)
```
