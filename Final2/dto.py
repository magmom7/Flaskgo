# User정보를 보유하게 되는 구조의 class

class UserDTO:
    def __init__(self, id, name, pw, interest):
        self.uid = id
        self.uname = name
        self.upw = pw
        self.uinterest = interest

    def getId(self):
        return self.uid
    
    def getName(self):
        return self.uname

    def getPw(self):
        return self.upw

    def getInterest(self):
        return self.uinterest
    
    def __str__(self):
        return f"id : {self.uid}, name : {self.uname}, pw : {self.upw}, interest : {self.uinterest}"



class BoardDTO:
    def __init__(self, idx, title, content, input_date, user_id):
        self.bidx = idx
        self.btitle = title
        self.bcontent = content
        self.bdate = input_date
        self.bid = user_id

    def getIdx(self):
        return self.bidx
        
    def getTitle(self):
        return self.btitle
    
    def getContent(self):
        return self.bcontent

    def getInputDate(self):
        return self.bdate  

    def getId(self):
        return self.bid

    def __str__(self):
        return f"{self.bidx},{self.btitle}, {self.bcontent}, {self.bdate}, {self.bid}"


# if __name__ == "__main__":
#     boardInfo = boardDTO(1, "제목", "내용..", "21-06-20", 1)
#     print(boardInfo)