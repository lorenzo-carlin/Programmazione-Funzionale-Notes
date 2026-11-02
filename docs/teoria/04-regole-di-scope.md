## Inferenza di tipi in ML

ML si aspetta che:
- nella valutazione di un'**espressione aritmetica**, tutti gli operandi abbiano lo stesso tipo
- nella valutazione di un'**espressione di confronto**, entrambi gli argomenti siano dello stesso tipo
- nella valutazione di un'**espressione condizionale**, i tipi di `then` e di `else` devono essere uguali
- se un'espressione viene usata come **argomento di una funzione**, allora il parametro deve essere di quel tipo
- se l'espressione che definisce il **risultato di una funzione** è di un determinato tipo, allora la funzione ritorna tale tipo

> **Osservazione**
>
> Se non c'è modo di determinare il tipo degli argomenti di una funzione overloaded (ad esempio `+` e `*`), ML usa il tipo di default (per somme e prodotti è `int`).
>
> Se invece non c'è modo di determinare i tipi degli argomenti e gli operatori non vengono usati, viene usato il tipo generico `'a`. Se ci sono due argomenti di cui non possiamo determinare il tipo, che non vengono usati e che non hanno relazione tra loro, vengono usati i tipi generici `'a` e `'b`.

## Environment

L'**environment** è l'insieme delle associazioni tra nomi e oggetti denotabili che esistono a runtime in uno specifico punto del programma in uno specifico momento dell'esecuzione.

La **dichiarazione** è il meccanismo (implicito o esplicito) che crea le associazioni nell'environment.

Un **blocco** è una sezione del programma che è identificata da un segno di apertura e uno di chiusura (`{}` in C e Java, `let ... in ... end` in ML) che contiene la dichiarazione locale a quella regione.
Esistono:
- **blocchi associati ad una procedura**: sono il corpo di una procedura
- **blocchi in-line (anonimi)**: possono apparire in una posizione qualsiasi dove ci sono dei comandi
I blocchi possono essere annidati tra loro in ML, come in C.

L'environment in un blocco può essere suddiviso in:
- **environment locale**: variabili locali, parametri formali
- **environment non locale**: associazioni ereditate da altri blocchi esterni
- **environment globale**: contiene associazioni comuni a tutti i blocchi (ex. variabili globali)

Un environment è definito da:
1. Regole di visibilità
2. Regole di scope
3. Regole per il passaggio dei parametri
4. Politica di binding ( = associazione tra nome e oggetto denotabile)

### Regole di visibilità

Una dichiarazione locale in un blocco è visibile in questo blocco e in tutti quelli annidati, fino a quando non viene dichiarata un'altra variabile con lo stesso nome. In tale caso la prima dichiarazione rimane ma è nascosta/irraggiungibile.
Le dichiarazioni dentro a un blocco non sono visibili all'esterno di questo.

### Regole di scope

Le regole di scope specificano meglio le regole di visibilità.
Un riferimento non locale in un blocco può essere risolto in due modi:
1. **Scope statico**: nel blocco che contiene sintatticamente il blocco corrente
2. **Scope dinamico**: nel blocco che è stato eseguito immediatamente prima del blocco corrente

#### Scope statico

Un nome non locale è risolto nel blocco che lo include testualmente.

```C++
 {
	 int x = 0;
	 void fie(int n) {
		 x = n+1;
	 }
	 fie(3);
	 write(x);
	 {
		 int x = 0;
		 fie(3);
		 write(x);
	 }
	 write(x);
 }
```

In questo caso, secondo lo scope statico, viene stampato `4 0 4`, perché la variabile `x` nella funzione `fie()` è sempre quella definita la riga prima della funzione, ossia nel blocco che testualmente contiene la funzione.
Se cambiassimo il nome della seconda `x` in `y`, di fatto non cambierebbe nulla.

**Vantaggi**:
- il programma è di più facile comprensione/lettura
- il compilatore può collegare le occorrenze del nome con la loro dichiarazione corretta (=> ottimizzazione del codice)
- il compilatore ha informazioni importanti sul metodo di storage delle variabili, rendendo l'esecuzione più efficiente

ALGOL, Pascal, C/C++, Ada, Scheme, **ML** e Java **usano scope statico**.

#### Scope dinamico

Un nome non locale è risolto nel blocco che è stato attivato più recentemente e che non è stato ancora disattivato.

```C++
 {
	 int x = 0;
	 void fie(int n) {
		 x = n+1;
	 }
	 fie(3);
	 write(x);
	 {
		 int x = 0;
		 fie(3);
		 write(x);
	 }
	 write(x);
 }
```

Nello stesso esempio di prima adesso viene stampato `4 4 4`, perché la seconda chiamata a `fie(3)` viene applicata sulla `x` all'interno del secondo blocco.
In questo caso, se cambiassimo il nome della seconda `x` in `y`, l'output sarebbe decisamente diverso.

**Vantaggi**:
- si può cambiare il comportamento del programma tramite ridefinizione di variabili non locali

**Svantaggi**:
- rende più difficile la lettura del programma
- è meno efficiente

> **Esercizio 4.1**
>
> Considera il seguente frammento di codice scritto in pseudo-codice e che usa scope statico. `read(Y)` consente la lettura di `Y` da standard input.
> Qual è l'output del programma?

```C++
int X = 0;
int Y;
void fie() {
	X++;
}
void foo() {
	X++;
	fie();
}
read(Y);
if(Y > 0) {
	int X = 5;
	foo();
} else {
	foo();
}
write(X);
```

L'output è `2`, in quanto la `X` da considerare è la prima dichiarata e viene incrementata due volte: una da `fie()` e una da `foo()`.

> **Esercizio 4.2**
>
> Considera il seguente frammento di codice scritto in pseudo-codice e che usa scope dinamico.
> Qual è l'output del programma?

```C++
int X;
X = 1;
int Y;
void fie() {
	foo();
	X = 0;
}
void foo() {
	int X;
	X = 5;
}
read(Y);
if(Y > 0) {
	int X;
	X = 4;
	fie();
} else {
	fie();
}
write(X);
```

- Assumiamo `Y > 0`: `foo()` crea una sua `X` locale che sparisce quando termina la funzione; `fie()` azzera la `X` creata all'interno dell'if, che però sparisce uscendo dall'istruzione condizionale. La `X` globale non viene toccata e vale ancora 1, quindi l'output è `1`.
- Assumiamo `Y <= 0`: `foo()` lavora sempre sulla sua variabile locale, che poi scompare, mentre `fie()` inizializza a 0 la variabile globale. Dunque l'output è `0`.

> **⚠️ Attenzione**
>
> In ML si usa lo scope statico!
