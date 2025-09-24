# [Platinum V] Karaoke Meetup - 18820 

[문제 링크](https://www.acmicpc.net/problem/18820) 

### 성능 요약

메모리: 188384 KB, 시간: 1648 ms

### 분류

다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색, 최단 경로, 데이크스트라, 트리에서의 다이나믹 프로그래밍, 트리에서의 전방향 다이나믹 프로그래밍, 트리의 지름

### 제출 일자

2025년 9월 24일 12:19:22

### 문제 설명

<p>The judges of the South Pacific Programming Contest are planning their next secret karaoke meetup and are looking for a place to hold it. Last time, they asked Timothy to pick the location, but of course, he just picked somewhere really close to his house, and far from everyone else’s! This year, you would like to pick a meeting location that is fair.</p>

<p>All the judges live in the same city. The city consists of various locations in which the meeting could be held and roads that connect pairs of locations. The city is built such that for each pair of locations, there is exactly one path between them. Each road has a length and can be used to travel in either direction. You consider a meeting point fair if the distances from each of the judges’ houses are similar. For each location, its <em>fairness score</em> is the ratio A/B, where A is the minimum distance from the location to any judges’ house and B is the largest distance. What is the maximum fairness score for all vertices?</p>

### 입력 

 <p>The first line contains two integers n (2 ≤ n ≤ 200 000), which is the number of locations in the city, and k (2 ≤ k ≤ n), which is the number of judges.</p>

<p>The next k lines describe the location of the judges’ houses. Each of these lines contains a single integer ℓ (1 ≤ ℓ ≤ n), which is the location of this judge’s house. No two judges live at the same location.</p>

<p>The next n − 1 lines describe the roads in the city. Each of these lines contains three integers u (1 ≤ u ≤ n), v (1 ≤ v ≤ n), and w (1 ≤ w ≤ 10<sup>9</sup>), which denotes a road between locations u and v with a length of w.</p>

### 출력 

 <p>Display the maximum fairness score as a reduced fraction.</p>

