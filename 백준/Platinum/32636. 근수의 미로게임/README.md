# [Platinum IV] 근수의 미로게임 - 32636 

[문제 링크](https://www.acmicpc.net/problem/32636) 

### 성능 요약

메모리: 155968 KB, 시간: 1052 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색, 최단 경로, 데이크스트라, 게임 이론

### 제출 일자

2025년 9월 4일 17:15:55

### 문제 설명

<p>근수와 승형이는 근수의 미로게임을 즐기려고 한다. 미로는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>×</mo><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N \times M$</span></mjx-container> 크기의 격자판으로 이루어져 있으며, 빈 칸, 장애물, 시작점, 도착점으로 이루어져 있다. 미로에 시작점은 단 한 개 존재하며 도착점은 한 개 이상 존재할 수도, 존재하지 않을 수도 있다.</p>

<p>현재 근수는 시작점에 있다. 모든 도착점에는 근수가 좋아하는 도마 우마루 인형이 있어서 근수는 도착점 중 한 곳으로 이동하고 싶어 한다. 승형이는 이러한 근수가 못마땅한지 근수를 최대한 방해하려고 한다. 근수와 승형이는 한 턴마다 다음과 같은 행동을 게임이 끝나기 전까지 반복한다.</p>

<ol>
	<li>현재 있는 위치가 도착점이라면 근수가 게임에서 승리한다.</li>
	<li>현재 있는 위치가 도착점이 아니라면, 승형이는 네 방향(위, 아래, 왼쪽, 오른쪽) 중 하나를 선택한다.</li>
	<li>근수는 승형이가 선택한 방향을 제외한 세 방향 중 한 방향을 선택해서 그 방향으로 한 칸 움직인다. 움직이려고 하는 위치에 장애물이 있으면 그 즉시 승형이가 게임에서 승리하며, 움직인 곳이 이미 방문했던 장소거나 격자판 밖이라면 그 즉시 승형이가 게임에서 승리한다.</li>
</ol>

<p>근수는 게임을 이기고 싶어하고, 이긴다면 근수가 도착점에 도달하는 턴 수를 최대한 줄이고 싶어한다. 승형이는 게임을 이기고 싶어하고, 이기지 못한다면 근수가 도착점에 도달하는 턴 수를 최대한 늘리고 싶어한다. 근수와 승형이가 항상 최선의 전략으로 게임을 한다고 가정할 때 근수가 게임에서 이길 수 있는지, 이긴다면 도착점에 도달할 때까지 얼마나 걸리는지 구해보자.</p>

### 입력 

 <p>첫 번째 줄에 미로의 크기인 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 주어진다 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>,</mo><mi>M</mi><mo>≤</mo><mn>500</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \leq N, M \leq 500)$</span> </mjx-container></p>

<p>두 번째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>+</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N+1$</span></mjx-container>번째 줄까지 미로에 대한 정보가 주어진다. <span style="color:#c0392b;"><code>.</code></span>은 빈 칸, <span style="color:#c0392b;"><code>#</code></span>은 장애물, <span style="color:#c0392b;"><code>S</code></span>는 시작점, <span style="color:#c0392b;"><code>G</code></span>는 도착점을 의미한다. 미로에 시작점은 단 한 개 존재하며 도착점은 한 개 이상 존재할 수도, 존재하지 않을 수도 있다.</p>

### 출력 

 <p>근수와 승형이가 항상 최선의 전략으로 게임을 한다고 가정할 때 근수가 도착점에 도달하는 턴 수를 출력한다. 만약 근수가 게임에서 이길 수 없다면 <span style="color:#c0392b;"><code>-1</code></span>을 출력한다.</p>

