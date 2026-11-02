## Input e Output in ML

Dal momento che uno dei principi fondanti del paradigma di programmazione funzionale è di non avere side effects, input e output non dovrebbero essere ammessi. Nonostante ciò, ML permette di effettuarli.

### Output

Il comando `print()` stampa una stringa.

```sml
> print;
(* val it = fn: string -> unit *)
```

> **Osservazione**
>
> Il tipo di `print` è `string -> unit`.
> `unit` è usato per espressioni e funzioni che non ritornano nulla ed ha un unico valore: `()`.

```sml
> print ("ab");
(* abval it = (): unit *)
> print ("ab\n");
(* ab
val it = (): unit *)
> fun testZero(0) = print("zero\n")
	| testZero(_) = print("not zero\n");
(* val testZero = fn: int -> unit *)
> testZero(2);
(* not zero
val it = (): unit *)
```

Per stampare un valore che ha tipo diverso da `string` è necessario usare funzioni di casting che trasformano altri tipi in `string`, permettendo di stamparli. Di seguito alcuni esempi:

- stampare un carattere:

```sml
> val c = #"a";
(* val c = #"a": char *)
> str;
(* val it = fn: char -> string *)
> print(str(c));
(* aval it = (): unit *)
```

- stampare un **reale**:

```sml
> val x = 1.0E50;
(* val x = 1E50: real *)
> print(Real.toString(x));
(* 1E50val it = (): unit *)
```

- stampare un **intero**:

```sml
> print(Int.toString(123));
(* 123val it = (): unit *)
```

- stampare un **booleano**:

```sml
> print(Bool.toString(true));
(* trueval it = (): unit *)
```

### Compound statements

ML dà anche la possibilità di scrivere dei **compound statements**, che permettono di eseguire più comandi nella stessa linea di codice. Ritornano molto utili per le stampe.

```sml
> (print(Real.toString(1.0E50)); print(Int.toString(123)) );
(* 1E50123val it = (): unit *)
```

> **Osservazione**
>
> Il tipo di un compound statement è sempre quello dell'ultimo statement che contiene.

### Input in ML

ML mette a disposizione numerose funzioni per la lettura in **input da un file di testo**. Di seguito sono riportate le principali:

(si assuma che il file in lettura sia come segue)

```text
12
ab
```

- **apertura** di un file:

```sml
> val infile = TextIO.openIn("test");
(* val infile = ?: TextIO.instream  *)
```

- **controllo** se è stata raggiunta la **fine dello stream**:

```sml
> TextIO.endOfStream(infile);
(* val it = false: bool *)
```

- **lettura di n caratteri** (in questo caso 4):

```sml
> TextIO.inputN(infile,4);
(* val it = "12\na": string *)
> TextIO.inputN(infile,1);
(* val it = "b": string *)
> TextIO.inputN(infile,1);
(* val it = "\n": string *)
```

- **lettura di una riga** intera:

```sml
> val infile = TextIO.openIn("test");
(* val infile = ?: TextIO.instream *)
> TextIO.inputLine(infile);
(* val it = SOME "12\n": string option *)
> TextIO.inputLine(infile);
(* val it = SOME "ab\n": string option *)
> TextIO.inputLine(infile);
(* val it = NONE: string option *)
```

> **Osservazione**
>
> Il tipo di ritorno di queste ultime funzioni è **`string option`**. In generale, `T option` vale:
>
> - `SOME v`, se il valore da ritornare è `v` di tipo `T`
> - `NONE`, altrimenti
>
> È utile perché permette, ad esempio, di accorgersi di quando siamo arrivati al termine dello stream.

- **chiusura** del file:

```sml
> TextIO.closeIn(infile);
(* val it = (): unit *)
```

- **lettura del file completo**:

```sml
> val infile = TextIO.openIn ("test");
(* val infile = ?: TextIO.instream *)
> val s = TextIO.input (infile);
(* val s = "12\nab\n": string *)
```

- **lettura** di un **singolo carattere**:

```sml
> TextIO.input1;
(* val it = fn: TextIO.instream -> char option *)
```

> **Osservazione**
>
> Queste funzioni di I/O possono essere usate anche all'interno di altre funzioni da noi definite.

