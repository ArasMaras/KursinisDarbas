### Ataskaita apie "Tic Tac Toe" žaidimo įgyvendinimą

#### Įvadas

**Kursinio darbo tikslas**: Šio kursinio darbo tikslas yra įgyvendinti "Tic Tac Toe" žaidimą naudojant Python programavimo kalbą, demonstruojant tvirtus objektinio programavimo (OOP) principus ir projektavimo šablonus.

**Programos aprašymas**: "Tic Tac Toe" žaidimo programa leidžia dviem žmonėms žaisti vienas prieš kitą. Programa taip pat apima rezultatų lentelę, kuri seka kiekvieno žaidėjo pergales ir išsaugo šią informaciją JSON failo formatu.

**Kaip paleisti programą**:
1. Nuklonuokite repozitoriją, kurią sudaro kodas.
2. Užtikrinkite, kad jūsų sistemoje būtų įdiegta Python 3.x versija.
3. Paleiskite programą įvykdę komandą `python tic_tac_toe.py` terminalo arba komandinėje eilutėje.
4. Sekite ekrane esančius nurodymus, įveskite žaidėjų vardus ir atlikite žaidimo veiksmus.

**Kaip naudotis programa**:
- Žaidėjai paeiliui įveda savo žingsnius pasirinkdami numerį, atitinkantį laukelį 3x3 žaidimo lentelėje.
- Žaidimas tęsiasi, kol žaidėjas laimi, žaidimas baigiasi lygiosiomis arba žaidėjai nusprendžia nebetęsti žaidimo.

### Kūnas/Analizė

**Objektinio programavimo (OOP) principų įgyvendinimas**

1. **Encapsulation:**
   - **Apibūdinimas**: Inkapsuliacija yra duomenų (atributų) ir metodų (funkcijų), veikiančių su šiais duomenimis, sujungimas į vieną vienetą (klasę).
   - **Naudojimas kode**: Tokios klasės kaip `Player`, `Game` ir `ScoreBoard` inkapsuliuoja savo duomenis ir metodus, užtikrinant duomenų vientisumą ir lengvą priežiūrą.

   ```python
   class Player:
       def __init__(self, name, symbol):
           self.name = name
           self.symbol = symbol

       def get_move(self):
           try:
               move = int(input(f"Žaidėjo {self.name} ({self.symbol}) eilė. Kurią dėžutę pasirinksite? : "))
               return move
           except ValueError:
               print("Neteisinga įvestis!!! Bandykite dar kartą.")
               return self.get_move()
   ```

2. **Abstraction:**
   - **Apibūdinimas**: Abstrakcija apima vidinės įgyvendinimo detalės slėpimą ir rodo tik objekto būtiniausias savybes.
   - **Naudojimas kode**: `Player` klasė abstrahuoja proceso, kaip gauti žaidėjo ėjimą, supaprastindama sąveiką su žaidimu.

   ```python
   class Player:
       def get_move(self):
           try:
               move = int(input(f"Žaidėjo {self.name} ({self.symbol}) eilė. Kurią dėžutę pasirinksite? : "))
               return move
           except ValueError:
               print("Neteisinga įvestis!!! Bandykite dar kartą.")
               return self.get_move()
   ```

3. **Inheritance:**
   - **Apibūdinimas**: Paveldėjimas yra mechanizmas, leidžiantis vienai klasei (vaikinei klasei) įgauti savybes ir elgesį iš kitos (tėvinės) klasės.
   - **Naudojimas kode**: `HumanPlayer` klasė paveldi `Player` klasės atributus ir metodus.

   ```python
   class HumanPlayer(Player):
       pass
   ```

4. **Polymorphism:**
   - **Apibūdinimas**: Polimorfizmas leidžia skirtingų klasių objektams būti traktuojamiems kaip bendros tėvinės klasės objektai.
   - **Naudojimas kode**: Tie patys `Player` ir `HumanPlayer` klasės turi `get_move()` metodą, leidžiantį juos panaudoti keičiamai `Game` klasėje.

   ```python
   class Player:
       def get_move(self):
           try:
               move = int(input(f"Žaidėjo {self.name} ({self.symbol}) eilė. Kurią dėžutę pasirinksite? : "))
               return move
           except ValueError:
               print("Neteisinga įvestis!!! Bandykite dar kartą.")
               return self.get_move()

   class HumanPlayer(Player):
       pass
   ```

