# [Platinum IV] Another Brick in the Wall - 4533 

[문제 링크](https://www.acmicpc.net/problem/4533) 

### 성능 요약

메모리: 114308 KB, 시간: 132 ms

### 분류

너비 우선 탐색, 자료 구조, 데이크스트라, 그래프 이론, 그래프 탐색, 구현, 평면 그래프, 최단 경로

### 제출 일자

2025년 9월 9일 12:01:48

### 문제 설명

<p>After years as a brick-layer, you've been called upon to analyze the structural integrity of various brick walls built by the Tetrad Corporation. Instead of using regular-sized bricks, the Tetrad Corporation seems overly fond of bricks made out of strange shapes. The structural integrity of a wall can be approximated by the fewest number of bricks that could be removed to create a gap from the top to the bottom. Can you determine that number for various odd walls created by Tetrad?</p>

### 입력 

 <p>Input to this problem will begin with a line containing a single integer X (1 ≤ X ≤ 100) indicating the number of data sets. Each data set consists of two components:</p>

<ul>
	<li>A single line, "M N" (1 ≤ M,N ≤ 20) where M and N indicate the height and width (in units), respectively, of a brick wall;</li>
	<li>A series of M lines, each N alphabetic characters in length. Each character will indicate to which brick that unit of the wall belongs to. Note that bricks will be contiguous; each unit of a brick will be adjacent (diagonals do not count as adjacent) to another unit of that brick. Multiple bricks may use the same characters for their representation, but any bricks that use identical characters will not be adjacent to each other. All letters will be uppercase.</li>
</ul>

### 출력 

 <p>For each data set, output the fewest number of bricks to remove to create a gap that leads from some point at the top of the wall, to some point at the bottom of the wall. Assume that bricks are in fixed locations and do not "fall" if bricks are removed from beneath them. A gap consists of contiguous units of removed bricks; each unit of a gap must be adjacent (diagonals do not count) to another unit of the gap. </p>

