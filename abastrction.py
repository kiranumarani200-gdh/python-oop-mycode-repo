from abc import ABC, abstractmethod
class shape(ABC):
        @abstractmethod
        def are(self):
            pass

class circle(shape):
      def are(self):
            print ("Area =3.142")
      
c=circle()
c.are()      