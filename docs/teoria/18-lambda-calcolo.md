Il **Lambda calcolo** è un linguaggio di programmazione molto semplice e Turing completo. È il primo linguaggio ed è stato creato addirittura prima del concetto stesso di linguaggio di programmazione.

Il suo **scopo** è di porre delle basi matematiche formali per la programmazione funzionale.

## Breve storia del lambda-calcolo

Il lambda-calcolo viene sviluppato dal logico Alonzo Church nel 1932, stesso periodo in cui Alan Turing stava inventando la macchina di Turing in Inghilterra. Turing incontra e studia da Church a Princeton e dimostra che il lambda-calcolo, la macchina di Turing e la ricorsione generale sono equivalenti e definiscono la classe delle funzioni computabili.

Il lambda-calcolo si chiama così perché inizialmente nei primi scritti di Church la variabile $x$ veniva utilizzata per identificare la variabile di una funzione. In particolare, la lettera veniva preceduta dall'accento circonflesso. Per trovare un simbolo più comodo però fu scelto il simbolo $\lambda$.

## Obiettivo

Porre le basi matematiche per la programmazione funzionale.

Se la macchina di Turing è il fondamento matematico per i linguaggi di programmazione imperativa, il lambda calcolo è la base teorica per i linguaggi di programmazione funzionale.

## Ingredienti del $\lambda$-calcolo

1. **variabili**
2. **funzioni**, che sono delle lambda astrazioni sulle variabili
3. **applicazione** delle funzioni ai valori

>[!esempio]
>$(\lambda x.x^2)$ corrisponde alla funzione di elevamento al quadrato.
>$(\lambda x.x^2)7 = 49$ è l'applicazione di tale funzione ad un'espressione.

Un'**espressione** nel $\lambda$-calcolo può essere:
- $x$, una variabile $\in V$
- $\lambda x.e$, una funzione che prende in input un parametro $x$ e valuta l'espressione $e$
- $e_1 \space e_2$, l'applicazione di due espressioni

## Operazioni del $\lambda$-calcolo

- **Astrazione** di un termine rispetto alla variabile $x$.
  $\lambda x.e$ è la funzione che, quando applicata ad un valore $v$, produce $e$ in cui $v$ sostituisce $x$.
- **Applicazione** di una funzione ad un argomento.
  $e_1 \space e_2$ è l'applicazione di una funzione $e_1$ ad un argomento $e_2$.

## Terminologia

Nella scrittura $\lambda x.e$ abbiamo che:
- $\lambda x$ si chiama **binder**
- $e$ si chiama **corpo** (o scope) dell'astrazione

Se abbiamo $\lambda x.xy$ invece:
- $\lambda x$ è il **binder**
- $x$ è una **variabile bound**
- $y$ è una **variabile free**

### Variabili free

L'insieme delle **variabili free** di un'espressione è definito (a seconda del tipo di espressione) come:
- $F_v(x) = \{x\}$
- $F_v(\lambda x.e) = F_v(e) \setminus \{x\}$
- $F_v(e_1e_2) = F_v(e_1) \cup F_v(e_2)$

>[!esempio]
>Le variabili free dell'espressione $\lambda x.y(\lambda y.xyu)$ sono la prima $y$ e $u$.

### Variabili bound

L'insieme delle **variabili bound** di una espressione è definito (a seconda del tipo di espressione) come:
- $B_v(x) = \emptyset$
- $B_v(\lambda x.e) = \{x\} \cup B_v(e)$
- $B_v(e_1e_2) = B_v(e_1) \cup B_v(e_2)$

>[!esempio]
>Le variabili bound dell'espressione $\lambda x.y(\lambda y.xyu)$ sono $x$ e la seconda $y$.

### Convenzioni

- L'applicazione è associativa a sinistra.
  Ad esempio, $yzx$ corrisponde a $(yz)x$
- Le parentesi possono essere utilizzate per leggibilità, ma non sono necessarie
- Il corpo di una lambda si estende il più a destra possibile.
  Ad esempio, $\lambda x.x \lambda z.xzx$ corrisponde a $\lambda x.(x \lambda z.(xzx))$

>[!esercizio]
>Rendere le parentesi esplicite nella seguente espressione: $(\lambda p.pz) \lambda q.w \lambda w.wqzp$
>
>$((\lambda p.(p z)) (\lambda q.(w (\lambda w.(((w q) z) p)))))$

>[!esercizio]
>Nella seguente espressione dire quali sono, se ce ne sono, le variabili bound e a quali $\lambda$ sono associate, e quali sono free: $\lambda s.sz \lambda q.sq$
>- la prima $s$ è bound al $\lambda s$
>- la $z$ è free
>- la seconda $s$ è bound al $\lambda s$
>- la $q$ è bound al $\lambda q$

