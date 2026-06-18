
---

>[!esercizio] Esercizio 6.1
>Scrivere le espressioni per:
>1. Aprire un file in lettura
>2. Leggere 5 caratteri di tale file
>3. Leggere una riga di tale file
>4. Vedere qual è il prossimo carattere sullo stream, senza leggerlo
>5. Leggere tutto il file intero
>6. Chiudere il file

```sml
> val input = TextIO.openIn("Test.txt");

> TextIO.inputN(input,5);

> TextIO.inputLine(input);

> TextIO.lookahead(input);

> TextIO.input(input);

> TextIO.closeIn(input);
```

>[!esercizio] Esercizio 6.2
>Scrivere una funzione `getList(filename)` che legge un file, estrae le parole e le mette in una lista.

```sml
> fun getWord(input: TextIO.instream) = 
    if TextIO.endOfStream(input) then ""
    else 
      let
        val c = TextIO.inputN(input, 1);
      in
        if (c = " " orelse c = "\n") then ""
        else c^getWord(input)
      end;

> fun getList(input: TextIO.instream) =
    if TextIO.endOfStream(input) then []
    else
      let
        val next = getWord(input);
      in
        next::getList(input)
      end;

(* val getWord = fn: TextIO.instream -> string
val getList = fn: TextIO.instream -> string list *)
> val input = TextIO.openIn("Test.txt");
(* val input = ?: TextIO.instream *)
> getList(input);
(* val it = ["Nel", "mezzo", "del", "cammin", "di", "nostra", "vita", "mi", "ritrovai", "per", ...]: string list
val it = (): unit *)
```

>[!esercizio] Esercizio 6.3
>Scrivere una funzione `returnThird(L)` che, data in input una lista di interi `L`, ritorna il terzo elemento. Se la lista è troppo corta, alza un'eccezione `shortList` e ne fa l'handling stampando "List too short.\n It only contains `n` elements.\n", dove `n` è il numero di elementi nella lista.

```sml
> exception shortList of int;

> fun listLength(nil) = 0
    | listLength(L: int list) = 1+listLength(tl(L));

> fun returnThird1(L) =
    let
      val size = listLength(L);
    in
      if size < 3 then raise shortList(size)
      else hd(tl(tl(L)))
    end;

> fun returnThird(L) = returnThird1(L) handle shortList(size) => (print("List too short.\n" ^ "It only contains " ^ Int.toString(size) ^ " elements.\n"); 0);

(* exception shortList of int
val listLength = fn: int list -> int
val returnThird1 = fn: int list -> int
val returnThird = fn: int list -> int *)
> returnThird([1,2,3,4]);
(* val it = 3: int *)
> returnThird([1,2]);
(* List too short.
It only contains 2 elements.
val it = 0: int *)
```

>[!esercizio] Esercizio 6.4
>Scrivere una funzione `fact` che, dato un intero `n`, ritorna $n!$ se $n > 0$, $1$ se $n = 0$ e $0$ se $n < 0$, con il messaggio di errore "Negative argument `x` found", dove `x` è l'argomento. 

```sml
> exception negativeArgument of int

> fun fact1(0) = 1
    | fact1(n) =
      if n < 0 then raise negativeArgument(n)
      else n*fact1(n-1);

> fun fact(n) = fact1(n) handle negativeArgument(n) => (print("Negative argument " ^ Int.toString(n) ^ " found\n"); 0);

(* val fact1 = fn: int -> int
exception negativeArgument of int
val fact = fn: int -> int *)
> fact(~2);
(* Negative argument ~2 found
val it = 0: int *)
> fact(0);
(* val it = 1: int *)
> fact(5);
(* val it = 120: int *)
```

>[!esercizio] Esercizio 6.5
>Scrivere una funzione `tabulate` che prende un valore iniziale `a`, un incremento `delta`, un numero di punti `n` e una funzione `F` (dai reali ai reali) e stampa una tabella con 2 colonne, rispettivamente `x` e `F(x)`, con `x` che parte da `a` e viene incrementato di `delta` `n` volte.

