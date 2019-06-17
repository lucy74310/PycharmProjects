from point import Point

# self 를 통해 접근할 수 있는 메소드 => 인스턴스 메소드
# self 없이.. 클레스 변수에 접근, 일반 메소드 Point.m() => 클래스 메소드


def test_bound_instance_method():
    p = Point()
    p.setx(10)
    p.sety(20)
    p.show()


def test_unbound_class_method():
    p = Point()
    Point.setx(p, 10)
    Point.sety(p, 20)
    Point.show(p)


def test_other_method():
    print(Point.class_method())
    print(Point.static_method())


def main():
    # test_bound_instance_method()
    # test_unbound_instance_method()
    test_other_method()


if __name__ == '__main__':
    main()



