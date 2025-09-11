# [Platinum IV] Speedy Escape - 5036 

[문제 링크](https://www.acmicpc.net/problem/5036) 

### 성능 요약

메모리: 112280 KB, 시간: 176 ms

### 분류

그래프 이론, 이분 탐색, 최단 경로, 데이크스트라, 매개 변수 탐색

### 제출 일자

2025년 9월 11일 19:09:38

### 문제 설명

<p>The Newton brothers are planning to rob a bank in the city of Alviso and want to figure out a way to escape the city’s only police car. They know that their car is faster than the police car so if they could just reach one of the highways exiting the city they will be able to speed away from the police.</p>

<p>The police car has a maximum speed of 160 km/h. Luckily, the brothers know where the police car will start (it’s parked at the police station). To be on the safe side they assume that the police car will start moving as soon as they leave the bank and start their car (this is when the alarm goes off).</p>

<p>The brothers want to find a fixed route that ensures that they are able to leave the city no matter what route the police car take and at what speed it drives. However, since the brothers are not very confident drivers they don’t want to drive faster than necessary. Luckily they have recently invested in a new hi-tech in-car police escape system that you have constructed. This system will tell them what the minimal top speed needed to escape is (and probably other useful things like what route to take).</p>

<p>Let’s turn the clock back a bit to the time when you were constructing the escape system and focused on finding the minimal required speed. Can you get it right?</p>

<p>You may treat all roads as infinitesimally narrow and both cars as point objects. If the brothers ever end up at the same point (on any road or intersection) at the same time as the police car they will be caught and by Murphy’s law if there is any possibility of this happening it will happen. The two cars start simultaneously and can accelerate/decelerate instantaneously at any time to any speed below or equal to its maximum speed. They can also change roads at intersections or direction anywhere on a road instantaneously no matter what speed they are traveling at.</p>

### 입력 

 <p>The first line of the input consists of three integers n, m and e, where 2 ≤ n ≤ 100 describe the number of intersections, 1 ≤ m ≤ 5000 describes the number of roads in the city and 1 ≤ e ≤ n describes the number of highway exits. Then follow m lines, each consisting of three integers a, b, l such that 1 ≤ a < b ≤ n and 1 ≤ l ≤ 100 describing a road of length l hundred meters from intersection a to intersection b. Then follows a line of e integers, each one a number in 1, . . . , n describing which intersections are connected to highway exits. Finally there is a line with two integers b and p (1 ≤ b, p ≤ n and b ≠ p) describing the intersections where the brothers and the police cars start, respectively.</p>

<p>It will always be possible to travel from any intersection to any other intersection. Roads are only connected at intersection points (although they may cross using bridges or tunnels at others points). Roads can be used in both directions but there cannot be more than one road between two intersections.</p>

### 출력 

 <p>The minimal speed in km/h required to escape or the word IMPOSSIBLE if it is impossible. In the first case any answer with either absolute or relative error smaller than 10<sup>−6</sup> is acceptable.</p>

