# 인접한 두 정점 사이의 간선만 고려해도 되는 이유


### [Proof 1]

정답을 구성하는 터널 N-1개 중에서 어떤 한 터널을 택해서 해당 터널이 잇는 행성을 P, Q라고 하자.

정의에 의해 해당 터널의 길이는 |xP-xQ|, |yP-yQ|, |zP-zQ| 중 가장 작은 값이다.


|xP-xQ|가 해당 터널의 길이인 경우,

만약 어떤 한 행성 M의 x좌표 xM이 xP와 xQ 사이의 값이라면 다음과 같은 과정을 통해 정답보다 전체 비용 합이 더 작은 조합을 만들 수 있다.

(정답이 정답이 아님, 모순)


1. P, Q를 잇는 해당 터널을 제거한다.

전체 비용은 |xP-xQ| 감소하며, Spanning Tree에서 간선 하나를 제거한 것이므로 M은 P와 Q 중에 하나와는 연결되어 있고 다른 하나와는 연결되어 있지 않게 된다.

처음에 P, Q를 정하는 순서를 임의로 정할 수 있으므로 이때 M과 연결되어 있지 않은 행성을 P라고 하자.

2. P와 M 사이에 터널을 새로 건설한다.

정의에 의해 새로 건설한 터널의 길이는 min(|xP-xM|, |yP-yM|, |zP-zM|) 이므로 |xP-xM| 이하이다.

건설 후 Spanning Tree 조건을 만족하게 되어 다시 모든 행성이 서로 연결되며, |xP-xM| < |xP-xQ| 이므로 전체 비용 합은 처음의 정답보다 더 작아진다.


|yP-yQ|가 해당 터널의 길이인 경우,

|zP-zQ|가 해당 터널의 길이인 경우도 동일한 과정으로 모순이 도출된다.


따라서 정답을 구성하는 터널이 존재하는 축을 기준으로 봤을 때 터널로 이어지는 두 행성 사이에는 다른 행성이 존재해선 안된다.

---------------------------------------------------------------------------------------------------------------------------------------------------

### [Proof 2]

모든 축에 대해 인접하지 않은 두 정점 A와 B가 있다고 하자.

두 정점을 연결하는데 드는 비용을 결정하는 축의 값에 따라 모든 점을 축 위에 찍어 놓았다고 생각해보자.

A와 B는 사이에 점이 최소 1개 이상 있을 것이다.

이 점들을 r0,r1,⋯,rk 라고 하자.

이렇게 한 후, 모든 간선을(O(N2)의 간선) 추가하고 크루스칼 알고리즘을 수행한다고 해보자.

크루스칼 알고리즘은 가중치가 작은 간선들부터 차례로 검사하므로 E(A,B)를 검사하기 전에 E(A,r0),E(r0,r1),E(r1,r2),⋯,E(rk,B) 들을 먼저 검사했을 것이다.

크루스칼 알고리즘은 간선을 두 가지중 하나로 처리하는데,
1. 간선을 추가
2. 간선이 연결된 두 정점이 이미 하나의 컴포넌트이므로 추가하지 않음.

어떤 경우든 간에 검사한 간선의 양 쪽 정점은 하나의 컴포넌트였거나, 하나의 컴포넌트가 되므로 검사 후에는 반드시 하나의 컴포넌트라는 사실을 알 수 있다.

따라서 E(A,B)를 검사하는 시점에서는 반드시 A,B가 하나의 컴포넌트라는 사실을 알 수 있으므로 E(A,B)는 크루스칼 알고리즘에서 절대 추가되지 않는 간선임을 알 수 있다.

결국 임의의 축에 대해 인접하지 않은 두 정점 사이의 간선은 크루스칼 알고리즘 수행 과정에서 사용되지 않는다는 것을 알 수 있으므로, 인접한 두 정점 사이의 간선만을 이용해도 된다는 것을 알 수 있다.



출처: [백준 질문 게시판](https://www.acmicpc.net/board/view/10945)
