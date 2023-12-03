# Description
___
Welcome to our project!

In this project we sought to build a digital version of the game _Jenga_. 

___
# Table of Contents 

| | Description |
|-|------|
|Unfamiliar with Jenga?|Explains the main concepts related to the Jenga boardgame. If you have prior knowledge you can skip this section|
|Data Structures| Section of listed Data Structures as well as why and how we implemented them into the project.|
|Algorithms| Section of listed Algorithms as well as why and how we implemented them into the project|
|Project Analysis| This section delves into the time complexity of the chosen Algorithms and how they function with the Data structures that we have implemented|
|Results| Contains the results of the methods listed above and how the project turned out|

___
### Unfamiliar with _Jenga_? <div id='id-section1'/>

Rules and objective of the game:

Players take turns removing one block at a time from a tower constructed of 54 blocks. Each block removed is then placed on top of the tower, creating a progressively more unstable structure.

Starting off, players take turns removing one block from any level below the highest completed one and placing it horizontally atop the tower, perpendicular to any blocks on which it is to rest.

Once a level contains three blocks, it is complete and may not have any more blocks added to it.

The game ends when any portion of the tower collapses, caused by either the removal of a block or its new placement. The last player to complete a turn before the collapse is the winner.
___
## Data Structures

### 3D matrix (Tower) :

- Since we wanted to make a vertical tower with different levels and sides, we immediately identified that in the game of _Jenga_, a 3-Dimensional Matrix would be the most effective data structure to store and manipulate all the values.
#### Reasons :
1. **Spatial Representation:**
    - _Jenga_ towers are three-dimensional structures, and a 3D matrix is well-suited for spatial representation. Each element in the matrix corresponds to a specific location in the tower, allowing for an intuitive and accurate representation of the tower's structure.
2. **Layered Structure:**
    - The tower consists of layers of _Jenga_ blocks, and the 3D matrix can be used to organize these layers. Each layer is represented as a 2D matrix within the 3D matrix, with individual elements representing the presence or absence of a _Jenga_ block at a specific position.
3. **Ease of Manipulation:**
    - Manipulating the _Jenga_ tower involves adding or removing blocks at specific positions. The 3D matrix provides a straightforward way to perform these operations, as each element in the matrix corresponds to a block in the tower.
4. **Efficient Indexing:**
    - Accessing specific positions within the tower is efficient using 3D matrix indices. The indices can be used to locate and modify the state of a particular block in constant time.
5. **Visualization:**
    - The 3D matrix facilitates the visualization of the tower's structure in the code. Developers can easily understand and reason about the state of the tower by examining the matrix, making it a valuable tool for debugging and code comprehension.

### Hash Table (Leaderboard):

A Hash Table (or dictionary in Python) is chosen for the leaderboard for the following reasons:

1. **Efficient Lookup Time:**
    - Hash Table provide constant time complexity `O(1)` for key-based operations like looking up a player's score. This ensures that retrieving a player's score from the leaderboard is fast and efficient.
2. **Unique Player Names:**
    - Each player's name serves as a unique identifier (key) in the Hash Table. This prevents conflicts or overwrites, ensuring that each player's score is accurately represented.
3. **Dynamic Player Addition/Removal:**
    - Hash Table can dynamically grow or shrink based on the number of players participating. This flexibility is crucial in a game where players can join or leave, as it allows for easy updates to the leaderboard.

##### Linked List (Backtracking)

- A linked list is chosen for tracking moves in order to facilitate backtracking in the game. Here's why a linked list is a suitable choice:

1. **Sequential Order:**
    - Linked lists maintain the order of elements, which is essential for tracking moves chronologically. Each node in the linked list represents a move, and the order of nodes corresponds to the order in which moves were made during the game.
2. **Constant Time Insertion/Deletion:**
    - Inserting or deleting a move from a linked list is a constant time `O(1)` operation when given the node to be added or removed. This is advantageous for backtracking, as it allows for efficient undoing of moves.