>[!esercizio]
>Nella seguente espressione dire quali sono, se ce ne sono, le variabili bound e a quali $\lambda$ sono associate, e quali sono free: $( \lambda s.sz) \lambda q.w \lambda w.wqzs$
>- la prima $s$ è bound al $\lambda s$
>- la prima $z$ è free
>- la prima $w$ è free
>- la seconda $w$ è bound al $\lambda w$
>- la $q$ è bound al $\lambda q$
>- la seconda $z$ è free
>- la seconda $s$ è free

## Riduzione-$\beta$

La **riduzione-$\beta$** è il processo che riduce le espressioni del $\lambda$-calcolo, valutandole.

>[!esempio] Esempi di riduzione-$\beta$
>- $(\lambda x.x + x)5 \to 5+5 \to 10$
>- $(\lambda x.3)5 \to 3$
>- $(\lambda x.(\lambda y.y - x)) 4 \space 5 \to (\lambda y.y - 4) 5 \to 5 - 4 \to 1$
>- $(\lambda f.f \space 3)(\lambda x.x + 1) \to (\lambda x.x + 1) 3 \to 4$

>[!esempio] Esempi generici di riduzione-$\beta$
>- $(\lambda x.x)z \to z$
>- $(\lambda x.y)z \to y$
>- $(\lambda x.x \space y)z \to z \space y$
>- $(\lambda x.x \space y)(\lambda z.z) \to (\lambda z.z)y \to y$
>- $(\lambda x. \lambda y.x \space y)z \to \lambda y.z \space y$

Come abbiamo visto dagli esempi precedenti, la riduzione-$\beta$ può essere applicata alle funzioni di ordine superiore. Consideriamo, per esempio, una funzione che data una funzione $f$ restituisca la funzione $f \circ f$: $\lambda f. \lambda x. f(fx)$
Per verificare se funziona, applichiamola alla funzione successore, definita come $\lambda y.y + 1$:
$(\lambda f. \lambda x.f(f x))(\lambda y.y + 1) \rightarrow$
$\lambda x.(\lambda y. y+1 ) (( \lambda y. y+1 ) x) \rightarrow$
$\lambda x.(\lambda y.y+1)(x+1) \rightarrow$
$\lambda x.(x+1) + 1$
Ed effettivamente $\beta$-ridurre l'espressione ci porta ad ottenere il successivo del successivo.

## Sostituzione

