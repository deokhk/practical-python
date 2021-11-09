# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False) -> list:
    '''
    line을 파싱해 레코드의 목록을 생성
    '''
    # 입력 데이터 파일에 컬럼 헤더가 없지만 사용자 정의 컬럼을 선택하는 경우, 예외 발생
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(lines, delimiter=delimiter)

    # 헤더가 존재하는 경우 헤더를 읽음
    if has_headers:
        headers = next(rows)

    # 컬럼 선택기가 주어지면, 지정한 컬럼의 인덱스를 찾는다.
    # 또한 결과 딕셔너리에 사용할 헤더의 집합을 좁힌다.
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []
    records = []
    for i, row in enumerate(rows, start=1):
        if not row:    # 데이터가 없는 행을 건너뜀
            continue
        # 특정 컬럼이 선택되었으면 필터링
        if indices:
            row = [ row[index] for index in indices]
        # 형변환이 필요한 경우 수행
        if types:
            try:
                row = [ func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {i}: Couldn't convert {row}")
                    print(f"Row {i}: Reason {e}")
        # 헤더가 존재하는 경우, 딕셔너리를 만듬. 그렇지 않은 경우, 튜플 생성.
        if has_headers:
            record = dict(zip(headers, row))
        else: 
            record = tuple(row)
        records.append(record)
    return records