3. **Memory Efficiency:**
    - Linked lists dynamically allocate memory for each move, making them memory-efficient. This is particularly useful in scenarios where the number of moves can vary, and memory needs to be managed dynamically.
4. **Backtracking Support:**
    - The structure of a linked list allows for straightforward backtracking. When a player decides to undo a move, the game can navigate the linked list to the previous node, effectively reverting the game state to the previous move.
  
___
### Algorithms:

#### Backtracking:

- Due to this being a digital game we wanted to implement backtracking so that the player could undo their moves. Due to implementing the Linked List Data Stucture, we can make these moves in O(n)

- **Undoing Moves:**
    - Backtracking is used to allow players to undo moves. In a game like _Jenga_, where the goal is to maintain the stability of the tower, giving players the ability to backtrack allows them to reconsider their moves if they feel they have removed the wrong piece. This feature enhances the user experience and strategic decision-making.

**Key Advantages:**

1. **Flexibility:**
    - Backtracking provides flexibility by allowing players to explore different move sequences and strategies. It adds a layer of interactivity and engagement as players can experiment without the fear of irreversible consequences.
2. **Error Correction:**
    - In a game with complex rules and potential for mistakes, backtracking serves as a mechanism for error correction. If a player realizes that a move has negatively impacted the tower's stability, they can backtrack to a previous state and try an alternative approach.

#### QuickSort : O(n log n)

**Purpose:**

- **Leaderboard Sorting:**
    - QuickSort is employed to sort the leaderboard in descending order based on player scores. This ensures that the player with the highest score is positioned at the top of the leaderboard, providing a clear and easily interpretable ranking.

**Key Advantages:**

1. **Efficient Sorting:**
    - QuickSort is known for its efficiency in sorting large datasets. In the context of a leaderboard, where scores are likely to be dynamic and change frequently, the ability to quickly re-sort the leaderboard is essential for maintaining an up-to-date ranking.
2. **Descending Order:**
    - Sorting in descending order is important for leaderboard presentation. It allows players to easily identify the top performers and adds a competitive element to the game. QuickSort, with its average time complexity of O(n log n), ensures fast sorting even for larger leaderboards.
3. **Consistent User Experience:**
    - A consistently sorted leaderboard provides a better user experience. Players can quickly assess their standing and compare their scores with others, fostering competition and engagement.

___
### Project Analysis: Time Complexity

##### Backtracking:

- The time complexity of backtracking with a linked list depends on the specific operations done  during backtracking. The operations of note would involve:

1. **Undoing Moves (Backtracking):**
    - In a linked list, undoing a move involves navigating from the current state to the previous state. This operation is typically a constant time operation (`O(1)`) because, in a linked list, moving to the previous node can be done directly.
    
1. **Inserting Moves (Adding to the Linked List):**
    - When a new move is made, it needs to be added to the linked list. This operation is also a constant time operation (`O(1)`) because inserting a new node at the beginning or end of a linked list can be done in constant time.
    
1. **Deleting Moves (Removing from the Linked List):**
    - Removing a move during backtracking involves deleting a node from the linked list. This operation is, again, a constant time operation (`O(1)`) because, in a linked list, removing a node at a given position can be done in constant time if the reference to the node is available.

##### QuickSort :

1. **Average Case Time Complexity:**
    
    - The average time complexity of QuickSort is `O(n log n)`. This is based on the partitioning of the array and the recursive sorting of subarrays. In the average case, QuickSort efficiently sorts the leaderboard array.
2. **Worst Case Time Complexity:**
    
    - The worst-case time complexity of QuickSort is `O(n^2)`. This occurs when the pivot is consistently chosen as the minimum or maximum element, leading to unbalanced partitioning. However, in practice, the worst case is uncommon, especially with good pivot selection strategies.
3. **Data Characteristics:**
    
    - The leaderboard likely contains a small number of scores, and the data is not expected to be highly unorganized. QuickSort is well-suited for efficiently sorting small to moderately sized arrays with random or semi-random data.

___

## Results