La sostituzione $e[e'/x]$ rimpiazza ogni occorrenza **libera** di $x$ in $e$ con $e'$.

- Se $e$ è una variabile:
  - $x[e'/x] = e'$
  - $y[e'/x] = y$, se $y \neq x$
- Se $e$ è un'applicazione $e_1 e_2$:
  $(e_1 e_2)[e'/x] = (e_1[e'/x])(e_2[e'/x])$
- Se $e$ è un'astrazione $\lambda y.e_1$:
  - se $y = x$: $(\lambda x.e_1)[e'/x] = \lambda x.e_1$ (le occorrenze di $x$ nel corpo sono bound e non si sostituiscono)
  - se $y \neq x$ e $y \notin F_v(e')$: $(\lambda y.e_1)[e'/x] = \lambda y.e_1[e'/x]$
  - se $y \neq x$ e $y \in F_v(e')$: si rinomina prima $y$ tramite $\alpha$-conversione, poi si sostituisce

## $\alpha$-equivalenza e $\alpha$-conversione

Cosa succede, invece, se abbiamo $y \in F_v(e_2)$?
Ad esempio in $(\lambda x. \lambda y.x y)y$: sostituendo banalmente $y$ al posto di $x$ otterremmo $\lambda y.y y$, ma ciò è un errore perché la $y$ era una variabile libera e diventa bound (cattura di variabile).
La soluzione è rinominare la $y$ legata dalla $\lambda$ interna. Rinominiamola, ad esempio, $v$:
$(\lambda x. \lambda y.x y)y \mapsto (\lambda x. \lambda v.x v)y \mapsto \lambda v.y v$

Due **espressioni** $e_1$ e $e_2$ si dicono **$\alpha$-equivalenti** quando differiscono solo nei nomi delle variabili bound.
Ad esempio, se $y$ non è presente nell'espressione $e$, allora $\lambda x.e \equiv_{\alpha} \lambda y.e[y/x]$.

L'$\alpha$-conversione viene usata proprio per evitare il problema di cui abbiamo parlato prima.

## Regole per la riduzione $\beta$

1. Le applicazioni sono associative verso sinistra: $M N L = (M N) L$
2. Il corpo di una $\lambda$ si estende verso destra il più possibile: $\lambda x.x \lambda z.x z x$ corrisponde a $(\lambda x.(x \lambda z.(x z x)))$
3. Se ci sono le parentesi, utilizzare le regole di precedenza dettate da esse
4. Altrimenti, la precedenza è data a sinistra
5. Attenzione a quando una variabile viene catturata, in particolare quando una variabile free diventa bound. Ciò genera un errore e si deve procedere a rinominare tale variabile.

>[!warning] Attenzione
>Le riduzioni $\beta$ non sono simmetriche.

>[!osservazione]
>Un'espressione si dice in forma normale se non si può $\beta$-ridurre ulteriormente.

Una riduzione-$\beta$ può terminare in una forma normale o può anche andare avanti all'infinito, come nell'esempio $(\lambda x.xx)(\lambda x.xx)$.

>[!teorema]
>Se $e$ può essere ridotta a $e_1$ grazie ad una riduzione-$\beta$ e $e$ può essere ridotta a $e_2$ grazie ad una riduzione-$\beta$, allora esiste un $e_3$ tale che sia $e_1$ che $e_2$ possono essere ridotti a $e_3$ tramite una riduzione-$\beta$.

>[!esercizio] Esercizio
>Ridurre alla forma normale l'espressione $(\lambda x.x(xy))(\lambda z.zx)$.

**Soluzione**:
$(\lambda x.x(xy))(\lambda z.zx) \rightarrow$
$(\lambda z.zx)((\lambda z.zx)y) \rightarrow$
$(\lambda z.zx)(yx) \rightarrow$
$(yx)x$

## Codifiche in $\lambda$-calcolo

Il $\lambda$-calcolo, per come visto finora, è molto astratto e molto limitato. Nonostante ciò, è molto potente ed espressivo:
- è Turing completo
- i booleani, le coppie, le costanti e le operazioni aritmetiche possono essere espresse tramite il $\lambda$-calcolo, vediamo come:

### Booleani

- **True** = $\lambda x. \lambda y.x$
- **False** = $\lambda x. \lambda y.y$

### Costrutto `if`

- **If a then b else c** = a b c

>[!esempio]
>- **If true then b else c** = $(\lambda x. \lambda y.x) b \; c \to (\lambda y.b)c \to b$
>- **If false then b else c** = $(\lambda x. \lambda y.y)b \; c \to (\lambda y.y)c \to c$

### Operatori booleani

- Not: $\lambda x.x \space false \space true$
- And: $\lambda x. \lambda y.x y \space false$
- Or: $\lambda x. \lambda y.x \space true \space y$

### Coppie

Codifica di una coppia $(a,b)$:
- $(a,b) = \lambda x.x \; a \; b$
- $first = \lambda f. f \; true$
- $second = \lambda f.f \; false$

### Numeri naturali

Per codificare i numeri naturali si fa uso degli assiomi di Peano:
- 0 è un numero naturale
- se `n` è un numero naturale, anche `succ(n)` lo è
Dunque si codifica 0 come $\lambda f. \lambda x.x$, e poi si applica la funzione `succ()` $n$ volte per ottenere $n$. In particolare, $n$ è rappresentato tramite la funzione di ordine superiore che mappa una funzione $f$ alla sua composizione $n$ volte.
Ricapitolando, si ha che:
- $0 = \lambda f. \lambda x.x$
- $1 = \lambda f. \lambda x. f \; x$
- $2 = \lambda f. \lambda x. f(f \; x)$
- $3 = \lambda f. \lambda x. f(f(f \; x))$
- $4 = \lambda f. \lambda x. f(f(f(f \; x)))$
- ...
La funzione `succ()` viene così definita: $succ = \lambda n.\lambda f.\lambda x.f \,(n \; f \; x)$, in quanto prende $n \; f \; x$, che è $f$ applicata $n$ volte a $x$, e vi applica $f$ ancora una volta.

### Operazioni sui numeri naturali

- verifica che un numero sia zero: $\lambda z.z(\lambda y.false)true$
- addizione: se $n$ significa "*$f$ viene applicata $n$ volte a $x$*", allora $n+m$ significa "*applica $f$ $n$ volte al risultato dell'applicazione di $f$ $m$ volte a $x$*". Da cui si ricava: $\lambda n. \lambda m. \lambda f. \lambda x. n f(m f x)$

### Considerazioni finali

La sintassi del $\lambda$-calcolo è complessa. Perciò è possibile fare un leggero abuso di notazione, utilizzando numeri, operazioni ed espressioni, come nel caso di $\lambda x.(x+2)$ o $\lambda x. if \; x = 1 \; then \; x \; else \; 0$, dove vengono usate come abbreviazioni di espressioni del $\lambda$-calcolo puro.

### Ricorsione

Supponiamo di voler scrivere la funzione ricorsiva per il calcolo del fattoriale.
$\lambda n.if \; (n = 0) \; then \; 1 \; else \; (n * (f (n-1)))$
Questa scrittura non funziona, perché non possiamo definire quale sia la variabile $f$, dal momento che non possiamo riferirci alla funzione stessa tramite un nome.
Scriviamo allora la funzione come: $G = \lambda f. \lambda n. if \; n = 0 \; then \; 1 \; else \; n * f(n-1)$
Vogliamo allora trovare una funzione $f$ tale che $f = G(f)$, dove $G$ è una funzione di ordine superiore che prende una funzione come argomento e ritorna una funzione.
Un modo per calcolare tale funzione è la **Y combinator**: $\lambda f. (\lambda x. f(xx))(\lambda x. f(xx))$
La Y combinator è una funzione che applicata a $G$ ritorna la funzione $f$ che stavamo cercando.
