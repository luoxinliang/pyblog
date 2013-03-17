from math import ceil

#分页类
class Paginator(object):
    def __init__(self,cur,total,page_size=15,show_page_count=10):
        self.cur = int(cur)
        self.total = total
        self.page_size = page_size
        self.show_page_count = show_page_count
        self._num_pages = 0
        
    def get_page_count(self):
        "Returns the total number of pages."
        if self._num_pages == 0:
            if self.total <= 0:
                self._num_pages = 0
            else:
                self._num_pages = int(ceil(self.total / float(self.page_size)))
        return self._num_pages
    
    def has_next(self):
        return self.cur<self.get_page_count()
    
    def has_pre(self):
        return self.cur>1
    
#    def get_show_pages(self):
#        return [self._get_left(),self._get_right()]
    
    def has_left_point(self):
        return self.get_left() != 1
     
    def has_right_point(self):
        return self.get_right() < self.get_page_count()
            
    def get_left(self):
        left = self.cur - self.show_page_count/2
        if left<1:
            left=1
        return left
            
    def get_right(self):
        right = self.cur + self.show_page_count/2
        if right>self.get_page_count():
            right=self.get_page_count()
        return right