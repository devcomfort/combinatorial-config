import pytest
from combinatorial_config.normalize_range_field import normalize_range_field


def test_single_value():
    """
    [목적]
    RangeField가 (stop,) 단일 값 튜플로 들어올 때, 표준 형식 (start, stop, step) 3-튜플로 올바르게 변환되는지 검증합니다.
    [시나리오·설명]
    파라미터 범위를 (끝값,)만 명시하여 전달하는 경우가 많고,
    관례적으로 (0, stop, 1)로 간주/보정되어야 합니다. (ex: range(3) == (0,3,1))
    """
    assert normalize_range_field((3,)) == (0, 3, 1)


def test_two_values():
    """
    [목적]
    RangeField가 (start, stop) 2-튜플로 들어올 때, 표준 형식 (start, stop, step=1)로 변환되는지 검증합니다.
    [시나리오·설명]
    사용자 입력·API·설정 등에서 기본 step을 생략하는 경우,
    항상 1로 채워 구조적 정규화가 필요합니다. (실제 범위 생성 or 프로세싱 일관성 위해)
    """
    assert normalize_range_field((2, 5)) == (2, 5, 1)


def test_three_values():
    """
    [목적]
    RangeField가 이미 (start, stop, step) 3-튜플인 경우 별도의 변환 없이 그대로 반환되는지 확인합니다.
    [시나리오·설명]
    외부에서 완전한 범위 값이 이미 제공된다면 변형 없이 사용되는 것이 정상 동작입니다.
    """
    assert normalize_range_field((1, 10, 2)) == (1, 10, 2)


def test_invalid_type():
    """
    [목적]
    RangeField 계약에 어긋나는 잘못된 입력에 대해 ValueError가 raise되는지 검증합니다.
    [시나리오·설명]
    - ("a",) : 숫자가 아닌 값이 들어옴 (계약 위반)
    - (1, "b") : 일부만 숫자, 나머지는 잘못된 값 (계약 위반)
    - (1, 2, 3, 4) : 4-튜플은 허용 길이(1~3)를 벗어남 (계약 위반)
    - [] : 튜플 타입이 아닌 경우 (완전 계약 위반)
    각 케이스는 입력 검증 실패 시, 반드시 ValueError 발생이 약속되어야 합니다.
    """
    with pytest.raises(ValueError):
        normalize_range_field(("a",))
    with pytest.raises(ValueError):
        normalize_range_field((1, "b"))
    with pytest.raises(ValueError):
        normalize_range_field((1, 2, 3, 4))
    with pytest.raises(ValueError):
        normalize_range_field([])  # not a tuple
