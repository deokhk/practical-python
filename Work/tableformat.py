# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        테이블 헤딩을 반환.
        '''
        raise NotImplementedError()
    
    def row(self, rowdata):
        '''
        테이블 데이터의 단일 행을 반환.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    테이블을 일반 텍스트 포맷으로 출력
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    포트폴리오 데이터를 CSV 포맷으로 출력
    '''
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    포트폴리오 데이터를 HTML 포맷으로 출력
    '''
    def headings(self, headers):
        print("<tr>", end='')
        for h in headers:
            print(f"<th>{h}</th>", end='')
        print("</tr>")
    
    def row(self, rowdata):
        print("<tr>", end='')
        for d in rowdata:
            print(f"<td>{d}</td>", end='')
        print("</tr>")

class FormatError(Exception):
    pass

def create_formatter(fmt:str):
    '''
    입력에 따라 사용자가 원하는 포매터를 생성
    '''
    if fmt == "txt":
        formatter = TextTableFormatter()
    elif fmt == "csv":
        formatter = CSVTableFormatter()
    elif fmt == "html":
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {fmt}')
    return formatter

def print_table(portfolio, columns:list, formatter:TableFormatter):
    formatter.headings(columns)
    for s in portfolio:
        rowdata = [str(getattr(s, colname)) for colname in columns]
        formatter.row(rowdata)