5. **Uždarumas**
   - **Apibūdinimas**: Uždarumas apibrėžia, kad klasės nariai (atributai ir metodai) yra pasiekiami tik iš tos pačios klasės arba iš jos pakopų, ne iš išorinės programos.
   - **Naudojimas kode**: Klasėse, pavyzdžiui, `Player`, `Game`, `ScoreBoard`, užtikrinamas uždarumas, apsaugant vidinius duomenis nuo tiesioginio prieigos iš išorės.

   ```python
   class Player:
       def __init__(self, name, symbol):
           self.name = name
           self.symbol = symbol
           self.__score = 0  # private attribute

       def increment_score(self):
           self.__score += 1

       def get_score(self):
           return self.__score
   ```

    ```
### Naudoti projektavimo šablonai

1. **Singletono šablonas**
   - **Apibūdinimas**: Užtikrina, kad klasė turėtų tik vieną egzempliorių ir suteikia globalų prieigą prie to egzemplioriaus.
   - **Naudojimas kode**: `ScoreBoard` klasė naudoja Singletono šabloną, kad užtikrintų, jog visoje programoje egzistuos tik vienas rezultatų lenta.

   ```python
   class ScoreBoard:
       _instance = None

       def __new__(cls):
           if cls._instance is None:
               cls._instance = super(ScoreBoard, cls).__new__(cls)
               cls._instance.scores = {}
           return cls._instance
   ```

2. **Fabriko metodo šablonas**
   - **Apibūdinimas**: Suteikia sąsają kurti objektus, bet leidžia vaikinėms klasėms keisti objektų tipą, kurie bus sukurti.
   - **Naudojimas kode**: `GameFactory` klasė yra Fabriko metodo šablonas, kuris kuria `Game` objektus su skirtingais žaidėjais.

   ```python
   class GameFactory:
       @staticmethod
       def create_game(player1_name, player2_name):
           game = Game()
           game.add_player(HumanPlayer(player1_name, 'X'))
           game.add_player(HumanPlayer(player2_name, 'O'))
           return game
   ```
  ### Failo operacijos (Skaitymas iš failo ir rašymas į failą)

**Naudojimas kode**: Programa išsaugo rezultatų lentelės duomenis į JSON failą (`scoreboard.json`) ir juos įkelia paleidus programą.

```python
class ScoreBoard:
    # ...

    def save_to_file(self, filename='scoreboard.json'):
        with open(filename, 'w') as f:
            json.dump(self.scores, f)

    def load_from_file(self, filename='scoreboard.json'):
        try:
            with open(filename, 'r') as f:
                self.scores = json.load(f)
        except FileNotFoundError:
            self.scores = {}
```

### Rezultatai ir Santrauka

**Rezultatai**:

- Įgyvendinta veikianti "Tic Tac Toe" žaidimo programa su rezultatų lentele.
- Sėkmingai naudoti OOP principai ir projektavimo šablonai.
- Įgyvendintos failo operacijos, skirtos išsaugoti ir įkelti rezultatų lenteles duomenis.

**Išvados**:

Programa sėkmingai demonstruoja OOP principų ir projektavimo šablonų naudojimą.
Galimos ateities plėtros galimybės apima sudėtingesnių AI žaidėjų pridėjimą, daugybinio žaidimo variantų įvedimą per tinklą arba gerinant vartotojo sąsają.
  
**Ateities Perspektyvos**:

Programą galima plėtoti, kad ji palaikytų daugiau žaidėjų, papildomus žaidimo režimus ar alternatyvias lentos dydžio parinktis.
Klaidų tvarkymo, žaidimo statistikos ir vartotojo sąsajos tobulinimas galėtų pagerinti žaidėjo patirtį.

### Nuorodos

- Python dokumentacija
- Projektavimo šablonai: Elements of Reusable Object-Oriented Software
- Stack Overflow ir įvairios internetinės forumų platformos klaidų šalinimui ir vadovavimui

Ši ataskaita sėkmingai demonstruoja funkcionalaus "Tic Tac Toe" žaidimo įgyvendinimą naudojant Python, efektyviai panaudojant OOP principus, projektavimo šablonus ir failo operacijas. Programa suteikia tvirtą pagrindą būsimoms plėtros ir plečiamumo galimybėms.
