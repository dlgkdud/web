import random

class Mine():
    def __init__(self) -> None:
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600

        CELL_SIZE = 50
        # self.COLUMN_COUNT = SCREEN_WIDTH // CELL_SIZE
        # self.ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE
        self.COLUMN_COUNT = 9
        self.ROW_COUNT = 9
        self.__clean()
        
    def __clean(self):
        self.grid = [[{'mine': False, 'open': False, 'mine_count_around': 0,\
                        'flag': False} for _ in range(self.COLUMN_COUNT)]\
                        for _ in range(self.ROW_COUNT)]
        
    def __make_mine(self, mine_count = 10):
        for _ in range(mine_count):
            while True:
                self.column_index = random.randint(0, self.COLUMN_COUNT - 1)
                self.row_index = random.randint(0, self.ROW_COUNT - 1)
                tile = self.grid[self.row_index][self.column_index]
                if not tile['mine']:
                    tile['mine'] = True 
                    break
    
    def __set_mine_count(self):
        for i in range(self.ROW_COUNT):
            for j in range(self.COLUMN_COUNT):
                _tmp = self.__get_mine_count_around(i, j)
                self.grid[j][i]['mine_count_around'] = _tmp
        return

    def generate_mine(self):
        self.__clean()
        self.__make_mine(10)
        self.__set_mine_count()
        return self.grid
    
    # 접근 가능한 셀인지 판단
    def __in_bound(self, column_index, row_index):
        if (0 <= column_index < self.COLUMN_COUNT and 0 <= row_index < self.ROW_COUNT):
            return True
        else:
            return False

    # 각 타일을 오픈
    def open_tile(self, column_index, row_index): 
        if not self.__in_bound(column_index, row_index):
            return
    
        tile = self.grid[row_index][column_index]
        if not tile['open']:
            tile['open'] = True
        else:    
            return 'open'
    
        if tile['mine']:
            return 'mine'
    
        mine_count_around = self.get_mine_count_around(column_index, row_index)
        if mine_count_around > 0:
            tile['mine_count_around'] = mine_count_around
        else:
            arounds = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dc, dr in arounds:
                column_index_around, row_index_around = (column_index + dc, row_index + dr)
                self.open_tile(column_index_around, row_index_around)
    
    # 주변 지뢰 개수를 리턴
    def __get_mine_count_around(self, column_index, row_index):
        count = 0
        arounds = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dc, dr in arounds:
            column_index_around, row_index_around = (column_index + dc, row_index + dr)
            if self.__in_bound(column_index_around, row_index_around) and \
                self.grid[row_index_around][column_index_around]['mine']:
                count += 1
        return count
