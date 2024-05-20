# Report on Tic Tac Toe Game Implementation

## Introduction

**Goal of the Coursework**: The goal of this coursework is to implement a Tic Tac Toe game in Python, demonstrating a solid understanding of Object-Oriented Programming (OOP) principles and design patterns.

**Application Description**: The Tic Tac Toe game allows two human players to play against each other. The program includes a scoreboard that tracks wins for each player and saves this data to a JSON file.

**How to Run the Program**:
1. Clone the repository containing the code.
2. Ensure Python 3.x is installed on your system.
3. Run the program in your preferred Python environment, e.g., in Visual Studio Code by clicking the "Run Python file" button.


**How to Use the Program**:
- Players take turns entering their moves by selecting a number corresponding to a position on the 3x3 game board.
- The game continues until a player wins, the game is drawn, or the players choose not to continue.

## Body/Analysis

### Implementation of Object-Oriented Programming (OOP) Pillars

1. **Encapsulation**
   - **Description**: Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit (class).
   - **Usage in Code**: Classes such as `Player`, `Game`, and `ScoreBoard` encapsulate their data and methods, ensuring data integrity and ease of maintenance.

   ===python
   class Player:
       def __init__(self, name, symbol):
           self.name = name
           self.symbol = symbol

       def get_move(self):
           try:
               move = int(input(f"Player {self.name} ({self.symbol}) turn. Which box? : "))
               return move
           except ValueError:
               print("Wrong Input!!! Try Again")
               return self.get_move()
   ===

2. **Abstraction**
   - **Description**: Abstraction refers to the concept of hiding internal implementation details and showing only the necessary features of an object.
   - **Usage in Code**: The `Player` class abstracts the process of getting a move from the user, simplifying the interaction with the game.

   ===python
   class Player:
       def get_move(self):
           try:
               move = int(input(f"Player {self.name} ({self.symbol}) turn. Which box? : "))
               return move
           except ValueError:
               print("Wrong Input!!! Try Again")
               return self.get_move()
   ===

3. **Inheritance**
   - **Description**: Inheritance is the mechanism by which one class (child class) acquires the properties and behaviors of another class (parent class).
   - **Usage in Code**: The `HumanPlayer` class inherits from the `Player` class, inheriting its attributes and methods.

   ===python
   class HumanPlayer(Player):
       pass
   ===

4. **Polymorphism**
   - **Description**: Polymorphism allows objects of different classes to be treated as objects of a common superclass.
   - **Usage in Code**: Both `Player` and `HumanPlayer` classes have the `get_move()` method, allowing them to be used interchangeably in the `Game` class.

   ===python
   class Player:
       def get_move(self):
           try:
               move = int(input(f"Player {self.name} ({self.symbol}) turn. Which box? : "))
               return move
           except ValueError:
               print("Wrong Input!!! Try Again")
               return self.get_move()

   class HumanPlayer(Player):
       pass
   ===

### Design Patterns Used

1. **Singleton Pattern**
   - **Description**: Ensures a class has only one instance and provides a global point of access to that instance.
   - **Usage in Code**: The `ScoreBoard` class uses the Singleton Pattern to ensure there is only one scoreboard instance throughout the program.

   ===python
   class ScoreBoard:
       _instance = None

       def __new__(cls):
           if cls._instance is None:
               cls._instance = super(ScoreBoard, cls).__new__(cls)
               cls._instance.scores = {}
           return cls._instance
   ===

2. **Factory Method Pattern**
   - **Description**: Provides an interface for creating objects, but allows subclasses to alter the type of objects that will be created.
   - **Usage in Code**: The `GameFactory` class is a Factory Method Pattern that creates instances of `Game` with different players.

   ===python
   class GameFactory:
       @staticmethod
       def create_game(player1_name, player2_name):
           game = Game()
           game.add_player(HumanPlayer(player1_name, 'X'))
           game.add_player(HumanPlayer(player2_name, 'O'))
           return game
   ===

### File Operations (Reading from and Writing to File)

- **Usage in Code**: The program saves scoreboard data to a JSON file (`scoreboard.json`) and loads it when the program starts.

   ===python
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
   ===

## Results and Summary

- **Results**:
  - Implemented a functional Tic Tac Toe game with scoreboard tracking.
  - Used OOP principles and design patterns effectively.
  - Implemented file operations to save and load scoreboard data.

- **Conclusions**:
  - The program successfully demonstrates the use of OOP principles and design patterns.
  - Future extensions could include adding more sophisticated AI players, adding multiplayer options over network, or improving the user interface.

- **Future Prospects**:
  - The program could be extended to support more players, additional game modes, or alternative board sizes.
  - Improvements in error handling, game statistics, and user interface could enhance the player experience.

## References

- Python Documentation
- Design Patterns: Elements of Reusable Object-Oriented Software
- Stack Overflow and various online forums for troubleshooting and guidance
