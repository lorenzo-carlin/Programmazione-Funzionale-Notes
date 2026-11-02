## Tipi di dati astratti

Quando definiamo una nuova struttura dati e non nascondiamo la sua specifica implementazione, noi potremmo tranquillamente lavorare sulla struttura interna del tipo di dato invece che utilizzare i metodi definiti apposta per interagire con essa.

Con l'astrazione dei dati si vuole **nascondere l'implementazione interna** del tipo di dato, che allo user deve essere invisibile. Si vuole **separare l'interfaccia dall'implementazione**.

> **Esempio**
>
> Supponiamo di avere un set. Con l'astrazione possiamo chiamare su di esso le funzioni dedicate (`empty`, `union`, `insert`, `is_member`), ma non conosciamo come è implementato il set (se è un vector, una lista o altro).

In ML (come in Java) esistono dei modi per "nascondere" l'implementazione di un tipo di dato e di renderne disponibile solo l'interfaccia: `signatures` e `structures`.

## Structures e signatures

Le **`structure`** contengono una sequenza di dichiarazioni delle componenti di una struttura. Dentro una `structure` vengono definite tutte le variabili, le funzioni, le eccezioni, ... della struttura che si vuole creare.

Le **`signature`** sono la parte di "interfaccia" e contengono tutto quello che vogliamo che lo user possa vedere.

La relazione tra `structure` e `signature` è many-to-many.

> **Osservazione**
>
> Questo è il meccanismo che viene utilizzato anche quando noi chiamiamo i tipi `String`, `Int`, `Real`, ...
> Questi tipi, che noi consideriamo come "primitivi", sono però costruiti nello stesso esatto modo in cui noi possiamo costruire strutture (tipi) personalizzate.

### `Structure`

**Sintassi**:

```sml
structure <identifier> = struct
	<elements of the structure>
end
```

**Esempio**:

```sml
> structure IntLT = struct
	type t = int
	val lt = (op <)
	val eq = (op =)
end;

(* structure IntLT:
sig val eq: ''a * ''a -> bool
	val lt: int * int -> bool
	eqtype t
end *)
```

In questo caso è stata creata una struttura `IntLT` che dichiara un tipo `t` (alias di `int`) e due funzioni, `lt` e `eq`, che implementano rispettivamente il confronto minore e il confronto di uguaglianza.

**Esempio**:

```sml
structure IntDiv = struct
	type t = int
	fun lt (m, n) = (n mod m = 0)
	val eq = (op =)
end;

(* structure IntDiv:
sig val eq: ''a * ''a -> bool
	val lt: int * int -> bool
	eqtype t
end; *)
```

In questo esempio invece la struttura `IntDiv` dichiara il tipo `t` (alias di `int`) e implementa due funzioni, `lt` e `eq`, che controllano rispettivamente se un valore è divisibile per un altro e se due valori sono uguali.

> **⚠️ Attenzione**
>
> La funzione `lt` è introdotta dalla keyword `fun` perché si tratta di una definizione sintattica della funzione, ovvero stiamo definendo cosa fa quella funzione, che parametri riceve in input e cosa dà in output.
> La funzione `eq` invece è introdotta dalla keyword `val` perché di fatto stiamo assegnando l'operatore `=`, quindi un'operazione già fatta e finita. ad una funzione di nome `eq`. Stiamo facendo quindi un binding e non una definizione di funzione.

#### Long identifiers

I **long identifiers** servono per accedere alle funzioni di una struttura e, di conseguenza, usarle.

```sml
IntLT.lt (3,4);
(* val it = true: bool *)
IntDiv.lt(3,4);
(* val it = false: bool *)
IntLT.lt (3,4);
(* val it = true: bool *)
IntDiv.lt(3,4);
(* val it = false: bool *)
```

### `Signature`

Le signatures vanno più nello specifico, specificando il tipo delle variabili e delle funzioni di una struttura.

