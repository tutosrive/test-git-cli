class Map:
  def __init__(self) -> None:
    self.__time:str = ''
    self.__site:str = 'Colombia'
    self.__size:int = 5

  def getSixe(self) -> str:
    return self.__size
    
	def getSite(self) -> str:
	  return self.__site

  def setSize(self, size) -> None:
    self.__size = size