> **Esercizio 5.1**
>
> Scrivere una funzione `is_lower_than5` che usa il costrutto `case` per simulare un `if-then-else` sul valore 5. Deve ritornare 1 se il valore in input è minore di 5, altrimenti ritorna 2.

```sml
> fun is_lower_than5 x = case x<5 of
      true => 1
    | false => 2;
(* val is_lower_than5 = fn: int -> int *)
> is_lower_than5(3);
(* val it = 1: int *)
> is_lower_than5(6);
(* val it = 2: int *)
> is_lower_than5(5);
(* val it = 2: int *)
```

> **Esercizio 5.2**
>
> Scrivere una funzione `thousandthPower` che, dato un numero reale `x` utilizza `let val` per calcolare $x^{1000}$.

```sml
> fun thousandthPower (x: real) =
  let
    val ten = x*x*x*x*x*x*x*x*x*x;
    val hun = ten*ten*ten*ten*ten*ten*ten*ten*ten*ten;
    val tho = hun*hun*hun*hun*hun*hun*hun*hun*hun*hun;
  in
    tho
  end;
(* val thousandthPower = fn: real -> real *)
> thousandthPower(1.0);
(* val it = 1.0: real *)
> thousandthPower(1.1);
(* val it = 2.469932918E41: real *)
```

> **Esercizio 5.3**
>
> Riscrivere la funzione `split` senza usare un pattern (la tupla) dentro a `let val`, ma usando le referenze alle componenti della tupla.

```sml
> fun split(nil) = (nil,nil)
	| split([a]) = ([a],nil)
    | split (a::b::cs) =
      let
        val M = #1 (split(cs));
        val N = #2 (split(cs));
      in
        (a::M,b::N)
	  end;
(* val split = fn: 'a list -> 'a list * 'a list *)
> split [1,2,3,4,5,6];
(* val it = ([1, 3, 5], [2, 4, 6]): int list * int list *)
> split [1,2,3,4,5];
(* val it = ([1, 3, 5], [2, 4]): int list * int list *)
```

> **Esercizio 5.4**
>
> Riscrivere la funzione `powerSet` usando `let val` e calcolando `powerSet(xs)` una volta sola.

```sml
> fun insertAll (a, nil) = (nil)
    | insertAll (a, x::xs) = ([a]@x)::insertAll(a,xs);

> fun powerSet (nil) = ([[]])
    | powerSet (x::xs) =
      let
        val t = powerSet(xs);
      in
        (t@insertAll(x,t))
      end;

(* val insertAll = fn: 'a * 'a list list -> 'a list list
val powerSet = fn: 'a list -> 'a list list *)
> powerSet([1,2,3]);
(* val it = [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]: int list list *)
```

> **Esercizio 5.5**
>
> Scrivere una funzione `sumPairs` che prende una lista di coppie di interi e ritorna una coppia di interi, dove il primo elemento è la somma di tutti i primi elementi delle coppie e il secondo quella dei secondi elementi.

```sml
> fun sumPairs(nil) = (0,0)
    | sumPairs((x,y)::xs) =
      let
        val (M,N) = sumPairs(xs);
      in
        (x+M, y+N)
      end;
(* val sumPairs = fn: (int * int) list -> int * int *)
> sumPairs([(1,2),(3,4),(5,6)]);
(* val it = (9, 12): int * int *)
> sumPairs([]);
(* val it = (0, 0): int * int *)
```

> **Esercizio 5.6**
>
> Riscrivere la funzione `maxList` per trovare il massimo in una lista di reali, usando `let val`.

```sml
> fun maxList([x:real]) = x
    | maxList(x::zs) =
      let
        val mx = maxList(zs);
      in
        if x > mx then x
        else mx
      end;
(* Es6.sml:1: warning: Matches are not exhaustive.
val maxList = fn: real list -> real *)
> maxList([1.0,3.8,4.6,5.7,2.3,3.0,5.5]);
(* val it = 5.7: real *)
```

> **Esercizio 5.7**
>
> Scrivere una funzione `doubleExp` che, dato in input un reale `x` e un intero non negativo `i`, calcoli $x^{2^i}$, facendo una sola chiamata ricorsiva.

```sml
> fun doubleExp(x:real, 0) = (x)
    | doubleExp(x:real, i:int) =
      let
        val t = doubleExp(x, i-1);
      in
        t*t
      end;
(* val doubleExp = fn: real * int -> real *)
> doubleExp(1.1,3);
(* val it = 2.14358881: real *)
```

> **Esercizio 5.8**
>
> Scrivere una funzione `sumList` che prende una lista di interi e ritorna una coppia, in cui il primo elemento è la somma degli elementi in posizione dispari e il secondo la somma di quelli in posizione pari.

```sml
> fun sumList(nil) = (0,0)
    | sumList([a]) = (a,0)
    | sumList(a::b::xs) =
      let
        val (x, y) = sumList(xs);
      in
        (a+x,b+y)
      end;
(* val sumList = fn: int list -> int * int *)
> sumList([1,2,3,4]);
(* val it = (4, 6): int * int *)
> sumList([]);
(* val it = (0, 0): int * int *)
```

> **Esercizio 5.9**
>
> Scrivere una funzione `printList` che stampa una lista di interi data in input.

```sml
> fun printList(nil) = print("")
    | printList(x::xs) =
      (print(Int.toString(x)); print("\n"); printList(xs));
(* val printList = fn: int list -> unit *)
> printList [1,2,3];
(* 1
2
3
val it = (): unit *)
> printList nil;
(* val it = (): unit *)
```

> **Esercizio 5.10**
>
> Scrivere una funzione `comb: int*int -> unit` che calcola $\binom{n}{m}$ e stampa `n`, `m` e il risultato.

```sml
> fun factorial(0) = 1
    | factorial(n) = n*factorial(n-1);

> fun comb(n,m) = print("n is " ^ Int.toString(n) ^ "\nm is " ^ Int.toString(m) ^ "\nResult is " ^ Int.toString(factorial(n) div (factorial(m)*factorial(n-m))) ^ "\n");

(* val factorial = fn: int -> int
val comb = fn: int * int -> unit *)
> comb(5,2);
(* n is 5
m is 2
Result is 10
val it = (): unit *)
```

> **Esercizio 5.11**
>
> Scrivere una funzione `printXs` che, dato un intero `n`, stampa il carattere `'X'` $2^n$ volte.

```sml
> fun printXs(0) = print("X")
    | printXs(n) = (printXs(n-1); printXs(n-1));
(* val printXs = fn: int -> unit *)
> printXs(3);
(* XXXXXXXXval it = (): unit *)
```