Di fatto, la **signature** è come un **contratto che una structure deve rispettare**.  Dice che una structure deve avere determinati tipi e funzioni, con determinati nomi e tipi.

**Esempio**:

```sml
signature ORDERED = sig
	type t
	val lt : t * t -> bool
	val eq : t * t -> bool
end;
```

Questo esempio ci dice che la signature `ORDERED` prevede un tipo `t` e due funzioni `lt` e `eq` con determinati tipi. Quindi tutte le structure che vogliono implementare tale signature devono avere quelle caratteristiche.

**Esempio**:

```sml
signature QUEUE = sig
	type 'a queue
	exception QueueError
	val empty : 'a queue
	val isEmpty : 'a queue -> bool
	val singleton : 'a -> 'a queue
	val insert : 'a * 'a queue -> 'a queue
	val remove : 'a queue -> 'a * 'a queue
end;
```

**Esempio**:

```sml
signature STACK =
sig
	eqtype 'a stack
	val empty: 'a stack
	val pop: 'a stack -> 'a option
	val push: 'a * 'a stack -> 'a stack
end;
```

In questo esempio ci viene detto che `'a stack` è equality type, ossia un tipo che supporta operazioni di equivalenza.

### `structure` che implementa una `signature`

La signature è "l'interfaccia", dunque all'esterno è visibile soltanto quello che è scritto all'interno della signature. Nella structure possono esserci più cose ma a noi vengono nascoste se non fanno parte della signature.

```sml
structure Stack = struct
	type 'a stack = 'a list
	val empty = []
	val push = op::
	fun pop [] = NONE
	  | pop (tos::rest) = SOME tos
end:> STACK;
```

> **⚠️ Attenzione**
>
> La dichiarazione `:>` dice che `Stack` è una implementazione della signature `STACK`. I componenti che non sono presenti nella signature non sono visibili all'esterno.

## Alberi binari di ricerca (BST)

**Proprietà fondamentale**: se `x` è la label di un nodo `n`, allora ogni label `y` nel subtree di sinistra di `n` soddisfa `lt(y,x)` (ossia $y < x$) e ogni label `y` nel subtree di destra soddisfa `lt(x,y)` (ossia $x < y$).

Per i prossimi esempi avremo bisogno di una funzione `lt` che implementi l'ordinamento.

**Esempi di funzioni di ordinamento per altri tipi**:

```sml
> fun intLT (x,y) = x < y;
(* val intLT = fn: int * int -> bool *)

> fun lower (nil) = nil
	| lower (c::cs) = (Char.toLower c)::lower (cs);
(* val lower = fn: char list -> char list *)

> fun strLT (x,y) =
    implode (lower (explode x)) < implode (lower (explode y));
(* val strLT = fn: string * string -> bool *)
```

### Trovare un elemento in un BST

Scriviamo una funzione `Lookup` che va a cercare un valore all'interno del BST:

```sml
> datatype 'a btree = Empty | Node of 'a * 'a btree * 'a btree;
(* datatype 'a btree = Empty | Node of 'a * 'a btree * 'a btree *)

> fun lookup lt Empty x = false
	| lookup lt (Node(y,left,right)) x =
		if lt(x,y) then lookup lt left x
		else if lt(y,x) then lookup lt right x
			else true;
(* val lookup = fn: ('a * 'a -> bool) -> 'a btree -> 'a -> bool *)
```

**Esempio**:

```sml
> val t = Node ("ML",
	Node ("as",
		Node ("a",Empty,Empty),
		Node ("in",Empty,Empty)
		),
	Node ("types",Empty,Empty)
	);
(* val t = Node ("ML", Node ("as", Node ("a", Empty, Empty), Node ("in", Empty,Empty)), Node ("types", Empty, Empty)): string btree *)
> lookup strLT t "function";
(* val it = false: bool *)
> lookup strLT t "ML";
(* val it = true: bool *)
```

