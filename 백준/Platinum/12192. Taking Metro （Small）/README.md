# [Platinum V] Taking Metro (Small) - 12192 

[문제 링크](https://www.acmicpc.net/problem/12192) 

### 성능 요약

메모리: 115076 KB, 시간: 316 ms

### 분류

데이크스트라, 그래프 이론, 최단 경로

### 제출 일자

2025년 11월 6일 14:22:58

### 문제 설명

<p>Tom is taking metros in the city to go from station to station.</p>

<p>The metro system in the city works like this:</p>

<ul>
	<li>There are <strong>N</strong> metro lines in the city: line 1, line 2, ..., line <strong>N</strong>.</li>
	<li>For each metro <strong>i</strong>, there are <strong>SN</strong><strong><sub>i</sub></strong> stations. Let's assume they are <strong>S</strong><strong><sub>i,1</sub></strong>,<strong>S</strong><strong><sub>i,2</sub></strong>, ... , <strong>S</strong><strong><sub>i,SN</sub></strong><strong><sub>i</sub></strong>. These stations are ordered from one end point to the other end point. The metro is running in both directions. In other words, the metro is going from <strong>S</strong><strong><sub>i,1</sub></strong> -> <strong>S</strong><strong><sub>i,2</sub></strong> -> ... -> <strong>S</strong><strong><sub>i,SN</sub></strong><strong><sub>i</sub></strong>, and <strong>S</strong><strong><sub>i,SN</sub></strong><strong><sub>i</sub></strong> -> <strong>S</strong><strong><sub>i,SN</sub></strong><strong><sub>i</sub></strong><strong><sub>-1</sub></strong> -> ... -> <strong>S</strong><strong><sub>i,1</sub></strong>. You can take the metro from any station and get off at any station. It takes a certain time to travel from one station to the next station. It takes <strong>Time</strong><strong><sub>i,1</sub></strong> minutes to travel from <strong>S</strong><strong><sub>i,1</sub></strong> to <strong>S</strong><strong><sub>i,2</sub></strong>, <strong>Time</strong><strong><sub>i,2</sub></strong> minutes to travel from <strong>S</strong><strong><sub>i,2</sub></strong> to <strong>S</strong><strong><sub>i,3</sub></strong>, etc. It takes the same time in the other direction.</li>
	<li>There are <strong>M</strong> transfer tunnels. Each transfer tunnel connects two stations of different metro lines. It takes a certain amount of time to travel through a tunnel in either direction. You can get off the metro at one end of the tunnel and walk through the tunnel to the station at the another end.</li>
	<li>When you arrive at a metro station of line <strong>i</strong>, you need to wait <strong>W</strong><strong><sub>i</sub></strong> minutes for the next metro.</li>
</ul>

<p>Now, you are going to travel from one station to another. Find out the shortest time you need.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow.</p>

<p>Each test case starts with an integer <strong>N</strong>, the number of metro lines. <strong>N</strong> metros descriptions follow. Each metro description starts with two integers <strong>SN</strong><strong><sub>i</sub></strong> and <strong>W</strong><strong><sub>i</sub></strong>, the number of stations and the expected waiting time in minutes. The next line consists of <strong>SN</strong><strong><sub>i</sub></strong><strong>-1</strong> integers, <strong>Time</strong><strong><sub>i,1</sub></strong>, <strong>Time</strong><strong><sub>i,2</sub></strong>, ..., <strong>Time</strong><strong><sub>i,SN</sub></strong><strong><sub>i</sub></strong><strong><sub>-1</sub></strong>, describing the travel time between stations.</p>

<p>After the metro descriptions, there is an integer <strong>M</strong>, the number of tunnels. <strong>M</strong> lines follow to describe the tunnels. Each tunnel description consists of 5 integers, <strong>m1</strong><strong><sub>i</sub></strong>, <strong>s1</strong><strong><sub>i</sub></strong>, <strong>m2</strong><strong><sub>i</sub></strong>, <strong>s2</strong><strong><sub>i</sub></strong>, <strong>t</strong><strong><sub>i</sub></strong> which means the tunnel is connecting stations <strong>S</strong><strong><sub>m1</sub></strong><strong><sub>i</sub></strong><strong><sub>,s1</sub></strong><strong><sub>i</sub></strong> and station <strong>S</strong><strong><sub>m2</sub></strong><strong><sub>i</sub></strong><strong><sub>,s2</sub></strong><strong><sub>i</sub></strong>. The walking time of the tunnel is <strong>t</strong><strong><sub>i</sub></strong>.</p>

<p>The next line contains an integer <strong>Q</strong>, the number of queries. Each of the next <strong>Q</strong> lines consists of 4 integers, <strong>x1</strong>, <strong>y1</strong>, <strong>x2</strong>, <strong>y2</strong>, which mean you are going to travel from station <strong>S</strong><strong><sub>x1,y1</sub></strong> to station <strong>S</strong><strong><sub>x2,y2</sub></strong>.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>W</strong><strong><sub>i</sub></strong> ≤ 100.</li>
	<li>1 ≤ <strong>Time</strong><strong><sub>i,j</sub></strong> ≤ 100.</li>
	<li>1 ≤ <strong>m1</strong><strong><sub>i</sub></strong> ≤ <strong>N</strong>.</li>
	<li>1 ≤ <strong>s1</strong><strong><sub>i</sub></strong> ≤ <strong>SN</strong><strong><sub>m1</sub></strong><strong><sub>i</sub></strong>.</li>
	<li>1 ≤ <strong>m2</strong><strong><sub>i</sub></strong> ≤ <strong>N</strong>.</li>
	<li>1 ≤ <strong>s2</strong><strong><sub>i</sub></strong> ≤ <strong>SN</strong><strong><sub>m2</sub></strong><strong><sub>i</sub></strong>.</li>
	<li><strong>m1</strong><strong><sub>i</sub></strong> and <strong>m2</strong><strong><sub>i</sub></strong> will be different.</li>
	<li>1 ≤ <strong>t</strong><strong><sub>i</sub></strong> ≤ 100.</li>
	<li>1 ≤ <strong>Q</strong> ≤ 10.</li>
	<li>1 ≤ <strong>x1</strong> ≤ <strong>N</strong>.</li>
	<li>1 ≤ <strong>y1</strong> ≤ <strong>SN</strong><strong><sub>x1</sub></strong>.</li>
	<li>1 ≤ <strong>x2</strong> ≤ <strong>N</strong>.</li>
	<li>1 ≤ <strong>y2</strong> ≤ <strong>SN</strong><strong><sub>y2</sub></strong>.</li>
	<li>Station <strong>S</strong><strong><sub>x1,y1</sub></strong> and station <strong>S</strong><strong><sub>x2,y2</sub></strong> will be different.</li>
	<li><span style="line-height:1.6em">1 ≤ </span><strong style="line-height:1.6em">N</strong><span style="line-height:1.6em"> ≤ 10.</span></li>
	<li>0 ≤ <strong>M</strong> ≤ 10.</li>
	<li>2 ≤ <strong>SN</strong><strong><sub>i</sub></strong> ≤ 100.</li>
	<li>The total number of stations in each case is at most 100.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x:", where x is the test case number (starting from 1), then followed by <strong>Q</strong> lines, each line containing an integer y which is the shortest time you need for that query. If it's impossible, output -1 for that query instead.</p>

