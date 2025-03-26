class Map:
  def __init__(self):
    self.__site:str = 'Colombia'
    self.__size:int = 5

  def getSize(self) -> str:
    return self.__size
    
	def getSite(self) -> str:
	  return self.__site