### Inserire un elemento in un BST

Scriviamo una funzione `insert` che inserisce un valore nel BST.

```sml
> fun insert lt Empty x = Node(x,Empty,Empty)
	| insert lt (T as Node (y,left,right)) x =
		if lt (x,y) then Node (y,(insert lt left x),right)
		else if lt (y,x) then Node (y,left,(insert lt right x))
			else T;
(* val insert = fn: ('a * 'a -> bool) -> 'a btree -> 'a -> 'a btree *)

> insert strLT t "function";
(* val it = Node ("ML", Node ("as", Node ("a", Empty, Empty), Node ("in", Node ("function", Empty, Empty), Empty)), Node ("types", Empty, Empty)): string btree *)
```

### Rimuovere un elemento in un BST

Scriviamo una funzione `delete` che rimuove un elemento dal BST, se tale elemento esiste.
Come supporto, prima definiamo una funzione ausiliaria `deletemin` che, dati un BST, ritorna il BST dopo aver rimosso l'elemento con label minima (quindi quello più a sinistra).

```sml
> exception EmptyTree;
(* exception EmptyTree *)

> fun deletemin (Empty) = raise EmptyTree
	| deletemin (Node(y,Empty,right)) = (y,right)
	| deletemin (Node(w,left,right)) =
		let val (y,L) = deletemin(left)
		in (y,Node(w,L,right))
		end;
(* val deletemin = fn: 'a btree -> 'a * 'a btree *)

> fun delete lt Empty x = Empty
	| delete lt (Node(y,left,right)) x =
		if lt (x,y) then Node(y,(delete lt left x),right)
		else if lt (y,x) then Node(y,left,(delete lt right x))
			else
				case (left,right) of
					(Empty,r) => r |
					(l,Empty) => l |
					(l,r) =>
					let val (z,r1) = deletemin(r)
					in Node (z,l,r1)
					end;
(* val delete = fn: ('a * 'a -> bool) -> 'a btree -> 'a -> 'a btree *)
```

### Visitare tutti i nodi di un BST

Scriviamo una funzione che somma tutti i valori del BST.

```sml
> fun sum (Empty) = 0
	| sum (Node(a,left,right)) = a + sum (left) + sum (right);
(* val sum = fn: int btree -> int *)
```

Scriviamo una funzione che crea una lista con i nodi dell'albero visitati in pre-order.

```sml
fun preOrder (Empty) = nil
	| preOrder(Node(a,left,right)) = [a] @ preOrder (left) @ preOrder (right);
(* val preOrder = fn: 'a btree -> 'a list *)
```

## Alberi

### Dichiarazione

Datatype per descrivere un albero radicato generico, non per forza binario.

```sml
> datatype ('label) tree =
	Node of 'label * 'label tree list;
(* datatype 'a tree = Node of 'a * 'a tree list *)

> Node (1, [
	Node (2,nil),
	Node (3, [
		Node (4,nil),
		Node (5, [
			Node (7,nil)
		]),
		Node (6,nil)
	])
]);
(* val it =
Node (1, [Node (2, []), Node (3, [Node (4, []), Node (5, [Node (7, [...])]), Node (6, [])])]): int tree *)
```

### Somma dei valori dei nodi

Scriviamo una funzione `sum` che somma tutte le label dei nodi dell'albero.

```sml
> fun sum (Node(a,nil)) = a
	| sum (Node(a,t::ts)) = sum(t) + sum (Node(a,ts));
(* val sum = fn: int tree -> int *)
```

Possiamo farlo equivalentemente usando le funzioni di ordine superiore

```sml
> fun sum (Node(a,L)) = a + foldr (op +) 0 (map sum L);
(* val sum = fn: int tree -> int *)
```

## Strutture restrittive

Consideriamo una struttura `Mapping`, che manipola coppie chiave-valore, così definita:

