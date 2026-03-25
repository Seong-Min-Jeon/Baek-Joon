# [Diamond V] Cafebazaar’s Chess Tournament - 18333 

[문제 링크](https://www.acmicpc.net/problem/18333) 

### 성능 요약

메모리: 154092 KB, 시간: 576 ms

### 분류

수학, 누적 합, 고속 푸리에 변환

### 제출 일자

2026년 3월 25일 09:54:37

### 문제 설명

<p>Ali hosts a yearly chess tournament for CafeBazaar’s Shab-e Yalda festival. In a chess tournament, each pair of participants play a game against each other exactly once. Moreover, players are granted one point for a win, a half point for a draw, and no points for a loss toward their tournament score.</p>

<p>Danial has built a system to predict the result of Ali’s tournament. Based on experience, he has assigned an opening skill and an ending skill to each of n participants in the tournament. For the i-th participant, let us denote the former with o<sub>i</sub> and the latter with e<sub>i</sub>. In a game between the i-th and j-th participants, Danial decides the result of the game according to the following rules:</p>

<ol>
	<li>If o<sub>i</sub> > o<sub>j</sub> and e<sub>i</sub> > e<sub>j</sub>, then the i-th participant wins the game.</li>
	<li>If o<sub>j</sub> > o<sub>i</sub> and e<sub>j</sub> > e<sub>i</sub>, then the j-th participant wins the game.</li>
	<li>Otherwise, the game ends in a draw.</li>
</ol>

<p>To make the tournament more exciting, Ali wants to invite Danial to join the other n participants in the tournament. Since Danial has no prior experience in chess, he decides to practice for the tournament. Based on the amount of training, Danial can end up with any opening and ending skill. However, Danial has promised Ali that he will train in such a way that his opening skill will be <strong>different</strong> from the opening skill of the other participants. He will also keep his ending skill <strong>different</strong> from the ending skill of the other participants.</p>

<p>For his advertisement campaign, Ali wants to know the number of distinct possible final scores that Danial might get based on Danial’s rules mentioned above. For example, Danial can achieve the scores 0, 1.5, 2.5, 3, 4, and 5 in the sample. For instance, the score 3 is obtained by setting the opening and ending skills of Danial to be 1.5. Since Ali and all other CafeBazaar programmers are busy planning the event, he has turned to you for help. Write a program to calculate this value.</p>

### 입력 

 <p>The first line of the input contains a single integer n (1 ⩽ n ⩽ 200 000), the number of participants. The i-th line of the next n lines contains two integers o<sub>i</sub> and e<sub>i</sub> (1 ⩽ o<sub>i</sub>, e<sub>i</sub> ⩽ n), the opening and ending skills of the i-th participant, respectively. Note that the limits for opening and ending skills do not apply to Danial’s opening and ending skills. More specifically, Danial’s opening and ending skills can be any real numbers.</p>

### 출력 

 <p>In the only line of the output, print the number of distinct possible final scores for Danial.</p>

