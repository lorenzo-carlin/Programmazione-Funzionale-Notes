## Funzioni built-in di ordine superiore

> **Osservazione**
>
> In ML le funzioni built-in sono in forma curried.

### Funzione `map`

Fa la stessa cosa della funzione `simpleMap`.
Accetta due parametri: una funzione e una lista di oggetti. Applica la funzione data ad ogni oggetto della lista e ritorna la lista dei risultati.

```sml
> map (fn x => x + 2) [1,2,3];
(* val it = [3, 4, 5]: int list *)
```

Definizione di `map`:

```sml
> fun map F =
	let
		fun M nil = nil
		  | M(x::xs) = F x :: M xs
	in
		M
	end;
(* val map = fn: ('a -> 'b) -> 'a list -> 'b list *)
```

### Funzione `foldr`

Fa la stessa cosa della funzione `reduce`, ma parte dall'elemento più a destra e procede verso sinistra.

```sml
> foldr (fn (a,b) => a+b) 2 [1,2,3]
(* val it = 8: int *)
```

Questo esempio calcola $f(1, f(2, f(3, 2))) = 1+(2+(3+2)) = 8$.

Definizione di `foldr`:

```sml
> fun foldr F y nil = y
	| foldr F y (x::xs) = F (x,foldr F y xs);
(* val foldr = fn: ('a * 'b -> 'b) -> 'b -> 'a list -> 'b *)
```

### Funzione `foldl`

Fa la stessa cosa della funzione `reduce`, ma parte dall'elemento più a sinistra e procede verso destra.

```sml
> foldl (fn (a,b) => a+b) 2 [1,2,3]
(* val it = 8: int *)
```

Questo esempio calcola $f(3, f(2, f(1, 2))) = 3 + (2 + (1 + 2)) = 8$.

### Funzione `List.filter`

Processa una lista e ritorna una nuova lista contenente solo gli elementi che soddisfano un certo predicato. Prende in input un predicato e una lista (in forma curried).

```sml
> List.filter;
(* val filter : ('a -> bool) -> 'a list -> 'a list *)
> List.filter (fn x => x mod 2 = 0) [1, 2, 3, 4, 5];
(* val it = [2, 4]: int list *)
```

## Composizione di funzioni in ML

La composizione di due funzioni $F$ e $G$ è la funzione $H$ tale che $H(x) = G(F(x))$.

```sml
> fun comp (F,G,x) = G(F(x));
(* val comp = fn: ('a -> 'b) * ('b -> 'c) * 'a -> 'c *)
> comp (fn x=> x+3, fn y=>y*y+2*y, 10);
(* val it = 195: int *)
```

### Operatore `o`

L'operatore `o` esegue la composizione di due funzioni. La prima indicata è quella più esterna nella composizione (nel caso precedente la $G$).

```sml
> fun F x = x+3;
(* val F = fn: int -> int *)
> fun G y = y*y + 2*y;
(* val G = fn: int -> int *)
> val H = G o F;
(* val H = fn: int -> int *)
> H 10;
(* val it = 195: int *)
> op o;
(* val it = fn: ('a -> 'b) * ('c -> 'a) -> 'c -> 'b *)
```

## Data types

I Data types specificano dei valori e le operazioni consentite su tali valori.
In ML possiamo definire nuovi tipi o rinominare dei tipi già esistenti.

### Rinominare tipi: `type`

Con la keyword `type` possiamo rinominare un tipo.

```sml
> type signal = int list;
(* type signal = int list *)
> val v = [1,2]: signal;
(* val v = [1, 2]: signal *)
```

È anche possibile parametrizzare una definizione di tipo. Come nel seguente esempio, dichiariamo `mapping` essere una lista di coppie di due tipi che però non vengono specificati (indicati con `'c` e `'d` ma corrispondono a `'a` e `'b`, in quanto ML da nomi ai tipi che ancora sono "generici" in ordine alfabetico).

```sml
> type ('c,'d) mapping = ('c * 'd) list;
(* type ('a, 'b) mapping = ('a * 'b) list *)
> val words = [("in",6),("a",1)] : (string,int) mapping;
(* val words = [("in", 6), ("a", 1)]: (string, int) mapping *)
```

### Creare nuovi tipi: `datatype`

Con la keyword `datatype` è possibile creare dei nuovi tipi. Necessita di due parti:
1. Il **costruttore del tipo** (nome del datatype)
2. I **costruttori dei possibili valori** che può assumere

```sml
> datatype fruit = Apple | Pear | Grape;
(* datatype fruit = Apple | Grape | Pear *)
```

In questo esempio il datatype è `fruit` e i suoi possibili valori sono `Apple`, `Pear`, `Grape`.

