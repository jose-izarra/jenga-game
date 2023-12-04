<img src="image.png" width="100" height="100">

``Run newJenga.py to play the game!``

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
|Project Analysis: Time Complexity| This section delves into the time complexity of the chosen Algorithms and how they function with the Data structures that we have implemented|


___

# Unfamiliar with _Jenga_? <div id='id-section1'/>

Rules and objective of the game:

Players take turns removing one block at a time from a tower constructed of 54 blocks. Each block removed is then placed on top of the tower, creating a progressively more unstable structure.

Starting off, players take turns removing one block from any level below the highest completed one and placing it horizontally atop the tower, perpendicular to any blocks on which it is to rest.

Once a level contains three blocks, it is complete and may not have any more blocks added to it.

The game ends when any portion of the tower collapses, caused by either the removal of a block or its new placement. The last player to complete a turn before the collapse is the winner.
___
# Data Structures

## 3D matrix (Tower) :

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

## Array (Leaderboard) :

- The simplest way for us to have stored the leaderboard values was with an array. This was just for convenience sake, since the indexing allowed for us to not have to worry about external values, and due to our design we would not have more than 2 players being tracked at the same time. As such we opted to use a standard Array. Furthermore, there are more reasons for this choice.
#### Reasons :

1. **Leaderboard Representation:**
    - An array is utilized to represent the leaderboard in the _Jenga_ game. Each element in the array corresponds to a player, and the array maintains an ordered list of scores.
2. **Simple and Direct Indexing:**
    - The array allows for simple and direct indexing, where each player's score is associated with their position in the array. This simplicity facilitates straightforward access and modification of player scores.
3. **Static Size:**
    - Unlike a hashmap, the array has a static size, meaning it is pre-allocated with a fixed number of slots. This size determines the maximum number of players that can be accommodated in the leaderboard.
#### Key Details:

- **Insertion and Retrieval:**
    - The time complexity for inserting a new score or retrieving an existing score from the array is `O(1)` because array indexing is a constant time operation.
- **Sorting (if needed):**
    - If sorting is required for the leaderboard, the time complexity would be O(n log n) for the sorting operation. However, this might be a periodic operation rather than occurring after every score update.


## Stack (Move Tracking):

- For the tracking of the moves we used a stack. This was a simple choice especially because of the nature of the data structure. Simply put, we would have the moves placed at the top of the stack following a LIFO, which would make backtracking an easy operation for us when it came for the time to implement it.

1. **Backtracking Operations:**
    - A stack is employed to facilitate backtracking operations in the _Jenga_ game. As a player makes moves and can potentially undo them, the stack keeps track of the sequence of moves, allowing for efficient undoing of the last move.
2. **Last-In-First-Out (LIFO):**
    - The stack follows the Last-In-First-Out (LIFO) principle, where the most recently added move is the first to be removed. This aligns with the nature of backtracking, where the latest move needs to be undone before previous moves.
3. **Efficient Undoing:**
    - The stack's LIFO behavior allows for efficient undoing of moves. Popping the top of the stack corresponds to undoing the last move made in the game.
#### Key Details:

- **Push and Pop Operations:**
    - The time complexity for push (adding a move to the stack) and pop (removing the last move from the stack) operations is typically `O(1)`. These operations are constant time and don't depend on the size of the stack.

#### Considerations in the _Jenga_ Game:

- **Undoing Moves:**
    - The stack is crucial for implementing the backtracking mechanism in the game, allowing a player to undo moves and explore different paths in the gameplay given the current scenario.

___
# Algorithms:

## Backtracking with a Stack: `O(n)`

1. **Undoing Moves (Backtracking):**
    - Undoing a move with a stack involves popping the top element of the stack. This operation is a constant time operation `O(1)` since it directly accesses the top of the stack.
2. **Inserting Moves (Adding to the Stack):**
    - When a new move is made, it needs to be pushed onto the stack. This operation is also a constant time operation `O(1)` as it involves adding an element to the top of the stack.
3. **Deleting Moves (Removing from the Stack):**
    - Removing a move during backtracking involves popping the top element from the stack. Like inserting moves, this operation is a constant time operation `O(1)`.

#####  **Key Advantages:**

1. **Flexibility:**
    - Backtracking provides flexibility by allowing players to explore different move sequences. 
2. **Error Correction:**
    - In a game with complex rules and potential for mistakes, backtracking serves as a mechanism for error correction. If a player realizes that a move has negatively impacted the tower's stability, they can backtrack to a previous state and try an alternative approach.

##### Considerations:

- **Space Complexity:**
    - Using a stack for backtracking may have implications for space complexity, especially if the stack becomes large. However, in practice, for games such as _Jenga_ with a moderate number of moves, the space usage is often reasonable.

## QuickSort : `O(n log n)`

