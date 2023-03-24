class Star_Cinema:
    hall_list=[]

    def entry_hall(self):
        self.hall_list.append(self)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.seats={}
        self.show_list=()
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        Star_Cinema.entry_hall(self)

    # def entry_show(self,id,movie_name,time):
    #     make_tuple=tuple(id,movie_name,time)
    #     self.show_list+=make_tuple

person1=Hall(1,2,3)
print(person1.hall_list)
