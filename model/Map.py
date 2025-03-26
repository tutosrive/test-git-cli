class Map:
  def __init__(self):
    self.__site:str = 'Colombia'
    self.__size:int = 5
    
  def getSite(self):
    return self.__site
	def getSite(self) -> str:
	  return self.__site
