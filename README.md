#Eksamensdisposition
#Sushi Menu Maker 3000

##1. Indledning##
Sushi Menu Maker 3000 er et konsolbaseret program udviklet i Python. Formålet er at gøre det muligt at administrere et sushi-menukort, hvor brugeren nemt kan oprette, vise, redigere og slette forskellige typer sushi.

##2. Funktionalitet##
Programmet har en hovedmenu med følgende funktioner:
•	Opret sushi med navn, pris, ingredienser og eventuel sovs og sesam.
•	Vis menukortet grupperet efter sushi-type.
•	Rediger eksisterende sushi.
•	Slet sushi fra menukortet.
•	Sorter menukortet efter navn, pris eller nyeste.
•	Eksporter menukortet til en tekstfil ved afslutning.

Programmet anvender CRUD-principperne og validerer brugerens input for at håndtere ugyldige indtastninger.

##3. Hoveddelen – Programmets opbygning##
Programmet er opdelt i moduler med ansvar for henholdsvis brugerinteraktion, datamodeller og eksport.

**Objektorienteret programmering (OOP):**
**•	Klasser og nedarvning:** Sushi er superklasse for Nigiri og Maki, mens Uramaki nedarver fra Maki.
**•	Indkapsling:** Private attributter samt getters og setters beskytter og validerer data.
**•	Komposition:** SushiMenuMachine indeholder og administrerer en liste af sushi-objekter.
**•	Enum:** Anvendes til ingredienser og sorteringsmuligheder.

**Andre Python-koncepter:**
•	Lister, for- og while-løkker.
•	if/elif/else og match/case.
•	Inputvalidering og exception handling.
•	Sortering og filhåndtering.

##4. Konklusion
Projektet demonstrerer anvendelsen af grundlæggende Python og objektorienteret programmering i en CRUD-applikation.
En mulig forbedring er at reducere gentaget kode (DRY-princippet), særligt ved visning og eksport af menukortet.