- **Leaderboard Sorting:**
    - QuickSort is employed to sort the leaderboard in descending order based on player scores. This ensures that the player with the highest score is positioned at the top of the leaderboard, providing a clear and easily interpretable ranking.

##### **Key Advantages:**
1. **Recursion:**
	- QuickSort utilizes recursion as a key element of its sorting strategy. The algorithm recursively divides the array of scores into smaller subarrays, sorting each subarray independently.
2. **Efficient Sorting:**
    - QuickSort in the context of a leaderboard, where scores are dynamic and change frequently, the ability to quickly re-sort the leaderboard is essential for maintaining an up-to-date ranking.
3. **Descending Order:**
    - Sorting in descending order is important for leaderboard presentation. QuickSort, with its average time complexity of `O(n log n)`, ensures fast sorting even for larger leaderboards if this were to support a larger playerbase.


## Linear Search for Tower Probabilities: `O(n)`

- To update the probabilities of the towers layers and pieces, we use Linear Search which has a time complexity of `O(n)`, meaning that we go through the entire tower as one piece's change will impact the probabilities of the layers in each as well.

1. **Checking Tower Probabilities:**
    - Linear search is employed to check the probabilities associated with the state of the _Jenga_ tower. This involves updating for specific configurations, and conditions within the tower matrix that influence the probability of the tower falling over.
2. **Dynamic Probability Evaluation:**
    - Linear search in this context implies a dynamic evaluation of the tower's stability. The algorithm traverses the tower matrix to identify relevant conditions that contribute to the overall probability calculation. For example in the case of a side and center piece missing in a layer, it will undoubtedly cause the layers above to fall.

##### Considerations:

- The main thing to mention here is that we know this algorithm is not perfect for the job, but it gets it done with a reasonable accuracy. Specifically considering the case that when a piece is removed and the tower does not fall, this would imply that the probabilities of the tower falling will only be updated to the layers above the piece that was removed. This in our case could be added as an improvement, but the worst case scenario if we were only to update the layers above the removed piece would still be done in linear `O(n)` time, so we did not think it that big of an issue.
___
# Project Analysis: Time Complexity

## Table Summary
| **Algorithm** | **Decription** | **Time Complexity (Worst Case)** | **Time Complexity (Average Case)** |
|-|-|-| - |
| **Backtracking** | Ability to go back after each move if you don't feel you removed the right piece | `O(n)`| `O(n)` |  
| **QuickSort** | sed to sort the leaderboard in descending order | `O(n^2)` | `O(n log n)`|
| **Linear/Sequential Search**| Used to update the tower's balance and probability of collapsing after each move made| `O(n)` | `O(n)` |

## Backtracking : `O(n)`

- The time complexity of backtracking with a stack depends on the specific operations done during backtracking. In the worst possible scenario we would have to go through the entire stack giving us a time complexity of `O(n)`, however, the operations that go through the stack themselves are of `O(1)` time complexity. The operations of note would involve:

1. **Undoing Moves (Backtracking):**
    - In a stack, undoing a move involves popping the most recent move, thus making the previous move now the current one. This operation is typically done in constant time `O(1)`.
    
1. **Inserting Moves (Adding to the Stack):**
    - When a new move is made, it needs to be added to the stack via a push. This operation is essentially just adding the new move into the top of the stack and is usually a constant time operation  of  `O(1)`.
    
1. **Deleting Moves (Removing from the Stack):**
    - Similar to Undoing Moves, removing a move during backtracking involves popping from the stack. This operation is, again, a constant time operation `O(1)` because, in a stack, the move will be at the top. For all intents and purposes, this is the same as backtracking.

## QuickSort : `O(n log n)`

1. **Average Case Time Complexity:**
    
    - The average time complexity of QuickSort is `O(n log n)`. This is based on the partitioning of the array and the recursive sorting of subarrays. In the average case, QuickSort efficiently sorts the leaderboard array.
2. **Worst Case Time Complexity:**
    
    - The worst-case time complexity of QuickSort is `O(n^2)`. This occurs when the pivot is consistently chosen as the minimum or maximum element, leading to unbalanced partitioning. However, in practice, the worst case is uncommon, especially with good pivot selection strategies.
3. **Data Characteristics:**
    
    - The leaderboard likely contains a small number of scores, and the data is not expected to be highly unorganized. QuickSort is well-suited for efficiently sorting small to moderately-sized arrays with random or semi-random data.

## Linear Search : `O(n)`

#### Time Complexity:

- **Average Case:**
    - For the average case, Linear search will run at (quite obviously) `O(n)` time complexity, where n is the size of the tower matrix. Linear search sequentially examines elements and layers in this case to make sure that any conditions being met impact the tower's probability of falling
- **Worst Case:**
    - For the worst case, Linear search also has an `O(n)` time complexity. In the worst case, the search operation needs to traverse the entire tower matrix to evaluate its stability. Which although a negligible for the most part in this game since we do not have to scale it the game, we would normally look for a better method to look over the probabilities

___
