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

#### Kūnas/Analizė

**Objektinio programavimo (OOP) principų įgyvendinimas**

1. **Inkapsuliacija**
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