```sml
> structure Mapping = struct
	exception NotFound;
	val create = nil;
	fun lookup (d,nil) = raise NotFound
	  | lookup (d,(e,r)::es) =
			if d=e then r
			else lookup (d,es);
	fun insert (d,r,nil) = [(d,r)]
	  | insert (d,r,(e,s)::es) =
			if d=e then (d,r)::es
			else (e,s)::insert(d,r,es)
end;
```

Ora come ora è una struttura polimorfica, lo possiamo notare facendo

```sml
> Mapping.create;
(* val it = []: 'a list *)
```

Adesso restringiamo la struttura `Mapping` e la costringiamo ad assumere solo coppie `(string, int)`, tramite una signature `SIMAPPING`, che applichiamo ad una struttura `SiMapping` a cui assegniamo `Mapping`.

```sml
> signature SIMAPPING = sig
	val create : (string * int) list;
	val insert : string * int * (string * int) list -> (string * int) list;
	val lookup : string * (string * int) list -> int
end;

> structure SiMapping : SIMAPPING = Mapping;
(* structure SiMapping: SIMAPPING *)
```

### Accesso ai campi della struttura

Per accedere alle variabili e alle funzioni definite dentro alle strutture dobbiamo sempre ricordare di anteporre il nome della struttura e un punto.

```sml
> val m = SiMapping.create;
(* val m = []: (string * int) list *)
> val m = SiMapping.insert ("in",6,m);
(* val m = [("in", 6)]: (string * int) list *)
> val m = SiMapping.insert ("a",1,m);
(* val m = [("in", 6), ("a", 1)]: (string * int) list *)
> SiMapping.lookup ("in",m);
(* val it = 6: int *)
```

### Apertura di una struttura

Se invece volessimo accedere a variabili e funzioni di una struttura senza anteporre il nome, una possibile soluzione sarebbe quella di "aprire" la struttura, ossia di portarla al livello del programma principale. Tutte le variabili e le funzioni definite nella struttura diventano quindi delle variabili e funzioni accettate dal linguaggio ML. Questa operazione di apertura si fa con la keyword `open`.

> **⚠️ Attenzione**
>
> Quando apriamo una struttura con `open` dobbiamo ricordare che tutto ciò che normalmente ha lo stesso nome di ciò che è stato definito dentro alla struttura in questione verrà rinominato. Questo potrebbe portare a situazioni di disagio non volute.

```sml
> 2 > 1;
(* val it = true: bool *)

> open String;
(* val < = fn: string * string -> bool
val <= = fn: string * string -> bool
val > = fn: string * string -> bool
… *)

> 1 > 2;
(* poly: : error: Type error in function application.
Function: > : string * string -> bool
Argument: (1, 2) : int * int
Reason:
Can't unify int (*In Basis*) with string (*In Basis*)
(Different type constructors)
Found near 1 > 2
Static Errors *)
```

## Funtori

Immaginiamo di avere una struttura `BST` che rappresenta un albero binario di tipo astratto.

```sml
> structure BST = struct
	exception EmptyTree;
	datatype 'a btree = Empty | Node of 'a * 'a btree * 'a btree;
	fun lookup lt Empty x = false
	  | lookup lt (Node(y,left,right)) x =
			if lt(x,y) then lookup lt left x
			else
				if lt(y,x) then lookup lt right x
				else true;
	fun insert lt Empty x = Node(x,Empty,Empty)
	  | insert lt (T as Node (y,left,right)) x =
			if lt (x,y) then Node (y,(insert lt left x),right)
			else
				if lt (y,x) then Node (y,left,(insert lt right x))
				else T;
	fun deletemin (Empty) = raise EmptyTree
	  | deletemin (Node(y,Empty,right)) = (y,right)
	  | deletemin (Node(w,left,right)) =
		let
			val (y,L) = deletemin(left)
		in
			(y,Node(w,L,right))
		end;
	fun delete lt Empty x = Empty
	  | delete lt (Node(y,left,right)) x =
			if lt (x,y) then Node(y,(delete lt left x),right)
			else
				if lt (y,x) then Node(y,left,(delete lt right x))
				else
					case (left,right) of (Empty,r) => r
									   | (l,Empty) => l
									   | (l,r) => let val (z,r1) = deletemin(r)
					in
						Node (z,l,r1)
					end;
end;
```

