# https://school.programmers.co.kr/learn/courses/30/lessons/62048

def solution(w, h):
    """
    패턴 하나를 살펴보자 (ex. ww * hh == 3 * 4)
          *   *   *     ===> ww의 경우, 모두 사용 가능
    (!) | * |   |   |   ===> hh의 경우, 한 번이 누락됨
    ->  | > | * |   |
    ->  |   | > | * |
    ->  |   |   | > |

    따라서, 한 패턴 내에서 사용할 수 없는 칸의 개수는 (ww + hh - 1) 개가 된다!
    """

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return w * h - (w + h - gcd(w, h))


def solution1(w, h):
    """
    ref: https://school.programmers.co.kr/questions/48902

    -   주어진 직사각형을 1x1 grid로 나누고, 대각선에 위치한 cell을 지우면 일정 패턴이 반복되게 된다.
        이때, w와 h의 최대공약수를 gcd라 하면, 해당 패턴을 감싸는 크기는 (w // gcd) * (h // gcd)가 된다.
        하나의 패턴을 감싸는 크기를 ww * hh라 하자.
    -   하나의 패턴만 놓고 봤을 때, 대각선에 위치한 cell을 지우고 나머지 cell을 테트리스처럼 (좌&하 방향으로) 모으면
        그 크기가 (ww - 1) * (hh - 1)가 되는 것을 확인할 수 있다.
    -   하나의 패턴에서 사용할 수 없는 정사각형의 개수는 ww * hh - (ww - 1) * (hh - 1)가 된다.
    -   해당 패턴은 gcd개 있으므로, 주어진 직사각형에서 사용할 수 없는 정사각형의 개수는
        gcd * (ww * hh - (ww - 1) * (hh - 1)) 로 구할 수 있다.
    """

    def get_gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # w, h의 최대공약수 구하기
    gcd = get_gcd(w, h)

    # 하나의 패턴을 감싸는 크기 구하기
    ww, hh = w // gcd, h // gcd

    # 주어진 직사각형에서 사용할 수 없는 정사각형의 개수 구하기
    removed = gcd * (ww * hh - (ww - 1) * (hh - 1))

    return w * h - removed
