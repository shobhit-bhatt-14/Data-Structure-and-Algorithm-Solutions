# Data Structure and Algorithm

**Problem 1)** Write a program that takes a string and a character as input and returns the frequency of the character in the given string.

### Input Format:

● Input the string  
● Input the character

### Output Format:

● Print the frequency of character in the given string

**Sample Input 1:**  
Programming  
m  
**Sample Output 1:**  
2  
**Explanation 1:**  
The input string is Programming in which character "m" occurred twice and hence, the output is 2.

**Sample Input 2:**  
Programming  
N  
**Sample Output 2:**  
1  
**Explanation 2:**  
The input string is Programming and the character whose frequency is to calculated is "N". However, the string does not have "N", it consists of "n" due to which the frequency is 1.

**Sample Input 3:**  
Algorithms  
x  
**Sample Output 3:**  
0  
**Explanation 3:**  
The input string does not consist of character "X" or "x" and hence the output is 0.

---

**Problem 2)** You are given an array A(0-indexed) having N elements. Consider the following pseudo-code of insertion sort algorithm for sorting it:

_for (int i = 1; i < N; i = i + 1) {_  
_int j = i;_  
_while (j > 0 && a[j] < a[j - 1]) {_  
_swap(a[j], a[j - 1]);_  
_j = j - 1;_  
_}_  
_}_

Since, sorting the array takes too many swaps, you are allowed to rotate the array any number of
times. Rotating an array involves removing the last element and putting it at the start of the array.
Calculate the minimum number of swaps required in the above algorithm after rotating the array as
many times as needed modulo 10^9+7.

### Function Description:

Complete the minSwaps function in the editor below. It has the following parameter(s):

![Problem 2](/2.png "Problem 2")

### Constraints:

● 1<=N<=2\*10^5  
● 1<=A[i]<=2\*10^5

### Input Format:

● The first line contains an integer, N, denoting the number of elements in A.  
● Each line i of the N subsequent lines (where 0 ≤ i < N) contains an integer describing A[i].

### Output Format:

● An integer denoting the minimum number of swaps required.

**Sample Input 1:**  
6  
2  
8  
4  
1  
1  
5  
**Sample Output 1:**  
3  
**Explanation 1:**  
The number of swaps required for insertion sort in the original array is: 8.  
The minimum swaps required for insertion sort is 3 when array is rotated to [1,1,5,2,8,4]

**Sample Input 2:**  
4  
4  
3  
2  
1  
**Sample Output 2:**  
2  
**Explanation 2:**  
The rotation is: [2,1,4,3] when the minimum number of swaps required for insertion sort is 2.

---

**Problem 3)** The members of a certain society follow a secret mechanism for exchanging messages. They pass a series of numbers as encoded in the format: N1-N2@N2-N3

Here N1, N2, N3 and N4 are integer numbers and "@" is the delimiter used to specify the end of a word and, is used to express the end of a character and "-" is the delimiter used to indicate the end of a number.

The encryption works by processing the key given below:  
“Realize that excellent marks qualify everybody for jumps in wages”

For example the words “I am” will be encoded as “1-5@1-3,4-1” where the first value 1 represents the word in the key (i.e. Realize) and the number 5 represents the value of the character in the word (i.e. Realize).

Given a string input of such an encoded message write a method to decrypt the message and display it.

**_Hint_**: Try to think on the lines of using methods, modifiers, return type and inbuilt Java methods such as “math” or "string".

### Input Format

● A string “s” containing the message to be encoded.

### Output Format

● A string “b” displays the decoded message.

### Constraints

● Length of s<10^3

**Sample Input 1:**  
1-1,6-7,6-7,5-6@10-3,1-3,5-2,4-4  
**Sample Output 1:**  
Roof gauk  
**Explanation 1:**  
1-1 represents the 1st letter of the 1st word in key i.e., R in Realize. Similarly, 6-7 represents the 7th letter in the 6th word in the key i.e., O in Everybody. So on and so forth. Hence, the decoded message is Roof gauk.

**Sample Input 2:**  
2-2,1-3,4-1,1-3@1-4,5-2,1-4,5-2  
**Sample Output 2:**  
hama lulu  
**Explanation 2:**  
2-2 represents the 2nd letter of the 2nd word in key i.e., H in that. Similarly, 1-3 represents the 3rd letter in the 1st word in the key i.e., A in Realize. So, on and so forth. Hence, the decoded message is hama lulu.

**Sample Input 3:**  
10-1,6-7,4-3,6-8@5-1,5-2,1-3,6-8@1-6,1-3,3-3,4-4  
**Sample Output 3:**  
word quad zack  
**Explanation 3:**  
10-1 represents the 1st letter of the 10th word in key i.e., W in Wages. Similarly, 6-7 represents the 7th letter in the 6th word in the key i.e., A in Realize. So on and so forth. Hence, the decoded message is Word quad zack.