Ora vogliamo rendere questa struttura parametrica. In particolare, vogliamo definire uno `string BST`.
Per fare ciò dovremmo definire una funzione `lt` appropriata per fare i confronti e riscrivere totalmente la struttura.

```sml
> fun lower (nil) = nil
	| lower (c::cs) = (Char.toLower c)::lower (cs);
(* val lower = fn: char list -> char list *)

> fun lt (x,y) = implode (lower (explode x)) < implode (lower (explode y));
(* val lt = fn: string * string -> bool *)
```

Se ora dichiarassimo nuovamente la struttura `BST` chiamandola `StringBST` otterremmo questo output:

```sml
(* structure StringBST:
	sig
		exception EmptyTree
		datatype 'a btree = Empty |
							Node of 'a * 'a btree * 'a btree
		val delete: string btree -> string -> string btree
		val deletemin: 'a btree -> 'a * 'a btree
		val insert: string btree -> string -> string btree
		val lookup: string btree -> string -> bool
end *)
```

Possiamo notare che il tipo astratto `'a` rimane in alcuni posti.

Qui entra in gioco il concetto di **funtore**. Un funtore è una struttura che prende come argomento una struttura e ritorna una nuova struttura.

```sml
functor <identifier> (<structure name>: <signature>) = <structure definition>
```

Riprendiamo l'esempio precedente, dell'albero binario. Un funtore può prendere in ingresso una struttura con un operatore `lt` e produrre una struttura che incorpora tale operatore. Si seguono i seguenti step:

#### 1. Definiamo una signature `TOTALORDER` che va in input al funtore

Tale signature deve contenere l'operatore `lt`, per l'ordinamento.

```sml
> signature TOTALORDER = sig
	type element;
	val lt : element * element -> bool
end;

(* signature TOTALORDER = sig type element val lt: element *
element -> bool end *)
```

#### 2. Definiamo un funtore `MakeBST` che riceve una struttura `S` con signature `TOTALORDER` e produce una struttura

```sml
functor MakeBST (Lt: TOTALORDER):
	sig
		type 'label btree
		exception EmptyTree;
		val create : Lt.element btree;
		val lookup : Lt.element * Lt.element btree -> bool;
		val insert : Lt.element * Lt.element btree -> Lt.element btree;
		val deletemin : Lt.element btree -> Lt.element * Lt.element btree;
		val delete : Lt.element * Lt.element btree -> Lt.element btree
end
=
	struct
		open Lt;
		datatype 'label btree =
			Empty |
			Node of 'label * 'label btree * 'label btree;
		val create = Empty;
		fun lookup (x, Empty) = ...
		fun insert (x, Empty) = ...
		exception EmptyTree;
		fun deletemin (Empty) = ...
		fun delete (x,Empty) = ...
end;
```

#### 3. Definiamo una structure `String` con signature `TOTALORDER` e con un operatore di confronto tra stringhe

```sml
structure String: TOTALORDER =
struct
	type element = string;
	fun lt (x,y) =
		let
			fun lower (nil) = nil
			  | lower (c::cs) = (Char.toLower c)::lower (cs);
		in
			implode (lower (explode (x))) < implode (lower( explode(y)))
		end;
end;
```

#### 4. Applichiamo `MakeBST` alla structure `String` per produrre la structure desiderata

```sml
structure StringBST = MakeBST (String);
```

---

[← Torna all'Indice del Corso](../index.md)
