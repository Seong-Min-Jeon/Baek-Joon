# [Platinum IV] S-Nim - 6699 

[문제 링크](https://www.acmicpc.net/problem/6699) 

### 성능 요약

메모리: 32412 KB, 시간: 1432 ms

### 분류

게임 이론, 스프라그–그런디 정리

### 제출 일자

2026년 2월 12일 10:58:23

### 문제 설명

<p>Arthur and his sister Caroll have been playing a game called Nim for some time now. Nim is played as follows:</p>

<ul>
	<li>The starting position has a number of heaps,all containing some,not necessarily equal, number of beads.</li>
	<li>The players take turns chosing a heap and removing a positive number of beads from it.</li>
	<li>The first player not able to make a move, loses.</li>
</ul>

<p>Arthur and Caroll really enjoyed playing this simple game until they recently learned an easy way to always be able to find the best move:</p>

<ul>
	<li>Xor the number of beads in the heaps in the current position (i.e. if we have 2, 4 and 7 the xor-sum will be 1 as 2 xor 4 xor 7 = 1).</li>
	<li>If the xor-sum is 0, too bad, you will lose.</li>
	<li>Otherwise, move such that the xor-sum becomes 0. This is always possible.</li>
</ul>

<p>It is quite easy to convince oneself that this works. Consider these facts: </p>

<ul>
	<li>The player that takes the last bead wins.</li>
	<li>After the winning player’s last move the xor-sum will be 0.</li>
	<li>The xor-sum will change after every move.</li>
</ul>

<p>Which means that if you make sure that the xor-sum always is 0 when you have made your move, your opponent will never be able to win, and, thus, you will win.<br>
Understandibly it is no fun to play a game when both players know how to play perfectly (ignorance is <br>
bliss). Fourtunately, Arthur and Caroll soon came up with a similar game, S-Nim, that seemed to solve this problem. Each player is now only allowed to remove a number of beads in some predefined set S, e.g. if we have S = {2, 5} each player is only allowed to remove 2 or 5 beads. Now it is not always possible to make the xor-sum 0 and, thus, the strategy above is useless. Or is it?</p>

<p>Your job is to write a program that determines if a position of S-Nim is a losing or a winning position. A position is a winning position if there is at least one move to a losing position. A position is a losing position if there are no moves to a losing position. This means, as expected, that a position with no legal moves is a losing position.</p>

### 입력 

 <p>Input consists of a number of test cases.</p>

<p>For each test case: The first line contains a number k (0 < k ≤ 100)<br>
describing the size of S, followed by k numbers s<sub>i</sub> (0 < s<sub>i</sub> ≤ 10000) describing S. The second line contains a number m (0 < m ≤ 100) describing the number of positions to evaluate. The next m lines each contain a number l (0 < l ≤ 100) describing the number of heaps and l numbers h<sub>i</sub> (0 ≤ h<sub>i</sub> ≤ 10000) describing the number of beads in the heaps.</p>

<p>The last test case is followed by a 0 on a line of its own.</p>

### 출력 

 <p>For each position:</p>

<ul>
	<li>If the described position is a winning position print a ’W’.</li>
	<li>If the described position is a losing position print an ’L’. Print a newline after each test case.</li>
</ul>

