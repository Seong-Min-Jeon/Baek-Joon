# [Platinum III] Playing With Stones - 7824 

[문제 링크](https://www.acmicpc.net/problem/7824) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

게임 이론, 스프라그–그런디 정리

### 제출 일자

2026년 2월 12일 13:34:16

### 문제 설명

<p>You and your friend are playing a game in which you and your friend take turns removing stones from piles. Initially there are N piles with a1, a2, a3, …, aN number of stones. On each turn, a player must remove at least one stone from one pile but no more than half of the number of stones in that pile. The player who cannot make any moves is considered lost. For example, if there are three piles with 5, 1 and 2 stones, then the player can take 1 or 2 stones from first pile, no stone from second pile, and only 1 stone from third pile. Note that the player cannot take any stones from the second pile as 1 is more than half of 1 (the size of that pile). Assume that you and your friend play optimally and you play first, determine whether you have a winning move. You are said to have a winning move if after making that move, you can eventually win no matter what your friend does.</p>

### 입력 

 <p>The first line of input contains an integer T (T ≤ 100) denoting the number of testcases. Each testcase begins with an integer N (1 ≤ N ≤ 100) the number of piles. The next line contains N integers a1, a2, a3, …, aN (1 ≤ ai ≤ 2 * 10<sup>18</sup>) the number of stones in each pile.</p>

### 출력 

 <p>For each testcase, print “YES” (without quote) if you have a winning move, or “NO” (without quote) if you don‟t have a winning move.</p>

