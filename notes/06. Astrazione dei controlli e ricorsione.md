
---
## Modalità di passaggio di parametri a funzione

Una **funzione** o procedura è un pezzo di codice identificato da un nome, con un environment locale ed in grado di scambiare informazioni con il resto del codice tramite dei parametri.

Meccanismi per lo scambio di informazioni con il codice esterno:
- parametri
- valori di ritorno
- environment non locale

I parametri possono essere di tre tipologie:
1. parametri di input
2. parametri di output
3. parametri di input/output

### 1. Passaggio per valore

Viene passata una copia del parametro (o dell'r-value passato alla funzione), che viene trattata come una variabile locale.
La trasmissione avviene dal main alla funzione.
Eventuali modifiche al parametro formale non toccano il parametro attuale e, una volta che la proceduta termina, il parametro formale viene eliminato.

```C++
int y = 1;
void foo(int x) {
	x = x+1;
}
...
y = 1;
foo(y+1);
```

Quando viene chiamata `foo()` gli viene passato il parametro `y+1`, che equivale a 2. Viene quindi creata una copia di `x` e questa viene incrementata a 3. Successivamente la copia è distrutta.
Dunque, alla fine del programma, `x` non esiste e `y` è uguale a 1.

**PRO:**
- semantica più semplice
- accesso rapido al parametro formale

**CONTRO:**
- la chiamata può essere costosa se l'elemento da copiare è pesante

### Passaggio per riferimento

Alla funzione viene passato un riferimento al parametro attuale. Quest'ultimo deve essere un'espressione con l-value (= un'espressione che identifica un'area di memoria ben definita).
Il riferimento al parametro e il parametro attuale puntano alla stessa cosa (aliasing). Quindi ogni modifica fatta sul riferimento viene applicata anche al parametro attuale.
La trasmissione avviene dal main alla funzione e anche viceversa.
Alla fine della funzione il riferimento tra parametro formale e parametro attuale viene cancellato.

```C++
int y = 1;
void foo(reference int x) {
	x = x+1;
}
...
y = 1;
foo(y);
```

Quando viene chiamata la funzione `foo()` viene creata `x`, ossia un riferimento alla cella di memoria di `y`, che contiene il valore 1. Tale valore viene incrementato di 1 nella funzione e questa modifica permane anche fuori dalla funzione.
Dunque, alla fine del programma, `x` non esiste e `y` è uguale a 2.

**PRO:**
- la chiamata è più efficiente, perché non viene copiato nulla

**CONTRO:**
- la semantica è più complicata
- l'accesso al parametro formale è leggermente più lento

### Passaggio per costante

Il parametro non viene passato esplicitamente alla funzione ma è una costante (`const` in C++, `final` in Java), dunque è visibile nella funzione. Chiaramente è passato in sola lettura, non può essere modificato in nessun modo.
L'implementazione del passaggio è a discrezione del compilatore (i parametri più grossi solitamente sono passati per riferimento, mentre quelli piccoli per valore).

### Passaggio per risultato

Il parametro attuale è un'espressione il cui risultato è un l-value. Non c'è nessun collegamento tra il parametro formale e il parametro attuale nel corpo della funzione. Quando la procedura termina, il valore del parametro formale è assegnato alla variabile corrispondente all'l-value del parametro attuale.
La trasmissione avviene output-only, ossia solo dalla procedura al main.

```C++
void foo(result int x) {
	x = 8;
}
...
y = 1;
foo(y);
```

In questo caso, quando la funzione `foo()` termina il valore di `x` viene assegnato alla variabile ottenuta tramite l'value di `y`.

### Chiamata per valore risultato

Simile alla precedente, ma questa volta la trasmissione è bidirezionale, con il parametro formale che è usato come una variabile locale. Il parametro attuale deve essere un'espressione che produce un l-value.
All'inizio della funzione, il parametro attuale viene valutato e il suo r-value viene assegnato al parametro formale. Alla fine della funzione, il valore del parametro formale viene assegnato alla variabile corrispondente al parametro attuale.

```C++
void foo(value-result int x) {
	x = x+1;
}
...
y = 8;
foo(y);
```

In questo caso, quando viene chiamata `foo()`:
1. `x` viene creata come variabile locale
2. ad `x` viene assegnato il valore di `y` (8)
3. `x = x+1` (9)
4. ad `y` viene assegnato il valore di `x`
5. `x` viene distrutta

Dunque, alla fine del programma `x` non esiste e `y` è uguale a 9.

La comunicazione dunque è bidirezionale.

### Chiamata per nome

Viene creata una copia del parametro attuale nel parametro formale.
Una chiamata alla funzione `f` equivale a eseguire il corpo di `f` sopo aver sostituito i parametri attuali al parametro formale. Ogni volta che il parametro formale appare, valutiamo di nuovo quello attuale.
I parametri in questione sono di input/output, la trasmissione è bidirezionale.
Non è così semplice come appare, bisogna saper gestire variabili con lo stesso nome.
Questo metodo di passaggio di parametri a funzione non viene più usato nella programmazione imperativa.

```C++
int z, w;
void fie(name int x) {
	int y;
	y = x+1;
}
...
z = 1;
w = 2;
fie(z+w);
```

In questo caso la variabile `x` viene definita come `z+w` e quindi quando si va ad eseguire `y = x+1` in verità si ha `y = z+w+1`.

```C++
int z;
void fie(name int x) {
	int y;
	x = x+1;
	y = 0;
}
...
z = 1;
fie(z);
```

In questo caso `x` è definita come `z` e quindi quando si va ad eseguire `x = x+1` in verità si sta eseguendo anche `z = z+1`. Dunque alla fine della funzione `z` vale 2.

>[!warning] Problema
>Se, all'interno della funzione, viene dichiarata una nuova variabile con lo stesso nome di una che definisce un parametro formale, come nell'esempio seguente, il risultato sarebbe incorretto.

```C++
int x = 0;
int foo(name int y) {
	int x = 2;
	return x + y;
}
...
int a = foo(x+1);
```

Il parametro attuale `x` viene "catturato" dalla dichiarazione locale e si ha che `x+y` diventa `x+(x+1)`, ma una riga prima `x` è stata ridefinita a 2. 

Per evitare questa situazione, il parametro non deve essere valutato nell'ambiente della funzione, ma in quello del chiamante. La soluzione è di passare una coppia (*closure*) `<exp,env>` invece di passare soltanto `x+1`, con:
- `exp` che è il parametro attuale, non valutato
- `env` è l'environment al momento della chiamata
In questo modo `y` ha memoria della `x` dichiarata nell'environment del chiamante e quindi si ha `x + y = 2 + 0 + 1 = 3`.

### Esercizi

>[!esercizio] Esercizio 5.1
>Dire cosa verrà stampato dal seguente frammento di codice che usa scoping dinamico. I parametri sono passati per riferimento.

```C++
{
	int x = 2;
	int fie(reference int y) {
		x = x+y;
	}
	{
		int x = 5;
		fie(x);
		write(x);
	}
	write(x);
}
```

**Output**: `10 2`

>[!esercizio] Esercizio 5.2
>Dire cosa verrà stampato dal seguente frammento di codice che usa scoping dinamico. I parametri sono passati per nome.

```C++
{
	int x = 2;
	void fie(name int y) {
		x = x+y;
	}
	{
		int x = 5;
		{
			int x = 7;
		}
		fie(x++);
		write(x);
	}
	write(x);
}
```

**Output**: `6 7`

>[!esercizio] Esercizio 5.3
>Dire cosa verrà stampato dal seguente frammento di codice. I parametri sono passati per valore risultato.

```C++
int X = 2;
void foo(value-result int Y) {
	Y++;
	write(X);
	Y++;
}
foo(X);
write(X);
```

**Output**: `2 4`

## Ricorsione

>[!esempio] Esempio
>Scriviamo la funzione `reverse`, che inverte il contenuto di una lista.
>- Caso base: una lista vuota ritorna una lista vuota
>- Passo induttivo: concateniamo la `tail` invertita della lista alla e la `head` della lista

```sml
> fun reverse L = 
	if L = null then nil
	else reverse (tl L) @ [hd L];
(* val reverse = fn: ''a list -> ''a list *)

> reverse [1,2,3,4];
(* val it = [4, 3, 2, 1]: int list *)
> reverse ["ab", "bc", "cd"];
(* val it = ["cd", "bc", "ab"]: string list *)
```

>[!warning] Attenzione
>Se, in ML, scriviamo una funzione usando la sintassi `val <nome> = fn <param> => <expression>`, nel caso in cui la funzione sia ricorsiva bisogna aggiungere la keyword `rec`.
>In questo caso diventerebbe, `val rec <nome> = fn <param> => <expression>`.
>Ciò non è più necessario quando definiamo la funzione con `fun`.

### Ricorsione mutua

In ML, due funzioni possono chiamarsi a vicenda ricorsivamente.

>[!esempio] Esempio
>Scriviamo una funzione che prende una lista `L` e produce una lista che contiene solo gli elementi di `L` che si trovano a indice dispari (il primo, il terzo, ...).

Proviamo a scrivere tale funzione così:
```sml
> fun take(L) =
	if L = nil then nil
	else hd(L)::skip(tl(L));

> fun skip(L) =
	if L = nil then nil
	else tale(tl(L));

(* poly: : error: Value or constructor (skip) has not been declared
Found near if L = nil then nil else hd (L) :: skip (tl (L)) *)
```

Il primo tentativo non funziona, perché la `skip` viene usata prima di essere stata dichiarata. La soluzione è usare la keyword `and`, che ha sintassi come segue:

```sml
fun
	<definizione della prima funzione>
and
	<definizione della seconda funzione>
and
	...
```

Riscriviamo dunque la soluzione all'esempio precedente usando `and`:
```sml
> fun
take(L) =
	if L = nil then nil
	else hd(L) :: skip(tl(L))
and
skip(L) =
	if L = nil then nil
	else take(tl(L));
	
(* val skip = fn: ''a list -> ''a list
val take = fn: ''a list -> ''a list *)

> take([1,2,3,4,5]);
(* val it = [1,3,5]: int list *)
```
