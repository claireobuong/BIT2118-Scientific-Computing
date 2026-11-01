# Task 9: Eigenvalues and Eigenvectors

## 1. Inputs and Mathematical Operations

In this task, I used NumPy to calculate the eigenvalues and eigenvectors of a matrix representing a small computer network. The network has four nodes labelled A, B, C and D. The adjacency matrix shows how the nodes are connected.

The program uses NumPy's `np.linalg.eig()` function to calculate the eigenvalues and eigenvectors. It then identifies the largest eigenvalue and uses its corresponding eigenvector to calculate the importance of each node. The importance scores are normalised so that their total adds up to 1.

## 2. Parameter Change and Results

In the original program, the network had five connections between the four nodes. The program produced the following results:

- Dominant eigenvalue: `2.5616`
- Node A importance: `0.2192`
- Node B importance: `0.2808`
- Node C importance: `0.2808`
- Node D importance: `0.2192`
- Verification error: `2.6921477609369894e-15`

To see how changing the network would affect the results, I added another connection between node A and node D. This made all four nodes directly connected to one another.

The modified program produced the following results:

- Dominant eigenvalue: `3.0`
- Node A importance: `0.2500`
- Node B importance: `0.2500`
- Node C importance: `0.2500`
- Node D importance: `0.2500`
- Verification error: `0.0`

After adding the connection between A and D, all four nodes had the same importance score. This is because every node was now connected to all the other nodes. The dominant eigenvalue also increased from approximately `2.5616` to `3.0`.

## 3. Explanation of Output

The program successfully calculated the eigenvalues and eigenvectors of the network matrix. In the original network, nodes B and C had higher importance scores than nodes A and D. This showed that B and C had a more central position in the network.

After adding the connection between A and D, all the nodes had an equal importance score of 0.25. This showed that the network had become fully connected, with no node being more important than another according to the calculated scores.

The verification errors were either zero or extremely close to zero. This confirms that the calculated eigenvector satisfied the eigenvalue equation within the expected numerical accuracy.

## 4. Related Real-World Case: Ranking Web Pages Using PageRank

For the real-world application, I modified the program to demonstrate how eigenvalues and eigenvectors can be used to rank web pages. The example uses five pages named Home, News, Shop, Blog and Contact. The connections between the pages represent links from one page to another.

### Assumptions

- The website has five pages.
- The links between the pages are represented using an adjacency matrix.
- A page receives importance from the pages linking to it.
- A damping factor of 0.85 is used in the PageRank calculation.
- The importance scores are normalised so that their total is 1.

### Inputs and Outputs

The program uses the website's link structure to create a transition matrix. It then applies the damping factor to form the Google matrix. NumPy is used to calculate its eigenvalues and eigenvectors. The eigenvector corresponding to the dominant eigenvalue is used to determine the PageRank scores of the five pages.

The program produced the following results:

- Dominant eigenvalue: `1.0`
- Home: `0.3193`
- Blog: `0.2095`
- News: `0.2095`
- Shop: `0.1626`
- Contact: `0.0991`
- Total of PageRank scores: `1.0`

### Interpretation

The results show that the Home page had the highest PageRank score of 0.3193, making it the most important page in this example. Blog and News had equal scores of 0.2095, followed by Shop with 0.1626. Contact had the lowest score of 0.0991.

The scores add up to 1, showing that they were correctly normalised. The results demonstrate how the link structure of a website can be used to determine the relative importance of its pages.

Overall, this task helped me understand how eigenvalues and eigenvectors can be used to measure the importance of nodes in a network. The PageRank example also showed how the same mathematical concept can be applied to ranking web pages based on their links.