> **Esercizio**
>
> Scrivere una funzione `makeList1` che legge i caratteri di un file e li mette in una lista.

```sml
> fun makeList1 (infile, NONE) = nil
	| makeList1 (infile, SOME c) = c::makeList1(infile, TextIO.input1(infile));
(* val makeList1 = fn: TextIO.instream * char option -> char list *)
> fun makeList(infile) = makeList1(infile, TextIO.input1(infile));
(* val makeList = fn: TextIO.instream -> char list *)
```

- **lettura del prossimo carattere**, **senza modificare lo stream**:

```sml
> TextIO.lookahead;
(* val it = fn: TextIO.instream -> char option *)
```

- **controllo** di quanti caratteri sono disponibili nello stream, fino a un massimo di `n` (ritorna `SOME m`, con `m <= n`, oppure `NONE` a fine stream)

```sml
> TextIO.canInput;
(* val it = fn: TextIO.instream * int -> int option *)
> TextIO.canInput(infile,50);
(* val it = SOME 10: int option *)
```

Per trasformare un tipo `'a option` nel rispettivo tipo `'a` si usa la funzione `valOf`. Se però il valore è `NONE`, solleva l'eccezione `Option`.

```sml
> valOf;
(* val it = fn: 'a option -> 'a *)
> fun convert (a: 'a option) = valOf(a);
(* val convert = fn: 'a option -> 'a *)
```

## Eccezioni in ML

Esempi di **eccezioni predefinite** in ML:

```sml
> 5 div 0;
(* Exception- Div raised *)
> hd (nil: int list);
(* Exception- Empty raised *)
> tl (nil: real list);
(* Exception- Empty raised *)
> chr (500);
(* Exception- Chr raised *)
```

È possibile anche definire noi delle **eccezioni personalizzate**:

```sml
> exception Foo;
(* exception Foo *)
> Foo;
(* val it = Foo: exn *)
> raise Foo;
(* Exception- Foo raised *)
```

> **Osservazione**
>
> `exn` è il tipo delle eccezioni.

> **Esempio**
>
> Scriviamo una funzione che calcola $\binom{n}{m}$.

```sml
> exception BadN;
(* exception BadN *)
> exception BadM;
(* exception BadM *)
> fun comb(n,m)=
	if n<0 then raise BadN
	else if m<0 orelse m>n then raise BadM
	else if m=0 orelse m=n then 1
	else comb(n-1,m) + comb (n-1,m-1);
(* val comb = fn: int * int -> int *)
> comb(5,2);
(* val it = 10: int *)
> comb(~1,0);
(* Exception- BadN raised *)
> comb(5,6);
(* Exception- BadM raised *)
```

È possibile definire delle eccezioni che accettano dei tipi come argomento, con la seguente sintassi:

```sml
exception <identifier> of <type>
```

```sml
> exception Foo of string;
(* exception Foo of string *)
> Foo;
(* val it = fn: string -> exn *)
> raise Foo ("bar");
(* Exception- Foo "bar" raised *)
> raise Foo(5);
(* poly: : error: Type error in function application. *)
> raise Foo;
(* poly: : error: Exception to be raised must have type exn. *)
```

Tramite la sintassi

```sml
<expression> handle <match>
```

è possibile fare **handling delle eccezioni**.

```sml
> exception OutOfRange of int * int;

> fun comb1(n,m)=
	if n <= 0 then raise OutOfRange (n,m)
	else if m<0 orelse m>n then raise OutOfRange (n,m)
	else if m=0 orelse m=n then 1
	else comb1 (n-1,m) + comb1 (n-1,m-1);
(* val comb1 = fn: int * int -> int *)

> fun comb (n,m) = comb1 (n,m) handle
	OutOfRange (0,0) => 1
	| OutOfRange (n,m) => (
		print ("out of range: n=");
		print (Int.toString(n));
		print (" m=");
		print (Int.toString(m));
		print ("\n");
		0
	);
(* val comb = fn: int * int -> int *)
```

## Polimorfismo delle funzioni in ML