```sml
> fun tabulate(a, delta, 0, f) = nil
    | tabulate(a, delta, n, f) = (print(Real.toString(a) ^ " " ^ Real.toString(f(a)) ^ "\n"); tabulate(a+delta, delta, n-1, f));

(* val tabulate = fn: real * real * int * (real -> real) -> 'a list *)
> tabulate(1.0,0.1,9,fn x => x*x);
(* poly: : warning: The type of (it) contains a free type variable. Setting it to a unique monotype.
1.0 1.0
1.1 1.21
1.2 1.44
1.3 1.69
1.4 1.96
1.5 2.25
1.6 2.56
1.7 2.89
1.8 3.24
val it = []: _a list *)
```

>[!esercizio] Esercizio 6.6
>Utilizzando la funzione `simpleMap`, rimpiazzare ogni elemento negativo di una lista di reali con 0.

```sml
> fun simpleMap (F,nil) = nil
    | simpleMap (F,x::xs) = F(x) :: simpleMap(F,xs);

> fun pos (a: real) =
    if a < 0.0 then 0.0
    else a
  
(* val simpleMap = fn: ('a -> 'b) * 'a list -> 'b list
val pos = fn: real -> real *)
> simpleMap(pos, [0.0,1.0,~2.1,~2.3]);
(* val it = [0.0, 1.0, 0.0, 0.0]: real list *)
```

>[!esercizio] Esercizio 6.7
>Utilizzando la funzione `reduce`, trovare il massimo in una lista di reali.

```sml
> exception EmptyList;

> fun reduce(F, nil) = raise EmptyList
    | reduce(F, [a]) = a
    | reduce(F, x::xs) = F(x, reduce(F, xs));

> fun max(a: real, b: real) = 
    if a > b then a
    else b;

(* exception EmptyList
val reduce = fn: ('a * 'a -> 'a) * 'a list -> 'a
val max = fn: real * real -> real *)
> reduce(max, [1.1,2.2,4.4,3.3]);
(* val it = 4.4: real *)
```

>[!esercizio] Esercizio 6.8
>Utilizzando la funzione `filter`, trovare gli elementi in una lista di reali che sono maggiori di 0.

```sml
> fun filter(P, nil) = nil
    | filter(P, x::xs) =
      if P(x) then x::filter(P, xs)
      else filter(P, xs);

> fun pos(x: real) =
    if x < 0.0 then false
    else true;

(* val filter = fn: ('a -> bool) * 'a list -> 'a list
val pos = fn: real -> bool *)
> filter(pos, [1.1,~1.2,~1.3,1.4]);
(* val it = [1.1, 1.4]: real list *)
```

>[!esercizio] Esercizio 6.9
>Scrivere una funzione `readAndSum` che, dato un file di testo  contenente un numero per ogni riga, trasforma ogni riga nell'intero corrispondente e ritorna la somma di tutti questi.

```sml
> fun readAndSum1(input: TextIO.instream) =
    if TextIO.endOfStream(input) then 0
    else
      let
        val line = valOf(TextIO.inputLine(input));
        val x = valOf(Int.fromString(line));
      in
        x+readAndSum(input)
      end;

> fun readAndSum(file: string) =
    let
      val input = TextIO.openIn(file);
      val sum = readAndSum1(input);
    in
      TextIO.closeIn(input);
      sum
    end;

(* val readAndSum1 = fn: TextIO.instream -> int
val readAndSum = fn: string -> int *)
> readAndSum("numbers.txt");
(* val it = 23: int *)
```

>[!esercizio] Esercizio 6.10
>Scrivere, nella forma curried, una funzione `applyList` che prende una lista di funzioni ed un valore e applica ogni funzione a tale valore, producendo una lista dei risultati.

```sml
> fun applyList nil a = nil
    | applyList (x::xs) a = (x(a)::applyList xs a);

> fun square (x) = x*x;

> fun neg (x) = ~x;

> fun zero (x) = 0;

> fun half (x) = x div 2;

(* val applyList = fn: ('a -> 'b) list -> 'a -> 'b list
val square = fn: int -> int
val neg = fn: int -> int
val zero = fn: 'a -> int
val half = fn: int -> int *)
> applyList([square, neg, zero, half]) 10;
(* val it = [100, ~10, 0, 5]: int list *)
```
