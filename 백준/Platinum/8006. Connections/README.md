# [Platinum IV] Connections - 8006 

[문제 링크](https://www.acmicpc.net/problem/8006) 

### 성능 요약

메모리: 122544 KB, 시간: 596 ms

### 분류

자료 구조, 데이크스트라, 그래프 이론, 최단 경로

### 제출 일자

2025년 9월 15일 21:46:28

### 문제 설명

<p>Byteotian Ministry of Infrastructure has decided to create a computer program that helps to find quickly the lengths of routes between arbitrary towns. It would be small wonder if the inhabitants of Byteotia always wanted to find the shortest route. However, it happens that they want to know the k-th shortest route. Moreover, cycles in routes are possible, i.e. routes that have recurring towns.</p>

<p>If there are 4 routes between two towns and their lengths are 2, 4, 4 and 5, then the length of the shortest connection is 2, the second shortest is 4, the third is 4, and the fourth is 5.</p>

<p>Write a program which:</p>

<ul>
	<li>reads from the standard input a description of Byteotian road network and queries     concerning lengths of journey routes,</li>
	<li>computes and writes to the standard output answers to the queries read.</li>
</ul>

### 입력 

 <p>In the first line of the standard input there are two positive integers n and m, separated by a single space, 1 ≤ n ≤ 100, 0 ≤ m ≤ n^2-n. They are the number of towns in Byteotia and the number of roads connecting the towns, respectively. The towns are numbered from 1 to n.</p>

<p>In each of m successive lines there are three integers separated by single spaces: a, b and l, a≠b, 1 ≤ l ≤ 500. Each triple describes one one-way road of length l enabling to move from the town a to b. For each two towns there exist at most one road that enables to move in the given direction.</p>

<p>In the following line there is one integer q, 1 ≤ q ≤ 10,000, denoting the number of queries. In the successive q lines there are queries written, one per line. Each query has a form of three integers separated by single spaces: c, d and k, 1 ≤ k ≤ 100. Such a query refers to the length of the k-th shortest route from the town c to the town d.</p>

### 출력 

 <p>Your program should write to the standard output the answers to the queries read, one answer per line. In the i-th line the answer to the i-th query should be written: one integer equal to the length of the route being sought or -1, when such a route does not exist.</p>

<p> </p>