Il **polimorfismo** di una funzione è la sua capacità di essere applicata a valori di tipi differenti (polimorfismo parametrico) o di avere comportamenti diversi in base ai tipi (overloading). Dal momento che ML è un linguaggio strongly typed, deve essere possibile determinare tutti i tipi prima ancora di eseguire il codice. Nonostante ciò, possiamo definire funzioni i cui tipi sono parzialmente o completamente flessibili.

> **Osservazione**
>
> Il tipo `'a` è usato per indicare il **generico tipo polimorfico**.

```sml
> fun identity (x) = x;
(* val identity = fn: 'a -> 'a *)
> identity (2);
(* val it = 2: int *)
> identity (2.0);
(* val it = 2.0: real *)
> identity (2) + floor (identity (3.5));
(* val it = 5: int *)
```

**Operatori che impongono vincoli di tipo**:

- operazioni aritmetiche: `+`, `-`, `*`, `~`
- divisioni: `/`, `div`, `mod`
- operatori di confronto: `<`, `>`, `<=`, `>=`
- connettivi booleani: `andalso`, `orelse` e `not`
- operatore di concatenazione delle stringhe: `^`
- operatori di conversione di tipi: `ord`, `chr`, `real`, `str`, `floor`, `ceil`, `round` e `trunc`

Operatori che non impongono un tipo concreto (restano polimorfici):

- costruttori e selettori delle tuple: `(..,..)`, `#1`, `#2`, ...
- costruttori e selettori delle liste: `::`, `@`, `hd`, `tl`, `nil`, `[]`
- `null`

Gli operatori di uguaglianza `=` e `<>` non sono pienamente polimorfici: richiedono tipi di uguaglianza (`''a`), come spiegato sotto.

## Uguaglianza di tipi in ML

I tipi che permettono l'uso di `=` e `<>` sono gli interi, i booleani, i caratteri, le stringhe, le tuple e le liste i cui elementi sono tipi di uguaglianza; non lo sono i reali e le funzioni.

> **Osservazione**
>
> Le variabili di tipo che sono limitate a tipi che supportano gli operatori di uguaglianza vengono indicate con `''a`.

### Esempi

```sml
> fun identity_eq(x) =
	if (x=x) then x
	else x;
(* val identity_eq = fn: ''a -> ''a *)
> identity_eq(2);
(* val it = 2: int *)
> identity_eq(2.0);
(* poly: : error: Type error in function application.
Function: identity_eq : ''a -> ''a
Argument: (2.0) : real
Reason: Can't unify ''a to real (Requires equality type)
Found near identity_eq (2.0)
Static Errors *)
```

```sml
> fun identity_t(x:''a) = x;
(* val identity_t = fn: ''a -> ''a *)
> identity_t(2);
(* val it = 2: int *)
> identity_t(2.0);
(* poly: : error: Type error in function application.
Function: identity_t : ''a -> ''a
Argument: (2.0) : real
Reason: Can't unify ''a to real (Requires equality type)
Found near identity_t (2.0)
Static Errors *)
```

```sml
> val M: ''a list=[];
(* val M = []: ''a list *)
> 2::M;
(* val it = [2]: int list *)
> val M: ''a list=[];
(* val M = []: ''a list *)
> 2.0::M;
(* poly: : error: Type error in function application.
Function: :: : real * real list -> real list
Argument: (2.0, M) : real * ''a list
Reason: Can't unify real to ''a (Requires equality type)
Found near 2.0 :: M
Static Errors *)
```

```sml
> fun first_eq(L) =
	if (hd(L)=hd(L)) then hd(L)
	else hd(L);
(* val first_eq = fn: ''a list -> ''a *)
> first_eq([2]);
(* val it = 2: int *)
> first_eq([2.0]);
(* poly: : error: Type error in function application.
Function: first_eq : ''a list -> ''a
Argument: ([2.0]) : real list
Reason: Can't unify ''a to real (Requires equality type)
Found near first_eq ([2.0])
Static Errors *)
```

> **Osservazione**
>
> Per controllare se una lista è vuota si può usare la funzione `null L`.

```sml
> fun rev3 (L) =
	if null(L) then nil
	else rev3(tl(L)) @ [hd(L)];
(* val rev3 = fn: 'a list -> 'a list *)
> rev3 [floor,trunc, ceil];
(* val it = [fn, fn, fn]: (real -> int) list *)
```