```sml
> fun isApple (x) = (x = Apple);
(* val isApple = fn: fruit -> bool *)
> isApple (Pear);
(* val it = false: bool *)
> isApple(Apple);
(* val it = true: bool *)
> isApple (Cherry);
(* poly: : error: Value or constructor (Cherry) has not been declared
Found near isApple (Cherry) *)
```

I costruttori dei possibili valori dei datatype possono prendere in input degli argomenti, secondo la seguente sintassi:

```sml
> datatype (<parameters>) <identifier> =
	  <first constructor expression> |
	  …
	  <last constructor expression>
```

Un costruttore può anche prendere un argomento:

```sml
> datatype fruit2 = Cherry of int;
(* datatype fruit2 = Cherry of int *)
```

In questo modo ogni espressione della forma `Cherry(intero)` è un valore di tipo `fruit2`.

Il costruttore dei valori possibili viene usato per costruire delle espressioni che sono i valori per quel tipo.

Possiamo usare questi tipi per creare unioni di tipi diversi, ad esempio possiamo definire il tipo `element` che è una coppia `('a * 'b)` ma può anche essere un singolo `'a`:

```sml
> datatype ('a,'b) element =
	P of 'a * 'b |
	S of 'a;
(* datatype ('a, 'b) element = P of 'a * 'b | S of 'a *)
> P("a",1);
(* val it = P ("a", 1): (string, int) element *)
> P(1.0,2.0);
(* val it = P (1.0, 2.0): (real, real) element *)
> S(["a","b"]);
(* val it = S ["a", "b"]: (string list, 'a) element *)
```

> **Esempio**
>
> Data una lista di `elements`, scrivere una funzione `sumElList` che somma gli interi al secondo posto, quando esistono.

```sml
> fun sumElList (nil) = 0
	| sumElList (S(x)::L) = sumElList (L)
	| sumElList (P(x,y)::L) = y + sumElList (L);
(* val sumElList = fn: ('a, int) element list -> int *)
```

### Datatypes definiti ricorsivamente

L'esempio tipico è quello dell'albero binario, in cui ogni nodo può:
- essere vuoto
- avere due figli, ognuno dei quali è a sua volta un nodo

```sml
> datatype 'label btree =
	Empty |
	Node of 'label * 'label btree * 'label btree;
(* datatype 'a btree = Empty | Node of 'a * 'a btree * 'a btree *)
```

```sml
> val myTree =
	Node("ML",
		Node("as",
			Node("a",Empty,Empty),
			Node("in",Empty,Empty)),
		Node("types",Empty,Empty)
	);

(* val myTree = Node ("ML", Node ("as", Node ("a", Empty, Empty), Node ("in", Empty, Empty)), Node ("types", Empty, Empty)): string btree *)
```

> **Esempio**
>
> Scrivere una funzione `printTree` che, data una `string btree`, stampa le label dell'albero: prima la label del primo nodo, poi quelle del suo sottoalbero di sinistra e poi quelle del suo sottoalbero di destra.

```sml
> fun printTree Empty = ()
	| printTree (Node(a,lt,rt)) = (print(a); print(" "); printTree(lt); printTree(rt));
(* val printTree = fn: string btree -> unit *)
> printTree(myTree);
(* ML as a in types val it = (): unit *)
```

### Ricorsione mutua nella definizione di datatype

Si utilizza la keyword `and`, come per le funzioni.

> **Esempio**
>
> Consideriamo i binary tree pari (ogni path dalla radice a una foglia attraversa un numero pari di nodi) e i binary tree dispari. Proviamo a definirli.

```sml
> datatype 'label evenTree =
	  Empty |
	  Enode of 'label * 'label oddTree * 'label oddTree
  and
	  'label oddTree = Onode of 'label * 'label evenTree * 'label evenTree;
(* datatype 'a evenTree = Empty | Enode of 'a * 'a oddTree * 'a oddTree
datatype 'a oddTree = Onode of 'a * 'a evenTree * 'a evenTree *)
> val t1 = Onode (1,Empty,Empty);
(* val t1 = Onode (1, Empty, Empty): int oddTree *)
> val t2 = Onode (1,Empty,Empty);
(* val t2 = Onode (1, Empty, Empty): int oddTree *)
> val t3 = Enode (3,t1,t2);
(* val t3 = Enode (3, Onode (1, Empty, Empty), Onode (1, Empty, Empty)): int evenTree *)
> val t4 = Onode (4,t3,Empty);
(* val t4 = Onode (4, Enode (3, Onode (1, Empty, Empty), Onode (1, Empty, Empty)), Empty): int oddTree *)
```
